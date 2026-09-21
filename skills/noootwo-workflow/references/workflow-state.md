# Workflow State

For non-direct, cross-skill, or external-skill work, do not write state here. Invoke the `noootwo-state` skill: read its `SKILL.md` and follow it.

## Read

Use the state helper for a field or tail instead of reading a whole state file:

- `scripts/noootwo-state.sh state --field stage`
- `scripts/noootwo-state.sh events --last 5`
- `scripts/noootwo-state.sh summary`

## Record

After each specialist returns, hand workflow's next frontier to `noootwo-state`:

- current stage, last owner, last result, next trigger
- settled and unsettled facts
- open blockers and waiting condition

`noootwo-state` owns the form and location. Workflow only supplies the content and abstract properties.

## Re-entry

On any new invocation, read current state through `noootwo-state`, then read git status and the newest relevant artifacts. Prefer the recorded next trigger when it still matches reality; replace it when new evidence changes the frontier.

Direct single-file edits stay direct and do not create state.
