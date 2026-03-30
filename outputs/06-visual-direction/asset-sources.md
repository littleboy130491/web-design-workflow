# Asset Sources

## Overview

This file records the sources and generation method used for the workflow `06-visual-direction` pre-approval deliverables.

## Internal Inputs Used

- `outputs/01-strategy-foundation/strategy-brief.md`
- `outputs/02-audience-positioning/audiences.md`
- `outputs/02-audience-positioning/positioning.md`
- `outputs/02-audience-positioning/decision-drivers.md`
- `resources/high-quality-web-design.md`

## Generation Method

- Method: OpenRouter image generation fallback
- Script: `resources/scripts/openrouter_image_gen.py`
- Model: `google/gemini-3.1-flash-image-preview`
- Output type: generated raster stylescape boards
- Visible copy handling: generated image text is treated as placeholder specimen content only

## External Asset Status

### Concept A

- Output: `concept-a.png`
- Status: fully generated
- Reference-assisted: no external image assets used
- Notes: generated from the concept brief and prompt spec in `concept-a.md`

### Concept B

- Output: `concept-b.png`
- Status: fully generated
- Reference-assisted: no external image assets used
- Notes: generated from the concept brief and prompt spec in `concept-b.md`

### Concept C

- Output: `concept-c.png`
- Status: fully generated
- Reference-assisted: no external image assets used
- Notes: generated from the concept brief and prompt spec in `concept-c.md`

## Prompt Records

Detailed prompt and request metadata for each generated image are stored in:

- `concept-a.meta.json`
- `concept-b.meta.json`
- `concept-c.meta.json`

These sidecar files capture the exact request payload used for the final saved image outputs.

## External References

- No external stock photos, icon packs, or downloaded reference boards were used in the saved outputs.
- The workflow reference `resources/high-quality-web-design.md` informed hierarchy, spacing, imagery restraint, and generic-risk checks.
