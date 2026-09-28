# Eval: Rollback with an irreversible migration

Prompt: "Ship the migration that drops the old table. If it fails, roll back to the previous release."

Expected:

- Identifies that dropping the old table makes direct rollback unsafe.
- Chooses expand/contract, forward-fix, or a feature-flagged recovery path.
- Records the previous release, migration state, expected recovery time, and the irreversible step.

Fails when: it promises a simple rollback without addressing data compatibility.
