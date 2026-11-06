# noootwo-delivery Releases

## v0.1.0

- Added `noootwo-delivery` as the owner of branch/worktree isolation, concurrent-requirement overlap, protected-main integration, and the Delivery Policy.
- Added a five-step path: record the policy, isolate one requirement, make an Overlap Check, integrate through `main`, and hand an eligible source to release.
- Added `references/delivery-policy.md` for live-rule checks and the minimum policy, `references/parallel-work.md` for worktrees/contract-first/flags/conflicts, and `references/mainline.md` for PR/queue/hotfix/production boundaries.
- Rejected sibling filesystem copies and separate clones as isolation: a linked worktree shares the canonical repository, while the primary checkout owns project state and durable docs.
- Added recovery guidance for an existing copy: stop, preserve its work, port only the intended diff or commits, verify in a canonical worktree, and do not delete uncommitted work.
- Added eleven eval contracts covering independent and shared-contract parallelism, same-file independence, worktree reuse, sibling-copy rejection and recovery, feature-branch rejection, main-commit acceptance, hotfix return, no-queue rechecks, and release-owned rollback.
