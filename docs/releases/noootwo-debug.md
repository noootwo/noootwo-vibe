# noootwo-debug Releases

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
