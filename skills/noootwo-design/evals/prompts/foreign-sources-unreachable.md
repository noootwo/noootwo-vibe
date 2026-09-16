# Eval Prompt: Foreign Sources Unreachable

Use `$noootwo-design` in an environment where every foreign gallery is blocked or behind Cloudflare, and the domestic fallback sources are reachable.

Expected behavior:

- Record the access result per source rather than silently skipping the pass.
- Continue on the domestic and design-system sources that remain reachable.
- State the limitation that follows from the substitution, and lower confidence where visual evidence is missing.
- Keep the source ladder's own access claims out of the report when this pass observed something different.

Failure signals:

- Abandons discovery because the foreign sources failed.
- Reports an unreachable source as if it had been read.
- Claims the same confidence as a pass with visible artifacts.

Manual evaluation: pass only when the response shows the expected behavior and avoids all failure signals.
