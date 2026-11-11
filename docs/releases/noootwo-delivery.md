# noootwo-delivery Releases

## v0.2.0

- Added write-fanout lanes inside one requirement: one integration branch, one linked worktree and worker per lane, one integrator, one required rejoin order, and one state writer.
- Added the Lane Map contract for worker/task, collection/stop, liveness source and lease times, evidence handoff, exact base SHAs, owned files, acceptance, shared-contract owner, required rejoin order, state writer, blocked-lane handling, and cleanup.
- Rejoin now reviews and merges one frozen lane SHA at a time, imports oversized worker evidence through the integrator, reruns the lane and combined checks after each, stops on blocked/needs-context work or a new shared contract, and keeps the main PR closed while blocked meaning can change the integration branch.
- Worktree fallback now resolves the primary checkout and creates every lane from a recorded base SHA under `$PRIMARY/.worktrees`, never under the current linked-worktree root and never as a nested worktree. Missing ignore coverage is fixed in the shared repository-local exclude, not by dirtying the primary checkout's tracked files.
- No worker or secondary worktree writes `.noootwo`; all snapshot, event, and evidence writes serialize through the integrator.
- Lane merges and integration-branch commits are local custody for review, not approval to push, merge through protected `main`, tag, or publish.
- Compaction recovery never re-dispatches a completed lane; running or orphaned work is inspected against its custody handles, branch, exact commit, and Result Packet first.
- Added eval contracts for isolated write lanes, primary-root base correctness, shared-contract serialization, custody, single-branch integration, and strict state ownership.

## v0.1.0

- Added `noootwo-delivery` as the owner of branch/worktree isolation, concurrent-requirement overlap, protected-main integration, and the Delivery Policy.
- Added a five-step path: record the policy, isolate one requirement, make an Overlap Check, integrate through `main`, and hand an eligible source to release.
- Added `references/delivery-policy.md` for live-rule checks and the minimum policy, `references/parallel-work.md` for worktrees/contract-first/flags/conflicts, and `references/mainline.md` for PR/queue/hotfix/production boundaries.
- Rejected sibling filesystem copies and separate clones as isolation: a linked worktree shares the canonical repository, while the primary checkout owns project state and durable docs.
- Added recovery guidance for an existing copy: stop, preserve its work, port only the intended diff or commits, verify in a canonical worktree, and do not delete uncommitted work.
- Added eleven eval contracts covering independent and shared-contract parallelism, same-file independence, worktree reuse, sibling-copy rejection and recovery, feature-branch rejection, main-commit acceptance, hotfix return, no-queue rechecks, and release-owned rollback.
