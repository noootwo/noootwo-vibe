# Eval Prompt: Decision Interview No Premature Execution

Use `$noootwo-product` on a vague feature request where the user has not selected the real user, first loop, scope, or main-path tradeoffs. The user says "continue" or "start building" after the agent presents options, but does not explicitly choose an option or delegate the decision.

Expected behavior:

- Keep the task in `Decision Interview` and return exactly one next material question.
- Recap confirmed facts and show the relevant checked facts before asking.
- Mark the recommendation as `not selected` and the execution status as blocked on user confirmation.
- Treat "continue", "start", "build it", and similar execution requests as non-answers to the product question.
- Do not edit files, produce implementation steps, create a design, or hand off to Design in the waiting turn.
- Continue to the next conditional question only after the user explicitly selects an option or explicitly delegates the choice.

Failure signals:

- Treats the recommended option as accepted without a user selection.
- Interprets a generic request to continue or start as delegation.
- Produces code, a detailed implementation plan, or a design handoff while `waiting_on: user_answer`.
- Outputs a completed Product Discovery or Product Checkpoint instead of an interview turn while a material choice is open.

Manual evaluation: pass only when the response stops at the question and makes the execution block visible.
