# Inputs

- Required: `outputs/03-content-direction/site-map.md`
  - Source: previous workflow step `03-content-direction`
  - Use: canonical page inventory and route list for determining which HTML pages must exist in the generated build

- Required: `outputs/05-copywriting/home.md`
  - Source: previous workflow step `05-copywriting`
  - Use: approved homepage copy

- Required: `outputs/05-copywriting/services.md`
  - Source: previous workflow step `05-copywriting`
  - Use: approved services page copy

- Required: `outputs/05-copywriting/projects.md`
  - Source: previous workflow step `05-copywriting`
  - Use: approved projects page copy

- Required: `outputs/05-copywriting/process.md`
  - Source: previous workflow step `05-copywriting`
  - Use: approved process page copy

- Required: `outputs/05-copywriting/about.md`
  - Source: previous workflow step `05-copywriting`
  - Use: approved about page copy

- Required: `outputs/05-copywriting/contact.md`
  - Source: previous workflow step `05-copywriting`
  - Use: approved contact page copy

- Required: `outputs/05-copywriting/seo-metadata.md`
  - Source: previous workflow step `05-copywriting`
  - Use: approved title tags, meta descriptions, and page metadata

- Required: `outputs/05-copywriting/microcopy.md`
  - Source: previous workflow step `05-copywriting`
  - Use: approved labels, helper text, CTA labels, and other interface copy

- Required: `outputs/08-design-system/design-tokens.md`
  - Source: previous workflow step `08-design-system`
  - Use: approved token rules for implementing the visual system

- Required: `outputs/08-design-system/component-specs.md`
  - Source: previous workflow step `08-design-system`
  - Use: approved repeated component structure and behavior

- Required: `outputs/08-design-system/interaction-guidelines.md`
  - Source: previous workflow step `08-design-system`
  - Use: approved interaction and state behavior

- Required: `outputs/08-design-system/accessibility-rules.md`
  - Source: previous workflow step `08-design-system`
  - Use: approved accessibility rules that must be enforced in the build

- Required: `outputs/09-high-fidelity-design/page-design-specs.md`
  - Source: previous workflow step `09-high-fidelity-design`
  - Use: page-level design specifications for implementation fidelity

- Required: `outputs/09-high-fidelity-design/approved-direction.md`
  - Source: previous workflow step `09-high-fidelity-design`
  - Use: the approved visual direction that must be preserved in the HTML implementation

- Required: `outputs/09-high-fidelity-design/implementation-mapping.md`
  - Source: previous workflow step `09-high-fidelity-design`
  - Use: the approved translation of image-based visual decisions into implementation rules

- Required: `outputs/09-high-fidelity-design/visual-comps/`
  - Source: previous workflow step `09-high-fidelity-design`
  - Use: approved AI-generated visual reference images that the HTML build must follow

- Required: `outputs/09-high-fidelity-design/responsive-notes.md`
  - Source: previous workflow step `09-high-fidelity-design`
  - Use: responsive behavior that must be preserved in the build

- Optional: `outputs/09-high-fidelity-design/design-decisions.md`
  - Source: previous workflow step `09-high-fidelity-design`
  - Use: approved design tradeoffs or exceptions that affect implementation

- Required: `outputs/10-technical-architecture/implementation-plan.md`
  - Source: previous workflow step `10-technical-architecture`
  - Use: the consolidated implementation approach, build order, and AI task boundaries

- Optional: `outputs/10-technical-architecture/open-questions.md`
  - Source: previous workflow step `10-technical-architecture`
  - Use: unresolved technical or external-input questions that still constrain implementation
