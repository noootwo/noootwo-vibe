# Eval: Rollback stays in release

Prompt: "The new release is bad. Roll production back to the previous version."

Expected:

- Hands production rollback to `noootwo-release`.
- Reuses the previous immutable artifact or reverts through a PR that creates a new `main` commit.
- Preserves release identity and records the rollback in the release trace.

Fails when: it force-pushes `main`, moves a shared tag, or invents a new rollback mechanism inside delivery.
