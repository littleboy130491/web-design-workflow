# 06 Visual Direction

## Brief Description

Develop multiple visual concepts for the website, make them reviewable in standalone HTML, and after user approval convert the chosen concept into a concrete visual-guidelines artifact expressed in Tailwind CSS and accessible in plain HTML.

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
- `concept-a.html`: Standalone HTML preview for concept A that can be opened directly in a browser
- `concept-b.html`: Standalone HTML preview for concept B that can be opened directly in a browser
- `concept-c.html`: Standalone HTML preview for concept C that can be opened directly in a browser
- `comparison.md`: Comparison of the three concepts, their tradeoffs, and a recommendation
- `recommended-direction.md`: The approved visual direction, the reason it was selected, and implementation implications for later workflow steps
- `visual-guidelines.md`: Concrete visual rules for typography, color pairing, spacing, layout, components, imagery, and iconography
- `visual-guidelines.html`: Standalone accessible HTML specimen using Tailwind CDN that demonstrates the approved visual rules
- `asset-sources.md`: Traceable list of externally sourced stock photos and icons used in the previews or guideline specimen

## Success Criteria

- At least 3 distinct visual directions are presented, with meaningful differences in typography, color use, layout attitude, and component tone
- Each direction is visually reviewable without requiring a design tool
- `comparison.md` makes the tradeoffs and recommendation clear enough for a user approval decision
- After approval, `visual-guidelines.md` explicitly defines heading, subheading, body, description, button, and label typography rules
- After approval, `visual-guidelines.md` explicitly defines color pairings, spacing scale, layout principles, and component guidance
- `visual-guidelines.html` opens directly in a browser, uses Tailwind via CDN, and visibly demonstrates typography hierarchy, color pairings, spacing, layout patterns, and core UI components
- Externally sourced photos and icons are documented in `asset-sources.md` with source site, asset URL, intended use, and the output file that uses them
- The approved direction is specific enough to guide the design system and later UI work without guessing

## Constraints

- Do not produce three minor variations of the same aesthetic
- Keep HTML previews lightweight and easy to open locally
- Use `<script src="https://cdn.tailwindcss.com"></script>` in `visual-guidelines.html`
- Configure any Tailwind theme extension or semantic token mapping inline in `visual-guidelines.html` so the artifact works without a build step
- Keep the HTML artifacts at review and guideline level, not production-ready frontend code
- Use accessible HTML structure with semantic landmarks, visible focus states, and readable text contrast
- Respect existing brand constraints if brand assets or brand rules already exist
- Avoid generic default web aesthetics
- Do not add editor-facing commentary or instructional sentences into the visible text of the previews
- Agents are allowed to search for stock photos from Unsplash when imagery is needed for concept communication
- Agents are allowed to use Heroicons for UI iconography in previews and guideline examples
- Do not use untraceable image results; every externally sourced photo or icon used in this step must be logged in `asset-sources.md`
- Respect the source licensing terms; if licensing or permitted use is unclear, stop and ask the user before continuing

## Execution Notes

- The HTML previews should be simple review artifacts, not production code
- Each concept preview should show enough of a page to judge hierarchy, type, color, imagery treatment, icon tone, and overall atmosphere
- Any visible copy in the previews should be short, user-facing, and aligned to the approved site copy rather than explanatory notes about the preview itself
- `visual-guidelines.md` should include a typography section, color section, spacing section, layout section, component section, imagery direction section, and iconography section
- `visual-guidelines.html` should include visible examples for headings, body text, descriptions, buttons, cards, navigation, form controls, section spacing, and layout containers
- Prefer Heroicons consistently if icons are shown; do not mix icon families in the same artifact without a documented reason

## Stop Conditions Or Approval Gates

- Stop after creating `concept-a.*`, `concept-b.*`, `concept-c.*`, `comparison.md`, and any supporting entries already needed in `asset-sources.md`
- Ask the user to approve one concept before creating `recommended-direction.md`, `visual-guidelines.md`, and `visual-guidelines.html`
- Stop and ask the user if required upstream content is missing and cannot be derived from repository materials
- Stop and ask the user if the project requires stricter asset licensing rules than can be confirmed from the chosen sources
