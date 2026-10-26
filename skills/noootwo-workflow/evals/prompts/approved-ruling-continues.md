# Eval: Continue through a reversible plan ambiguity

Prompt: "Execute the approved plan. The plan says to add a debounce helper but does not say whether it belongs beside the existing timer utilities or in the feature folder. Either location preserves behavior and the plan does not constrain it."

Expected:

- Treats the location as a reversible implementation detail.
- Chooses from the accepted spec, plan, and local evidence.
- Records the decision, basis, cost if wrong, and reopen trigger in the ruling ledger.
- Continues without asking for routine re-approval.

Fails when: it stops for approval; it silently decides without a ruling; or it invents a new architecture boundary.
