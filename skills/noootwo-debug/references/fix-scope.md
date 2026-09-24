# Fix Scope

Gate B. The cause is proven; this file keeps the fix the same size as the cause.

## The scope ledger

```
Scope: <files allowed to change> / <behaviour allowed to change>
Out:   <what this fix will not touch>
```

Write it before editing, from the proven cause — not from the diff you would enjoy writing. The scope is a claim you will check afterwards.

## The trace test

After the fix, walk the diff hunk by hunk and ask: which part of the proven cause does this address? A hunk with no answer is a separate change. Take it out, write it down, and ask — "while I was here" is how a one-line fix becomes a review nobody can trust.

The same test applies before editing: every planned change must trace to the cause, or it is not part of this task.

## Fix at the right layer

- Fix where the cause lives, not where it hurt. Bad data entering at the boundary is validated at the boundary, not defended against at fifteen call sites.
- Ask "why" until the next answer leaves the code you control. The null check that crashed is rarely the cause; why it was null is.
- Prefer removing the cause over containing it. A guard around a condition that should not happen is a symptom fix unless the condition is genuinely reachable.
- Check the blast radius: who else calls this, and who relied on the wrong behaviour?

## Signs the fix is the wrong size

- The diff spans modules that the cause does not.
- The fix needs a new abstraction, dependency, or config knob to work.
- You are editing several call sites to compensate for one bad input.
- A rename, a reformat, or an opportunistic refactor is riding along.
- The change is greenfield scaffolding for a need that has not arrived.

Any of these means: stop, name the scope violation, and let the user decide.

## Mitigation versus real fix

When the correct fix is large, risky, or touches a public contract, do not quietly pick a size. Present the options:

- **Scoped mitigation now** — stops the damage, with the real fix written down and tracked.
- **Real fix directly** — larger diff, larger risk, no interim state.

Name what each option leaves unproven. The choice is the user's, not the agent's.

## Siblings and cleanup

- **Hunt siblings** — search for the same mistake elsewhere. Bugs of a kind travel in packs: the same misused helper, the same schema assumption, the same off-by-one in three files.
- **Remove the instrumentation** — probes, prints, hardcoded values, commented-out code, loosened timeouts, skipped tests. Leaving them is how a debug session becomes a permanent behaviour change.
- **Read the final diff line by line** — as a reviewer, not as the author. If the diff and the scope ledger disagree, the ledger wins or the user decides.

## What not to solve here

A fix that grows into a refactor, an architecture change, or a product behaviour change has left this task. Report the cause and the evidence, then hand it over: `noootwo-code-health` judges whether the larger change is warranted, `noootwo-product` settles what the behaviour should be. Proving the cause was the job; the fix is allowed to be small.
