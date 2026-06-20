---
name: noootwo-design
description: Use as the front-door Noootwo workflow for non-trivial UI and interface design work. Classify the task, decide whether exploration is required, route to quick/standard/deep/production/review, and enforce the design contract before implementation.
---

# Noootwo Design

This is the front-door skill for the Noootwo Design plugin. Use it to decide how a design task should proceed before implementation.

## Shared Core

This plugin keeps its shared references, templates, evals, and scripts at the repository root:

- `references/`
- `scripts/`
- `assets/noootwo-harness-template/`
- `evals/prompts/`

Read only what the task needs.

## Task Classification

Classify the task on these dimensions before choosing a path:

- `change magnitude`
- `direction uncertainty`
- `implementation commitment`
- `artifact verifiability`
- `system continuity`

Route based on those dimensions:

- `quick`: local polish that preserves the existing direction
- `adopt-project`: first Noootwo pass on an existing project
- `standard`: non-trivial design work with meaningful visual decisions
- `deep`: stronger exploration, higher taste risk, or previous output was too generic
- `production`: implementation-bound work with an accepted direction
- `extract-system`: refresh durable system memory and tokens
- `review`: critique an artifact and decide the return path

## Workflow Contract

For non-trivial work, use this loop:

`intake -> exploration -> direction brainstorm -> user decision -> design contract -> implementation plan -> artifact -> review -> handoff`

Do not skip directly from request to implementation when:

- high-impact uncertainty remains
- multiple viable directions exist
- the task creates a new structure, visual language, or information hierarchy

## Delegation To Specialized Skills

When the task specifically needs one of these deeper passes, use the sibling skill directly:

- `noootwo-style-discovery`
  Use for research-heavy discovery, direction territories, influence discovery, and mechanism transfer before drafting.
- `noootwo-design-review`
  Use for screenshot critique, running artifact review, layout defect diagnosis, generic drift detection, and return-action decisions.
- `noootwo-detail-translation`
  Use when the direction is approved but implementation is drifting toward defaults or losing authored detail.

## Required Project Context

Durable context lives in `.noootwo/`. If missing, bootstrap from `assets/noootwo-harness-template/` or run:

```bash
python scripts/bootstrap_noootwo_harness.py /path/to/project
```

Useful project files:

- `.noootwo/brief.md`
- `.noootwo/directions.md`
- `.noootwo/specs/active-design.md`
- `.noootwo/plans/active-implementation.md`
- `.noootwo/review.md`

## Blocking Rules

- Do not implement non-trivial UI before the brief exists.
- Do not implement direction-sensitive work before a direction is chosen or explicitly delegated.
- Do not edit non-trivial UI files before the approved design contract and implementation plan exist.
- Do not call work `ready` without artifact evidence.

## Reference Map

- `references/workflow-cost-model.md`
- `references/structured-design-spec.md`
- `references/project-integration.md`
- `references/research-protocol.md`
- `references/canvas-artifact-loop.md`
- `references/review-rubric.md`
