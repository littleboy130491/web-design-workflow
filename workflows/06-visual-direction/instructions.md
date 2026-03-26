# 06 Visual Direction

## Brief Description

Develop multiple visual directions for the website, make them reviewable in standalone HTML, and isolate style decisions from page-copy review so the user can approve the visual language before later steps formalize it.

## Expected Input

- `outputs/01-strategy-foundation/strategy-brief.md`
- `outputs/04-messaging-framework/messaging-framework.md`
- Relevant page copy from `outputs/05-copywriting/`
- Any existing brand assets or brand constraints already present in the repository

## Expected Outputs

Create the following files inside `outputs/06-visual-direction/`:

- `concept-a.md`: Visual rationale, typography, color, imagery, iconography, motion, and layout principles for concept A
- `concept-b.md`: Visual rationale, typography, color, imagery, iconography, motion, and layout principles for concept B
- `concept-c.md`: Visual rationale, typography, color, imagery, iconography, motion, and layout principles for concept C
- `concept-a.html`: Standalone HTML preview for concept A that can be opened directly in a browser and uses the same minimal specimen content as the other concepts
- `concept-b.html`: Standalone HTML preview for concept B that can be opened directly in a browser and uses the same minimal specimen content as the other concepts
- `concept-c.html`: Standalone HTML preview for concept C that can be opened directly in a browser and uses the same minimal specimen content as the other concepts
- `comparison.md`: Comparison of the three concepts, their tradeoffs, composition differences, generic-risk assessment, and a recommendation
- `style-review.md`: Structured review artifact that lists the visual variables the user should react to, including heading scale, spacing density, color balance, image prominence, border treatment, radius, shadow, and icon tone
- `recommended-direction.md`: The approved visual direction, the reason it was selected, and implementation implications for later workflow steps
- `visual-guidelines.md`: Concrete visual rules for typography, color pairing, spacing, composition, layout, components, imagery, iconography, and anti-patterns to avoid
- `visual-guidelines.html`: Standalone accessible HTML specimen using Tailwind CDN that demonstrates the approved visual rules
- `asset-sources.md`: Traceable list of externally sourced stock photos and icons used in the previews or guideline specimen

## Success Criteria

- At least 3 distinct visual directions are presented, with meaningful differences in composition, type attitude, color balance, spacing rhythm, and image treatment
- All concept previews use the same or equivalent minimal specimen content so the comparison stays focused on style instead of copy
- Each direction is visually reviewable without requiring a design tool
- `comparison.md` makes the tradeoffs and recommendation clear enough for a user approval decision and explicitly notes where a concept risks looking generic, template-like, or overly modular
- `style-review.md` gives the user clear style levers to react to, including what feels too tight, too large, too decorative, too flat, too dark, or too generic
- The concept previews are specific enough to guide later design work without drifting into page-level copywriting or implementation detail
- After approval, `visual-guidelines.md` explicitly defines heading, subheading, body, description, button, and label typography rules
- After approval, `visual-guidelines.md` explicitly defines color pairings, spacing scale, composition rules, layout principles, component guidance, and anti-patterns
- `visual-guidelines.html` opens directly in a browser, uses Tailwind via CDN, and visibly demonstrates typography hierarchy, color pairings, spacing, layout patterns, signature composition patterns, and core UI components
- Externally sourced photos and icons are documented in `asset-sources.md` with source site, asset URL, intended use, and the output file that uses them
- The approved direction is specific enough to guide the design system and later UI work without guessing
- At least one concept proves a non-generic premium direction through scale contrast, dominant media or content framing, and section rhythm rather than through repeated cards alone
- The approved direction defines how to avoid a page that looks like stacked information cards, agency-template blocks, or dashboard-like panels with swapped copy

## Constraints

- Do not produce three minor variations of the same aesthetic
- Keep HTML previews lightweight and easy to open locally
- Use `<script src="https://cdn.tailwindcss.com"></script>` in `visual-guidelines.html`
- Configure any Tailwind theme extension or semantic token mapping inline in `visual-guidelines.html` so the artifact works without a build step
- Keep the HTML artifacts at review and guideline level, not production-ready frontend code
- Use accessible HTML structure with semantic landmarks, visible focus states, and readable text contrast
- Respect existing brand constraints if brand assets or brand rules already exist
- Avoid generic default web aesthetics
- Do not use generic default font stacks in the previews unless an existing brand system explicitly requires them
- Do not add editor-facing commentary or instructional sentences into the visible text of the previews
- Do not let the previews become content-review artifacts, page-strategy artifacts, or copy experiments
- Do not invent persuasive copy, fake contact details, or UI labels that are not grounded in approved copy or neutral specimen text
- Do not equate premium with rounded boxes, shadows, pill tags, or staggered cards alone
- Do not let every section resolve to equal-weight cards, equal-width grids, or interchangeable panels
- Do not approve a direction that could be mistaken for a generic SaaS, dashboard, or agency template after the copy is swapped
- Agents are allowed to search for stock photos from Unsplash when imagery is needed for concept communication
- Agents are allowed to use Heroicons for UI iconography in previews and guideline examples
- Do not use untraceable image results; every externally sourced photo or icon used in this step must be logged in `asset-sources.md`
- Respect the source licensing terms; if licensing or permitted use is unclear, stop and ask the user before continuing

## Execution Notes

- The HTML previews should be simple review artifacts, not production code
- Each concept preview should show enough of a page to judge hierarchy, type, color, imagery treatment, icon tone, and overall atmosphere
- Use minimal, neutral, reusable specimen content across all concepts so the visual comparison stays fair
- Any visible copy in the previews should be short, user-facing, and aligned to approved copy or neutral specimen text rather than explanatory notes about the preview itself
- Treat composition, scale contrast, whitespace, and section rhythm as first-class decisions before component styling
- Give each concept a primary compositional device such as a feature canvas, gallery rail, editorial split, proof band, or framed content block, and describe how supporting sections avoid becoming repetitive card walls
- If cards appear in a concept, use them as support for list-like content rather than as the universal container for every section
- The previews should help the user react to style choices such as heading size, spacing density, image dominance, border sharpness, radius softness, shadow weight, and color balance
- `style-review.md` should include a structured prompt set for typography, spacing and density, layout and composition, imagery and crop style, icon usage, border or radius or shadow treatment, and color and contrast
- `visual-guidelines.md` should include a typography section, color section, spacing section, composition section, layout section, component section, imagery direction section, iconography section, and an anti-patterns section
- The composition section should define dominant block hierarchy, density changes between sections, acceptable grid usage, and how many similarly weighted boxes may appear before the layout is considered too repetitive
- `visual-guidelines.html` should include visible examples for headings, body text, descriptions, buttons, cards, navigation, form controls, section spacing, layout containers, and at least one signature non-card-led composition pattern
- Prefer Heroicons consistently if icons are shown; do not mix icon families in the same artifact without a documented reason

## Stop Conditions Or Approval Gates

- Stop after creating `concept-a.*`, `concept-b.*`, `concept-c.*`, `comparison.md`, `style-review.md`, and any supporting entries already needed in `asset-sources.md`
- Ask the user to approve one concept before creating `recommended-direction.md`, `visual-guidelines.md`, and `visual-guidelines.html`
- Stop and ask the user if required upstream content is missing and cannot be derived from repository materials
- Stop and ask the user if all viable concepts still feel too generic, too boxy, or too template-like after the first exploration pass
- Stop and ask the user if the previews cannot be compared fairly because content differences are affecting the judgment
- Stop and ask the user before approving a direction if the only differentiators are palette, typography, or card styling rather than composition
- Stop and ask the user if the project requires stricter asset licensing rules than can be confirmed from the chosen sources
