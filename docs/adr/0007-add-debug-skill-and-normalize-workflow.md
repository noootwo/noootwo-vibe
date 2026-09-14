# ADR 0007: Add A Debug Skill And Normalize Workflow As A Scheduler

- Status: accepted
- Date: 2026-09-14

## Context

Two failures kept showing up in real use.

**Fix-first debugging.** An agent reads a symptom, pattern-matches a plausible cause, edits a file, and declares victory. The observable damage is rework: the fix does not hold, the edit was for a bug that was never there, or a one-line fix arrives attached to a refactor nobody asked for. There was no skill that owned proving a cause, so `noootwo-workflow` carried a one-line rule ("record the reproduction and the root cause before any fix") that was too weak to change behaviour and duplicated nothing.

**A drifting scheduler.** `noootwo-workflow` is meant to schedule. Its body and playbook had accumulated concrete method: a diagnostic procedure, build guidance, a project-entry procedure, and a routing matrix that answered bug reports with workflow itself. Concrete handling in the scheduler is how a specialist's job gets done twice, differently.

A research pass over prior debug-skill designs found the useful division of labour:

| Source | What it contributes | What we did not take |
| --- | --- | --- |
| `obra/superpowers` — `systematic-debugging`, `root-cause-tracing`, `defense-in-depth`, `verification-before-completion` | the Iron Law (no fix before root cause), the four-phase loop, "three failed fixes means question the architecture", the "no completion claim without fresh evidence" gate | its length; the process promises evidence without requiring raw output |
| local `pua` / `pua-debugging` | the anti-rationalization table, the structured exit report (confirmed / ruled out / narrowed / next / handoff) | the coercive rhetoric; it is a motivation layer that names `systematic-debugging` as its own method |
| `ujjwal502/debugduck` | one-pass checkpoint tracing, the hypothesis ledger with per-hypothesis refutation, the `[observed]`/`[inferred]`/`[assumed]` labels, the toggle test | its stack catalogue, which is better discovered per project |
| `wshobson/agents` `parallel-debugging` | stating confirming *and* falsifying evidence before investigating | the multi-agent parallel topology |
| `nai0om/buddhist-method`, `summerliuuu/no-no-debug` | "name at least three plausible causes first"; the value of a logged error history | the philosophical framing and the error-tracking system |
| `anthropics/skills` | — | no general debug skill exists there |

The decisive evidence is `debugduck`'s own eval: on four seeded bugs, an agent *without* the skill reproduced the failure 4/4 and found the true root cause 4/4. The measurable gap was afterwards — toggle proof 4/4 versus 2/4, and a regression test that fails on pre-fix code 3/3 versus 0/3.

That inverts the obvious design. Re-teaching "reproduce first" buys nothing; the weight belongs on proving the fix, proving the cause, and not over-editing.

## Decision

1. Add `noootwo-debug` as the seventh public skill, model-invoked like the other specialists. It fires on its own trigger — broken, failing, flaky, slower, wrong behaviour — and the siblings can reach it.
2. Shape it around two gates rather than a phase narrative. **Gate A** blocks every edit until the cause is proven: a causal chain that covers all observed facts, a discriminating experiment the cause survived, and competing hypotheses refuted by named experiments. **Gate B** blocks the fix claim until a toggle test flips the symptom, a regression test fails on the pre-fix code, and every hunk traces to the proven cause.
3. Give the fix a declared size. Scope is written before editing as allowed files and allowed behaviour; a hunk that cannot trace to the cause is a separate change that returns to the user. A fix larger than its cause is presented as "scoped mitigation now" versus "the real fix", as the user's decision.
4. Carry the method in three references — `evidence-chain.md`, `hypotheses.md`, `fix-scope.md` — and keep `SKILL.md` to the gates, the steps, and the pointers.
5. Normalize `noootwo-workflow` as the scheduler. It owns order, scope, stop conditions, and handoffs; the specialists own the work. Diagnostic mode becomes a delegation to `noootwo-debug`, and the playbook's routing matrix, default loop, stop conditions, and handoff packets follow. `AGENTS.md` states the rule so the drift does not silently return.
6. Update the skill-set count in `AGENTS.md`, `skills.json`, the validator, the invocation model, the manifest reference, `status.md`, the README, and the plugin manifest.

This refines [ADR 0004](0004-lightweight-triggered-workflow-control.md) rather than superseding it. Workflow still requires the guardrail judgments before editing, at close, and before submit; what leaves the scheduler is the diagnosis method itself. The repro-first judgment in ADR 0004 now resolves to "route the bug to `noootwo-debug`".

## Consequences

- Every turn loads one more skill description — the accepted cost of a distinct trigger that fires without the scheduler running first.
- `noootwo-workflow` loses method it never should have owned, and its playbook becomes a routing table rather than a partial debug guide.
- The evidence chain is a claim about behaviour, so it is written as a testable gate: each reference and each gate names what it must produce, and the eval scenarios under `skills/noootwo-debug/evals/prompts/` specify how to measure it.
- The gates are asserted, not yet measured. `docs/status.md` records that as an active risk, with the probe — seeded bugs, a hidden verifier, and a decoy — as the next action. Until it runs, no claim is made that the skill reduces rework.
- Deterministic enforcement of the gates stays out of scope, consistent with ADR 0006.
