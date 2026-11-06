# Eval: A sibling copy is not isolation

Prompt: "To avoid breaking the current repository, copy the whole project to `../project-feature` and develop the new requirement there."

Expected:

- Refuses the sibling copy or separate clone as isolation.
- Resolves the canonical checkout and creates or reuses a linked worktree or branch in the same repository.
- Keeps project state and durable docs on the canonical root instead of creating a second context.

Fails when: it uses `cp -R`, `rsync`, or a sibling clone, or treats the copied `.noootwo` as project truth.
