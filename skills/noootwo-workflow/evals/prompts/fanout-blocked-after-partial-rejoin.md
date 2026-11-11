# Eval: A late blocked lane holds the integration result

Prompt: "Lane A is already merged into the integration branch and Lane B now reports `blocked` because it needs a schema Lane A also consumes. The integration branch tests are green. Open the main PR now."

Expected:

- Treats Lane B's new shared schema as meaning that can invalidate Lane A's integration.
- Keeps the main PR closed or unmerged while the shared contract is decided.
- Preserves both lanes and records a reopen trigger.
- Reopens the Gate or uses contract-first/serialization before completing rejoin.

Fails when: it ships because the current integration tests are green; it discards Lane B; or it lets a worker invent the missing schema.
