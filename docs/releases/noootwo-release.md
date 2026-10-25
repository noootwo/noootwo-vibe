# noootwo-release Releases

## v0.3.1

- Added the package-wide context lifecycle and compressed the always-loaded description.
- Release identity, ledger, provenance, rollback, deployment trace, and health rules are unchanged.

## v0.3.0

- Added the Release Verification Ledger: one open queue for checks that must be decided at the release boundary, with explicit item ownership, evidence, status, and release conditions.
- Requirement-level detail stays in its completed Change Check; repeated cross-cutting checks are deduped by command or evidence boundary instead of copied once per feature.
- Before versioning or tagging, the ledger is reconciled against the exact release-candidate commit. The Release Check consumes each remaining item once.
- The completed ledger is sealed into the immutable release record before the open working ledger is reset. Sealed evidence is never deleted.
- Added `references/release-verification-ledger.md`, a lifecycle eval, and ADR 0021. The release skill keeps ownership of the lifecycle; `noootwo-state` chooses the storage path and form.

## v0.2.0

- Release now requires a Release Check for the exact commit before the Release Plan: full suite or CI evidence, full Structure Sweep, release evidence, and named gaps.
- A green Change Check is explicitly not release readiness; missing evidence routes back through `noootwo-workflow`.
- Added the Release Check evidence field to the Release Plan and a new eval for the Change Check / Release Check boundary.

## v0.1.0

- Added `noootwo-release` as the release-engineering owner: version policy, tags, immutable artifacts, release notes, deployment traces, provenance, rollback, and release health.
- Added a mandatory Release Plan covering version source, compatibility, artifact identity, configuration, deployment markers, provenance gaps, rollback/forward-fix, and post-release health.
- Added references for versioning, artifacts, deployment traces, rollback, and release health, plus release evals for version conflicts, SemVer classification, missing release notes, artifact promotion, missing traces, irreversible migrations, missing provenance, and production regression localization.
- Release consumes code-health readiness and persists release facts through `noootwo-state`; external CI/CD tools remain optional execution resources.
