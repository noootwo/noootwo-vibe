# Eval Prompt: Directionally Right But Generic Drift

Use `$noootwo-design` on a design result that mostly follows the chosen direction but still feels generic in execution.

Expected behavior:

- Use review to diagnose mechanism loss, default-component smell, or surface-only styling.
- Return to the earliest stage that can fix the drift, often approved spec, implementation plan, or artifact.
- Preserve the chosen direction instead of replacing it with a new unrelated aesthetic.

Failure signals:

- Calls the result ready because the overall vibe seems close enough.
- Only suggests “polish more” without naming where the drift comes from.
- Restarts from zero when the real issue is implementation drift.
