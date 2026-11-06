---
name: noootwo-delivery
description: "Use for branch/worktree isolation, sibling copies, concurrent requirements, merge conflicts, or protected main; one canonical repo and state root, production stays main-only."
---

# Noootwo Delivery

Own the path from a requirement's working copy to protected `main`: workspace isolation, overlap decisions between concurrent requirements, integration, and the recorded Delivery Policy. Code health owns readiness and review; release owns version, artifact, deployment trace, and rollback. Context lifecycle `write -> select -> compress -> isolate -> verify`: load this skill and triggered reference sections; route references over 200 lines through headings or query hits; cap live excerpts at 80 lines; put output over 16 KiB in cold evidence with path and hash; isolate only independent read-only work; keep one writer; verify summaries against source.

## When this runs

- Two or more requirements are active in one repository.
- Work needs a separate branch or worktree, or two agents would otherwise share a checkout.
- A merge conflict, PR to protected `main`, or merge queue is in scope.
- A hotfix must return to the mainline before it can ship.
- The project has no explicit rule for branch isolation, production source, or concurrent work.

## Inputs

- The repository's default branch, contributor rules, CI checks, and live platform protection.
- Current worktree, branch, uncommitted changes, and any active requirement.
- Requirement scope: expected files, shared contracts, migrations, generated output, and acceptance.
- The integration tool in use: native worktree, git worktree, PR/MR host, merge queue, and CI.

## 1. Fix the policy in one place

Read `CONTRIBUTING.md`, `AGENTS.md`, CI configuration, branch protection, and environment rules before changing workflow. The live platform rule wins over a document; an unenforced document is a gap, not a guard.

When no policy exists, create one from `references/delivery-policy.md` and place the durable policy through the `noootwo-state` skill: read its `SKILL.md` and follow it. Keep the default short: protected main, PR integration, checks on the current base, exact-main production, and a hotfix path. Record the project's actual merge method and review rule instead of copying a universal preference.

**Done when:** the branch, integration, production-source, hotfix, and rollback owners have a live value or an explicit gap; no required rule exists only in this conversation.

## 2. Isolate one requirement

Resolve repository identity before creating isolation: `git rev-parse --show-toplevel`, `git rev-parse --git-common-dir`, and `git worktree list --porcelain`. A linked worktree shares the primary checkout's `.git`; a sibling directory with its own `.git` is a separate clone, not isolation. Never create a sibling copy with `cp -R`, `rsync`, or an adjacent `git clone` to protect the current checkout. If a copy already exists, stop and reconcile it using `references/parallel-work.md`.

Detect an existing linked worktree before creating another. Reuse it when it already belongs to this requirement; never nest worktrees. Use the harness's native worktree capability when available, otherwise use the git fallback in `references/parallel-work.md`. Start from the latest `origin/<default-branch>` and give the branch a short, requirement-specific name. The primary checkout owns project-level `.noootwo` state and durable docs merge through one repository history; from a linked worktree, pass the primary root to `noootwo-state` rather than creating a second context. Concurrent state writes serialize through one writer; append events or hand off a current-snapshot update instead of racing it.

A single tiny edit with no concurrent writer may stay in place. Isolation is required when another requirement is active, the work will be reviewed, or the branch must merge independently. One checkout has one writer: switch branches only after the current requirement is committed or handed off.

**Done when:** the canonical checkout, worktree path, branch name, base commit, and active requirement are known; no sibling copy, second state root, or nested/orphaned worktree was created.

## 3. Decide overlap before parallel work

Before two requirements proceed, make one Overlap Check:

```markdown
Overlap Check
- Requirement A / B:
- Expected files:
- Shared API, schema, event, component, or config contract:
- Migration / generated output:
- Decision: parallel | serialize | contract-first
- Merge order and reopen trigger:
```

Use `references/parallel-work.md`. Independent files and independent contracts may proceed in parallel. Serialize when both touch the same semantic region, the same migration order, or an irreversibly generated artifact. Use contract-first when both need the same interface but can work behind it: land a backward-compatible contract first, then rebase both requirements. A large rename or cross-cutting refactor lands before feature edits that would otherwise keep rebasing it.

Same file is not a permanent lock. Separate, semantically independent edits may remain parallel; shared meaning is the dependency. Incomplete shared work uses a feature flag; schema changes use expand/contract; generated clients have one owner.

**Done when:** every concurrent requirement has a parallel, serialize, or contract-first decision with its merge order, or the work is explicitly held.

## 4. Integrate through protected main

Before merge, update the branch from the latest target, rerun the required checks on that base, and confirm the review/Change Check is complete. Open a PR/MR against `main`. Use the merge queue when the platform provides one; otherwise update the branch and rerun required checks on the resulting merge candidate. Direct pushes, local merges to `main`, and long-lived integration branches bypass the gate.

Resolve conflicts from the two changes' intent, not by choosing `ours` or `theirs` wholesale. Read the commits, PR description, issue, and tests; keep both behaviours where the product requires them; rerun the affected checks. Hotfixes branch from `main`, return through a PR, and only then enter release.

**Done when:** the merge commit is on protected `main`, the required checks and review cover the current base, and the branch/worktree is preserved for PR follow-up or cleaned after merge.

## 5. Hand production to release

Production may build or deploy only the exact commit of protected `main`, or an annotated release tag whose commit is reachable from protected `main`. A feature branch, release branch, floating tag, or mutable branch reference is not a production source. Build once and promote the same artifact; do not rebuild per environment.

When the task includes versioning, tagging, build, deployment, or rollback, invoke the `noootwo-release` skill: read its `SKILL.md` and follow it. Rollback is a new controlled action: redeploy the previous immutable artifact or revert through a PR to `main`; never rewrite `main` history.

**Done when:** release receives the eligible commit SHA, tag if any, artifact identity, and the policy location; no production path starts outside protected `main`.

## Hand off

- Persist a new policy, Overlap Check decision, or branch/worktree map → invoke `noootwo-state`.
- Readiness, review, or the next owner is missing → invoke `noootwo-workflow`.
- Version, tag, artifact, deployment trace, rollback, or release health → invoke `noootwo-release`.

## References

- `references/delivery-policy.md` — the minimal policy template, live-rule checks, and default guardrails.
- `references/parallel-work.md` — worktree detection/creation, the Overlap Check, contract-first, flags, migrations, and conflict intent.
- `references/mainline.md` — PR and merge-queue integration, post-merge verification, hotfixes, and production boundaries.

Missing skill fallback: first try `npx -y skills add noootwo/noootwo-vibe --global --agent codex --skill <name> --yes`; if install fails, take the smallest direct fallback and mark the record `skill-missing: <name>` (for persistence, write the owning file directly).
