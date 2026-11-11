# Eval: Worktrees are created under the primary checkout

Prompt: "We are editing inside a linked worktree. Create a lane worktree with a relative `.worktrees/lane-a` path from `origin/main`."

Expected:

- Resolves `ROOT`, `COMMON`, and `PRIMARY` before creation.
- Fetches the actual default branch, records its exact `BASE_SHA`, and branches from that SHA.
- Runs `git -C "$PRIMARY" worktree add "$PRIMARY/.worktrees/<slug>" -b ... "$BASE_SHA"`.
- Ensures `.worktrees/` is ignored through the shared repository-local exclude without editing the primary checkout's tracked files.
- Never creates the lane under the current linked-worktree root or nests a worktree.

Fails when: it runs `git worktree add .worktrees/lane-a` from the linked worktree; it dirties the primary checkout by appending to a tracked `.gitignore`; it uses a moving `origin/main` name after recording a different base; or it creates a sibling clone.
