# Eval: Reuse existing isolation

Prompt: "Start a new feature; the current checkout is already a linked worktree for this requirement."

Expected:

- Detects the linked worktree and confirms it is not a submodule.
- Reuses the existing checkout instead of creating another worktree.
- Reports the branch, base, and current writer state.

Fails when: it nests a new worktree or switches to the main checkout unnecessarily.
