# Eval Prompt: Deep Work Without Captured References

Use `$noootwo-design` on a deep redesign where the response cites three named products as references but captures nothing into `.noootwo/references/`.

Expected behavior:

- Capture each source locally, or record `capture: unreachable` with the observed reason and continue.
- Extract real values from a reachable source instead of describing it from memory.
- Record each source's evidence level, accessibility result, and provenance in `source.md`.
- Carry what was borrowed into `reference-board.md` under `Landed as`.

Failure signals:

- Cites products from memory and calls the evidence verified.
- Skips discovery because the named sources are behind a login.
- Captures screenshots and never maps them to a token, component, or rule.

Manual evaluation: pass only when the response shows the expected behavior and avoids all failure signals. The matching artifact check is `python scripts/validate_noootwo_readiness.py <project> --deep-mode`.
