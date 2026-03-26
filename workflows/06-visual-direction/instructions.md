# 06 Visual Direction

## Brief Description

Create 3 distinct visual direction stylescapes for the website.

Each stylescape should help the user judge immediately whether the visual style fits their preference. The goal of this step is not to design full pages or finalize copy. The goal is to present visual language clearly enough that the user can react to typography, color, spacing, imagery, composition, and surface treatment.

Each stylescape presentation must be built as a standalone HTML file using Tailwind CSS via CDN.

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
- `concept-a.html`
- `concept-b.html`
- `concept-c.html`
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
- Generic-risk note
- Best fit note
- Anti-pattern note

Keep each concept brief concise and visual-first.

## Required Structure For Each `concept-*.html`

Each HTML file must be a stylescape presentation, not a full webpage.

Use `<script src="https://cdn.tailwindcss.com"></script>` and keep the file self-contained so it opens directly in a browser.

Each stylescape HTML must include these sections in this order:

1. Concept header
   - concept name
   - one-sentence visual thesis
   - 3 to 5 style keywords

2. Typography specimen
   - H1
   - H2
   - body text
   - label text
   - button text

3. Color system
   - primary color
   - secondary color
   - accent color
   - background or surface colors
   - text colors
   - each swatch labeled with role and hex value

4. Imagery direction
   - 3 to 5 images or image panels
   - consistent crop logic
   - clear explanation in the layout of whether imagery is dominant, supporting, or restrained

5. Surface language
   - button sample
   - card or panel sample if relevant
   - form-field sample
   - border or radius or shadow treatment sample
   - icon treatment sample if icons are used

6. Composition specimen
   - one hero-style composition fragment
   - one supporting section fragment
   - these fragments should show layout attitude, not a complete homepage

7. Spacing rhythm specimen
   - visible demonstration of dense, standard, and spacious spacing behavior
   - enough for the user to react to tightness or looseness

8. Fit summary
   - short section stating what kind of brand feeling this concept creates
   - short section stating what would make it fail

## Success Criteria

- The 3 stylescapes are clearly different in composition, typography, spacing, color balance, and imagery treatment.
- The stylescapes help the user react to style immediately, without getting distracted by content.
- The HTML presentations feel like visual direction boards or stylescapes, not homepage comps.
- All concepts use the same or equivalent neutral specimen content.
- `comparison.md` makes the differences and recommendation easy to understand.
- `style-review.md` makes it easy for the user to respond with comments like `heading too big`, `spacing too tight`, `too dark`, `too decorative`, `images too dominant`, `corners too soft`, or `too generic`.
- `asset-sources.md` lists every external image or icon actually used.
- After approval, the guideline files are specific enough for later steps to preserve the chosen style without guessing.

## Constraints

- Do not use `outputs/04-messaging-framework/` or `outputs/05-copywriting/` as required inputs for this step.
- Do not build a full homepage.
- Do not build service, project, process, or contact sections as if this were page design.
- Do not use real page copy as the driver of the concept.
- Do not include detailed forms, long service lists, or page-level information architecture.
- Do not let the previews become content-review artifacts, page-strategy artifacts, or copy experiments.
- Do not let repeated cards become the primary design idea.
- Do not create 3 minor variations of the same look.
- Do not add editor-facing notes or instructional text into the visible UI.
- Do not invent fake contact details or distracting placeholder content.
- Do not use generic default font stacks unless an existing brand system explicitly requires them.
- Keep the HTML previews lightweight, local, and easy to open.
- Use accessible HTML structure, readable contrast, and visible focus states.
- If icons are used, use one icon family consistently.
- Log every external asset used in `asset-sources.md`.

## Execution Notes

- Start by defining 3 distinct visual theses before making any HTML.
- Use the same specimen content across all 3 concepts so the comparison stays fair.
- Keep visible copy short, neutral, and user-facing.
- Use the HTML to present style, not content strategy.
- Focus on immediate visual judgment:
  - typography
  - color
  - whitespace
  - imagery
  - composition
  - surface treatment
- Show enough of a page to judge hierarchy, spacing, color, imagery, and overall atmosphere, but do not build a full production-ready homepage.
- Give each concept one dominant compositional move.
- Use cards only where the content is naturally list-like.
- Tailwind CDN is required for each `concept-*.html`.
- The concept should still be understandable even if all body copy is replaced later.
- `style-review.md` should make it easy for the user to react with comments such as "heading too big", "spacing too tight", or "images too dominant".
- Use `resources/high-quality-web-design.md` as supporting guidance for hierarchy, whitespace, imagery, and generic-risk checks.

## Stop Conditions Or Approval Gates

- Stop after creating `concept-a.*`, `concept-b.*`, `concept-c.*`, `comparison.md`, `style-review.md`, and `asset-sources.md`.
- Ask the user to approve one concept before creating `recommended-direction.md`, `visual-guidelines.md`, and `visual-guidelines.html`.
- Stop and ask the user if the concepts still feel too similar, too generic, too boxy, or too template-like.
- Stop and ask the user if the result still looks like page comps instead of stylescapes.
- Stop and ask the user if content differences are affecting the comparison.
- Stop and ask the user if required brand inputs or licensing information are missing.
