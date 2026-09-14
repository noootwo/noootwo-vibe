# Eval: Prove before fixing

Fixture: a small repo with one seeded bug and one decoy that looks suspicious and is innocent — for example, a wrong total caused by a parse function that drops text after a separator, with a deliberately audited rounding helper sitting next to it.

Prompt: "The invoice total is wrong for some orders. Fix it."

Expected:

- It states expected versus actual and attaches the raw failure, rather than paraphrasing the symptom.
- It reproduces the failure with a named command before editing anything.
- It localizes by tracing checkpoints from entry to symptom in one pass, or by bisecting, and names the first point where actual differs from expected.
- It writes the causal chain and rules out at least one competing hypothesis with a named experiment before the first edit.
- It leaves the decoy untouched.
- It verifies with a toggle — revert the fix, watch the symptom return, restore it — and with a regression test that fails on the pre-fix code.
- It reports the chain: cause, proof, scope, verification, and what remains open.

Fails when: it edits before the cause is proven; it pattern-matches the decoy; it restates the symptom as the cause; it claims the fix without a toggle or a failing-first regression test.
