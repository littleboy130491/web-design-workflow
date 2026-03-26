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
   - Read the previous step's `instructions.md` and `inputs.md`, then inspect the matching folder in `outputs/`.
   - Repeat this backward traversal until you reach the earliest missing dependency.
   - Execute dependencies in forward order once the required inputs are available.
6. If a missing input does not come from a previous workflow step, tell the user exactly what input is needed and ask them to provide it.
7. Once all inputs exist, tell the user which step is ready, what will be done next, and ask for confirmation before executing it.
8. After the user confirms, execute the current workflow step using `instructions.md` as the source of truth.
9. Produce the step outputs and store any non-Markdown artifacts in the matching `outputs/` folder when applicable.
10. After completing the step, summarize the result and ask whether to continue to the next step.

Do not ask the user to manually figure out workflow dependencies if the workflow files already define them. The agent should trace dependencies on its own.
Do not assume permission to run the rest of the workflow after completing one step. Default to explicit confirmation between steps unless the user clearly asks for end-to-end execution.
When executing a workflow, only create or modify files inside `outputs/` unless the user explicitly asks for changes elsewhere.
Treat file and folder references in workflow documents as repository-relative paths unless the workflow explicitly says otherwise.

## Missing Input Resolution Rules

When checking whether a workflow step can be executed:

- Read `inputs.md` first to identify every required input.
- If `inputs.md` references a previous step's `outputs/NN-name/` folder or a file within it, treat that as a dependency that must be satisfied before continuing.
- Read the referenced prior step's `instructions.md` and inspect the matching `outputs/NN-name/` folder to understand what should exist.
- When following file references from workflow documents, use the relative path exactly as written rather than converting it to an absolute path in the workflow definition.
- If the prior step output does not exist yet, execute that prior step first.
- Keep moving backward until you find a step whose inputs are available or until you reach an input that only the user can provide.
- When asking the user for a missing external input, be specific about the format or content needed.
- After the user provides the missing input, resume the dependency chain without restarting the whole workflow.
- Once the required inputs are available, pause and ask for confirmation before executing the now-ready step.

## Step Execution Rules

When executing a workflow step:

- Read `instructions.md` before taking action.
- Use `instructions.md` to understand the step's brief description, expected input, expected output, success criteria, constraints, and execution notes.
- Before executing the step, tell the user what step you are about to run and wait for confirmation.
- Create or update the matching `outputs/NN-name/` folder for the step.
- Write the actual deliverables for the step into that output folder, including Markdown outputs when applicable.
- Use the contents of `outputs/NN-name/` to verify that the produced result matches the expectations documented in `instructions.md`.
- If the step depends on outputs from another step, reference those upstream outputs explicitly while working.
- When referring to workflow files, inputs, or outputs during execution, use repository-relative paths in messages and artifacts.
- Do not mark a step complete if its documented outputs are incomplete or inconsistent with its success criteria.
- After the step is complete, ask the user whether to proceed to the next step instead of automatically continuing.
- Do not modify workflow definition files during execution unless the user explicitly asks for a workflow revision.

## Strategic Output Rules

When producing outputs for a workflow step, think strategically:

- Optimize for outputs that make downstream steps easier, clearer, and less error-prone.
- Preserve important assumptions, decisions, and rationale when they will affect later steps.
- Prefer structured, reusable outputs over vague summaries.
- Keep outputs aligned with the workflow's actual dependency chain.
- If a stronger output format will materially improve later execution, produce it as long as it remains consistent with the approved workflow.
- Put all produced outputs in `outputs/NN-name/`, including Markdown outputs.
- Treat `workflows/` as read-only during execution unless the user explicitly asks to revise the workflow.
- Do not invent missing user inputs; ask for them when they cannot be derived from prior steps or existing artifacts.
