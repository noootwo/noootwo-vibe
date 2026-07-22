# Eval Prompt: Confusing User Path

Use `$noootwo-product` on a product concept whose screens are plausible but the first-time user cannot tell what to do next or why the result matters.

Expected behavior:

- Diagnose the comprehension failure before writing more UI requirements.
- Compare the proposed first loop with the user's current alternative.
- Rewrite acceptance criteria as observable user understanding and progress.
- Choose `keep`, `revise`, `ask`, or `stop` with one return action.

Failure signals:

- Converts the confusion into a sitemap, dashboard, or CRUD workflow.
- Uses internal states, IDs, or status names as user-facing structure.
- Treats a pretty UI direction as enough to fix the product path.

Manual evaluation: pass only when the response shows the expected behavior and avoids all failure signals.
