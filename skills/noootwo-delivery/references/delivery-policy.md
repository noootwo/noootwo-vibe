# Delivery Policy

One short, project-owned policy keeps branch, integration, and production rules from living only in a conversation. The live platform remains authoritative; this file records the intended rule and the drift.

## Template

```markdown
# Delivery Policy

- Default branch: main
- Integration route: PR/MR required; direct push disabled
- Required checks on the current base:
- Review rule:
- Merge method: merge commit | squash | rebase
- Merge queue: enabled | not available; fallback
- Canonical checkout / state root:
- Work isolation: one linked branch/worktree per requirement; no sibling copy
- Shared boundaries: API | schema | event | component | config | generated files
- Production source: exact main commit or annotated tag on a main-reachable commit
- Hotfix route: branch from main -> PR -> main -> release
- Rollback owner and route:
- Preview/staging exception:
- Live-rule verification date:
- Known gaps:
```

Keep the policy proportional. A solo repository may use zero human approvals, but it still records the rule and runs its CI gate. A shared repository names the reviewer or code-owner rule. A platform that cannot enforce a rule is a recorded gap, not a reason to describe the rule as enforced.

## Minimum Default

- `main` is protected and accepts changes through a PR/MR.
- Required checks run on the current target base, not only on an old branch tip.
- Direct pushes, local merges to `main`, and production from a feature branch are rejected.
- A merge queue is used when available; otherwise the branch is updated and the resulting merge candidate is checked.
- One requirement uses one short-lived branch and, when concurrent, one linked worktree in the canonical repository.
- A sibling filesystem copy or separate clone never substitutes for isolation; project state and durable docs do not get a second root.
- Production is built from an exact `main` commit or an annotated tag on a `main`-reachable commit.
- A hotfix starts from `main` and returns through the same integration gate.
- Rollback uses an immutable previous artifact or a revert PR that produces a new `main` commit.

Preview and staging deployments may use a feature branch when they are clearly non-production and do not receive production data or credentials.

## Read the Live Rule

Use the project's host tooling; do not infer protection from `main`'s name alone. Read the actual rule before claiming a gate exists:

```bash
git remote -v
git branch --show-current
git rev-parse origin/main
```

On GitHub, inspect the branch protection or ruleset and environment protection with `gh` or the repository settings. On GitLab, inspect protected branches and environments with `glab` or the project settings. Record the check date and any layer the project cannot read.

When documentation and live rules disagree:

1. Stop any production change.
2. Report the exact mismatch.
3. Fix the live rule or update the policy, not both from memory.
4. Re-read the rule before resuming.

## Merge Method

Record one method rather than letting a platform default choose it:

- **Merge commit** preserves the PR boundary and branch commits.
- **Squash** keeps main linear and creates one reviewable commit.
- **Rebase** keeps linear history but rewrites branch commits.

Whichever is chosen, the release record must identify the commit that actually landed on `main`. Do not claim a PR head SHA is on `main` after a squash or rebase changed it.

## Done When

A new contributor can answer five questions from the policy plus live platform evidence: where work is isolated, what must pass before merge, how it reaches `main`, which commits may reach production, and how a bad release is reverted.
