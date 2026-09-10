# Eval Prompt: Decision Interview Fact Self-Serve

Use `$noootwo-product` on a product request where the repo, README, docs, or current UI can answer part of what would otherwise be a question (for example, existing users, platform, current entry points, or current flow), and one frontier question depends on that fact.

Expected behavior:

- Resolve the discoverable fact from the environment before the round; do not ask the user for it.
- Cite the source path or artifact for each discovered fact, or state explicitly that no such fact was found.
- If a blocking fact cannot be resolved, state that and still ask the rest of the settled frontier.
- Reserve user questions for genuine product decisions that change scope, IA, flow, states, or acceptance.

Failure signals:

- Asks the user a question the repo already answers.
- Blocks the whole round on one missing fact instead of asking the rest of the frontier.
- Invents a fact without a source path or an explicit "none found" note.

Manual evaluation: pass only when the response shows the expected behavior and avoids all failure signals.
