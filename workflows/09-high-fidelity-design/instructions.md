# 09 High Fidelity Design

## Brief Description

Resolve the final UI design for key pages using real content, the approved design system, the agreed page structure, and any approved photo or icon sources carried forward from earlier design steps.

## Expected Input

- Relevant page copy from `outputs/05-copywriting/`
- `outputs/07-information-architecture-and-wireframes/page-blueprints.md`
- `outputs/08-design-system/design-tokens.md`
- `outputs/08-design-system/component-specs.md`
- `outputs/06-visual-direction/asset-sources.md` if previously approved external photos or icons are part of the design direction

## Expected Outputs

Create the following files inside `outputs/09-high-fidelity-design/`:

- `page-design-specs.md`: Final layout, component usage, visual hierarchy, and page-specific notes
- `responsive-notes.md`: Mobile and desktop behavior, breakpoints, and adaptation rules
- `design-decisions.md`: Important design decisions and why they were made
- `asset-sources.md` only if new external photo or icon assets are introduced during this step

## Success Criteria

- Key pages are specified clearly enough for development
- Real content fits without breaking hierarchy
- Responsive behavior is resolved at the spec level
- Page-level design decisions remain consistent with the approved design system and earlier visual-direction rules
- Any newly introduced stock photos or icons are documented clearly enough for review and implementation

## Constraints

- Do not let visual styling override readability or conversion logic
- Stay consistent with the approved design system
- Do not rewrite approved page copy into explanatory design notes
- Use previously approved imagery and iconography rules unless there is a documented reason to extend them
- Agents are allowed to search Unsplash for stock photography and Heroicons for interface icons when page-level design work requires it
- If new external photo or icon assets are introduced in this step, log them in `asset-sources.md`
- Respect source licensing terms; if usage rights are unclear, stop and ask the user before continuing

## Execution Notes

- Use the real copy, not placeholder text
- Document any deviations from earlier wireframes or system rules
- If textual content is included in the specs, treat it as page copy or UI text, not as a place for editorial commentary
- Prefer previously approved photo and icon sources from earlier steps before introducing new external assets
- If new icons are required for UI examples, prefer Heroicons so icon style remains consistent with earlier design artifacts

## Stop Conditions Or Approval Gates

- Stop and ask the user if required upstream design-system inputs are missing
- Stop and ask the user if page requirements force a major deviation from the approved visual direction or component system
- Stop and ask the user if suitable imagery or icon assets cannot be found within the approved sourcing rules
