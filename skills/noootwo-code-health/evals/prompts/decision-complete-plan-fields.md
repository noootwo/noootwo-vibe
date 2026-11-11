# Eval: Reject an incomplete implementation plan

Prompt: "Start implementing from this plan."

Context: The plan lists steps but omits public interfaces, the Fan-out Check, observable test assertions, verification commands, and `Review Focus`.

Expected:

- Finds the answerable plan gaps before behavior changes.
- Requires file scope, `Interfaces`, a `Fan-out Check` with mode/units/rejoin, ordered steps, test assertions, verification commands, and `Review Focus`.
- Treats the missing Gate result as a drafted plan that Workflow must complete, not as permission for TDD to invent a mode.
- Treats `Review Focus` as the place for specification-implied risks that ordinary tests do not cover.
- Treats a serial default as valid only when the plan names why the slices are coupled, tiny, or lack host capability.
- Returns the plan for completion or records only reversible builder rulings that do not invent missing contracts.

Fails when: it treats ordered steps alone as decision-complete; it invents public interfaces; it starts multi-lane execution without an independence/rejoin decision; or it starts TDD while a material contract or assertion remains unstated.
