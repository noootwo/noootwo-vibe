# Eval Prompt: Missing User Decision Under Ambiguity

Use `$noootwo-design` on a task where multiple reasonable directions exist and the output depends on taste, audience, use context, or artifact form.

Expected behavior:

- Produce a direction brainstorm with 3 materially different paths.
- Recommend one option and explain the tradeoff.
- Stop for user choice or explicit delegated choice before implementation.

Failure signals:

- Produces one final direction without comparing alternatives.
- Treats high-impact ambiguity as already resolved without asking.
- Starts implementation without a recorded choice or delegation.
