# Eval: Promote one artifact

Prompt: "Build separate staging and production images from the same commit, then deploy both."

Expected:

- Rejects rebuilding per environment when one immutable artifact can be promoted.
- Keeps configuration separate from the artifact and records the config version.
- Records the artifact digest, commit, release ID, and target environments.

Fails when: it treats two independently built images as one release without evidence, or embeds environment-specific values in the artifact.
