# Eval: Reject an incomplete implementation plan

Prompt: "Start implementing from this plan."

Context: The plan lists steps but omits public interfaces, observable test assertions, verification commands, and `Review Focus`.

Expected:

- Finds the answerable plan gaps before behavior changes.
- Requires file scope, `Interfaces`, ordered steps, test assertions, verification commands, and `Review Focus`.
- Treats `Review Focus` as the place for specification-implied risks that ordinary tests do not cover.
- Returns the plan for completion or records only reversible builder rulings that do not invent missing contracts.

Fails when: it treats ordered steps alone as decision-complete; it invents public interfaces; or it starts TDD while a material contract or assertion remains unstated.
