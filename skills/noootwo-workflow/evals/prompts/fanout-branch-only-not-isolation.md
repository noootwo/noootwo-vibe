# Eval: A branch name alone is not a write lane

Prompt: "We have native workers but only one checkout. Create `codex/lane-a` and `codex/lane-b` branches, switch between them as the workers run, and call that parallel write fan-out."

Expected:

- Rejects branch switching in one checkout as isolation.
- Records `serial - no-native-isolation` or creates distinct linked worktrees from the primary checkout before dispatch.
- Keeps each working tree with one writer.
- Preserves the shared integration base and one integrator.

Fails when: it runs workers against one mutable checkout; it interprets two refs as two workspaces; or it hides the missing isolation behind a mode label.
