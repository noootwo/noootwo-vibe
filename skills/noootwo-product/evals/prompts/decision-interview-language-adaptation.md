# Eval Prompt: Decision Interview Language Adaptation

Use `$noootwo-product` on a Chinese request with one material unresolved product choice. The request intentionally includes English terms such as `PDF`, `Markdown`, `API`, and `preview`.

Expected behavior:

- Keep the interview one-question-at-a-time and wait for an explicit choice.
- Use Chinese for headings, explanations, option descriptions, and the waiting message.
- Preserve intentional technical terms, API names, file paths, and code identifiers where translating them would reduce precision.
- Describe the waiting state naturally, such as "当前状态：等待你的确认", rather than printing raw labels such as `Decision Interview Turn`, `Interview state`, or `blocked on user confirmation`.
- If the user's next message changes language or is intentionally mixed, adapt the prose language while preserving the relevant terms.

Failure signals:

- Uses an English-only template around Chinese content.
- Translates code identifiers mechanically or removes useful technical terms.
- Forces a single language when the user deliberately uses mixed terminology.
- Exposes internal ledger or execution-status keys in normal user-facing prose without need.

Manual evaluation: pass only when the result remains precise while reading naturally in the user's language.
