# Eval Prompt: A Path That Has Not Failed Yet

Use `$noootwo-debug` after fixing an input-validation bug, in a codebase where several sibling entry points still accept the same invalid state but have not yet received the triggering input.

Expected behavior:

- Keep the local fix scoped to the proven cause.
- Search sibling entry points, callers, mocks, migrations, and alternate paths that share the condition.
- Treat a working sibling as a near miss or fragile success, not as proof of safety.
- Record each sibling as affected, safe with reason, hypothesis, or not searched with reason.
- Add the smallest shared barrier or track each affected path with an owner and verification.

Failure signals:

- Fixes only the reported entry point and stops.
- Assumes untested siblings are safe because they have not failed in production.
- Flags every sibling as broken without checking the condition.
- Moves all sibling fixes into the current patch without a scope decision.

Manual evaluation: pass only when the response shows the expected behavior and avoids all failure signals.
