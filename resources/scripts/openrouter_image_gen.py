#!/usr/bin/env python3
"""Generate an image through OpenRouter and save it as a local PNG."""

from __future__ import annotations

import argparse
import base64
import json
import os
import sys
import urllib.error
import urllib.request
import binascii
from datetime import datetime, timezone
from pathlib import Path
from typing import Any


API_URL = "https://openrouter.ai/api/v1/chat/completions"
DEFAULT_MODEL = "google/gemini-3.1-flash-image-preview"
DEFAULT_MODALITIES = ["image", "text"]


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Generate an image via OpenRouter and save it locally."
    )
    prompt_group = parser.add_mutually_exclusive_group(required=True)
    prompt_group.add_argument("--prompt", help="Direct prompt text.")
    prompt_group.add_argument(
        "--prompt-file",
        type=Path,
        help="Path to a UTF-8 text file containing the prompt.",
    )
    parser.add_argument(
        "--out",
        type=Path,
        required=True,
        help="Where to save the generated image.",
    )
    parser.add_argument(
        "--meta-out",
        type=Path,
        help="Optional path for a JSON sidecar with request and response metadata.",
    )
    parser.add_argument(
        "--model",
        default=DEFAULT_MODEL,
        help=f"OpenRouter model slug. Default: {DEFAULT_MODEL}",
    )
    parser.add_argument(
        "--system-prompt",
        help="Optional system prompt sent before the user prompt.",
    )
    parser.add_argument(
        "--aspect-ratio",
        help="Optional aspect ratio hint passed through to the model.",
    )
    parser.add_argument(
        "--size",
        help="Optional size hint passed through to the model.",
    )
    parser.add_argument(
        "--moderation",
        choices=["auto", "low"],
        help="Optional OpenRouter moderation level.",
    )
    parser.add_argument(
        "--site-url",
        default="https://example.com",
        help="Value for the HTTP-Referer header. Default: https://example.com",
    )
    parser.add_argument(
        "--site-name",
        default="web-designer",
        help="Value for the X-Title header. Default: web-designer",
    )
    parser.add_argument(
        "--api-key-env",
        default="OPENROUTER_API_KEY",
        help="Environment variable that stores the OpenRouter API key.",
    )
    parser.add_argument(
        "--overwrite",
        action="store_true",
        help="Allow overwriting an existing output file.",
    )
    parser.add_argument(
        "--timeout",
        type=int,
        default=300,
        help="HTTP timeout in seconds. Default: 300",
    )
    return parser.parse_args()


def load_prompt(args: argparse.Namespace) -> str:
    if args.prompt is not None:
        prompt = args.prompt.strip()
    else:
        prompt = args.prompt_file.read_text(encoding="utf-8").strip()

    if not prompt:
        raise SystemExit("Prompt is empty.")
    return prompt


def build_payload(args: argparse.Namespace, prompt: str) -> dict[str, Any]:
    messages: list[dict[str, str]] = []
    if args.system_prompt:
        messages.append({"role": "system", "content": args.system_prompt})
    messages.append({"role": "user", "content": prompt})

    payload: dict[str, Any] = {
        "model": args.model,
        "modalities": DEFAULT_MODALITIES,
        "messages": messages,
    }

    if args.aspect_ratio or args.size:
        payload["image"] = {}
        if args.aspect_ratio:
            payload["image"]["aspect_ratio"] = args.aspect_ratio
        if args.size:
            payload["image"]["size"] = args.size

    if args.moderation:
        payload["moderation"] = args.moderation

    return payload


def request_completion(
    payload: dict[str, Any], api_key: str, args: argparse.Namespace
) -> dict[str, Any]:
    request = urllib.request.Request(
        API_URL,
        data=json.dumps(payload).encode("utf-8"),
        method="POST",
        headers={
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json",
            "HTTP-Referer": args.site_url,
            "X-Title": args.site_name,
        },
    )

    try:
        with urllib.request.urlopen(request, timeout=args.timeout) as response:
            charset = response.headers.get_content_charset("utf-8")
            return json.loads(response.read().decode(charset))
    except urllib.error.HTTPError as exc:
        body = exc.read().decode("utf-8", errors="replace")
        raise SystemExit(
            f"OpenRouter request failed with HTTP {exc.code}.\n{body}"
        ) from exc
    except urllib.error.URLError as exc:
        raise SystemExit(f"OpenRouter request failed: {exc.reason}") from exc


def extract_image_bytes(response_json: dict[str, Any]) -> bytes:
    try:
        images = response_json["choices"][0]["message"]["images"]
        url = images[0]["image_url"]["url"]
    except (KeyError, IndexError, TypeError) as exc:
        raise SystemExit(
            "OpenRouter response did not contain an image at "
            "choices[0].message.images[0].image_url.url."
        ) from exc

    if not isinstance(url, str) or not url.startswith("data:image/"):
        raise SystemExit("OpenRouter returned an unexpected image URL format.")

    try:
        _, encoded = url.split(",", 1)
        return base64.b64decode(encoded)
    except (ValueError, binascii.Error) as exc:
        raise SystemExit("Failed to decode the image data URL.") from exc


def write_metadata(
    meta_path: Path,
    args: argparse.Namespace,
    payload: dict[str, Any],
    response_json: dict[str, Any],
) -> None:
    assistant_message = (
        response_json.get("choices", [{}])[0].get("message", {})
        if isinstance(response_json.get("choices"), list)
        else {}
    )

    meta = {
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "api_url": API_URL,
        "model": args.model,
        "output_path": str(args.out),
        "request": payload,
        "response_text": assistant_message.get("content"),
        "response_id": response_json.get("id"),
        "usage": response_json.get("usage"),
    }
    meta_path.parent.mkdir(parents=True, exist_ok=True)
    meta_path.write_text(json.dumps(meta, indent=2) + "\n", encoding="utf-8")


def ensure_output_path(path: Path, overwrite: bool) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    if path.exists() and not overwrite:
        raise SystemExit(
            f"Output file already exists: {path}\n"
            "Pass --overwrite to replace it."
        )


def main() -> int:
    args = parse_args()
    prompt = load_prompt(args)
    ensure_output_path(args.out, overwrite=args.overwrite)

    api_key = os.environ.get(args.api_key_env)
    if not api_key:
        raise SystemExit(
            f"{args.api_key_env} is not set. Export it before running this script."
        )

    payload = build_payload(args, prompt)
    response_json = request_completion(payload, api_key, args)
    image_bytes = extract_image_bytes(response_json)
    args.out.write_bytes(image_bytes)

    if args.meta_out:
        write_metadata(args.meta_out, args, payload, response_json)

    timestamp = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    print(f"Saved image to {args.out}")
    if args.meta_out:
        print(f"Saved metadata to {args.meta_out}")
    print(f"Completed at {timestamp}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
