# Eval: Schedule one next step, not a full DAG

Prompt: "Add a tested export feature, review it, update the docs, and release it."

Expected:

- Workflow invokes one owner at a time and hands the next frontier to `noootwo-state` after each result.
- It does not precompute and execute a large fixed plan in one turn.
- TDD runs before review; review runs before release; docs run after behavior changes.

Fails when: it performs multiple specialist jobs itself, or treats the whole request as one direct edit.
