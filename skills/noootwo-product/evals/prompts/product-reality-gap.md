# Eval Prompt: Product Reality Gap

Use `$noootwo-product` after a user says a proposed app flow "doesn't feel like it understands the user" and "looks like dumb AI product thinking".

Expected behavior:

- Run `Product Reality Check` instead of only polishing the existing feature list.
- Name the real user, moment of use, current alternative, first loop, and user comprehension risk.
- Identify the naive-AI failure that caused the weak product decision.
- Return to Product Discovery, Product Checkpoint, or Product Choice Challenge when the first loop is not understandable.

Failure signals:

- Treats criticism as a request to add more features.
- Defends the prior plan without checking the user's moment of use.
- Hands off to design while the user cannot understand the main path.

Manual evaluation: pass only when the response shows the expected behavior and avoids all failure signals.
