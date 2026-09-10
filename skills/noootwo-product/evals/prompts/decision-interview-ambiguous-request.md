# Eval Prompt: Decision Interview Ambiguous Request

Use `$noootwo-product` on a broad request: "Build a student learning app with AI practice, notes, community, courses, leaderboard, and progress."

Expected behavior:

- Trigger `deep Decision Interview` before design or implementation.
- Check available repo/product truth before asking; facts are the agent's job.
- Organize the open choices as a decision tree and ask the whole settled frontier in one round.
- Number each question, offer 2-3 meaningful options with one recommended answer, and separate questions with a horizontal rule.
- Park questions whose prerequisites are still open for a later round; do not guess answers to unsettled prerequisites.
- Wait for the user's answers; recommendations are not approval.
- Explain how each answer changes first loop, scope, main path, states, or acceptance.
- Mark execution as blocked while material choices are unanswered and do not produce implementation steps in the same turn.

Failure signals:

- Starts a full PRD or complete feature plan immediately.
- Asks one question per turn when several independent frontier questions are already answerable.
- Asks questions whose prerequisites are not yet settled, or silently assumes an unanswered branch.
- Sends the request directly to `$noootwo-design`.
- Treats all listed features as required for the first loop.
- Treats a build request or the recommended default as permission to execute.

Manual evaluation: pass only when the response shows the expected behavior and avoids all failure signals.
