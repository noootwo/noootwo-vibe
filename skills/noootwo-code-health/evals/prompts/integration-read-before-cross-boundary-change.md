# Eval: Integration Read before a cross-boundary change

Prompt: "Add an audit log. The backend API, storage, permissions, and frontend timeline all need to change. The repo already has a service layer and shared event types."

Expected:

- Invokes `noootwo-code-health` before writing production behavior.
- Reads the nearest callers, interfaces, data ownership, shared types, tests, and existing patterns.
- Produces a compact Change Shape with seam, owning boundary, contracts, reuse, reversibility, test seam, smallest first slice, and rejected alternatives.
- Hands the shape to `noootwo-tdd` or back to `noootwo-workflow`; it does not implement the feature during the read.
- Keeps product and visual decisions with their owning skills.

Fails when: it starts coding or TDD before the shape is settled, or it turns the README-scale feature into a broad architecture rewrite.
