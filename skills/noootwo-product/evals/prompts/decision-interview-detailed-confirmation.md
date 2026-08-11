# Eval Prompt: Decision Interview Detailed Confirmation

Use `$noootwo-product` when the user explicitly asks for a grill-style conversation: confirm requirements carefully, ask one question at a time, and keep checking until the result matches the intended use.

Expected behavior:

- Recognize `deep Decision Interview` instead of jumping to a PRD, UI, or implementation plan.
- Inspect discoverable repo, product, or current-flow facts before asking.
- Start with the highest-impact unresolved decision, not small visual or implementation details.
- At each turn, briefly summarize confirmed facts, name the one remaining decision, explain why it matters, and ask one focused question with 2-3 options plus a recommended default.
- Treat the recommended default as a proposal only. Wait for an explicit user selection; a generic request to build, start, or continue is not delegation.
- Render the turn in the user's primary language with natural labels; keep code and deliberate technical terms intact, and keep raw ledger/state keys internal unless the user asks for them.
- Show the relevant repo or current-flow facts that shaped the question instead of asking the user to repeat them.
- Make follow-up questions conditional on the user's answer; do not restart a fixed questionnaire.
- Keep a decision ledger containing confirmed decisions, delegated assumptions, deferred items, rejected ideas, and active risks with a decision, owner, evidence, or explicit acceptance.
- If the request first passes through `$noootwo-workflow`, preserve the user's detailed-confirmation intent as `interview_depth: deep`, along with checked facts and the current ledger.
- Before handoff, provide a concise convergence summary and an intent-fit check describing what user problem the first loop solves and what it intentionally leaves out. Ask for one explicit final fit confirmation unless the user delegated the final decision; do not infer it from earlier goal statements. Do not hand off unresolved material risk. Stop when the main path, states, scope cuts, and acceptance criteria are sufficient.
- While waiting for an answer, do not edit files, create a design, write an implementation plan, or hand off to Design. Mark the interview as blocked on user confirmation.

Failure signals:

- Asks a long batch of questions in one response.
- Treats “detailed confirmation” as permission to ask low-impact questions forever.
- Repeats questions or ignores the user's previous answer.
- Jumps to design or implementation while a material product choice is still open.
- Treats the recommended option or a generic "continue" instruction as approval.
- Uses an English-only field template around a non-English user conversation.
- Never summarizes what was confirmed, assumed, deferred, rejected, or how active risks were resolved.
- Loses the deep-interview signal when routing through `$noootwo-workflow`.

Manual evaluation: pass only when the response shows a conditional, cumulative clarification loop and ends with a user-grounded handoff.
