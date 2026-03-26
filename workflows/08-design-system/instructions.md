# 08 Design System

## Brief Description

Define the reusable visual and interaction system required to implement the website consistently and efficiently, using the approved visual-guideline artifacts as the stylistic source of truth.

## Expected Input

- `outputs/06-visual-direction/recommended-direction.md`
- `outputs/06-visual-direction/visual-guidelines.md`
- `outputs/06-visual-direction/visual-guidelines.html`
- `outputs/07-information-architecture-and-wireframes/page-blueprints.md`
- `outputs/07-information-architecture-and-wireframes/wireframes.md`
- `outputs/06-visual-direction/asset-sources.md` if visual-direction outputs rely on external sourced imagery or iconography

## Expected Outputs

Create the following files inside `outputs/08-design-system/`:

- `design-tokens.md`: Color, typography, spacing, radius, shadow, and other core tokens
- `component-specs.md`: Reusable components, states, variants, icon usage, and content rules
- `interaction-guidelines.md`: Motion, hover, focus, transitions, and interaction behavior
- `accessibility-rules.md`: Accessibility expectations relevant to this site and system
- `asset-sources.md` only if new external photo or icon assets are introduced during this step

## Success Criteria

- Reusable UI patterns are defined clearly enough for implementation
- Core components cover the needs of the planned site
- Accessibility expectations are explicit instead of implied
- The token and component rules stay consistent with the approved visual-guideline specimen from step `06-visual-direction`
- If icons or photography are part of the system, their usage rules are concrete enough for later design and implementation steps

## Constraints

- Do not overbuild a design system for hypothetical future needs
- Keep the system aligned to the approved visual direction
- Do not let component examples or usage notes drift into editorial prose or page-describing commentary
- Do not redefine the visual direction in this step; treat the approved visual-direction outputs as the stylistic source of truth
- If the system uses interface icons, default to Heroicons unless the approved direction explicitly justifies another family
- If the system uses sourced photography, keep it aligned to the approved imagery direction and documented sources
- If new external photo or icon assets are introduced in this step, log them in `asset-sources.md`
- Respect source licensing terms; if usage rights are unclear, stop and ask the user before continuing

## Execution Notes

- Favor practical component rules over abstract design language
- Include only the components and states the site actually needs
- Keep any sample text in component specs short and functional, using approved site copy where possible
- If icon usage is part of the system, specify Heroicons style guidance such as outline or solid usage, size ranges, alignment, and placement rules
- If photography is part of the design language, specify image treatment, crop tendency, subject matter direction, and placement rules derived from the approved visual direction
- Agents are allowed to search Unsplash for stock photography and Heroicons for interface icons when this step genuinely requires additional sourced examples or references

## Stop Conditions Or Approval Gates

- Stop and ask the user if `recommended-direction.md`, `visual-guidelines.md`, or `visual-guidelines.html` is missing
- Stop and ask the user if wireframes require component types that are not covered by the approved visual direction
- Stop and ask the user if the only way to proceed would be to introduce a different icon family or unapproved imagery direction
