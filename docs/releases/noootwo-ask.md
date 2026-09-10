# noootwo-ask Releases

## v0.1.0

- Added the router: the only user-invoked skill in the suite, switched with `policy.allow_implicit_invocation: false` so it costs no context load.
- Names the five specialist skills, the order to run them in, and how to choose between two of them.
- Introduced alongside the authoring standard and invocation model in `docs/agents/`, per ADR 0006.
