# 0028 — Delivery isolation and main-only production

## Status

Accepted on 2026-11-06 and shipped in workspace `0.27.0`.

## Context

The suite had a release owner for versioning, tags, immutable artifacts,
deployment traces, provenance, rollback, and release health. It had no owner for
the path that produces the release candidate in the first place:

- two concurrent requirements sharing one checkout or one shared contract;
- branch and worktree selection;
- a model creating a sibling filesystem copy or separate clone to avoid touching
  the current checkout, producing two histories, docs, and state roots;
- protected-main integration, merge queues, and current-base checks;
- a rule that production must not be built from a feature or unmerged release
  branch;
- a hotfix path that returns to the mainline before shipping.

The release skill's build-once and immutable-artifact rules could identify a
bad source after it was already chosen, but they did not define which source was
eligible. Workflow could schedule work but was not the delivery-method owner.
Code health could review readiness but did not own branch isolation or merge
policy.

## Research

No single public skill covered the whole practical chain. The strongest
mechanisms were split across separate skills:

- `obra/superpowers` v7.0.2, commit
  `22f0b463e7a5e579904dd6211a520321035526f7`: detect an existing linked
  worktree before creating one, distinguish a submodule, prefer native worktree
  tooling, keep the fallback directory ignored, run a clean baseline, close a
  branch only after integration evidence, and parallelize only independent
  work.
- `addyosmani/agent-skills`, commit
  `301b02b12bff98e4688e6984af6556802322bbde`: trunk-based development,
  short-lived branches, worktrees for parallel streams, small atomic changes,
  feature flags instead of long-lived incomplete branches, and immutable release
  tags.
- `fudesign2008/open-skills` v3.34.0, commit
  `22078941282b4032f3884179ce9c6799b1ddbedb`: live branch-protection reads,
  exact tip pinning, post-merge ancestry checks, worktree reuse, and
  remote-first release tags. Its A→B→C→R→D gate chain, coverage dependency,
  OpenSpec archive gate, mandatory squash prompt, and heavy records were
  rejected as disproportionate for this suite.
- `mattpocock/skills`: a useful counterexample. Its merge-conflict skill was
  removed by v1.3.0; the archived note says the agent can work through an
  ordinary merge or rebase without a dedicated skill. The remaining useful
  claim is that file-level partitioning is not the control; a large late
  refactor or a semantic contract conflict is the expensive case.

The standards basis is Trunk Based Development, DORA's trunk-based delivery
capability, Google Engineering Practices' small changes guidance,
Build/Release/Run from The Twelve-Factor App, GitHub protected branches,
required checks, merge queues, and environment rules, and GitLab merge trains
and protected environments.

## Decision

1. Add `noootwo-delivery` as a model-invoked public skill at `0.1.0`.
2. Delivery owns the Delivery Policy, one-requirement-per-branch/worktree
   isolation, the pre-parallel Overlap Check, protected-main integration, and
   the eligibility handoff to release.
3. A requirement with an active concurrent writer gets its own short-lived
   branch and worktree. Existing isolation is reused; worktrees are never
   nested. A tiny single-writer local edit may stay in place. A sibling
   filesystem copy or separate clone is never isolation: it has its own
   `.git`, refs, docs, and state. The primary checkout owns project-level
   `.noootwo`; linked worktrees pass that root to `noootwo-state`.
4. Shared file names alone do not serialize work. Shared API, schema, event,
   component, config, migration, or generated-output meaning does. The default
   resolution is serialize or contract-first; an incomplete feature uses a flag,
   and a schema change uses expand/contract.
5. Integration goes through a PR/MR to protected `main`, with required checks on
   the current base. Use a merge queue when available; otherwise update the
   branch and recheck the resulting merge candidate.
6. Production may build or deploy only the exact `main` commit, or an annotated
   release tag whose peeled commit is reachable from protected `main`. Feature
   branches, unmerged release branches, mutable branches, floating tags, and
   unrecorded working trees are rejected.
7. Hotfixes branch from `main`, return through the same gate, and only then
   enter release. Rollback stays in `noootwo-release` and uses a previous
   immutable artifact or a revert PR that creates a new `main` commit.
8. `noootwo-workflow` schedules delivery before the first concurrent write and
   after green/review for integration. `noootwo-release` owns the final source
   eligibility check, artifact identity, deployment, and rollback.

## Rejected alternatives

- **GitFlow or a long-lived integration branch as the default.** It increases
  divergence and delayed integration; trunk-based short branches are cheaper
  and match the existing `codex/*` workflow.
- **Permanent file ownership or lock files.** The expensive conflicts are
  semantic and contractual, not two independent edits in one file.
- **A worktree for every edit.** Direct, tiny, single-writer changes stay
  direct; isolation is conditional on concurrency or review/merge boundaries.
- **A sibling filesystem copy or separate clone for isolation.** It protects
  the current checkout at the cost of a second history, docs tree, and state
  root; integration becomes manual diff copying. If one exists, its intended
  change is ported into a linked worktree and verified before the copy is
  archived.
- **Per-requirement preview or production environments.** Preview isolation can
  be useful, but it is not a substitute for a main-only production source.
- **A universal merge queue.** Platforms differ; the requirement is current-base
  integration evidence, with the queue as the preferred mechanism when present.
- **Mandatory squash.** The project records one method; squashing is not a
  production-safety requirement and can obscure meaningful commits.
- **A five-part merge gate, mandatory coverage analyzer, OpenSpec archive, or
  three-option closeout menu.** Those mechanisms impose project-specific
  dependencies and ceremony; they are not the minimum that prevents the
  concrete failure.
- **Deploying a feature branch “just for the demo.”** A non-production preview
  is allowed when clearly isolated; production remains main-only.

## Consequences

- The public set grows from eleven to twelve skills.
- Workflow gains a delivery stage but keeps ownership of scheduling; release
  keeps versioning, artifacts, deployment, and rollback; code health keeps
  review and readiness.
- One canonical checkout owns project state; worktrees share the repository
  history and use the primary state root instead of creating a second context.
  Concurrent writes have one writer. ADR 0031 narrows this rule: no worker or
  secondary worktree writes snapshots, events, or evidence; all state writes
  return to the integrator because the helper's read-modify-write path is not
  concurrency-safe.
- A shared contract can no longer be “parallel because the files differ.”
- The live platform rule remains authoritative. A policy document that is not
  enforced by branch protection, environment rules, or CI is recorded as a gap,
  not described as a guard.
- The suite does not configure a remote repository or deploy anything. It
  supplies the policy and the release-time rejection rule; platform setup is an
  explicit operational task.

## Verification

- Eleven `noootwo-delivery` eval contracts cover independent parallel work,
  shared-contract serialization, same-file independence, worktree reuse,
  sibling-copy rejection and recovery, feature-branch rejection, main-commit
  acceptance, hotfix return, no-queue rechecks, and release-owned rollback.
- A `canonical-state-root` state contract covers recording project context
  from a linked worktree without creating a second `.noootwo`.
- `noootwo-release` adds a ten-point production-source reference and a
  `production-source-main-only` eval.
- Workspace validation enforces the public set, versions, descriptions, line
  budgets, reference pointers, and capability map.
- Fresh-session behavior and a live protected-branch audit remain open until
  they are actually run; no enforcement or behavior-saving claim is made before
  then.
