# Eval: Audit an existing product flow

Prompt: "Audit this onboarding flow and tell me what is wrong."

Expected:

- The agent reads repo and product facts first, then uses `references/product-audit.md` for the audit.
- It captures the flow in order and keeps every finding tied to a step.
- It separates product-flow friction, state/acceptance gaps, visual defects, and code defects.
- It routes visual defects to `noootwo-design` and code defects to `noootwo-review` instead of fixing them in the product pass.
- It says clearly when the flow cannot be captured and does not call a web search an audit.

Fails when: it skips capture and critiques from memory; it treats a screenshot as enough by itself; it rewrites UI in the same product pass.
