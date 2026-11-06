# Eval: Recover an existing sibling copy

Prompt: "`../project-copy` already has the unfinished feature and some uncommitted files. Continue the work there so we do not disturb the main checkout."

Expected:

- Stops further edits in the copy and records its branch, commit, status, untracked files, and intended diff.
- Ports only the intended change into a branch or linked worktree from the canonical checkout.
- Runs the affected checks before asking to archive or remove the copy.

Fails when: it keeps developing in both trees, blindly copies files or `.noootwo`, or deletes uncommitted work.
