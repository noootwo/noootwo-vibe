# Workflow Playbook

Use this only when the task is broad enough that a short direct path is not enough.

## Routing Matrix

| Signal | Route |
| --- | --- |
| UI, visual hierarchy, screenshots, `.noootwo/` | `$noootwo-design` |
| README, AGENTS, docs, ADR, status, release notes | `$noootwo-docs` |
| refactor, maintainability, architecture, code review | `$noootwo-review` |
| multi-step coordination, sequencing, release flow | `$noootwo-workflow` |

## Work Size

- `small`: one narrow file or behavior, existing tests/checks are clear.
- `medium`: several files, public behavior changes, docs likely affected.
- `large`: repo structure, release, migration, architecture, or multiple skills.

Small work can proceed directly after inspection. Medium work needs a short plan. Large work needs staged checkpoints and explicit validation.

## Default Loop

1. Inspect repo truth before deciding.
2. State the smallest viable path.
3. Implement in slices that can be tested independently.
4. Run the closest meaningful checks after each risky slice.
5. Update docs through `$noootwo-docs` when behavior, state, usage, or release changes.
6. Use `$noootwo-review` for broad code structure or release-bound review.

## Cost Controls

- Load only files needed for the current slice.
- Prefer manifests, status files, and focused references over reading long docs.
- Do not paste large reference material into plans or summaries.
- Do not introduce new gates unless they prevent a repeated failure.
