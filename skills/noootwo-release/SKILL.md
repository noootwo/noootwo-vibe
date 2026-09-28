---
name: noootwo-release
description: "Use when versioning, tagging, releasing, deploying, rolling back, or tracing a release: version policy, immutable artifact identity, changelog, provenance, deployment markers, and release health."
---

# Noootwo Release

Own release engineering: version, artifact, release record, deployment trace, rollback, and release health. Code health decides whether a change is ready; this skill owns how the release is identified, produced, promoted, traced, and reverted.

## When this runs

- A version, tag, changelog, release note, or compatibility decision is needed.
- A release is being prepared, built, promoted, deployed, or rolled back.
- A project needs runtime version traceability or release-health evidence.
- Onboarding finds a missing release path, or debugging needs a version/deployment trace.

## Inputs

- The readiness decision and known gaps from the upstream ship-readiness gate.
- The project's current version source, release policy, CI or deploy commands, artifact system, environments, and observability.
- If readiness is missing, not ready, or the next owner is unclear, invoke `noootwo-workflow`: read its `SKILL.md` and follow it.

## Release Plan

Produce this before changing a version, tag, artifact, or environment:

```markdown
Release Plan
- Version source of truth:
- Current version:
- Next version and rationale:
- Compatibility classification:
- Release ID / tag:
- Commit SHA:
- Artifact identity / digest:
- Config version:
- Changelog / release notes:
- Migration and deprecation notes:
- Provenance / SBOM / signature:
- Deployment markers:
- Rollback or forward-fix:
- Post-release health checks:
- Verification gaps:
```

## Modes

| Mode | Owns |
| --- | --- |
| `version` | version scheme, source of truth, compatibility, deprecation |
| `tag` | immutable release ID and the tag that points to it |
| `artifact` | build-once identity, digest, provenance, SBOM, signing |
| `deploy` | artifact promotion, configuration separation, environment markers |
| `trace` | version in logs, metrics, traces, health endpoints, build info |
| `rollback` | previous release, rollback or forward-fix, flags, migrations |
| `health` | release adoption, errors, latency, crashes, regressions |

## Rules

- One version source of truth per project. Record the chosen source as a decision in `noootwo-state`.
- A tag points to a version; it never creates one. Prefer annotated tags for release identifiers.
- Build once, promote the same artifact, and keep environment differences in configuration.
- A release is immutable and append-only. Any change creates a new release ID.
- Record at least artifact digest, commit SHA, build identity, environment, and build time.
- A missing SBOM, attestation, or signature is a recorded gap, never a claim of provenance.
- Rollback or forward-fix is mandatory in the release plan. Use expand/contract migrations for irreversible changes.
- Emit the minimum trace fields from [deployment-trace](references/deployment-trace.md) so a production problem can be mapped to one release.
- External CI, deployment, artifact, and observability tools are execution resources; this skill owns their policy and evidence, not their vendor configuration.

## Done when

The Release Plan is complete, the version and artifact identity are consistent, the deployment trace is defined or verified, rollback is explicit, post-release health checks are named, and every gap is recorded through `noootwo-state`.

## Hand off

- Persist release records, version decisions, deployment events, and evidence → invoke `noootwo-state`.
- Sequence release work, expand scope, or resolve an owner tie → invoke `noootwo-workflow`.
- A regression needs a proven cause → invoke `noootwo-debug`.

## References

- `references/versioning.md` — version source, SemVer, changelog, compatibility, and deprecation.
- `references/artifacts.md` — build/release/run, immutable artifact identity, provenance, and signing.
- `references/deployment-trace.md` — release markers in logs, metrics, traces, health, and build info.
- `references/rollback.md` — rollback, forward-fix, flags, migrations, canary, and blue/green.
- `references/release-health.md` — release adoption, regression, DORA signals, and diagnosis handoff.

Missing skill fallback: first try `npx -y skills add noootwo/noootwo-vibe --global --agent codex --skill <name> --yes`; if install fails, take the smallest direct fallback and mark the record `skill-missing: <name>` (for persistence, write the owning file directly).
