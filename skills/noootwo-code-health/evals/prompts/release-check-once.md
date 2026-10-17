# Eval: Release Check runs once with full evidence

Prompt: "Three requirements are merged and their Change Checks are green. Prepare the release, but do not rerun everything locally if CI already did it."

Expected:

- Labels the pass `Verification: release`.
- Uses CI for the exact commit as the full-suite evidence instead of duplicating it locally.
- Runs the full Structure Sweep and the release-evidence lens, including version, artifact, deployment trace, rollback, and named gaps.
- Hands the readiness decision to `noootwo-release`.
- Does not rerun each requirement's Change Check as a separate full audit.

Fails when: it treats the three Change Checks as release readiness, reruns the same full suite locally without a reason, or skips the Structure Sweep and release evidence.
