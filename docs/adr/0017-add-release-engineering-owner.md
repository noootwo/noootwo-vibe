# 0017 — Add noootwo-release as the release-engineering owner

## Status

Accepted.

## Context

The suite could judge whether code was ready to ship, schedule release work, and
persist release facts, but no skill owned the release-engineering method itself.
Version policy, immutable artifact identity, deployment traces, provenance,
rollback, and release health were scattered across code-health's readiness lens,
workflow's scheduling, and state's storage.

Semantic Versioning, Keep a Changelog, The Twelve-Factor App, OpenTelemetry
resource conventions, SLSA provenance, GitHub artifact attestations, Sentry
Releases, and DORA all treat release identity, artifact provenance, deployment
traceability, recovery, and release health as distinct engineering concerns.

## Decision

- Add `noootwo-release` as a model-invoked public skill with version `0.1.0`.
- The skill owns version policy, tags, immutable artifact identity, release
  records, deployment traces, provenance, rollback/forward-fix, and release
  health.
- `noootwo-code-health` keeps the ship-readiness gate and consumes the Release
  Plan; `noootwo-workflow` keeps scheduling; `noootwo-state` keeps persistence;
  `noootwo-debug` consumes release traces; `noootwo-onboard` routes missing
  release foundations to release.
- `tag` is a mode inside release, not the owner name.
- External CI, deployment, artifact, and observability tools are execution
  resources; release owns the policy and evidence, not a vendor binding.

## Consequences

- Release identity and rollback evidence become explicit completion criteria for
  non-direct releases.
- The public skill set grows from ten to eleven skills, with release inserted
  between code-health and state.
- Versioning and deployment remain one owner, so no separate versioning or
  deployment skill is added.
