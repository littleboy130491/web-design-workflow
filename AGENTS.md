# Workflow Builder Agent Guide

## Purpose

This repository is used for three different operating modes:

1. Designing or revising workflows.
2. Executing an existing workflow step by step.
3. Visualizing an existing workflow as a Mermaid diagram.

Use this file as the index and routing guide. Then follow the correct detailed instruction file for the task at hand.

## Instruction Routing

- If the user wants to create a new workflow, revise a workflow, or discuss workflow structure before files are written, follow `docs/workflow-authoring.md`.
- If the user wants to perform work using an existing workflow, follow `docs/workflow-execution.md`.
- If the user wants to visualize an existing workflow, follow `docs/workflow-diagram.md`.

## Default Behavior

- Do not mix authoring, execution, and diagramming rules unless the user is explicitly doing more than one.
- When the task is ambiguous, determine whether the user is asking to design the workflow, execute it, or visualize it.
- Prefer reading only the instruction file relevant to the current mode.
- Treat the detailed mode-specific instruction file as the source of truth once the mode is identified.

## Repository Layout

- Workflow definitions live under `workflows/`.
- Supporting artifacts live under `outputs/`.
- Diagram artifacts live under `resources/`.
- Mode-specific operating instructions live under `docs/`.

## Guardrails

- Do not create workflow artifacts before the user approves the workflow design, unless they explicitly ask you to do so.
- Do not ask the user to manually resolve dependencies that are already defined in workflow files.
- Do not execute an entire workflow in one shot unless the user explicitly asks for that behavior.
- Do not place generated outputs inside `workflows/`; place them in `outputs/`.
- When executing a workflow, only create or modify files inside `outputs/` unless the user explicitly asks for changes elsewhere.
- When generating workflow diagrams, place them in `resources/` unless the user explicitly asks for a different location.
