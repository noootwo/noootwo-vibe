# Eval: Keep independent product frontiers in one round

Prompt: "Build a lightweight review queue for our design team. We have no decision yet on whether it must work offline, whether comments are required in the first release, or whether reviewers can assign work to each other. The target users, review flow, and success signal are already settled."

Expected:

- Identifies the three independent unsettled decisions.
- Asks all three in one round, each with options, a recommendation, and a reason.
- Keeps dependent implementation details parked until those decisions are answered.
- Does not turn the turn into a one-question-per-round interview.

Fails when: it asks only one of several independent root decisions; it collapses the decisions into one vague question; it answers its own questions; or it starts implementation.
