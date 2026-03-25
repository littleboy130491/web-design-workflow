# Workflow Builder Agent Guide

## Purpose

This repository is used to design workflows collaboratively in chat, then materialize accepted workflows as structured files under `workflows/` and supporting artifacts under `resources/`.

## Default Operating Procedure

Follow this sequence for every workflow-building request:

1. Ask the user what workflow they want to create.
2. Propose a good workflow in chat.
3. If the user does not accept it, iterate in chat until they approve it.
4. After approval, create the workflow files and folders in the repository.

Do not skip the approval step before writing workflow artifacts unless the user explicitly asks you to do so.

## Chat Output Format For Proposed Workflows

When proposing a workflow in chat, present each suggested workflow step with:

- Brief description
- Expected input
- Expected output
- Success criteria
- Constraints

Keep the proposal practical and implementation-oriented. Prefer clear, numbered workflow steps.

## Iteration Rules

- If the user rejects or adjusts the workflow, revise the proposal in chat.
- Continue iterating until the user explicitly accepts the workflow.
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
- `outputs.md`
- `instructions.md`

Example:

```text
workflows/
  01-brief/
    inputs.md
    outputs.md
    instructions.md
```

## File Content Rules

### `inputs.md`

Describe the expected input for the current workflow step.

If the input comes from a previous workflow step, state that explicitly using the prior step's output path.

Example:

```md
Input from `01-brief/outputs.md`.
```

### `instructions.md`

Store the workflow-step information that was defined in chat in step 2, including:

- Brief description
- Success criteria
- Constraints
- Any execution notes needed to perform the step well

### `outputs.md`

Describe the expected output of the workflow step.

If the step produces files or assets beyond Markdown documentation, also create a matching folder in `resources/` and reference it from `outputs.md`.

Example:

```text
resources/
  02-planning/
```

Example `outputs.md` note:

```md
Output files can also be found in `resources/02-planning`.
```

## Resources Folder Rules

When a workflow step needs outputs that are more than just Markdown files:

1. Create a folder inside `resources/` using the same numeric prefix and workflow name.
2. Place the generated output files in that folder.
3. Mention that folder in the corresponding `workflows/NN-name/outputs.md`.

Example:

- Workflow step: `02-planning`
- Resource folder: `resources/02-planning`

## Quality Bar

The ideal workflow should be:

- Clear enough for another agent or human to execute
- Sequential and dependency-aware
- Minimal but complete
- Specific about inputs and outputs
- Explicit about what success looks like
- Honest about constraints and assumptions

## Guardrails

- Do not create vague workflow steps.
- Do not create workflow folders before the user accepts the workflow, unless explicitly instructed.
- Do not omit dependencies between steps when one step consumes another step's output.
- Do not place non-Markdown generated artifacts inside `workflows/`; place them in `resources/`.
- Keep names concise and filesystem-safe.
