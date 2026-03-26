# 07 Information Architecture And Wireframes

## Brief Description

Convert the approved content and visual direction into page blueprints, section hierarchy, UX flow, and low-fidelity wireframes.

## Expected Input

- `outputs/03-content-direction/site-map.md`
- Relevant page copy from `outputs/05-copywriting/`
- `outputs/06-visual-direction/recommended-direction.md`
- `outputs/06-visual-direction/visual-guidelines.md` if additional approved structural guidance is needed
- `outputs/06-visual-direction/asset-sources.md` if the wireframes include approved sourced image references or icon references

## Expected Outputs

Create the following files inside `outputs/07-information-architecture-and-wireframes/`:

- `page-blueprints.md`: Page-by-page section sequence, section goal, and conversion role
- `wireframes.md`: Low-fidelity structural wireframes and responsive notes
- `flow-notes.md`: Navigation logic, page transitions, and CTA path notes
- `asset-sources.md` only if new external photo or icon assets are introduced during this step

## Success Criteria

- Every core page has a clear structural plan
- Information hierarchy supports scanning and conversion
- Wireframes are sufficient to reduce layout ambiguity before detailed design
- Any sourced photo or icon references used in this step are documented clearly enough for later review

## Constraints

- Prioritize clarity and structure over visual polish
- Keep wireframes aligned with real content lengths
- Keep wireframe labels and annotations structural, not narrative or editorial
- Do not let image or icon selection dominate the purpose of the wireframe
- Agents are allowed to search Unsplash for stock photography and Heroicons for interface icons when specific references are needed to clarify structure or content intent
- Prefer labeled placeholders unless a sourced photo or icon reference materially improves structural clarity
- If new external photo or icon assets are introduced in this step, log them in `asset-sources.md`
- Respect source licensing terms; if usage rights are unclear, stop and ask the user before continuing
- Do not modify files outside `outputs/07-information-architecture-and-wireframes/`

## Execution Notes

- Define where proof, CTAs, and contact triggers appear
- Ensure the page structure supports both desktop and mobile use
- If text appears in the wireframes, it should be approved page copy or terse UI labeling, not commentary about the wireframe or page artifact
- If sourced imagery or icons are shown, treat them as supporting references for structure and intent, not as final visual-design decisions

## Stop Conditions Or Approval Gates

- Stop and ask the user if required upstream content or visual-direction inputs are missing
- Stop and ask the user if the only way to continue would be to turn the wireframes into high-fidelity page design
- Stop and ask the user if suitable sourced image or icon references cannot be found within the approved sourcing rules
