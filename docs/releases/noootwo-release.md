# noootwo-release Releases

## v0.2.0

- Release now requires a Release Check for the exact commit before the Release Plan: full suite or CI evidence, full Structure Sweep, release evidence, and named gaps.
- A green Change Check is explicitly not release readiness; missing evidence routes back through `noootwo-workflow`.
- Added the Release Check evidence field to the Release Plan and a new eval for the Change Check / Release Check boundary.

## v0.1.0

- Added `noootwo-release` as the release-engineering owner: version policy, tags, immutable artifacts, release notes, deployment traces, provenance, rollback, and release health.
- Added a mandatory Release Plan covering version source, compatibility, artifact identity, configuration, deployment markers, provenance gaps, rollback/forward-fix, and post-release health.
- Added references for versioning, artifacts, deployment traces, rollback, and release health, plus release evals for version conflicts, SemVer classification, missing release notes, artifact promotion, missing traces, irreversible migrations, missing provenance, and production regression localization.
- Release consumes code-health readiness and persists release facts through `noootwo-state`; external CI/CD tools remain optional execution resources.
