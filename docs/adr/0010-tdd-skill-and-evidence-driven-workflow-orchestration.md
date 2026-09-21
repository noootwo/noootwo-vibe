# 0010 — Add `noootwo-tdd` and evidence-driven workflow orchestration

## Status

Accepted.

## Context

`noootwo-workflow` routed tasks with a fixed Noootwo routing table and assumed a mostly linear stage. That caused two problems:

- A task outside the Noootwo set, such as slides, documents, or media work, had no reliable owner.
- A task started midway through a project could be mis-timed because the workflow guessed the stage instead of reading current project state.

`noootwo-review` already contained refactor heuristics and optimization work, but refactor, re-test, and user acceptance were mixed into one large playbook. The user also wanted the whole code development path to be TDD by default.

## Decision

- Add `noootwo-tdd` as a public model-invoked skill owning red-green-refactor and test quality.
- Keep `noootwo-review` as the owner of code and project-health review, refactoring, optimization, re-testing, and the user acceptance gate. Split refactor-specific content into `review-gate.md` and `refactoring-loop.md`.
- Make `noootwo-workflow` an evidence-driven re-entrant orchestrator. It reads current repo truth and `.noootwo/workflow-state.md`, matches one owner by intent, artifact shape, and available skill descriptions, then schedules one next step at a time.
- Allow workflow to discover and invoke other installed skills for work outside the Noootwo set. Those skills are execution resources, not additions to the public set or capability map.
- When no owner is clear or two owners tie, workflow stops with one or two candidates instead of guessing.

## Consequences

- The public skill set changes from nine to ten skills.
- `noootwo-workflow` no longer depends on a large keyword routing table; its behavior is measured by workflow eval scenarios.
- TDD is mandatory for behavior-changing code unless the user explicitly opts out for throwaway, generated, config-only, or no-op docs work.
- Direct single-file edits remain lightweight and do not require `.noootwo/workflow-state.md`.
