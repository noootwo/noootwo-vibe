# Eval: Settled means skip ahead

Prompt: a detailed request that names the user, the situation, the outcome, the scope boundary, the main path, the error and permission states, and the acceptance criteria. Repo facts agree.

Expected:

- The agent states that nothing is unsettled and asks no ceremonial question.
- It produces a Product Checkpoint or the Product-to-Design Handoff without showing a grilling round.
- It keeps remaining technical details as stated implementation assumptions rather than blocking questions.
- When UI work is next it invokes the `noootwo-design` skill and hands off the settled fields.

Fails when: it grills because the request is product-shaped; it re-asks facts already given; it blocks on a low-impact preference.
