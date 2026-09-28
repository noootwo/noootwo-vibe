# Eval: Localize a regression by release

Prompt: "Error rate increased after the latest deploy. Find which release introduced it."

Expected:

- Uses the deployment trace to identify the running release, commit, artifact, and environment.
- Compares the release against its predecessor using release-tagged errors, latency, or crash data.
- Hands the evidence to `noootwo-debug` for the proven cause instead of guessing the fix.

Fails when: it tries to debug from the deploy time alone, or rewrites the release history.
