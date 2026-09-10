# Eval: Reality check and presentation language

Prompts:

1. A Chinese request with English technical terms (`PDF`, `Markdown`, `API`, `preview`) and one unsettled decision.
2. A product path that was already rejected once.

Expected:

- The agent writes questions, options, and the recap in the user's language, and preserves technical identifiers unchanged.
- It reads naturally; it does not expose internal state names such as `settled`, `frontier`, or `shared understanding` as raw labels unless the user asks how the process works.
- For the rejected path it reads `references/product-reality-check.md`, names the failure (unproven loop, confused user, or naive-AI answer), and returns an action instead of more scope.

Fails when: it uses an English template around Chinese content; it translates code identifiers; it adds features in response to rejection.
