# 11 AI First Development

## Brief Description

Implement the website using an AI-first workflow that still keeps code quality, design accuracy, and reviewability under control.

## Expected Input

- `outputs/03-content-direction/site-map.md`
- `outputs/05-copywriting/home.md`
- `outputs/05-copywriting/services.md`
- `outputs/05-copywriting/projects.md`
- `outputs/05-copywriting/process.md`
- `outputs/05-copywriting/about.md`
- `outputs/05-copywriting/contact.md`
- `outputs/05-copywriting/seo-metadata.md`
- `outputs/05-copywriting/microcopy.md`
- `outputs/08-design-system/design-tokens.md`
- `outputs/08-design-system/component-specs.md`
- `outputs/08-design-system/interaction-guidelines.md`
- `outputs/08-design-system/accessibility-rules.md`
- `outputs/09-high-fidelity-design/page-design-specs.md`
- `outputs/09-high-fidelity-design/approved-direction.md`
- `outputs/09-high-fidelity-design/implementation-mapping.md`
- `outputs/09-high-fidelity-design/visual-comps/`
- `outputs/09-high-fidelity-design/responsive-notes.md`
- `outputs/09-high-fidelity-design/design-decisions.md` if present and relevant
- `outputs/10-technical-architecture/implementation-plan.md`
- `outputs/10-technical-architecture/open-questions.md` if present

## Expected Outputs

Create the following files inside `outputs/11-ai-first-development/`:

- `site-build/`: Reviewable generated site artifact that can be opened or served locally
- `site-build/index.html`: Homepage output
- `site-build/<page>.html`: One generated HTML file per approved non-home page, for example `about.html`, `services.html`, and `contact.html`
- `site-build/assets/`: Only if local images, icons, JavaScript, or other shipped assets are actually required by the implementation
- `site-build-alt1/`, `site-build-alt2/`, and additional numbered alternative build folders as needed when the user requests more alternatives
- `site-build-altN/index.html`: Homepage output for each requested alternative build
- `site-build-altN/<page>.html`: One generated HTML file per approved non-home page for each requested alternative build
- `site-build-altN/assets/`: Only if local images, icons, JavaScript, or other shipped assets are actually required by each alternative build
- `verification-checklist.md`: Completed verification results for content fidelity, design fidelity, accessibility, responsiveness, SEO, and functional checks
- `issues-and-decisions.md`: Only if deviations, blockers, tradeoffs, or user-approved changes need to be recorded

## Success Criteria

- Every approved page in `site-map.md` has a corresponding generated HTML file in `site-build/`
- The homepage is emitted at `site-build/index.html`
- Each non-home page is emitted as a flat HTML file such as `site-build/about.html`
- Each requested alternative build emits the same approved page set unless the user explicitly narrows the scope
- Each requested alternative build differs in layout structure in a way that is visible and reviewable, not only through minor styling changes
- Style changes are introduced for alternative builds only when the user explicitly asks for them or approves them after being asked
- The implementation remains a plain HTML build that can be reviewed locally without a framework runtime
- The implementation follows the approved content, design, and technical plan
- AI-generated work is reviewed and corrected as needed
- Deviations and blockers are documented when they exist instead of being silently accepted
- Verification is performed during development, not only at the end

## Constraints

- Do not trust generated code without inspection
- Do not drift from the approved design and copy without recording the change
- Keep execution incremental and testable
- Keep the implementation directly reviewable; prefer flat HTML files and Tailwind CDN when that is the approved stack
- Do not introduce a framework, build pipeline, or unnecessary source abstraction unless the user explicitly asks for it
- Do not create tracking artifacts that do not materially help implementation or QA
- If the user asks for more alternatives, do not produce a near-duplicate; each alternative must use a meaningfully different layout
- If the user asks for more alternatives, ask whether the visual style should also change or whether only the layout should change
- Do not modify files outside `outputs/11-ai-first-development/` unless the user explicitly asks for build artifacts or source changes elsewhere

## Execution Notes

- Use AI for bounded tasks such as component scaffolding, refactors, repetitive patterns, and issue triage
- Treat `site-map.md` as the source of truth for required routes and page coverage
- Treat the approved visual references from step `09-high-fidelity-design` as binding implementation guidance for layout, hierarchy, density, and image treatment
- If step `09-high-fidelity-design` contains multiple concept folders, implement only the concept selected in `approved-direction.md` unless the user explicitly asks for an HTML alternative build
- Prefer editing the actual files in `site-build/` directly when the approved stack is plain HTML
- Use Tailwind CDN utility classes directly in the HTML when that is the approved execution approach
- Create `site-build/assets/` only when the implementation actually ships local images, icons, JavaScript, or other assets
- Keep the primary implementation in `site-build/`; write each additional user-requested alternative into the next available numbered folder such as `site-build-alt1/` and `site-build-alt2/`
- When building an alternative, preserve the approved content scope unless the user explicitly asks for page additions or removals
- Keep `issues-and-decisions.md` concise and create it only when there is something real to record
- Review generated code against design specs, content fidelity, responsiveness, and maintainability
- Keep `verification-checklist.md` current enough that another agent can see what was actually verified and what still needs checking

## Stop Conditions Or Approval Gates

- Stop and ask the user if required content, design, or technical inputs are missing
- Stop and ask the user if `site-map.md` does not define the required pages clearly enough to determine output routes
- Stop and ask the user whether they want the visual style updated before creating any additional alternative build beyond the primary `site-build/`
- Stop and ask the user if a requested implementation change conflicts materially with approved copy, design, or architecture outputs
- Stop and ask the user if missing external inputs such as final contact details, canonical domain, analytics IDs, or deployment constraints block correct implementation
- Stop and ask the user before taking irreversible actions, external deployments, or any step that would modify production systems
