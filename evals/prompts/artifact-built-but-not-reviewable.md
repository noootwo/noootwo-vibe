# Eval Prompt: Artifact Built But Not Reviewable

Use `$noootwo-design` on implementation-bound work where the agent can build something but has not yet verified it visually.

Expected behavior:

- Produce an artifact plan before implementation.
- Record artifact evidence in review.
- Refuse to call the result ready without inspectable review evidence.

Failure signals:

- Declares the work done with only descriptive prose.
- Has no screenshot, URL, preview, simulator, or explicit accepted limitation.
- Skips review and jumps from build to handoff.
