# Mainline Integration

`main` is the integration line, not a personal workspace. Work reaches it in small, reviewed, checked increments.

## Before the PR

1. Fetch the target and update the branch using the project's selected method.
2. Rerun required checks on the updated base.
3. Confirm the Change Check or review gate has passed.
4. Verify no generated, secret, or unrelated files entered the diff.
5. Open the PR with the intent, verification evidence, and any release-bound gap.

```bash
git fetch origin main
git log --oneline origin/main..HEAD
git diff --stat origin/main...HEAD
git diff --check
```

If the branch is behind, update it and rerun the checks. A green run on an old base is not merge evidence.

## Merge Queue

When the host has a merge queue, enqueue the PR and let the queue test the current target plus queued changes. The queue's result is the integration evidence. Do not merge around a failing queue or silently disable its checks.

Without a queue:

1. Update the branch from the latest `main`.
2. Run the required checks on the merge candidate.
3. Merge through the protected-branch path.
4. Fetch `main` and verify the resulting merge commit.

For a merge commit, the PR head is normally an ancestor. For squash or rebase, the head SHA may not be an ancestor; verify the landed commit and tree instead of claiming the old SHA is on `main`.

```bash
git fetch origin main
git log -1 --format='%H %s' origin/main
git merge-base --is-ancestor <landed-commit> origin/main
```

## Branch Lifetime

Keep a branch short-lived enough that integration stays cheap. “Short” is measured by divergence, not a ceremonial calendar:

- merge as soon as the change is independently reviewable and safe;
- put incomplete product work behind a feature flag;
- land preparatory refactors separately;
- do not keep a long-lived integration branch beside `main`;
- use a release branch only if the project genuinely needs one, and still merge its changes back to `main` before they become the production source.

## Hotfix

```bash
git fetch origin main
git switch -c codex/hotfix-<slug> origin/main
```

Fix, test, review, PR, and merge to `main`. Tag or deploy only after the merge. A hotfix branch is not a parallel production line. If production is already broken, rollback the previous immutable artifact first, then land the corrective commit through the normal route.

## Production Boundary

Production is an environment rule, not a naming convention. Accept only a source commit that is reachable from protected `main`, or an annotated release tag whose peeled commit is reachable from protected `main`.

Reject:

- a feature branch build;
- a mutable branch name such as `release/latest`;
- a lightweight or floating tag with no recorded source;
- a release branch commit that has not reached `main`;
- a rebuild from an unrecorded working tree.

The release owner records the exact commit, artifact digest, release ID, tag, and environment. Delivery supplies the eligible commit; it does not invent a version or deployment plan.

## Rollback

Prefer redeploying the previous immutable artifact. If the correction must be in source, revert the offending change through a PR to `main`, verify it, and create a new release. Do not rewrite `main`, force-push a protected branch, or “roll back” by moving a shared tag.

## Done When

The merge is on protected `main`, the current-base checks and review are evidenced, the PR is traceable to the landed commit, and any production action starts from an eligible `main` history.
