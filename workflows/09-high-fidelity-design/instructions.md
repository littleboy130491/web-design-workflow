# 09 High Fidelity Design

## Brief Description

Resolve the final UI design for key pages by generating and approving AI-assisted visual references before HTML implementation begins.

## Expected Input

- Relevant page copy from `outputs/05-copywriting/`
- `outputs/06-visual-direction/recommended-direction.md`
- `outputs/06-visual-direction/visual-guidelines.md`
- `outputs/06-visual-direction/visual-guidelines.html`
- `outputs/07-information-architecture-and-wireframes/page-blueprints.md`
- `outputs/07-information-architecture-and-wireframes/wireframes.md`
- `outputs/08-design-system/design-tokens.md`
- `outputs/08-design-system/component-specs.md`
- `outputs/06-visual-direction/asset-sources.md` if previously approved external photos or icons are part of the design direction

## Expected Outputs

Create the following files inside `outputs/09-high-fidelity-design/`:

- `visual-comps/`: AI-generated visual reference images used to choose the final design direction
- `visual-comps/concept-a/`, `visual-comps/concept-b/`, `visual-comps/concept-c/`, and additional named concept folders as needed when the user asks for alternatives or when the first pass fails the design bar
- `visual-comps/concept-x/homepage-comp.png`: Homepage reference image for each generated concept
- `visual-comps/concept-x/inner-page-comp.png`: Representative inner-page reference image for each generated concept
- `visual-comps/section-crops/`: Optional cropped section references when the implementation needs clearer guidance for hero, cards, CTA, footer, or other dense sections
- `comp-review.md`: Pass or fail review of each explored comp set against the design bar, anti-pattern checklist, and approval decision
- `approved-direction.md`: Which generated concept was approved, where its files live, what must be preserved in implementation, and what remains flexible
- `implementation-mapping.md`: Translation of the approved visual references into implementation rules covering layout, spacing, hierarchy, image treatment, typography emphasis, and responsive intent
- `page-design-specs.md`: Final layout, component usage, visual hierarchy, and page-specific notes
- `responsive-notes.md`: Mobile and desktop behavior, breakpoints, and adaptation rules
- `design-decisions.md`: Important design decisions and why they were made
- `asset-sources.md` only if new external photo or icon assets are introduced during this step

## Success Criteria

- AI-generated visual references exist for the homepage and at least one representative inner page before implementation begins
- Each explored concept is stored as a separate named visual-comp set rather than mixed together
- One visual direction is explicitly approved rather than left implicit
- `comp-review.md` records what was explored, what failed, what passed, and why the approved option is acceptable
- The approved visual references are translated into implementation guidance clearly enough for development
- Key pages are specified clearly enough for development
- Real content fits without breaking hierarchy
- Responsive behavior is resolved at the spec level
- Page-level design decisions remain consistent with the approved design system and earlier visual-direction rules
- Any newly introduced stock photos or icons are documented clearly enough for review and implementation
- The approved comp set demonstrates a clear dominant composition above the fold rather than a stack of similarly weighted boxes
- The approved comp set uses cards and panels only as supporting structures, not as the primary visual answer to every section
- If the first exploration pass produces generic, boxy, or template-like results, at least one additional exploration pass is created before any direction is approved

## Constraints

- Do not let visual styling override readability or conversion logic
- Stay consistent with the approved design system
- Do not treat generated images as permission to invent new copy, structure, or brand direction
- Do not move to implementation before at least one homepage reference and one inner-page reference are approved
- Do not merge multiple alternative concepts into a hybrid direction unless the user explicitly asks for that
- Do not rewrite approved page copy into explanatory design notes
- Use previously approved imagery and iconography rules unless there is a documented reason to extend them
- Do not approve a comp where most major sections are rendered as equal-height cards, equal-width panels, or repetitive boxed rows without a stronger compositional idea
- Do not rely on rounded corners, soft shadows, chips, or staggered spacing alone to signal a premium result
- Do not treat a legible but template-like layout as acceptable high fidelity
- Do not lock a comp if it can reasonably be described as a stack of information cards with images attached
- Agents are allowed to search Unsplash for stock photography and Heroicons for interface icons when page-level design work requires it
- If new external photo or icon assets are introduced in this step, log them in `asset-sources.md`
- Respect source licensing terms; if usage rights are unclear, stop and ask the user before continuing

## Execution Notes

- Use the real copy, not placeholder text
- Generate multiple AI visual directions when the user asks for alternatives, and keep each concept in its own named folder
- If the user asks for more alternatives, make them meaningfully different in composition, hierarchy, density, or visual tone rather than near-duplicates
- If the first pass feels generic, boxy, or overly modular, generate another exploration pass before approval even if the user did not explicitly request alternatives
- Lock one approved direction before treating the step as complete
- Treat the generated images as binding reference for composition, density, hierarchy, color balance, and image treatment, not as a pixel-perfect frontend spec
- Review each comp for hero dominance, section rhythm, density contrast, whitespace, and overuse of similarly weighted boxes before approving it
- Favor fewer, larger compositional moves over many small support cards when both can solve the same content problem
- Use `comp-review.md` to record design-bar checks, rejected anti-patterns, and the exact reason an approved comp passes
- Record in `approved-direction.md` which concept won, why it won, and whether any non-winning concepts should still influence implementation
- Use `implementation-mapping.md` to state what must be preserved in HTML and what may adapt during responsive implementation
- Document any deviations from earlier wireframes or system rules
- If textual content is included in the specs, treat it as page copy or UI text, not as a place for editorial commentary
- Prefer previously approved photo and icon sources from earlier steps before introducing new external assets
- If new icons are required for UI examples, prefer Heroicons so icon style remains consistent with earlier design artifacts

## Stop Conditions Or Approval Gates

- Stop and ask the user if required upstream design-system inputs are missing
- Stop and ask the user if page requirements force a major deviation from the approved visual direction or component system
- Stop and ask the user if multiple generated visual directions are viable and the preferred direction is not obvious from the approved visual-guidance artifacts
- Stop and ask the user to choose a concept before handing off to step `10-technical-architecture` or step `11-ai-first-development` when multiple alternatives exist and none has been explicitly approved
- Stop and ask the user if generated visuals fail to meet the expected design bar and another round of exploration would materially change the direction
- Stop and ask the user if two exploration passes still feel too generic, too boxy, or too template-like to approve honestly
- Stop and ask the user before approval if `comp-review.md` still contains unresolved anti-pattern findings such as card-wall layouts, weak hero dominance, or repetitive equal-weight sections
- Stop and ask the user if suitable imagery or icon assets cannot be found within the approved sourcing rules
