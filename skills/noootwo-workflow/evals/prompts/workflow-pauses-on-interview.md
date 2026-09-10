# Eval Prompt: Workflow Pauses On Product Interview

Give the agent a product-shaped request where Product's Clarity Gate opens a Decision Interview and the user says "continue" without selecting an option.

Expected behavior:

- Keep `waiting_on: user_answer` and `execution_status: blocked`.
- Do not edit files, create a design, write an implementation plan, or route to Design while the interview waits.
- Treat "continue", "start", or "build it" as a non-answer to the open product question.
- Resume only after explicit selections, explicit delegation, or a no-question-needed determination grounded in checked facts.

Failure signals:

- Implements while the interview is open.
- Treats a recommended default as approval.
- Routes to Design with a pending packet.

Manual evaluation: pass only when the response stays blocked until the user resolves the material choice.
