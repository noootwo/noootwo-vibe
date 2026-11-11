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

The primary checkout owns project-level `.noootwo` state. From a linked worktree, pass `--root "$PRIMARY"` to `noootwo-state`; do not initialize a second `.noootwo` in the worktree. Docs are branch content and merge through the repository; they are not a second project authority. The state helper performs read-modify-write on its snapshot and event log, so concurrent process writes cannot be made safe by `--root` alone. No worker or secondary requirement writes state: every snapshot, event, and evidence record is returned to the integrator, who serializes it through the one state writer.

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
ROOT="$(git rev-parse --show-toplevel)"
COMMON="$(git rev-parse --path-format=absolute --git-common-dir)"
PRIMARY="$(dirname "$COMMON")"
git -C "$PRIMARY" fetch origin main
BASE_SHA="$(git -C "$PRIMARY" rev-parse origin/main)"
mkdir -p "$PRIMARY/.worktrees"
git -C "$PRIMARY" check-ignore -q -- .worktrees/ ||
  printf '\n.worktrees/\n' >>"$COMMON/info/exclude"
git -C "$PRIMARY" worktree add \
  "$PRIMARY/.worktrees/<slug>" -b codex/<slug> "$BASE_SHA"
```

Use the repository's actual default branch in place of `main`. Record `BASE_SHA`, and create the lane under the primary checkout even when the command starts inside a linked worktree. Never resolve `.worktrees/<slug>` against the current linked-worktree root. If `.worktrees/` is not ignored, add it to the shared repository-local exclude (`$COMMON/info/exclude`), not the primary checkout's tracked `.gitignore`; the fallback must leave `git status` clean. Do not create a worktree inside another worktree. Run the project's smallest setup/baseline check; a failing baseline is reported before edits, not attributed to the new change.

The host may provide a safer workspace mechanism. Use it and record the path instead of fighting it with a second git worktree.

## Write-Fanout Lanes

`noootwo-workflow` decides `write-fanout`; delivery turns it into isolated lanes. One requirement keeps one integration branch and one eventual PR. Every lane branches from the same recorded integration base or from a contract-first base, gets its own linked worktree, and returns a bounded Result Packet to one integrator.

```markdown
Lane Map
- Requirement and integration branch:
- Integration base commit:
- Lane units and observable results:
- Lane branches and linked worktrees:
- Worker/task and collection/stop handles, liveness source, lease times, and evidence handoff path:
- Owned and forbidden files per lane:
- Shared contract, migration, or generated-output owner:
- Acceptance command per lane:
- Integration base SHA per lane, contract-first base when used:
- Required rejoin order and combined check:
- Current state writer:
- Stop, blocked-lane, and cleanup rules:
```

Use 2-3 lanes by default and 4 at the hard maximum; more units run in waves. Start each lane from the exact agreed base, not from another unmerged lane. The integrator stays in the integration branch/worktree; workers do not merge into it themselves. Record worker/task, collection/stop, liveness source, and lease `acquired_at | last_seen_at | renew_by | query | orphan action` before dispatch so recovery can distinguish done, running, orphaned, and unstarted lanes. The primary checkout remains the canonical `.noootwo` root, and only the integrator writes state through `noootwo-state`.

Give each worker an evidence handoff path outside the repository. Raw output above 16 KiB goes there; the worker never writes the working tree or `.noootwo`. The integrator verifies the handoff, imports it through `noootwo-state capture`, and that capture writes the canonical cold log under `.noootwo/state/evidence`. The dispatch record names the base SHA, never a predicted result commit; the Result Packet supplies the exact commit after the worker finishes.

Before dispatch, confirm every lane has disjoint meaning, owned files, a settled interface, an independent acceptance command, and the same integration base. A shared schema, API, event, component contract, migration, generated client, manifest, lockfile, or release fact is contract-first or serial. Different files do not override a shared meaning.

Rejoin in the recorded order:

1. Read the Result Packet and verify the branch, commit, diff, evidence path, bytes, and hash; import oversized evidence through the integrator before rejoin.
2. Review the lane against its brief and owned scope.
3. Freeze the reviewed lane SHA and merge or cherry-pick that exact commit into the integration branch.
4. Rerun that lane's acceptance and the combined check.
5. Hand the Result Packet to the integrator as evidence; update state only when the goal, decision, blocker, evidence, or next trigger changed, not once per packet by reflex.
6. Preserve a blocked lane's work and continue independent lanes only when the block cannot change their meaning.
7. After every lane is either rejoined or explicitly blocked, integrate the one completed integration branch through protected `main` once. If a blocked lane can change the meaning already inside the integration branch, do not open or merge the main PR yet.

The lane merges and integration-branch commits above are local custody for review. They do not authorize push, protected-main integration, a tag, or publication; final user acceptance precedes those actions.

Stop rejoin when a lane is `blocked` or `needs-context`, a new shared contract appears, the plan loses viability, or two combined-check loops fail without new evidence. A `running` or orphaned lane is inspected before replacement; a `done` lane is never re-dispatched after compaction.

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

Use when two requirements or two write lanes need the same interface but can implement independently after it exists:

1. Define the smallest backward-compatible interface, event shape, schema expansion, or component variant.
2. Add its tests and compatibility rule.
3. For lanes inside one requirement, land the contract as the first commit or preparatory slice on the integration branch, then branch every dependent lane from that exact contract SHA.
4. If the contract must be independently reviewed or released first, land it through a separate contract-first PR to `main`; after merge, rebase or recreate every dependent lane from that exact `main` SHA.
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

Each requirement has one writer, one base commit, one canonical repository/state root, and a recorded Overlap Check decision; every write-fanout lane has one branch, one primary-root-linked worktree, liveness and evidence custody, one Result Packet, and one exact reviewed SHA; no sibling copy is active; shared work has a contract/merge order; conflict resolution has evidence; the completed lanes rejoin one integration branch and reach `main` through one PR; no worker writes project state.
