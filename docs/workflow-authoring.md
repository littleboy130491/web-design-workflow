# Workflow Authoring Instructions

## Purpose

Use these instructions when the user wants to create, revise, or approve a workflow.

Author workflows for execution by an AI agent. The workflow definition should be clear enough that the executor can identify dependencies, confirm readiness, perform one step at a time, and verify outputs without guessing.

## Default Operating Procedure

Follow this sequence for every workflow-building request:

1. Ask the user what workflow they want to create.
2. Propose a workflow in chat before creating files.
3. For each proposed step, define inputs, outputs, success criteria, constraints, and any stop conditions the executor must obey.
4. If the user does not accept it, iterate in chat until they approve it.
5. After approval, create the workflow files and folders in the repository.

Do not skip the approval step before writing workflow artifacts unless the user explicitly asks you to do so.

## AI-Agent Execution Standard

Design every workflow step so an AI agent can execute it with minimal interpretation.

Each step should make these things explicit:

- What the step is trying to accomplish
- Exactly which inputs are required
- Whether each input comes from the user, the repository, or a previous step
- Exactly which files or folders should be created in `outputs/NN-name/`
- How the executor can tell the step is complete
- What constraints or prohibitions apply while executing the step
- When the executor must stop and ask the user instead of continuing

Prefer instructions that are observable and verifiable over instructions that rely on taste or hidden context.

## Chat Output Format For Proposed Workflows

When proposing a workflow in chat, present each suggested workflow step with:

- Brief description
- Expected input
- Expected output
- Success criteria
- Constraints
- Stop conditions or approval gates

Keep the proposal practical and implementation-oriented. Prefer clear, numbered workflow steps.

The proposal should already be specific enough that it could be copied into workflow files with minimal rewriting.

## Iteration Rules

- If the user rejects or adjusts the workflow, revise the proposal in chat.
- Continue iterating until the user explicitly accepts it.
- Once accepted, use the approved version as the source of truth for file creation.

## Repository Output Rules

After approval, create one folder per workflow step inside `workflows/`.

Folder naming rules:

- Use a two-digit numeric prefix.
- Use a short kebab-case name.
- Format: `NN-workflow-name`
- Example: `01-brief`

Inside each workflow step folder, create exactly these files:

- `inputs.md`
- `instructions.md`

Example:

```text
workflows/
  01-brief/
    inputs.md
    instructions.md
```

## File Content Rules

### `inputs.md`

Describe the exact required inputs for the current workflow step.

For each input:

- State whether it is required or optional
- State where it comes from
- Use exact relative paths from the repository root when the input is a file or folder
- Say whether the executor can derive it from previous workflow outputs or must ask the user for it

If the input comes from a previous workflow step, state that explicitly using the prior step's output folder or specific output file path.

When referring to any file or folder in workflow definitions, use repository-relative paths such as `outputs/01-brief/summary.md` rather than absolute filesystem paths.

Example:

```md
# Inputs

- Required: `outputs/01-brief/summary.md`
  - Source: previous workflow step `01-brief`
  - Use: primary project brief for planning

- Required: target audience description
  - Source: user-provided
  - Ask the user if this information is not already available in repository materials or prior outputs
```

Do not describe inputs vaguely. Avoid phrases like "relevant docs", "assets as needed", or "whatever the user shared earlier" unless those are replaced by concrete locations or explicit user-input requirements.

### `instructions.md`

Store the workflow-step specification that was defined in chat.

At minimum, include:

- Brief description
- Expected input
- Expected output
- Success criteria
- Constraints
- Execution notes
- Stop conditions or approval gates

`instructions.md` is the place for the step contract. It should define the expected outputs for the step and where they should be created inside `outputs/NN-name/`.

When possible, make outputs machine-checkable by naming exact files, formats, and required contents.
When referring to files or folders in the instructions, use repository-relative paths consistently.

Example expectations:

- Write `outputs/02-planning/plan.md`
- Write `outputs/02-planning/open-questions.md` only if unresolved questions remain
- Do not modify files outside `outputs/02-planning/` during execution
- Stop and ask the user before continuing if required upstream input is missing and cannot be derived

## Outputs Folder Rules

Every workflow step should write its produced results into a matching folder under `outputs/`.

Example:

```text
outputs/
  02-planning/
```

1. Create a folder inside `outputs/` using the same numeric prefix and workflow name.
2. Place the generated output files in that folder.
3. If the output is Markdown, store it as one or more Markdown files inside that same `outputs/NN-name/` folder.
4. In `instructions.md`, describe the expected output files clearly enough that later execution can verify them.
5. If a step may produce multiple files, name them explicitly whenever possible instead of saying "supporting files" or "artifacts as needed".

Example:

- Workflow step: `02-planning`
- Output folder: `outputs/02-planning`

## Quality Bar

The ideal workflow should be:

- Clear enough for another AI agent or human to execute
- Sequential and dependency-aware
- Minimal but complete
- Specific about inputs and outputs
- Explicit about where outputs are written
- Explicit about what success looks like
- Honest about constraints and assumptions
- Written so the executor can tell when to continue, when to stop, and when to ask the user

## Authoring Guardrails

Use these guardrails while designing the workflow:

- Do not create vague workflow steps.
- Do not create workflow folders before the user accepts the workflow, unless explicitly instructed.
- Do not omit dependencies between steps when one step consumes another step's output.
- Do not create `outputs.md` inside `workflows/NN-name/`.
- Do put all produced outputs, including Markdown outputs, inside `outputs/NN-name/`.
- Do not place generated artifacts inside `workflows/`; place them in `outputs/`.
- Keep names concise and filesystem-safe.
- Do not rely on the executor to infer missing filenames, missing dependencies, or missing approval checkpoints.
- Do not use subjective instructions like "make it good", "polish if needed", or "use judgment" without concrete success criteria.
- Do not combine multiple major deliverables into one step if they have different inputs, outputs, or approval points.
- Do state exact output paths whenever possible.
- Do use repository-relative paths when referring to files or folders.
- Do state whether a missing input should trigger backward dependency resolution or a user question.
- Do state whether the step is allowed to modify anything outside its own `outputs/NN-name/` folder. Default expectation: no.
- Do add explicit approval gates when a step should pause before a consequential action, irreversible action, or external side effect.

## Preferred Step Shape

When a workflow is ready to be written to disk, each step should be close to this structure:

1. A narrow objective
2. Concrete required inputs
3. Explicit upstream dependencies
4. Explicit output files in `outputs/NN-name/`
5. Verifiable success criteria
6. Clear execution constraints
7. Clear stop conditions

If a proposed step cannot be written in that shape, refine the workflow before creating files.
