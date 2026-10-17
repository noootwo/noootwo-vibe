# Eval Prompt: A Proven Fix Still Needs A Systemic Close

Give `$noootwo-debug` a production bug that has been reproduced, localized, fixed, and verified with a toggle and regression test. The fix is one line and the original report is closed as “fixed”.

Expected behavior:

- Preserve the proven evidence chain and local fix.
- Add a `Systemic Close` before declaring the debug work complete.
- Name the three causal layers: mechanism, failed or missing control, and learning/process condition.
- Search for sibling paths and near-miss or fragile-success paths, recording the search scope and results.
- Choose the smallest recurrence barrier with an owner, verification, and disposition.
- State what remains uncertain instead of inventing a latent cause.

Failure signals:

- Ends with only the local fix, toggle, and regression test.
- Treats “the line is fixed” as proof that the class cannot return.
- Produces a long architecture wish list for a trivial isolated defect.
- Claims a latent path without a concrete condition, path, or hypothesis label.

Manual evaluation: pass only when the response shows the expected behavior and avoids all failure signals.
