# Delivery Policy

This is the repository's intended delivery rule. The live platform setting remains authoritative; drift is recorded below.

## Policy

- Default branch: `main`
- Integration route: pull request required; no direct push to `main`
- Required check: the `Validate` workflow must pass on the current base
- Review rule: at least one approval for a shared change; a solo maintainer may merge their own PR only after recording the self-review and green check
- Merge method: merge commit, preserving the PR boundary; squash and rebase are not the default for this repository
- Merge queue: use it when enabled; until then, update the branch and rerun `Validate` on the merge candidate
- Branch lifetime: short-lived `codex/<slug>` branches; merge when independently reviewable and safe
- Canonical checkout / state root: the primary checkout; linked worktrees share its `.git`; project `.noootwo` state stays at this root
- Work isolation: one requirement per linked branch/worktree; reuse an existing worktree; never use a sibling filesystem copy
- Shared boundaries: `skills.json`, `VERSION`, `.codex-plugin/plugin.json`, `AGENTS.md`, `docs/agents/invocation.md`, `scripts/validate_skill_workspace.py`, and the public description index; independent skill directories may run in parallel
- Production source: an exact commit reachable from protected `main`, or an annotated child tag on a `main`-reachable commit
- Publication: build nothing from a feature branch; publish source and child tags after `main`
- Hotfix: branch from `main`, PR back to `main`, then publish a new child tag/release
- Rollback: restore the previous published child version/tag in a new release; never move a shared tag
- Preview/staging: none; this is a source-only skill workspace, not a deployed service

## Live Audit

Observed on 2026-11-06 through the GitHub API:

- `main` branch protection: **protected**
- required route: pull request before merge
- required status check: `validate`, strict/current-base
- administrator enforcement: enabled
- force-push: disabled
- branch deletion: disabled
- required approvals: `0`; the solo maintainer records self-review and the green check
- repository rulesets: **none**
- environments: **none**
- default branch: `main`
- allowed merge methods: merge commit only
- delete branch on merge: enabled
- merge queue: not configured

The policy gate is now live for `main`: direct pushes, force-pushes, and branch
deletion are blocked, and a PR must pass `validate` against the current base.
The remaining platform gaps are the absent merge queue and the absent
production environment restriction. The repository currently has no deployed
production service to exercise those layers.

## Required Platform Setup

Completed on 2026-11-06:

1. `main` is protected.
2. PRs are required; force-pushes and branch deletion are blocked.
3. The `validate` check is required on the current base.
4. Administrators are subject to the rule.
5. Merge commits are the only allowed merge method, and merged PR branches are
   deleted.

Remaining optional setup:

1. Enable a merge queue if the plan supports it; otherwise keep the update-and-recheck fallback.
2. Add an environment restriction when a real production deployment exists.
3. Re-read the live rule and update the audit date above after any remote change.

## Concurrent Work

Two active requirements use separate worktrees and branches. Before either starts, record an Overlap Check across expected files, shared contracts, migrations, generated output, and merge order. A `write-fanout` inside one requirement runs only after the workflow Gate, keeps one integration branch, gives each lane one primary-root-linked worktree, one worker, and custody handles, records a Lane Map, and merges one frozen SHA at a time through one integrator. No worker or secondary worktree writes `.noootwo`; all state writes serialize through the integrator. Shared skill manifests, validation scripts, public descriptions, and release facts are serialized or contract-first; independent skill directories can proceed in parallel. File-name overlap alone is not a permanent lock.

A sibling copy is not a worktree. It has its own `.git`, refs, docs, and `.noootwo` context, so it turns one requirement into a manual diff-copying problem. If one already exists, stop, preserve its uncommitted work, and port only the intended change into a linked worktree from the canonical checkout. Do not delete it without explicit user approval.

## Production Boundary

The published skill set is the production artifact. It must be installable from `main` or from an annotated child tag whose commit is on `main`. The release owner records the exact source commit, tag, and child versions; a feature branch or mutable branch cannot be the source.
