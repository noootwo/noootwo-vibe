# Eval Prompt: The Same Bug Class Returned

Use `$noootwo-debug` on a bug that is the third occurrence of the same class in two months, with three separate local patches already shipped.

Expected behavior:

- Prove the current instance before changing anything.
- Identify the recurring mechanism, the repeated failed control, and the governing assumption or process that keeps allowing it.
- Move beyond single-loop patching: change the invariant, test, type/lint rule, observability, review gate, or skill/eval that owns the class.
- Route structural work to `noootwo-code-health` and durable facts to `noootwo-state` when it exceeds the local fix.
- Define the signal that would show the class returned again.

Failure signals:

- Ships a fourth patch with no recurrence barrier.
- Calls the repeated class “unrelated” without evidence.
- Claims a process change without naming where it lives or who verifies it.
- Expands into a broad rewrite before the local cause is proven.

Manual evaluation: pass only when the response shows the expected behavior and avoids all failure signals.
