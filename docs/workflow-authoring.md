# Workflow Authoring Instructions

## Purpose

Use these instructions when the user wants to create, revise, or approve a workflow.

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

Describe the expected input for the current workflow step.

If the input comes from a previous workflow step, state that explicitly using the prior step's output folder or specific output file path.

Example:

```md
Input from `outputs/01-brief/`.
```

### `instructions.md`

Store the workflow-step information that was defined in chat in step 2, including:

- Brief description
- Expected input
- Success criteria
- Constraints
- Any execution notes needed to perform the step well

`instructions.md` is the place for the step specification, including the expected outputs for the step and where they should be created inside `outputs/NN-name/`.

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

Example:

- Workflow step: `02-planning`
- Output folder: `outputs/02-planning`

## Quality Bar

The ideal workflow should be:

- Clear enough for another agent or human to execute
- Sequential and dependency-aware
- Minimal but complete
- Specific about inputs and outputs
- Explicit about where outputs are written
- Explicit about what success looks like
- Honest about constraints and assumptions

## Guardrails

- Do not create vague workflow steps.
- Do not create workflow folders before the user accepts the workflow, unless explicitly instructed.
- Do not omit dependencies between steps when one step consumes another step's output.
- Do not create `outputs.md` inside `workflows/NN-name/`.
- Do put all produced outputs, including Markdown outputs, inside `outputs/NN-name/`.
- Do not place generated artifacts inside `workflows/`; place them in `outputs/`.
- Keep names concise and filesystem-safe.
