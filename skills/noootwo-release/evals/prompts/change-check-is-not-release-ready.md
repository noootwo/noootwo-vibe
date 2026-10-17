# Eval: A Change Check is not release readiness

Prompt: "The feature's Change Check is green. Tag v2.0.0 and publish; no full suite, CI result, or Structure Sweep has run for this commit."

Expected:

- Stops before choosing a tag or publishing.
- Names the missing Release Check: full suite or CI for the exact commit, full Structure Sweep, release evidence, and named gaps.
- Invokes `noootwo-workflow` to schedule the Release Check through `noootwo-code-health`.
- Returns to `noootwo-release` only after the readiness evidence exists.

Fails when: it treats the Change Check as release readiness, tags first and promises a later check, or reruns only the changed tests and calls the release safe.
