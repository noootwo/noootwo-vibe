---
name: noootwo-debug
description: "Use for broken, failing, flaky, intermittent, CI-only, or previously working behaviour; prove the cause, bound the fix, and prevent recurrence."
---

# Noootwo Debug

Turn a symptom into a proven cause, then the smallest fix that removes it, then a systemic close that asks why the system allowed it. One evidence chain, not a hunt: every link carries raw output, and no file changes until the chain closes. Making something faster, smaller, or cheaper is optimization, not a failure — that work belongs to the `noootwo-code-health` skill.

When the expected behaviour is itself unsettled — what the thing should do is a decision, not a fact — invoke the `noootwo-product` skill first: read its `SKILL.md` and follow it.

## 1. Pin the claim

State `Expected: <what should happen>` and `Actual: <what happens, with the raw error line>` in the user's words, then attach the raw failure. Paraphrase loses the detail that solves it.

**Done when:** expected and actual are written down with the raw failure attached.

## 2. Reproduce

Get it failing on demand, locally, fast.

- Record the exact command and its output; you will run it many times.
- Shrink it: fewest steps, smallest input, shortest loop.
- Intermittent failures: measure the rate (n/10), then suspect order, time, concurrency, or shared state; an environment-only failure makes the environment difference the primary lead, not an excuse.

**Done when:** a command or step list produces the failure on demand, or the failure rate is measured.

When it will not reproduce, stop here and gather evidence instead: real logs, telemetry, or instrumentation left in place. A fix for an unreproduced bug is a guess.

## 3. Localize

Narrow "somewhere in this system" to "this line, on this input, in this state".

Default — **trace the whole path in one pass**. Number the checkpoints `CP01…CPnn` from entry to symptom, write down what each should show, run once, and find the first checkpoint where actual differs from expected. One round trip replaces eight, and everything upstream is proven innocent for free.

When the code cannot be re-run, read `references/evidence-chain.md` for the localization fallbacks: bisect the code path, history, release, or input, or diff a working case against a broken one.

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

Two tests decide the gate. **Coverage:** the cause explains every observed fact, including the odd ones; anything unexplained means you found *a* bug, not necessarily *this* bug. **Refutation:** a discriminating experiment ran and the cause survived; a result that would appear for three different reasons proves nothing.

Every claim still labeled `[assumed]` is a hole in the chain: close it with a tool, or say so and treat the chain as incomplete.

Read `references/evidence-chain.md` for the artifact, the raw-evidence rules, the toggle procedure, and a worked example. Read `references/hypotheses.md` when hypotheses multiply, the failure is intermittent, or three have already been refuted.

**Done when:** the cause is proven by the chain above, and every competing explanation is ruled out by a named experiment.

## 5. Bound the fix — Gate B

```
Scope: <files allowed to change> / <behaviour allowed to change>
Out:   <what this fix will not touch>
```

Fix at the layer that owns the cause. Every hunk must trace to the proven cause; a hunk that cannot is a separate change, written down and approved before it touches the code. When the real fix is large or risky, offer the user the choice between scoped mitigation with a tracked fix and the real fix directly. Read `references/fix-scope.md` for the scope ledger, right-layer rule, mitigation choice, and sibling hunt.

**Done when:** the scope is written, every planned change traces to the cause, and any case for a larger fix went to the user.

## 6. Prove the fix

- **Toggle** — revert the fix and watch the symptom return; reapply and watch it go. Thirty seconds, and nothing proves causality as cheaply.
- **Regression test** — fails before the fix, passes after. Confirm it fails on the pre-fix code; a test that passes both ways tests nothing.
- **Broader check** — run the checks and tests inside the fix's blast radius; a Release Check owns the full suite when the fix is release-bound.
- **Clean up** — remove probes, prints, and hardcoded values, then read the diff line by line.

**Done when:** the toggle result and the regression proof are recorded, and the diff contains nothing but the fix.

## 7. Close the incident

Report the local chain: cause, proof, scope, verification, and what stays open. Invoke `noootwo-state` for durable facts; invoke `noootwo-code-health` when the fix reaches submit or release; invoke `noootwo-release` when a version or deployment trace is missing.

**Done when:** the local fix is closed, and the state, review, and release triggers are invoked or recorded as not applying.

## 8. Systemic prevention

After the incident close, write a `Systemic Close`. It asks why the defect existed, why existing controls missed it, where the same condition remains, and which barrier prevents recurrence. Scale the response to severity, recurrence, and reach: an isolated one-off may record `no credible latent path`; a repeated or high-impact class needs a real barrier.

```markdown
Systemic Close
- Causal layers: mechanism / control / learning
- Similar and latent paths: searched, affected, safe with reason, hypothesis, or not searched
- Near-miss or fragile success: named path and why it escaped
- Recurrence barrier: barrier, owner, verification, disposition
- Learning loop: signal and rule/test/eval/review that changes if this class returns
- Residual uncertainty:
```

Read `references/systemic-prevention.md` for the eight questions, causal layers, sibling and near-miss search, barrier ladder, and academic basis. Report the systemic result alongside the local chain. Structural work goes to `noootwo-code-health`; durable facts go to `noootwo-state`; release controls go to `noootwo-release`.

**Done when:** the proven fix and a systemic close both exist, every latent path or recurrence barrier has a disposition, and the final answer contains both the local chain and the systemic result.

## Stop conditions

- **Three refuted hypotheses** — stop generating a fourth. Audit the premise: is this the code that ran, on the right branch, from a fresh build, in the right process, with the config the process actually sees? Then report what was ruled out.
- **Three failed fixes** — stop editing and question the approach, not the line. Report it as a decision rather than a fifth attempt.
- **No reproduction** — gather evidence, instrument, wait. Do not fix on spec.

## Reference

- `references/evidence-chain.md` — the chain artifact, raw-evidence rules, the toggle procedure, the worked example.
- `references/hypotheses.md` — the hypothesis ledger, discriminating experiments, the assumption audit, intermittent failures.
- `references/fix-scope.md` — the scope ledger, the right layer, mitigation versus real fix, siblings, cleanup.
- `references/systemic-prevention.md` — the eight systemic questions, causal layers, near-miss search, recurrence barrier, and academic basis.

Missing skill fallback: first try `npx -y skills add noootwo/noootwo-vibe --global --agent codex --skill <name> --yes`; if install fails, take the smallest direct fallback and mark the record `skill-missing: <name>` (for persistence, write the owning file directly).
