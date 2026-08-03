# Eval Prompt: Workflow Preserves Deep Interview

Start with `$noootwo-workflow` on a broad product request where the user explicitly says: "Please confirm the details like grill, one question at a time, until the result matches what I mean."

Expected behavior:

- Workflow routes the product ambiguity to `$noootwo-product` instead of conducting a long product interview itself.
- The handoff preserves `interview_depth: deep`, the user's explicit confirmation request, checked facts with source paths, and the current decision ledger.
- The handoff initializes every ledger field, even when empty, using the structured Product Interview Handoff packet.
- Product asks one material question per turn, carries confirmed decisions forward, and distinguishes deferred, rejected, and active-risk states.
- Product runs one explicit intent-fit confirmation before handoff unless the user delegated the final decision; it does not infer final fit from earlier goal statements.
- Product does not hand off while an unresolved active risk would change the main path, trust boundary, scope, or acceptance.

Failure signals:

- Workflow compresses a deep-confirmation request into a light checkpoint.
- Workflow drops the user's wording, checked facts, or decision ledger.
- Workflow sends an uninitialized or free-form packet that cannot distinguish empty fields from omitted fields.
- Product restarts a fixed questionnaire after routing.
- Product silently carries material risk into design or implementation.

Manual evaluation: pass only when deep interview intent survives the route and the final handoff is user-grounded.
