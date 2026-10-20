# noootwo-debug Releases

## v0.6.0

- Added the Diagnosis Map as the entry artifact for every debug request. Each claim records its problem class, evidence authority, decisive check, terminal status, stop bound, and handoff.
- Added layer-specific evidence authority for product, external, protocol, code-path, deployment, data, and agent-process claims. Documentation, source code, and live state no longer substitute for one another.
- Confirmation is read-only until every requested claim is `confirmed`, `refuted`, `insufficient`, or `decision-needed`. Only confirmed failures enter the existing Incident Path.
- Added one-check and stop rules so a long report, unrelated system tour, repeated evidence, or more available time cannot widen a settled claim.
- Added `references/diagnosis-map.md` and three evals covering cross-system audit drift, evidence authority, and mutation before a verdict.

## v0.5.0

- Added the Systemic Close as Step 8, organized around eight questions: after the incident is closed, debug asks why the defect existed, why existing controls missed it, where sibling or near-miss paths share the condition, which barrier prevents recurrence, and what learning loop changes if the class returns.
- Added `references/systemic-prevention.md` with eight causal questions, mechanism/control/learning layers, proportional response, sibling and fragile-success search, the recurrence-barrier ladder, and the academic basis from Reason, Leveson, Argyris, Google SRE, and Hollnagel.
- Added four eval scenarios: systemic close required, recurring bug double-loop, near-miss/fragile success, and trivial one-off proportionality.
- Scoped the post-fix broader check to the fix's blast radius; the full suite belongs to the Release Check when the fix is release-bound.
- Migration: completed debug reports now need a Systemic Close. An isolated defect may record `no credible latent path`; it may not omit the close.

## v0.4.0

- Added release-based localization and trace handoff: debug consumes version and deployment identity from `noootwo-release` and asks release to repair a missing trace.

## v0.3.0

- Updated code-health and optimization handoffs from `noootwo-review` to `noootwo-code-health`.

## v0.2.0

- Behaviour, state, and release facts now route to `noootwo-state` at close instead of a local docs owner.

## v0.1.2

- Sharpened the description around intermittent, CI-only, and previously working failures, and the same-size fix boundary.

## v0.1.1

- Tightened the trigger: `slower than expected` left the description, because optimization is not a failure. A regression — behaviour that used to work — is still this skill's work.
- Added the boundary line: making something faster, smaller, or cheaper belongs to `noootwo-review`.


## v0.1.0

- Initial public skill: evidence-chain debugging that proves a cause before any fix.
- Gate A blocks edits until the cause is proven — a causal chain that covers every observed fact, one discriminating experiment survived, and competing hypotheses refuted by named experiments.
- Gate B blocks the fix claim until a toggle test flips the symptom, a regression test fails on the pre-fix code, and the diff contains only change that traces to the cause.
- Scope is declared before editing as allowed files and allowed behaviour; a hunk that cannot trace to the cause is a separate change that goes back to the user.
- Stop conditions: three refuted hypotheses trigger an assumption audit instead of a fourth guess; three failed fixes stop the loop; an unreproduced failure gets instrumentation, not a speculative fix.
- References: `evidence-chain.md`, `hypotheses.md`, `fix-scope.md`.
