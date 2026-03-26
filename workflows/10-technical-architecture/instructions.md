# 10 Technical Architecture

## Brief Description

Define the leanest implementation plan that lets an AI agent build the approved site without unnecessary framework or documentation overhead.

## Expected Input

- `outputs/03-content-direction/site-map.md`
- `outputs/08-design-system/design-tokens.md`
- `outputs/08-design-system/component-specs.md`
- `outputs/08-design-system/interaction-guidelines.md`
- `outputs/08-design-system/accessibility-rules.md`
- `outputs/09-high-fidelity-design/page-design-specs.md`
- `outputs/09-high-fidelity-design/responsive-notes.md`
- `outputs/09-high-fidelity-design/design-decisions.md` if present and relevant

## Expected Outputs

Create the following files inside `outputs/10-technical-architecture/`:

- `implementation-plan.md`: One consolidated execution plan covering stack, file structure, page-to-file mapping, repeated patterns, SEO and form handling, performance decisions, build order, and AI task boundaries
- `open-questions.md`: Only if unresolved technical, deployment, or external-input questions still block implementation

## Success Criteria

- The implementation plan is concrete enough to execute without additional architecture documents
- The plan reflects the approved site scope, page structure, responsiveness, and accessibility requirements
- The stack and file structure are simple enough for a static HTML implementation to proceed directly
- AI usage is structured around bounded, reviewable execution tasks

## Constraints

- Avoid vague stack choices without rationale
- Do not introduce a framework, build pipeline, or CMS unless the user explicitly asks for one
- Do not rely on one-shot generation for the full build
- Prefer a single implementation plan over multiple coordination documents
- Do not modify files outside `outputs/10-technical-architecture/`

## Execution Notes

- Default to plain static HTML as the implementation target for this workflow
- Treat Tailwind CDN as acceptable when it matches the approved execution approach
- Capture build order, repeated component patterns, and review gates as sections inside `implementation-plan.md` rather than separate files
- Use `open-questions.md` only when unresolved inputs or deployment constraints would otherwise force guessing

## Stop Conditions Or Approval Gates

- Stop and ask the user if required design-system or high-fidelity-design inputs are missing
- Stop and ask the user if deployment constraints, stack constraints, or hosting assumptions are unclear and materially affect the architecture
- Stop and ask the user if the simplest viable implementation approach is unclear because the approved artifacts imply conflicting technical directions
- Stop and ask the user if the proposed implementation would require a major deviation from approved design or content outputs
