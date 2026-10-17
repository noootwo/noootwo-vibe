# Eval: Release Check runs once, not after every requirement

Prompt: "We finished four features this week. Each has a green Change Check. Now publish the release and use CI as the full-suite evidence."

Expected:

- Keeps the four Change Checks as requirement-level evidence.
- Routes to `noootwo-code-health` for one Release Check for the exact commit.
- Uses the CI run for that commit as the full-suite evidence instead of rerunning it locally.
- Requires the full Structure Sweep and release evidence before handing off to `noootwo-release`.
- Does not rerun each feature as a separate full audit.

Fails when: it treats the Change Checks as release readiness, reruns the whole suite locally without a reason, or skips the Structure Sweep and release evidence.
