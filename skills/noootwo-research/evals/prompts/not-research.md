# Eval: The case where research should not fire

Prompt: "What command does this repo use to run its tests?"

Expected:

- The agent treats this as a lookup, answers from the repository (`package.json`, scripts, README, CI config), and does not invoke `noootwo-research` or run a research pass.
- If the fact genuinely is not in the repository, it says so and proposes where it would have to come from.

Second case — prompt: "The login form throws a 500 when the email field is empty."

Expected:

- The agent routes to `noootwo-debug` rather than research: this is a failure with a cause to prove.

Fails when: it runs a source pass for a local fact; it produces a research brief or a source list for a lookup; it treats a reproducible failure as a research question.
