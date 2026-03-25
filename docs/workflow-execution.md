# Workflow Execution Instructions

## Purpose

Use these instructions when the user wants to perform work using an existing workflow.

## Workflow Execution Procedure

After a workflow has been created, use the workflow files to execute it step by step with the user.

Follow this sequence for every workflow-execution request:

1. Ask the user what they need to do.
2. Identify the relevant workflow step to execute.
3. Read that step's `instructions.md` and `inputs.md`.
4. Determine whether every required input already exists.
5. If an input is missing, resolve it before executing the current step:
   - If the input is provided by a previous workflow step, move backward to that previous step.
   - Read the previous step's `instructions.md`, `inputs.md`, and `outputs.md`.
   - Repeat this backward traversal until you reach the earliest missing dependency.
   - Execute dependencies in forward order once the required inputs are available.
6. If a missing input does not come from a previous workflow step, tell the user exactly what input is needed and ask them to provide it.
7. Once all inputs exist, execute the current workflow step using `instructions.md` as the source of truth.
8. Produce the step outputs and store any non-Markdown artifacts in the matching `resources/` folder when applicable.
9. Continue to the next step only when the current step's success criteria are satisfied.

Do not ask the user to manually figure out workflow dependencies if the workflow files already define them. The agent should trace dependencies on its own.

## Missing Input Resolution Rules

When checking whether a workflow step can be executed:

- Read `inputs.md` first to identify every required input.
- If `inputs.md` references a previous step's `outputs.md`, treat that as a dependency that must be satisfied before continuing.
- Read the referenced prior step's `outputs.md` to understand what should exist.
- If the prior step output does not exist yet, execute that prior step first.
- Keep moving backward until you find a step whose inputs are available or until you reach an input that only the user can provide.
- When asking the user for a missing external input, be specific about the format or content needed.
- After the user provides the missing input, resume the dependency chain without restarting the whole workflow.

## Step Execution Rules

When executing a workflow step:

- Read `instructions.md` before taking action.
- Use `instructions.md` to understand the step's brief description, success criteria, constraints, and execution notes.
- Use `outputs.md` to verify what must be produced before the step is considered complete.
- If the step depends on outputs from another step, reference those upstream outputs explicitly while working.
- Do not mark a step complete if its documented outputs are incomplete or inconsistent with its success criteria.

## Strategic Output Rules

When producing outputs for a workflow step, think strategically:

- Optimize for outputs that make downstream steps easier, clearer, and less error-prone.
- Preserve important assumptions, decisions, and rationale when they will affect later steps.
- Prefer structured, reusable outputs over vague summaries.
- Keep outputs aligned with the workflow's actual dependency chain.
- If a stronger output format will materially improve later execution, produce it as long as it remains consistent with the approved workflow.
- Do not invent missing user inputs; ask for them when they cannot be derived from prior steps or existing artifacts.
