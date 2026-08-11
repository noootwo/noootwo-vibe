# Eval Prompt: Skip Decision Interview When Clear

Use `$noootwo-product` on a detailed request that explicitly identifies the target user, use situation, user outcome, scope boundary, main path, relevant error or permission states, and observable acceptance criteria. Repo facts agree with the request and no material product choice remains.

Expected behavior:

- Run the Clarity Gate and classify the request as `clear`.
- Do not ask a ceremonial product question or display a Decision Interview ledger.
- Produce the smallest useful Product Checkpoint, Product-to-Design Handoff, or direct implementation route.
- Keep any remaining technical or low-impact presentation details as explicit implementation assumptions, not user-blocking product decisions.
- Preserve the user's language in the response and use natural labels rather than raw internal state names.

Failure signals:

- Starts Decision Interview only because the request is product-shaped or detailed.
- Re-asks facts already explicit in the request or repo.
- Blocks implementation on a low-impact technical preference.
- Shows `awaiting_user_answer` or another raw machine state when no material choice is open.

Manual evaluation: pass only when the response moves directly and proportionately from a clear brief to the next artifact.
