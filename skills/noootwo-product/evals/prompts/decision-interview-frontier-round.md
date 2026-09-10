# Eval Prompt: Decision Interview Frontier Round

Use `$noootwo-product` on a request with several independent, high-impact product gaps whose prerequisites are already settled (for example: unclear first user, unclear monetization stance, and unclear first-loop scope, none depending on each other).

Expected behavior:

- Run the Clarity Gate and classify as `ambiguous/high-risk` deep interview.
- Ask all settled-prerequisite questions in one round, numbered, each with 2-3 options and a recommended answer.
- Separate questions with a horizontal rule and open the round with a short confirmed-so-far recap.
- Park dependent questions whose prerequisite is still open; do not guess the dependency's answer.
- Wait for the user's answers before recomputing the frontier.

Failure signals:

- Asks only one question when several independent ones are answerable now.
- Dumps a fixed intake list including low-impact or technical questions.
- Answers its own questions without waiting for the user.
- Reveals a dependency answer it invented instead of parking the dependent question.

Manual evaluation: pass only when the response shows the expected behavior and avoids all failure signals.
