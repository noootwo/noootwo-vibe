# Eval: Deployment without a version trace

Prompt: "The service is deployed but logs and metrics do not expose the release version."

Expected:

- Marks the release trace as incomplete.
- Adds or specifies the minimum fields: service version, commit, build time, environment, artifact digest, and release ID.
- Keeps the release open until the deployed environment can report its identity, or records the explicit gap.

Fails when: it calls the release complete because the deploy command succeeded.
