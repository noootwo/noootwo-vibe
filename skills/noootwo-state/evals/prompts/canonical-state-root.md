# Eval: Use the canonical state root from a linked worktree

Prompt: "You are in a linked worktree and need to record the project context. `.noootwo` currently exists only in the primary checkout."

Expected:

- Resolves the primary checkout from `git rev-parse --git-common-dir` (or the registered primary worktree).
- Reads or writes state through the primary root with `--root <primary>`.
- Keeps docs and state on the canonical project authority instead of creating a worktree-local `.noootwo`.

Fails when: it initializes a second `.noootwo`, uses the worktree root by default, or treats the worktree state as the project truth.
