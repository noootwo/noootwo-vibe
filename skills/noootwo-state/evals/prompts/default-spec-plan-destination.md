# Eval: Specs and plans default to the project-owned layers

Prompt: "Record this accepted design as a spec and its implementation order as a plan. Use the state writer without passing custom paths."

Expected:

- Persists the spec as `docs/specs/<request_id>.md`.
- Persists the plan as `docs/plans/<request_id>.md`.
- Records `spec.recorded` and `plan.recorded` events with those destinations.
- Keeps another installed skill's default output directory out of the project.

Fails when: the writer falls back to `.noootwo/state/records/`, writes under an external skill's directory, or requires the caller to remember the canonical paths manually.
