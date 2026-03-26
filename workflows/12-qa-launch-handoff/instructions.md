# 12 QA Launch Handoff

## Brief Description

Validate the website for launch readiness and produce the operational documentation needed for deployment and handoff.

## Expected Input

- `outputs/11-ai-first-development/site-build/`
- `outputs/11-ai-first-development/verification-checklist.md`
- `outputs/11-ai-first-development/issues-and-decisions.md` if present
- Prior strategic, content, design, and technical outputs as validation references

## Expected Outputs

Create the following files inside `outputs/12-qa-launch-handoff/`:

- `qa-report.md`: Findings across functionality, responsiveness, accessibility, content fidelity, and visual consistency
- `launch-checklist.md`: Pre-launch checks, deployment checks, analytics readiness, and rollback considerations
- `handoff.md`: Final handoff notes, maintenance considerations, and known issues
- `rework-brief.md`: Only if the site is not launch-ready; identify the blocking issues, the owning workflow step to revisit, any required user input, and the recommended next action

## Success Criteria

- Critical issues are identified clearly
- Launch readiness is assessed honestly
- If the site is not launch-ready, the required rework path is explicit enough for another agent or the user to continue without guessing
- Handoff documentation is sufficient for another person or agent to continue work safely

## Constraints

- Do not mark the site as launch-ready if critical issues remain
- Keep known issues explicit and prioritized
- Do not silently fix implementation, copy, design, or architecture inside the QA step; route the work to the correct upstream step instead
- Do not modify files outside `outputs/12-qa-launch-handoff/`

## Execution Notes

- Validate the build against the original strategic, content, and design intent, not only against code-level correctness
- Separate critical launch blockers from minor polish items
- Make it clear which issues must be fixed before launch and which can be deferred safely
- If QA fails because the implementation does not match already approved artifacts, direct the rework back to `11-ai-first-development` with a concrete fix list
- If QA fails because approved copy, design system, high-fidelity design, or technical planning is missing, contradictory, or no longer sufficient, direct the rework back to the earliest owning workflow step and name that step explicitly
- If QA fails because external inputs are missing, such as final contact details, canonical domain, analytics IDs, deployment access, or legal text, recommend that the user provide those inputs before rerunning the affected workflow step
- If QA reveals multiple valid resolutions with user-facing tradeoffs, stop and ask the user for a decision instead of choosing unilaterally
- Use `rework-brief.md` to name the blocker, severity, owning step, required user action, and recommended next move

## Stop Conditions Or Approval Gates

- Stop and ask the user if the implementation outputs needed for validation are missing or incomplete
- Stop and ask the user before declaring launch readiness when unresolved issues remain ambiguous in severity
- Stop and ask the user if QA reveals a subjective product, visual, or content tradeoff that requires user preference
- Stop and ask the user if the fix would require changing an approved upstream artifact and the preferred direction is unclear
- Stop and ask the user if unresolved blockers depend on external credentials, deployment access, or business inputs that are not present in the repository
- Stop and ask the user if deployment or handoff requirements are unclear and materially affect the launch checklist
