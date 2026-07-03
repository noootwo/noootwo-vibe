# Workflow Playbook

Use this only when the task is broad enough that a short direct path is not enough.

## Contents

- Practice Basis
- Routing Matrix
- Work Size
- Mode Details
- Default Loop
- Handoff Packet Templates
- Cost Controls
- Stop Conditions

## Practice Basis

- Mature process skills use hard gates, red flags, and completion evidence instead of vague encouragement.
- Agent skill guidance favors progressive disclosure: keep the entry file short and load deeper references only when useful.
- Modern delivery practice favors small batches, clear ownership, and fresh verification over large speculative plans.

## Routing Matrix

| Signal | Route |
| --- | --- |
| UI, visual hierarchy, screenshots, `.noootwo/` | `$noootwo-design` |
| README, AGENTS, docs, ADR, status, release notes | `$noootwo-docs` |
| refactor, maintainability, architecture, code review | `$noootwo-review` |
| multi-step coordination, sequencing, release flow | `$noootwo-workflow` |
| bug, failing check, surprising runtime behavior | `$noootwo-workflow` diagnostic mode first, then specialist |

## Work Size

- `small`: one narrow file or behavior, existing tests/checks are clear.
- `medium`: several files, public behavior changes, docs likely affected.
- `large`: repo structure, release, migration, architecture, or multiple skills.

Small work can proceed directly after inspection. Medium work needs a short plan. Large work needs staged checkpoints and explicit validation.

## Mode Details

### Direct

Use for one narrow behavior or doc fix. State the file, change, and check. Avoid adding a multi-step plan unless uncertainty appears.

### Planned

Use for multi-file behavior, repo structure, public usage, or cross-skill work. Keep the plan short enough to fit in working memory:

- objective
- affected files/modules
- risks and non-goals
- execution slices
- verification commands
- docs/review/release handoffs

### Diagnostic

Use for test failures, bugs, regressions, broken installs, or unexpected behavior. Do not fix before identifying evidence:

- observed symptom and command/output
- reproduction path
- recent changes or likely boundary
- working comparison if one exists
- single hypothesis to test
- verifying command for the fix

### Release

Use when changing versions, tags, remotes, CI, local installs, or published packages. Always list:

- version source files
- manifests and README/docs that mirror versions
- validation commands
- tag names and conflict check
- install/sync target
- remote push evidence

### Recovery

Use after prior agent drift, repeated failed fixes, unclear half-finished work, or context compaction. First reconstruct current state from files, git, commands, and artifacts. Treat summaries as hints, not proof.

## Default Loop

1. Inspect repo truth before deciding.
2. State the smallest viable path.
3. Implement in slices that can be tested independently.
4. Run the closest meaningful checks after each risky slice.
5. Update docs through `$noootwo-docs` when behavior, state, usage, or release changes.
6. Use `$noootwo-review` for broad code structure or release-bound review.

## Handoff Packet Templates

### To `$noootwo-docs`

- Changed fact:
- Owning layer suspected:
- Files/commands touched:
- Validation or release evidence:
- Known stale docs to check:

### To `$noootwo-review`

- Behavior or structure changed:
- Files and nearest tests:
- Risk class:
- Verification command:
- Specific judgment requested:

### To `$noootwo-design`

- UI/artifact surface:
- Current design evidence:
- Direction uncertainty:
- Reviewable artifact path:
- Implementation boundary:

## Cost Controls

- Load only files needed for the current slice.
- Prefer manifests, status files, and focused references over reading long docs.
- Do not paste large reference material into plans or summaries.
- Do not introduce new gates unless they prevent a repeated failure.
- Collapse repeated status into a single status file instead of rewriting the same fact in README, AGENTS, and release notes.

## Stop Conditions

Stop and ask or reroute when:

- a high-impact product or architecture choice is unresolved
- the verification path is missing and cannot be inferred
- the change would alter public behavior beyond the user's request
- three fix attempts reveal new problems in different places
- the work needs a specialist skill and continuing here would duplicate that skill
