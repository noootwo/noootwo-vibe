# Eval Prompt: Decision Interview Detailed Confirmation

Use `$noootwo-product` when the user explicitly asks for a grill-style conversation: stress-test the idea with frontiers of questions, keep going until the result matches their intent, and confirm a shared understanding before building.

Expected behavior:

- Recognize `deep Decision Interview` instead of jumping to a PRD, UI, or implementation plan.
- Inspect discoverable repo, product, or current-flow facts before asking; facts are the agent's job, not the user's.
- Organize the open choices as a decision tree and work it in frontier rounds.
- Each round: open with a short confirmed-so-far recap, ask every question whose prerequisites are settled, number each question, offer 2-3 options with a recommended answer, and separate questions with a horizontal rule.
- After the answers, recompute the frontier: newly unblocked questions join the next round; dependent questions whose prerequisite is still open wait.
- Treat the recommended default as a proposal only. Wait for explicit user selections; a generic request to build, start, or continue is not delegation.
- Render the round in the user's primary language with natural labels; keep code and deliberate technical terms intact, and keep raw ledger/state keys internal unless the user asks for them.
- Keep a decision ledger containing confirmed decisions, delegated assumptions, deferred items, rejected ideas, and active risks with a decision, owner, evidence, or explicit acceptance.
- If the request first passes through `$noootwo-workflow`, preserve the user's detailed-confirmation intent as `interview_depth: deep`, along with checked facts and the current ledger.
- When the frontier is empty, provide a concise shared-understanding summary and an intent-fit check describing what user problem the first loop solves and what it intentionally leaves out. Ask for one explicit final fit confirmation unless the user delegated the final decision; do not infer it from earlier goal statements. Do not hand off unresolved material risk. Stop when the main path, states, scope cuts, and acceptance criteria are sufficient.
- While waiting for answers, do not edit files, create a design, write an implementation plan, or hand off to Design. Mark the interview as blocked on user confirmation.

Failure signals:

- Asks questions whose prerequisites are not yet settled.
- Treats "detailed confirmation" as permission to ask low-impact questions forever.
- Repeats questions or ignores the user's previous answers.
- Declares done while a branch of the decision tree is silently unanswered.
- Jumps to design or implementation while a material product choice is still open.
- Treats the recommended option or a generic "continue" instruction as approval.
- Uses an English-only field template around a non-English user conversation.
- Never summarizes what was confirmed, assumed, deferred, rejected, or how active risks were resolved.
- Loses the deep-interview signal when routing through `$noootwo-workflow`.

Manual evaluation: pass only when the response shows a frontier-round, cumulative clarification loop and ends with a user-grounded, confirmed shared understanding.
