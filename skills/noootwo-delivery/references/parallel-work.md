# Parallel Work

Parallelism is safe only when the work is independent in meaning. A separate directory prevents checkout collisions; it does not prevent semantic conflicts.

## Detect Isolation

Run these before creating anything:

```bash
git rev-parse --show-toplevel
git rev-parse --git-dir
git rev-parse --git-common-dir
git rev-parse --show-superproject-working-tree 2>/dev/null
```

`git-dir` and `git-common-dir` differ inside a linked worktree. The same difference appears inside a submodule; the superproject check distinguishes them. If the checkout is already a linked worktree for this requirement, reuse it. A detached HEAD belongs to the host workspace; create a named branch before pushing or merging, and leave host-owned cleanup to the host.

## Canonical Checkout and Copies

A linked worktree and a filesystem copy are different things:

- A linked worktree shares the primary checkout's `.git` object database, refs, and worktree registry. It has its own working tree and branch, but one repository history.
- A sibling copy or separate clone has its own `.git`, refs, branches, and project state. It cannot be integrated through the same worktree or merge path and is not isolation.

Resolve the canonical checkout before creating anything:

```bash
ROOT="$(git rev-parse --show-toplevel)"
COMMON="$(git rev-parse --git-common-dir)"
PRIMARY="$(cd "$(dirname "$COMMON")" && pwd)"
printf 'root=%s\nprimary=%s\ngit_common=%s\n' \
  "$ROOT" "$PRIMARY" "$COMMON"
```

The common directory is the repository's shared `.git`; its parent is the primary checkout, regardless of the order `git worktree list` prints. In a linked worktree, `ROOT` differs from `PRIMARY`, and `git-dir` differs from `git-common-dir`. In a standalone clone or copied directory, `ROOT` is its own primary and the common directory points into that standalone copy. A separate copy is not a worktree merely because it has the same remote URL.

Never use `cp -R`, `rsync`, or a sibling `git clone` when the goal is to avoid touching the current checkout. Commit or stash the current work, or create a linked worktree from the primary checkout. If a sibling directory with the same origin exists, stop and confirm it is not an older copy before reading or writing project state there.

Compare a same-origin sibling against `git worktree list`; a directory that is not registered there is a copy, not a worktree.

The primary checkout owns project-level `.noootwo` state. From a linked worktree, pass `--root "$PRIMARY"` to `noootwo-state`; do not initialize a second `.noootwo` in the worktree. Docs are branch content and merge through the repository; they are not a second project authority. Concurrent state writes serialize through one writer; other requirements append events or evidence, or hand the current-snapshot update to that writer.

### Recover an Existing Copy

Do not continue development in the copy and do not delete it to make the tree look clean. Reconcile it:

1. Stop edits in both the copy and the canonical checkout.
2. Record the copy's branch, commit, status, untracked files, and intended diff. Preserve uncommitted work with a patch, stash, or bundle.
3. Create a branch or linked worktree from the canonical checkout at the correct base.
4. Port only the intended commits or diff. Do not copy docs, `.noootwo`, generated output, or ignored files wholesale.
5. Run the affected checks in the canonical worktree and compare the result before asking to archive or remove the copy.

If the copy contains work that cannot be separated safely, stop and report the exact files and commits rather than choosing one side.

## Create a Worktree

Prefer the harness's native worktree tool. Without one, use git:

```bash
mkdir -p .worktrees
git check-ignore -q .worktrees || printf '\n.worktrees/\n' >> .gitignore
git worktree add .worktrees/<slug> -b codex/<slug> origin/main
```

Use the repository's actual default branch. If `.worktrees/` is not ignored, fix that before creating the worktree or the worktree contents can be committed. Do not create a worktree inside another worktree. Run the project's smallest setup/baseline check; a failing baseline is reported before edits, not attributed to the new change.

The host may provide a safer workspace mechanism. Use it and record the path instead of fighting it with a second git worktree.

## Overlap Check

Do this once per concurrent pair, before either writer changes shared meaning:

```markdown
Overlap Check
- Requirement A:
- Requirement B:
- Expected shared files:
- Shared contract: none | endpoint | schema | event | component API | config key | generated client
- Migration / generated output:
- Decision: parallel | serialize | contract-first
- Merge order:
- Reopen trigger:
```

Decision rules:

| Evidence | Decision |
| --- | --- |
| Different files and different contracts | `parallel` |
| Same file, different semantic regions, no shared contract | `parallel` with small PRs; escalate on a conflict |
| Same API/schema/event/component/config meaning | `contract-first` or `serialize` |
| Ordered migrations, one generated client, or a shared formatter output | `serialize` or give one owner |
| Wide rename or cross-cutting refactor | land the refactor first, then rebase feature work |
| Incomplete feature would break `main` | keep it behind a feature flag; do not hold a long branch |

A file is not territory. Do not assign permanent file ownership or add a lock file to avoid reading the actual dependency.

## Contract-First

Use when both requirements need the same interface but can implement independently after it exists:

1. Define the smallest backward-compatible interface, event shape, schema expansion, or component variant.
2. Add its tests and compatibility rule.
3. Merge that contract to `main` through the normal gate.
4. Rebase both requirements onto the new `main`.
5. Proceed in parallel only if the Overlap Check still says `parallel`.

For data, prefer expand/contract: add the new field or table, support both shapes, migrate readers/writers, then remove the old shape in a later change. For UI, add the new prop or variant before switching callers. For events, publish a compatible version before consumers depend on it.

## Resolve Conflicts by Intent

For each conflicted hunk, read:

- both commits and their messages;
- the PR/MR descriptions and linked issue;
- tests that encode the expected behaviour;
- the shared contract or migration order.

Preserve both behaviours when the product needs both; choose one only when the evidence says one intent supersedes the other. Do not resolve a semantic conflict by accepting one whole file. After resolution, run the affected checks and a combined integration check.

## Cleanup

Remove a worktree only after its branch is merged or the user explicitly discards it. Refuse to force-remove uncommitted work; surface the files first. A PR still under review keeps its worktree. The main checkout is never cleaned “for symmetry.”

## Done When

Each requirement has one writer, one base commit, one canonical repository/state root, and a recorded Overlap Check decision; no sibling copy is active; shared work has a contract/merge order; conflict resolution has evidence and a green combined check.
