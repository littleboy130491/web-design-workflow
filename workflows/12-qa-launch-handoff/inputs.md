# Inputs

- Required: `outputs/11-ai-first-development/site-build/`
  - Source: previous workflow step `11-ai-first-development`
  - Use: the actual flat HTML build and shipped assets that must be validated for launch readiness

- Required: `outputs/11-ai-first-development/verification-checklist.md`
  - Source: previous workflow step `11-ai-first-development`
  - Use: the implementation-step verification record that QA must confirm, extend, or correct

- Optional: `outputs/11-ai-first-development/issues-and-decisions.md`
  - Source: previous workflow step `11-ai-first-development`
  - Use: prior implementation deviations, blockers, or tradeoffs that QA must take into account

- Required: prior strategic, content, design, and technical outputs used as validation references
  - Source: previous workflow steps `01` through `10` as applicable
  - Use: confirm the built site matches approved strategy, content, design system, page design, and technical intent
  - At minimum, review `outputs/03-content-direction/site-map.md`, the approved page copy in `outputs/05-copywriting/`, `outputs/08-design-system/design-tokens.md`, `outputs/08-design-system/component-specs.md`, `outputs/08-design-system/interaction-guidelines.md`, `outputs/08-design-system/accessibility-rules.md`, `outputs/09-high-fidelity-design/page-design-specs.md`, `outputs/09-high-fidelity-design/responsive-notes.md`, and `outputs/10-technical-architecture/implementation-plan.md`
