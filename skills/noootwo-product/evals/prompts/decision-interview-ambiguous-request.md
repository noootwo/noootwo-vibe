# Eval Prompt: Decision Interview Ambiguous Request

Use `$noootwo-product` on a broad request: "Build a student learning app with AI practice, notes, community, courses, leaderboard, and progress."

Expected behavior:

- Trigger `Decision Interview` before design or implementation.
- Check available repo/product truth before asking.
- Ask one highest-impact product decision at a time.
- Offer 2-3 meaningful options with one recommended default.
- Wait for the user's explicit selection; the recommendation is not approval.
- Explain how the answer changes first loop, scope, main path, states, or acceptance.
- Mark execution as blocked while the question is unanswered and do not produce implementation steps in the same turn.

Failure signals:

- Starts a full PRD or complete feature plan immediately.
- Asks a long list of questions in one response.
- Sends the request directly to `$noootwo-design`.
- Treats all listed features as required for the first loop.
- Treats a build request or the recommended default as permission to execute.

Manual evaluation: pass only when the response shows the expected behavior and avoids all failure signals.
