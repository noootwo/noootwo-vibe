# Eval: Independent requirements run in parallel

Prompt: "Two unrelated requirements touch different feature folders and different APIs. Set up two agents to work at the same time."

Expected:

- Creates or reuses one isolated worktree/branch per requirement from current `main`.
- Records an Overlap Check with different files and contracts; chooses `parallel`.
- Keeps one writer per checkout and names the merge order.

Fails when: both agents share one checkout, branch switching happens mid-requirement, or a worktree is nested inside another.
