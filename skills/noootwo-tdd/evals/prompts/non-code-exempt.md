# Eval: Non-code work does not force TDD

Prompt: "Rename this markdown section and update the README."

Expected:

- The task is a no-op/docs change, so TDD does not fire.
- Workflow may use `noootwo-state` or direct editing, not `noootwo-tdd`.
- A user opt-out is not required for pure docs/config work.

Fails when: it writes a test for a markdown rename or blocks on TDD.
