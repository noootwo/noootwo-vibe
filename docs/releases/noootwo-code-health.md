# noootwo-code-health Releases

## v0.18.0

- Added a conditional Builder Check for non-obvious, cross-session, expensive, or cross-boundary handoffs. Closed local plans proceed directly to TDD.
- The Builder Check separates `plan-decided`, `builder-may-decide`, `user-decision-required`, and `blocking-ambiguity` before behavior changes.
- Decision-complete implementation plans now record file scope, `Interfaces`, ordered steps, observable test assertions, verification commands, `Review Focus`, and an initially empty ruling ledger.
- Reversible ambiguities during approved execution are recorded as rulings and continue; user-owned decisions, irreversible changes, security or privacy impact, external side effects or spend, and plan invalidation still stop.
- Added three opt-in eval contracts. Fresh model sessions remain unrun.

## v0.17.2

- Added the package-wide context lifecycle and compressed the always-loaded description.
- Lenses, Change Shape, Change Check, escalation, Release Check, and structural dispositions are unchanged.

## v0.17.1

- A disputed premise about failing behavior, the running build, deployment, or current data now routes to `noootwo-debug` or `noootwo-release` before an Integration Read or Change Shape.
- Added `confirm-premise-before-shape` so design cannot build an implementation around a defect or deployment state that has not been confirmed.

## v0.17.0

- Split verification into three evidence depths: `change`, `escalated`, and `release`.
- A completed requirement now gets a Change Check scoped to the diff, changed behavior, nearest callers, affected tests, and one to three lenses. It does not run the full suite or a whole-project Structure Sweep.
- A wide blast radius escalates the check only to the affected suites and lenses. A long task or a large diff does not by itself trigger a Release Check.
- Before release or a ship-readiness submit gate, one Release Check runs the full suite or uses CI evidence for the exact commit, performs the full Structure Sweep, and records release evidence and gaps.
- Updated the review gate, refactoring re-test, output contract, and evals to name the verification depth explicitly.

## v0.16.0

- Added the pre-implementation Integration Read and its compact Change Shape: intent and invariants, seam and ownership, contracts, reuse, reversibility, test seam, smallest first slice, and rejected alternatives.
- Added the trigger and skip rule: non-obvious, cross-boundary, contract, data, migration, or hard-structure changes run the read; obvious local changes do not.
- Kept the new pass inside code-health ownership; architecture, seams, test strategy, maintainability, performance, and optimization remain lenses rather than separate skills.
- Added `references/integration-read.md`, wired the review gate and preparatory-refactoring workflow to it, and added positive, skip, and product-boundary evals.

## v0.15.0

- Changed release readiness into a release-evidence lens: version, artifact, deployment trace, rollback, and release notes are now owned by `noootwo-release`.
- Added the release handoff for version, artifact, deployment trace, rollback, and release-health gaps. Compressed the body to stay within the 120-line budget.

## v0.14.0

- Renamed the skill from `noootwo-review` to `noootwo-code-health`; the old `noootwo-review` tag and release file remain as history.
- Display name is now `Noootwo Code Health（优雅代码）`; the description and short description use elegant and healthy as explicit trigger language.
- The capability is unchanged: change review, the Fowler refactoring health loop, structure sweeps, optimization, project health, re-testing, and acceptance.

## History

See [noootwo-review.md](noootwo-review.md) for releases before the rename.
