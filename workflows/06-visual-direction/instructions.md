# 06 Visual Direction

## Brief Description

Create 3 distinct visual direction stylescapes for the website.

Each stylescape should help the user judge immediately whether the visual style fits their preference. The goal of this step is not to design full pages or finalize copy. The goal is to present visual language clearly enough that the user can react to typography, color, spacing, imagery, composition, and surface treatment.

Use AI image generation to create each pre-approval stylescape as a polished raster visual-direction board. Do not build the pre-approval stylescapes in HTML.

## Expected Input

- `outputs/01-strategy-foundation/strategy-brief.md`
- `outputs/02-audience-positioning/audiences.md`
- `outputs/02-audience-positioning/positioning.md`
- `outputs/02-audience-positioning/decision-drivers.md`
- `resources/high-quality-web-design.md`
- Any existing brand assets or brand constraints already present in the repository

## Expected Output

Create these files in `outputs/06-visual-direction/` before approval:

- `concept-a.md`
- `concept-b.md`
- `concept-c.md`
- `concept-a.png`
- `concept-b.png`
- `concept-c.png`
- `comparison.md`
- `style-review.md`
- `asset-sources.md`

Create these files only after the user approves one concept:

- `recommended-direction.md`
- `visual-guidelines.md`
- `visual-guidelines.html`

## Required Structure For Each `concept-*.md`

Each concept brief must include:

- Concept name
- One-sentence visual thesis
- 3 to 5 style keywords
- Typography direction
- Color direction
- Spacing and density direction
- Imagery direction
- Composition direction
- Surface treatment direction
- AI stylescape prompt spec
- Prompt iteration note
- Generic-risk note
- Best fit note
- Anti-pattern note

Keep each concept brief concise and visual-first.

The AI stylescape prompt spec must include these labeled fields:

- Use case
- Asset type
- Primary request
- Scene or backdrop
- Subject
- Style or medium
- Composition or framing
- Lighting or mood
- Color palette
- Constraints
- Avoid

## Required Structure For Each `concept-*.png`

Each image file must be a stylescape presentation, not a full webpage or a final homepage mockup.

Export each stylescape as a single polished raster image. Use a stable filename so the image can be reviewed directly from `outputs/06-visual-direction/`.

Each stylescape image must visibly communicate these ideas:

1. Overall atmosphere
   - one dominant visual attitude
   - obvious emotional tone
   - clear distinction from the other two concepts

2. Typography attitude
   - visible hierarchy cues or editorial type energy
   - enough type treatment to judge scale, contrast, and form
   - do not rely on long readable generated text for evaluation

3. Color direction
   - primary, secondary, and accent behavior made visually legible
   - background or surface mood made visually legible
   - exact hex values must be recorded in the matching `concept-*.md`, not trusted to the image alone

4. Imagery direction
   - subject matter or crop tendency made visually clear
   - dominant, supporting, or restrained imagery usage made visually clear
   - enough variation to judge how the brand should feel, not just what one page looks like

5. Surface language
   - panel, texture, depth, border, radius, or shadow attitude made visible
   - enough material treatment to judge polish level and restraint

6. Composition tendency
   - one dominant compositional move
   - enough structure to judge hierarchy, balance, and whitespace
   - should read as a board or direction sheet, not a complete page layout

7. Spacing rhythm
   - visible cues for dense, standard, or spacious behavior
   - enough for the user to react to tightness or looseness

8. Presentation quality
   - polished enough to feel like an intentional stylescape
   - free from distracting text artifacts or malformed UI details that make comparison unreliable

## Success Criteria

- The 3 stylescapes are clearly different in composition, typography, spacing, color balance, and imagery treatment.
- The stylescapes help the user react to style immediately, without getting distracted by content.
- The generated images feel like visual direction boards or stylescapes, not homepage comps.
- The generated images look polished enough that they communicate atmosphere more effectively than quick HTML moodboards.
- All concepts use the same or equivalent neutral specimen content.
- `comparison.md` makes the differences and recommendation easy to understand.
- `style-review.md` makes it easy for the user to respond with comments like `heading too big`, `spacing too tight`, `too dark`, `too decorative`, `images too dominant`, `corners too soft`, or `too generic`.
- Each `concept-*.md` records enough exact type, color, and prompt detail that later steps can translate the approved direction into structured design rules without guessing.
- `asset-sources.md` lists every external image, icon, or reference asset actually used, and clearly notes when a concept is fully generated versus reference-assisted.
- After approval, the guideline files are specific enough for later steps to preserve the chosen style without guessing.

## Constraints

- Do not use `outputs/04-messaging-framework/` or `outputs/05-copywriting/` as required inputs for this step.
- Do not build a full homepage.
- Do not build service, project, process, or contact sections as if this were page design.
- Do not create the pre-approval stylescapes in HTML.
- Do not use real page copy as the driver of the concept.
- Do not include detailed forms, long service lists, or page-level information architecture.
- Do not let the previews become content-review artifacts, page-strategy artifacts, or copy experiments.
- Do not let repeated cards become the primary design idea.
- Do not create 3 minor variations of the same look.
- Do not add editor-facing notes or instructional text into the visible UI.
- Do not invent fake contact details or distracting placeholder content.
- Do not use generic default font stacks unless an existing brand system explicitly requires them.
- Do not rely on long readable generated text, exact font rendering, or exact hex fidelity inside the image itself for critical decisions.
- Keep the generated boards local, easy to review, and saved directly in `outputs/06-visual-direction/`.
- If icons are implied, keep the icon treatment direction consistent within each concept.
- If the image model generates distracting text artifacts or malformed interface details, regenerate or revise until the board is reviewable.
- Log every external asset used in `asset-sources.md`.

## Execution Notes

- Start by defining 3 distinct visual theses before generating any images.
- Write each `concept-*.md` before finalizing the corresponding image so the generated board is anchored to an explicit design hypothesis.
- Use the same specimen content across all 3 concepts so the comparison stays fair.
- Keep visible copy short, neutral, and user-facing.
- Use the generated image to present style, not content strategy.
- If a built-in image-generation tool is unavailable, use `resources/scripts/openrouter_image_gen.py` as the local fallback.
- The default OpenRouter model for this workflow is `google/gemini-3.1-flash-image-preview`.
- The operator may override that model in this workflow instruction for a given run when a different image model is preferred.
- Focus on immediate visual judgment:
  - typography
  - color
  - whitespace
  - imagery
  - composition
  - surface treatment
- Ask for a stylescape, moodboard, or visual-direction board rather than a production-ready homepage screenshot.
- Show enough structure to judge hierarchy, spacing, color, imagery, and overall atmosphere, but do not build a full production-ready homepage.
- Give each concept one dominant compositional move.
- Use cards only where the content is naturally list-like.
- The concept should still be understandable even if all body copy is replaced later.
- Keep exact font names, palette roles, hex values, and rationale in `concept-*.md` instead of depending on the generated image to render them faithfully.
- Save only the selected final image for each concept as `concept-a.png`, `concept-b.png`, and `concept-c.png` in `outputs/06-visual-direction/`.
- `style-review.md` should make it easy for the user to react with comments such as "heading too big", "spacing too tight", or "images too dominant".
- Use `resources/high-quality-web-design.md` as supporting guidance for hierarchy, whitespace, imagery, and generic-risk checks.
- After the user approves one concept, translate that approved image-led direction into `recommended-direction.md`, `visual-guidelines.md`, and `visual-guidelines.html` so later steps still receive structured implementation guidance.

## Stop Conditions Or Approval Gates

- Stop after creating `concept-a.md`, `concept-b.md`, `concept-c.md`, `concept-a.png`, `concept-b.png`, `concept-c.png`, `comparison.md`, `style-review.md`, and `asset-sources.md`.
- Ask the user to approve one concept before creating `recommended-direction.md`, `visual-guidelines.md`, and `visual-guidelines.html`.
- Stop and ask the user if the concepts still feel too similar, too generic, too boxy, or too template-like.
- Stop and ask the user if the result still looks like page comps or homepage screenshots instead of stylescapes.
- Stop and ask the user if text artifacts, anatomy errors, or other generation defects make the comparison unreliable.
- Stop and ask the user if content differences are affecting the comparison.
- Stop and ask the user if the available environment cannot generate the required image outputs.
- Stop and ask the user if required brand inputs or licensing information are missing.
