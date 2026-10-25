---
name: noootwo-release
description: "Use for versioning, release, deployment, rollback, or release tracing: ledger, artifact identity, provenance, markers, and health."
---

# Noootwo Release

Own release engineering: version, artifact, release record, deployment trace, rollback, and release health. Code health decides whether a change is ready; this skill owns how the release is identified, produced, promoted, traced, and reverted. Context lifecycle `write -> select -> compress -> isolate -> verify`: load this skill and triggered reference sections; route references over 200 lines through headings or query hits; cap live excerpts at 80 lines; put output over 16 KiB in cold evidence with path and hash; isolate only independent read-only work; keep one writer; verify summaries against source.

## When this runs

- A version, tag, changelog, release note, or compatibility decision is needed.
- A pending verification list, release verification ledger, or release readiness pass is needed.
- A release is being prepared, built, promoted, deployed, or rolled back.
- A project needs runtime version traceability or release-health evidence.
- Onboarding finds a missing release path, or debugging needs a version/deployment trace.

## Inputs

- The readiness decision, Release Check evidence, known gaps, and the open Release Verification Ledger from the upstream ship-readiness gate.
- The project's current version source, release policy, CI or deploy commands, artifact system, environments, and observability.
- If readiness is missing, not ready, or the next owner is unclear, invoke `noootwo-workflow`: read its `SKILL.md` and follow it.

## Release Verification Ledger

Keep one open Release Verification Ledger for the next release; read `references/release-verification-ledger.md` before creating or changing it. It is a release-bound queue, not a copy of each requirement's Change Check.

- If no ledger exists, create it at release preparation from the known release-bound checks; do not reconstruct every completed Change Check.
- Add only cross-cutting checks that cannot close inside one requirement, a requirement check whose evidence must be re-established at the candidate, or a known blocking gap.
- Dedupe by the check, exact boundary, and evidence command or path. Repeated features covered by one suite or contract produce one item.
- Before the Release Plan, reconcile open items, supersede obsolete entries, and revalidate them against the exact release-candidate commit.
- The Release Check consumes each remaining item once. Record evidence, owner, and status; `open` or `blocked` stops the release.
- Seal the completed ledger into the release record. Reset the open ledger only after the sealed copy exists; sealed evidence is never deleted.

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
- Release Check evidence:
- Release ledger / sealed record:
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
- A Change Check is not release readiness. Before the Release Plan, require a Release Check for the exact commit: full suite or CI evidence, full Structure Sweep, release evidence, and named gaps. If it is missing, invoke `noootwo-workflow` instead of releasing.
- Record at least artifact digest, commit SHA, build identity, environment, and build time.
- A missing SBOM, attestation, or signature is a recorded gap, never a claim of provenance.
- Rollback or forward-fix is mandatory in the release plan. Use expand/contract migrations for irreversible changes.
- Emit the minimum trace fields from [deployment-trace](references/deployment-trace.md) so a production problem can be mapped to one release.
- External CI, deployment, artifact, and observability tools are execution resources; this skill owns their policy and evidence, not their vendor configuration.

## Done when

The Release Plan is complete, the open ledger is reconciled, the Release Check evidence covers the exact commit, the version and artifact identity are consistent, the deployment trace is defined or verified, rollback is explicit, post-release health checks are named, and the completed ledger is sealed into the release record.

## Hand off

- Persist the open ledger, sealed release record, version decisions, deployment events, and evidence → invoke `noootwo-state`.
- Sequence release work, expand scope, or resolve an owner tie → invoke `noootwo-workflow`.
- A regression needs a proven cause → invoke `noootwo-debug`.

## References

- `references/versioning.md` — version source, SemVer, changelog, compatibility, and deprecation.
- `references/release-verification-ledger.md` — verification ledger scope, item contract, dedupe, reconcile, consume, seal, and reset.
- `references/artifacts.md` — build/release/run, immutable artifact identity, provenance, and signing.
- `references/deployment-trace.md` — release markers in logs, metrics, traces, health, and build info.
- `references/rollback.md` — rollback, forward-fix, flags, migrations, canary, and blue/green.
- `references/release-health.md` — release adoption, regression, DORA signals, and diagnosis handoff.

Missing skill fallback: first try `npx -y skills add noootwo/noootwo-vibe --global --agent codex --skill <name> --yes`; if install fails, take the smallest direct fallback and mark the record `skill-missing: <name>` (for persistence, write the owning file directly).
