# Eval Prompt: Decision Interview Stop When Ready

Use `$noootwo-product` after the user has confirmed real user, scenario, main path, scope cuts, states, and acceptance criteria.

Expected behavior:

- Stop asking Decision Interview questions.
- Produce Product Checkpoint or Product-to-Design Handoff when UI work is next.
- Record any delegated assumptions instead of reopening settled choices.
- Route clarified visual execution to `$noootwo-design` or implementation planning.
- Use natural labels in the user's language; do not expose raw interview-state fields after convergence.

Failure signals:

- Continues asking low-impact or repeated questions.
- Blocks handoff despite enough product path clarity.
- Adds a fixed questionnaire after the key decisions are settled.
- Shows an interview ledger when the Clarity Gate can skip the interview entirely.

Manual evaluation: pass only when the response shows the expected behavior and avoids all failure signals.
