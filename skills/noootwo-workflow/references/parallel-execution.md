# Parallel Execution

Parallel work is a schedule choice, not a success metric. Keep coupled work with one writer; fan out only when bounded units can be briefed and rejoined without duplicating decisions.

## Fan-out Gate

Run one Fan-out Gate after the current seam is settled and a non-direct plan is drafted, before the plan is accepted or any writer starts. The drafted plan supplies scope, interfaces, assertions, verification, and `Review Focus`; the recorded Gate result completes it and makes it execution-ready. When an Integration Read is required, the Gate runs after that shape. Re-run the Gate when the next step exposes two or more independently answerable unknowns, review splits into independent lenses, a second requirement becomes active, or compaction/session re-entry restores incomplete units.

```markdown
Fan-out Check
- Requirement / drafted plan:
- Mode: serial | read-fanout | write-fanout | requirement-parallel
- Units and observable results:
- Contract:
- Semantics / files:
- Verification:
- State / integration:
- Shared contract, migration, or generated output:
- Native worker and isolation capability:
- Merge or join order:
- Stop and rejoin condition:
```

`serial` is the default for coupled work. A task with a fan-out trigger records why the units fail independence, or why coordination cost exceeds the expected gain.

| Mode | Use | Ownership |
| --- | --- | --- |
| `serial` | Coupled decisions, one viable slice, or no native worker/isolation capability | One writer, one integrator |
| `read-fanout` | 2-3 independent research questions, explorations, triage claims, or review lenses | Read-only workers in a shared checkout; one lead joins the evidence |
| `write-fanout` | 2-3 independently briefable implementation slices with disjoint meaning and verification by default; 4 hard maximum | One linked worktree per lane from the integration branch; one integrator rejoins one lane at a time |
| `requirement-parallel` | Two or more independently deliverable requirements | `noootwo-delivery` owns one branch/worktree per requirement and the Overlap Check |

The default worker cap is 3 and the hard cap is 4. More units run in waves after earlier results reduce the frontier. A larger cap multiplies brief, review, integration, and token cost without buying independent decisions.

Capability is necessary but not sufficient; the mode still has to pass the independence questions.

| Mode | Native delegation | Native collection | Distinct linked working directory |
| --- | --- | --- | --- |
| `serial` | not required | not required | not required |
| `read-fanout` | required | required | not required; shared read-only checkout |
| `write-fanout` | required | required | required, one linked worktree per lane |
| `requirement-parallel` | optional | optional | required per independently delivered requirement |

A branch name alone is not isolation. If the host cannot create a distinct linked working directory from the primary checkout, do not call a branch or shared checkout a write lane.

## Independence

For each pair of proposed units, answer all four:

1. **Contract** - Can each unit name the settled interface without changing it?
2. **Semantics and files** - Can each unit change meaning without the other's code or generated output?
3. **Verification** - Does each unit have its own observable acceptance command or artifact check?
4. **State and integration** - Can one integrator merge or synthesize the results in a stated order without re-deciding a contract?

`write-fanout` requires four `yes` answers. A `no` means `serial`, `contract-first`, or a new slice. `read-fanout` requires independent questions and evidence returns; shared contracts do not matter only because the workers cannot write.

Shared schemas, events, migrations, design tokens, manifests, lockfiles, and generated clients are shared meaning. Land them first, give them one owner, or serialize the dependent lanes. Different file names alone do not prove independence.

Before dispatch, the integrator records the Fan-out Check and every lane's initial status in the current-state entry `fanout`. The plan may mirror the check, but it is not the recovery authority. A write fan-out also records the worker/task handle, collection/stop handle, liveness source, lease due time, evidence handoff path, base SHA, and expected acceptance result; the exact commit is produced by the worker later and belongs in the Result Packet, never predicted at dispatch. The capsule projects the `fanout` entry so compaction can distinguish done, running, orphaned, and unstarted work without guessing from a branch name.

The integrator maintains the lease. Record `acquired_at`, `last_seen_at`, `renew_by`, the host query handle, and the orphan action. Refresh `last_seen_at` only from a host task state or a returned packet. When `renew_by` passes without a terminal packet, mark the lane `orphaned` only after the host query and branch/commit inspection show no continuing work; never infer completion or failure from silence alone.

## Worker Brief

The lead constructs a fresh brief; do not rely on a worker inheriting the planning conversation.

```markdown
Worker Brief
- Unit:
- Goal and non-goals:
- Method owner:
- Read-only scope and evidence to return:
- Write base commit, branch, worktree, owned files, and forbidden files:
- Settled interfaces and constraints:
- Acceptance command or artifact check:
- Evidence handoff path outside the repository for raw output above 16 KiB:
- Worker/task handle, collection/stop handle, and liveness source:
- Return: Result Packet
```

Read-fanout fills the read-only scope and omits write fields. Write-fanout fills the exact base, branch, distinct linked-worktree path, ownership, evidence handoff, and custody handles.

Workflow owns the Fan-out Check, plan acceptance, mode, and required rejoin constraint. The integrator schedules `noootwo-code-health`'s Change Check; code health owns its verification decision. `noootwo-delivery` owns the executable Lane Map, lane isolation, merge mechanics, and one-at-a-time rejoin. The integrator owns the single current-state write. A worker owns one unit, follows its named skill, edits only the owned scope, and returns evidence. A worker does not spawn another worker, merge, write `.noootwo`, alter a shared contract, or widen scope. A read-only worker makes no repository or durable-state write.

Raw worker output above 16 KiB never travels inline and is never written to `.noootwo` by the worker. The worker writes it to the integrator-assigned temporary path outside the repository and returns that path. The integrator verifies the bytes and hash, imports the artifact through `noootwo-state capture`; that capture writes the canonical cold log under `.noootwo/state/evidence` and returns the handle. If no safe handoff channel exists, the worker returns a bounded result and the integrator reruns the smallest decisive capture itself.

A specialist invoked standalone stays serial unless it invokes `noootwo-workflow` and this Gate selects `read-fanout` or `write-fanout`. A specialist already running inside a selected mode returns its unit result without re-deciding the overall mode.

If the brief cannot state the base, owned files, settled contracts, and acceptance, the unit is not ready to dispatch.

## Result Packet

```markdown
Result Packet
- Unit and status: done | done-with-concerns | needs-context | blocked
- Read-only findings, sources, bounded result, and evidence handles:
- Write branch, exact commit, and diff range (omit for read-fanout):
- Files changed:
- Checks and evidence handles:
- Decisions and open questions:
- Conflicts or shared-contract discoveries:
```

Read-fanout has no branch, worktree, commit, or write requirement; its evidence handle is the deliverable. Write-fanout records the custody handles and exact SHA needed to recover or merge the unit. `done-with-concerns` proceeds to integrator review with the concern visible. `needs-context` returns to the brief owner. `blocked` stops that lane and triggers re-slicing, serialization, or a user-owned decision; it never causes a silent retry with the same brief.

## Rejoin

1. Collect every Result Packet and verify its branch, commit, files, evidence path, bytes, and hash.
2. Freeze the exact reviewed SHA; a branch name is not a merge target.
3. Review each diff against its brief before merging anything.
4. Rejoin or synthesize one unit at a time in the required order recorded by the Gate; delivery owns the executable Lane Map.
5. After each unit, rerun that lane's check and the combined check for the current integration point.
6. Rejoin every unblocked lane into the one integration branch, then integrate that branch through protected `main` once. If a blocked lane can change what is already there, keep the main PR closed until the meaning is resolved.
7. Have the integrator write current state only when the goal, decision, blocker, evidence, or next trigger actually changed; do not mirror every packet.

Use `noootwo-delivery` for the Lane Map, linked worktrees, merge mechanics in the required order, blocked-lane handling, and cleanup. Use `noootwo-state` for the single current snapshot; worker packets are evidence, not competing state.

Stop rejoin when a worker reports `blocked` or `needs-context`, a new shared contract or migration appears, integration fails twice without new evidence, or the accepted plan is no longer viable. A completed lane may remain intact while the blocked lane is re-sliced; do not merge a unit whose meaning now depends on the unresolved contract.

After compaction or session re-entry, recover the Fan-out Check and lane statuses from the capsule's `fanout` projection before dispatch. If the projection is truncated, read `state --entry fanout` for the exact custody record. Do not re-dispatch a `done` unit. For `running` work, query its worker/task handle and liveness source; stop or prove it terminal before replacement. When custody is lost, inspect the branch and exact commit and wait for or establish a safe takeover point. Re-dispatch only an unstarted or demonstrably incomplete unit with a new brief.

## Harness Capability

Probe the host once before choosing fan-out:

- native delegation: a subagent, agent, or task mechanism that accepts a bounded brief and returns a result;
- native isolation: a distinct working directory, normally a linked worktree created from the primary checkout; a branch name alone is not isolation;
- result retrieval: a way to wait for, collect, and stop workers without polling away the lead's context.

Use the native mechanism when present. Codex, Claude Code, Cursor, Copilot, and other hosts expose different names and limits; map the capabilities, not vendor-specific syntax. `read-fanout` requires delegation and collection. `write-fanout` additionally requires a distinct linked working directory per lane. If only isolation is missing, use read fan-out where applicable and run writes serial with `serial - no-native-isolation`; if delegation or collection is missing, record `serial - no-native-delegation` or `serial - no-native-collection`. A branch alone is not isolation, and an isolated directory without native delegation or collection is still serial.

Background shells, parallel terminal commands, and shared-checkout writers are not subagents. They do not receive an independent brief, cannot return a Result Packet reliably, and must not be used to imitate write fan-out.

## Done When

Every unit has one writer, a Worker Brief, a terminal Result Packet, and acceptance evidence. Write lanes have linked-worktree isolation and exact reviewed SHAs; shared meaning was contract-first or serialized; one integrator rejoined in the required order; the combined check passed; the integration branch reached `main` once; and the current state has one writer and no duplicate authority.
