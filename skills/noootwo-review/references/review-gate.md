# Review Gate

Use before submit, release, or implementation handoff when code changed. This is the decision boundary for scope, verification, refactor, and user acceptance.

## Scope

- Default scope is the current change: files and behavior touched by the task or diff.
- Full-project review or large refactor runs only when the user explicitly asks for it.
- Before expanding scope, stop and ask. A local cleanup with one safe answer does not need a question.

## TDD precondition

- Behavior-changing code must have a credible test before structural review.
- If tests are missing, brittle, or assert implementation rather than behavior, stop and invoke `noootwo-tdd`: read its `SKILL.md` and follow it.
- Review does not teach the TDD loop; it consumes the green test evidence.

## Review decision

Select lenses before reading widely. A small diff uses one to three lenses; a risky or release-bound diff includes correctness and testability.

Separate defects from future improvements. Report findings ordered by severity. Do not inflate severity to force cleanup.

## Refactor and optimization

- Refactor = behavior-preserving structural change. Use `references/refactoring-loop.md`.
- Optimization = measured metric change. Use `references/optimization-loop.md`.
- Both are changes, not findings; after either, rerun the closest full relevant test command.

## Re-test gate

A refactor or optimization is not accepted until:

- the behavior-preserving baseline stayed green,
- the full relevant test command is green,
- verification gaps are named explicitly when no practical test exists.

## User acceptance gate

For non-direct code changes, and for every refactor or optimization:

- stop and report the result,
- wait for explicit user acceptance,
- do not commit, push, tag, or publish before that acceptance.

Direct single-file edits with an obvious check and no structural change may close normally after verification.

## Output

For a structured review include applied lenses, skipped lenses and why, evidence read, findings, verification gaps, re-test evidence, acceptance state, and owning skill for each handoff.
