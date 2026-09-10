# Eval Prompt: Decision Interview Confirmation Gate

Use `$noootwo-product` in a deep interview where the user has just answered the last open frontier question, so every material choice is now selected or delegated.

Expected behavior:

- Recompute the frontier, observe it is empty, and stop asking new questions.
- Produce a shared-understanding summary: confirmed decisions, delegated assumptions, deferred items, rejected ideas, active risks with resolution/owner/evidence, and the next artifact.
- Include a plain intent-fit check: what user problem the first loop solves and what it deliberately does not solve.
- Ask one explicit final confirmation unless the user already delegated the final decision; do not infer fit from earlier goal statements.
- Wait for that confirmation before marking `ready_for_handoff` or producing Product-to-Design Handoff / implementation plans.
- If the user says the fit is wrong, reopen only the highest-impact mismatch and return to the interview state.

Failure signals:

- Continues asking low-impact questions after the frontier is empty.
- Treats the summary itself as user confirmation without asking.
- Hands off with an unresolved material risk or an unconfirmed intent fit.
- Restarts a fixed questionnaire after convergence.

Manual evaluation: pass only when the response shows the expected behavior and avoids all failure signals.
