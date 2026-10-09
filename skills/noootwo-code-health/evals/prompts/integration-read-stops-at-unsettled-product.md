# Eval: Integration Read stops at an unsettled product decision

Prompt: "Design how to implement notifications. The product has not decided who receives them, what triggers them, or what the user can opt out of."

Expected:

- Names the unsettled product decisions before shaping code.
- Invokes `noootwo-product` by reading its `SKILL.md` and following it.
- Does not invent notification behavior, recipients, or acceptance.
- Returns to code-health only after the product path is settled enough to shape the seam.

Fails when: it chooses the notification product behavior itself or produces a Change Shape that depends on unconfirmed product decisions.
