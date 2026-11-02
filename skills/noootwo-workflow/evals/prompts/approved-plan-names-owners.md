# Eval: A pasted plan names its owners before execution

Prompt: "PLEASE IMPLEMENT THIS PLAN", followed by a plan that lists files, ordered steps, and prose acceptance, but no test assertion, verification command, validation owner, or release boundary. The repository has `.noootwo/state/current.json`.

Expected:

- Treats the plan as approved and does not re-run product, design, or research.
- Before the first edit, names the current owner and its verification depth, and records the ruling that closes the plan's ordinary ambiguities.
- Marks the missing assertion or verification command as a not-execution-ready gap and has its owner close it instead of inventing validation.
- Names the release boundary when the plan can change a version, tag, artifact, deployment trace, or release fact.
- Updates state through `noootwo-state` when the plan's stage, owner, or blocker changes.

Fails when: it edits without naming a validation owner; it invents an acceptance test the plan never set; it re-enters product or design to re-decide the plan; or it treats the pasted plan as self-validating.
