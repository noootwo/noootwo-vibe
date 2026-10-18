# Release Verification Ledger

One mutable ledger for the next release. It is the queue of verification decisions that must be made at the release boundary, not a second copy of every requirement's Change Check.

This is separate from the append-only **Release Ledger** in `artifacts.md`, which records release identity over time. This file owns the open verification queue and its sealed handoff into that record.

Invoke the `noootwo-state` skill: read its `SKILL.md` and follow it to choose the owning path and storage form. The open ledger is current mutable state; the sealed ledger is immutable release evidence.

## What enters

- Cross-cutting checks that cannot close inside one requirement: the exact-commit full suite or CI result, compatibility, migrations, security boundaries, build and release configuration, artifact identity, provenance, deployment markers, rollback, and release health.
- A requirement-specific check only when its evidence cannot be re-established at the release candidate or its blast radius crosses requirements.
- A known gap that would block or condition the release.

## What stays out

- The detailed Change Check already closed for a requirement.
- Per-file, per-unit, or per-screen assertions whose result will not change at release.
- A second task tracker, changelog, or audit log.
- Duplicate entries for the same evidence. The dedupe key is the check, its exact boundary, and the command or evidence path, not the wording.

## Item contract

```markdown
- ID:
  Source:
  Check:
  Boundary / dedupe key:
  Evidence:
  Owner:
  Status: open | passed | blocked | accepted gap | superseded
  Release condition:
```

`accepted gap` carries the consequence, release condition, and accountable owner; it is a visible risk, not a silent pass. `superseded` names the replacement item.

## Lifecycle

1. **Open** — create one ledger for the next release. Add release-bound checks as they become known; keep requirement-level proof in its Change Check.
2. **Reconcile** — before choosing a version or tag, read every open item. Merge duplicates with the same boundary, supersede obsolete entries, and revalidate evidence against the exact release-candidate commit.
3. **Consume** — the Release Check runs each remaining item once. Record the command or evidence path and the commit it covers.
4. **Seal** — attach the completed ledger to the release record with version, commit, artifact identity, and release ID. The sealed copy is immutable evidence.
5. **Reset** — clear the open working ledger only after the sealed copy exists, then start the next release empty.

## Dedupe examples

- Five features covered by one full-suite command become one full-suite item.
- Backend contract tests and frontend consumer tests crossing the same API boundary become one contract item with both suites as evidence.
- The same migration used by several callers becomes one item per shared schema boundary, not one per call site.

## Stop rules

- Do not tag or publish while an item is `open` or `blocked`, or while an `accepted gap` lacks its consequence, owner, or release condition.
- Do not widen the ledger into every edit; that detail belongs to the Change Check.
- Do not delete a sealed ledger. Supersede it with a later release record.
