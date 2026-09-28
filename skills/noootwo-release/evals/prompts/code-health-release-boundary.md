# Eval: Code health and release stay separate

Prompt: "The code-health review says ready. Choose the version, tag it, deploy it, and make sure we can roll back."

Expected:

- Consumes the readiness decision without re-running code health.
- Calls `noootwo-release` for version, tag, artifact, deployment trace, rollback, and release health.
- Leaves structural health and acceptance with `noootwo-code-health`.

Fails when: release re-reviews code structure, or code-health tries to choose the version.
