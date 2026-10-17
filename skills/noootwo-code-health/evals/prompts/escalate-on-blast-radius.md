# Eval: Risk escalates the check without widening the whole audit

Prompt: "Change the shared event schema used by billing, notifications, and the admin timeline. The local handler test is green."

Expected:

- Labels the pass `Verification: escalated`.
- Recognizes the shared schema as a wide blast radius even though the diff is small.
- Adds the affected consumers' tests and the contract, data, and correctness lenses.
- Does not automatically run a full-project Structure Sweep or unrelated project-health audit.
- Names what remains for the Release Check.

Fails when: it stays on the local handler alone, or jumps from one shared-schema change to a full repository audit.
