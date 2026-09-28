# Eval: Route release engineering

Prompt: "Make sure the next release has a version, a tag, a deployment trace, and a rollback path."

Expected:

- Routes to `noootwo-release` rather than `noootwo-code-health` or a generic external deploy skill.
- Keeps the order: readiness from code-health, release plan from release, persistence through state.
- Does not let workflow choose the version or implement the deployment method itself.

Fails when: it treats release as a simple tag command, or lets workflow own the release plan.
