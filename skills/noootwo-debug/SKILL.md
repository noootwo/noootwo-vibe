---
name: noootwo-debug
description: "Use when something is broken, failing, flaky, or wrong: a bug, stack trace, failing test, regression, CI-only failure, or behaviour that used to work. Proves the cause before any fix."
---

# Noootwo Debug

Turn a symptom into a proven cause, then the smallest fix that removes it. One evidence chain, not a hunt: every link carries raw output, and no file changes until the chain closes. Making something faster, smaller, or cheaper is optimization, not a failure — that work belongs to the `noootwo-review` skill.

When the expected behaviour is itself unsettled — what the thing should do is a decision, not a fact — invoke the `noootwo-product` skill first: read its `SKILL.md` and follow it.

## 1. Pin the claim

State both halves in the user's words:

```
Expected: <what should happen>
Actual:   <what happens, with the raw error line>
```

Attach the original failure — stack trace, failing assertion, log line, error code. Paraphrase loses the detail that solves it.

**Done when:** expected and actual are written down with the raw failure attached.

## 2. Reproduce

Get it failing on demand, locally, fast.

- Record the exact command and its output; you will run it many times.
- Shrink it: fewest steps, smallest input, shortest loop.
- Intermittent: measure the rate (n/10), then suspect order, time, concurrency, shared state.
- Environment-only failures: the environment difference is the primary lead, not an excuse.

**Done when:** a command or step list produces the failure on demand, or the failure rate is measured.

When it will not reproduce, stop here and gather evidence instead: real logs, telemetry, or instrumentation left in place to catch the next occurrence. A fix for an unreproduced bug is a guess.

## 3. Localize

Narrow "somewhere in this system" to "this line, on this input, in this state".

Default — **trace the whole path in one pass**. Number the checkpoints `CP01…CPnn` from entry to symptom, write down what each should show, run once, and find the first checkpoint where actual differs from expected. One round trip replaces eight, and everything upstream is proven innocent for free.

Fallbacks, when the code cannot be re-run or the path is unknown:

- **Bisect the code path** — one checkpoint at the midpoint; a correct state there puts the cause downstream.
- **Bisect history** — `git bisect run <repro command>` when it used to work.
- **Bisect the input** — halve the input, the config, or the test data; keep halving.
- **Differential debugging** — diff a working case against a broken one and treat the differences as the suspect list.

**Done when:** you can name the checkpoint where the wrong thing happens.

## 4. Prove the cause — Gate A

No file edits before this gate closes.

```
Cause:        <chain from the cause to the symptom>
Discriminate: <the cheapest experiment that would refute this>
Result:       <what actually happened>
Falsified:    <competing hypothesis> — refuted by <experiment>
Labels:       [observed] / [inferred] / [assumed] on every claim
```

Two tests decide the gate:

- **Coverage** — the cause explains every observed fact, including the odd ones. Anything unexplained means you found *a* bug, not necessarily *this* bug.
- **Refutation** — a discriminating experiment ran and the cause survived it. A result that would appear for three different reasons proves nothing.

Every claim still labeled `[assumed]` is a hole in the chain: close it with a tool, or say so and treat the chain as incomplete.

Read `references/evidence-chain.md` for the artifact, the raw-evidence rules, the toggle procedure, and a worked example. Read `references/hypotheses.md` when hypotheses multiply, the failure is intermittent, or three have already been refuted.

**Done when:** the cause is proven by the chain above, and every competing explanation is ruled out by a named experiment.

## 5. Bound the fix — Gate B

```
Scope: <files allowed to change> / <behaviour allowed to change>
Out:   <what this fix will not touch>
```

Fix at the layer that owns the cause, with the smallest change that removes it. Every hunk must trace to the proven cause; a hunk that cannot is a separate change — write it down and ask before touching it.

When the real fix is large or risky, say so and offer the choice: a scoped mitigation now with the real fix tracked, or the real fix directly. That call belongs to the user.

Read `references/fix-scope.md` for the scope ledger, the right-layer rule, and the sibling hunt.

**Done when:** the scope is written, every planned change traces to the cause, and any case for a larger fix went to the user.

## 6. Prove the fix

- **Toggle** — revert the fix and watch the symptom return; reapply and watch it go. Thirty seconds, and nothing proves causality as cheaply.
- **Regression test** — fails before the fix, passes after. Confirm it fails on the pre-fix code; a test that passes both ways tests nothing.
- **Broader check** — run the suite, typecheck, and lint for collateral damage.
- **Siblings** — search for the same mistake elsewhere; bugs of a kind travel in packs.
- **Clean up** — remove probes, prints, and hardcoded values, then read the diff line by line.

**Done when:** the toggle result and the regression proof are recorded, and the diff contains nothing but the fix.

## 7. Close

Report the chain: the cause, the proof, the scope, the verification, and what stays open. When behaviour, state, or release facts changed, invoke the `noootwo-docs` skill to place them: read its `SKILL.md` and follow it. When the fix reaches submit or release, invoke the `noootwo-review` skill: read its `SKILL.md` and follow it.

**Done when:** the chain is in the answer, and the docs and review triggers are invoked or recorded as not applying.

## Stop conditions

- **Three refuted hypotheses** — stop generating a fourth. Audit the premise: is this the code that ran, on the right branch, from a fresh build, in the right process, with the config the process actually sees? Then report what was ruled out.
- **Three failed fixes** — stop editing and question the approach, not the line. Report it as a decision rather than a fifth attempt.
- **No reproduction** — gather evidence, instrument, wait. Do not fix on spec.

## Reference

- `references/evidence-chain.md` — the chain artifact, raw-evidence rules, the toggle procedure, the worked example.
- `references/hypotheses.md` — the hypothesis ledger, discriminating experiments, the assumption audit, intermittent failures.
- `references/fix-scope.md` — the scope ledger, the right layer, mitigation versus real fix, siblings, cleanup.
