# Inputs

- Required: `outputs/01-strategy-foundation/strategy-brief.md`
  - Source: previous workflow step `01-strategy-foundation`
  - Use: business goals, brand position, audience context, and strategic constraints that the visual direction must support

- Required: `outputs/02-audience-positioning/audiences.md`
  - Source: previous workflow step `02-audience-positioning`
  - Use: audience expectations, trust cues, and taste signals that should shape the visual tone

- Required: `outputs/02-audience-positioning/positioning.md`
  - Source: previous workflow step `02-audience-positioning`
  - Use: differentiation, confidence level, and brand posture the design should express

- Required: `outputs/02-audience-positioning/decision-drivers.md`
  - Source: previous workflow step `02-audience-positioning`
  - Use: proof priorities and trust signals that should influence emphasis and layout without forcing final copy

- Required: `resources/high-quality-web-design.md`
  - Source: repository reference
  - Use: supporting guidance for hierarchy, whitespace, imagery, surface treatment, and generic-risk checks while building stylescapes

- Optional: `resources/scripts/openrouter_image_gen.py`
  - Source: repository helper
  - Use: local OpenRouter fallback for generating pre-approval stylescape raster images when a built-in image tool is unavailable
  - Default model: `google/gemini-3.1-flash-image-preview`
  - Override: the workflow instruction may specify a different OpenRouter model for a given run

- Optional: existing logos, brand assets, photo libraries, inspiration boards, reference imagery, or brand rules already present in the repository
  - Source: repository files or user-provided assets
  - Use: visual constraints, reusable brand materials, or reference signals to steer the AI-generated stylescapes if they already exist
  - Ask the user only if the project is expected to follow existing brand rules and those materials cannot be found
