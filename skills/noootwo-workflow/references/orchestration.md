# Orchestration

Workflow schedules one next owner at a time. It does not precompute a full DAG. A Fan-out Gate may turn one drafted plan step into bounded independent units before acceptance, but it still has one integrator and one next decision.

## Loop

`snapshot -> route one owner -> specialist runs -> collect result -> update state when changed -> next step or stop`

Each cycle loads only what the current step needs. The specialist owns its method; workflow keeps order, scope, stop conditions, and handoffs.

A checkpoint is re-entry inside one turn, not a new plan: it refreshes the capsule and the frontier, then the loop matches one owner again from current evidence instead of continuing the previous read or probe sequence.

A new request, a phase shift, or a specialist return re-enters owner matching from the current artifact and evidence. The previously used specialist does not carry over, and a body read earlier in the session is not a reason to keep it.

## Precedence

Use this only to break a stage tie:

1. `noootwo-debug` for an unproven failure or regression.
2. `noootwo-research` for a decision that only outside evidence can settle.
3. `noootwo-product` for an unsettled real user, scope, main path, state, or acceptance.
4. `noootwo-design` for UI/visual/artifact work when the product path is settled but direction is not.
5. `noootwo-code-health` Integration Read before implementation when the seam is non-obvious; its Change Shape may call for preparatory refactoring, direct TDD, or another owner.
6. After the seam is settled and a non-direct plan is drafted, run the Fan-out Gate before acceptance. `noootwo-delivery` turns `write-fanout` or `requirement-parallel` into linked worktrees; it records a Lane Map for one requirement's write lanes and an Overlap Check across requirements or shared meaning.
7. `noootwo-tdd` for behavior-changing code, then `noootwo-code-health` for a Change Check after green before the work is reported done.
8. The integrator schedules `noootwo-code-health`'s Change Check. `noootwo-delivery` rejoins each frozen lane SHA into the local integration branch after its review/check; shared contracts must already be serialized or contract-first, and blocked meaning keeps mainline integration closed.
9. Stop for explicit user acceptance before push, protected-main integration, tag, or publish unless the current request already authorized that named action.
10. `noootwo-delivery` integrates the accepted completed branch once through protected `main`.
11. `noootwo-code-health` Release Check once before release or a ship-readiness submit gate: full suite or CI for the exact commit, full Structure Sweep, release evidence, and named gaps.
12. `noootwo-release` after code-health readiness and user acceptance when versioning, tagging, artifact identity, deployment trace, rollback, or release health is in scope.
13. `noootwo-state` after behavior, state, release facts, or instructions change, including unresolved structural findings and the Release Plan.

Do not turn this into a large condition table. If the current evidence points to a different owner, the evidence wins.

Plan acceptance after the Fan-out Gate makes the plan execution-ready. It authorizes local implementation, lane-custody, and local integration-branch rejoin commits; none is publication approval or a substitute for user acceptance of push, protected-main integration, tag, or publish.

## Scope

- Default scope is the current change or current diff.
- Integration Read is a design decision before behavior changes, not a full-project audit; a local change with an obvious seam and no contract, data, or migration impact skips it.
- Change Check stays on the touched path; a full-project Structure Sweep runs in the Release Check, on a documented trigger, or on an explicit user request.
- Do not run a Release Check after every requirement. A long task or a large diff does not by itself trigger one; blast radius does. Existing CI for the exact commit can satisfy the full-suite part.
- A specialist may hand back a sequencing decision to workflow; record it in state rather than reimplementing the specialist.
- One requirement has one integration branch and an eventual protected-main PR. `write-fanout` adds one linked worktree per lane, each with one worker and an independent acceptance check; one integrator merges one lane at a time. `requirement-parallel` uses one branch/worktree per requirement. Parallel work requires an Overlap Check; shared API, schema, event, component, config, migration, generated-output, or release meaning is serialized or contract-first. File-name overlap alone is not a permanent lock.
- Isolation is a linked worktree in the canonical repository, not a sibling copy or separate clone. Project state and durable docs keep one canonical root.
- Delivery supplies an eligible `main` commit to release. It does not choose a version, build artifact, deployment method, or rollback; those stay with `noootwo-release`.
- An installed external skill owns its method, not the project's documentation layout. Persist durable artifacts through `noootwo-state`; never create a new project convention under an external skill's directory.

## Fan-out Gate

Use `parallel-execution.md` after the seam is settled and a non-direct plan is drafted, before plan acceptance and the first write, and again when a new request exposes independent unknowns, review lenses, or requirements. The Gate result completes the drafted plan and makes it execution-ready. When code-health supplies a Change Shape, the Gate follows that shape; it never runs before the contracts are knowable.

```markdown
Fan-out Check
- Mode: serial | read-fanout | write-fanout | requirement-parallel
- Units and observable results:
- Contract / semantics / files / verification / integration:
- Shared contract, migration, or generated output:
- Native worker and isolation capability:
- Merge or join order:
- Stop and rejoin condition:
```

- `serial` is the default. When a fan-out trigger exists, record why the units are not independent or why coordination cost wins.
- `read-fanout` uses 2-3 read-only workers in a shared checkout and returns evidence to one lead.
- `write-fanout` uses 2-3 linked-worktree lanes by default and 4 at the hard maximum; every one of the four independence questions must pass.
- `requirement-parallel` hands one branch/worktree per requirement and the Overlap Check to `noootwo-delivery`.
- Read fan-out requires native delegation and collection. Write fan-out additionally requires a distinct linked working directory per lane; a branch alone is not isolation.
- A missing capability records `serial - no-native-delegation`, `serial - no-native-collection`, or `serial - no-native-isolation`; background shells do not substitute.

Before dispatch, persist the Fan-out Check plus worker/task handle, collection/stop handle, liveness source, base SHA, and lane status in the current-state entry `fanout`; a plan may mirror that record but cannot replace it. Workflow owns the brief, plan acceptance after the Gate, mode, and required rejoin constraint; the integrator schedules the Change Check that `noootwo-code-health` owns; delivery owns the executable Lane Map, merge mechanics, and one-at-a-time rejoin. A worker owns one unit and returns a Result Packet; it does not spawn, merge, write `.noootwo`, or change a shared contract. Only the integrator writes state, serializing every snapshot, event, and evidence record. The full worker/result contract and rejoin rules live in `parallel-execution.md`.

## Approved execution

An accepted plan is the authority for ordinary implementation choices. When the plan is silent or ambiguous:

1. Prefer the accepted spec.
2. Then prefer the accepted plan's interfaces, sequence, assertions, and `Review Focus`.
3. Then use current code, tests, and observed evidence.
4. If the choice is reversible, record a ruling and continue.

```markdown
Ruling
- Decision:
- Basis: spec | plan | evidence
- Cost if wrong:
- Reopen trigger:
```

Record the ruling beside the plan or in project state through `noootwo-state`. Do not re-ask for approval on naming, local structure, equivalent APIs, test organization, or another reversible detail already bounded by the plan.

A plan pasted by the user or produced by an external skill arrives approved but unowned. Before the first edit, name the current owner and its verification depth, and name the release boundary when the plan can change a version, tag, artifact, deployment trace, or release fact. If the plan lacks a test assertion, verification command, or recorded Gate result, it is not execution-ready: name the missing decision and let its owner close it instead of inventing the validation.

Stop approved execution for a user-owned product or "how" decision, an irreversible migration or data loss, a security or privacy impact, an external side effect or spend, or evidence that the plan as a whole is no longer viable. When the plan changes materially, return to the owner that can accept the new plan.

## Stop conditions

Stop and ask or reroute when:

- no clear owner exists
- a material product, architecture, or release choice is unresolved
- verification is missing and cannot be inferred
- the change would expand public behavior beyond the user's request
- two concurrent requirements share a contract or migration order and have no serialize/contract-first decision
- a fan-out worker reports `blocked` or `needs-context`, discovers a new shared contract or migration, or two rejoin checks fail without new evidence
- the target `main` moved after the checks and the merge candidate has not been rechecked
- a confirmation or diagnosis would need a source edit, rebuild, deployment, persistent data change, or a new system before its claims have verdicts
- several claims are being merged into one audit without evidence that they share a cause
- a second verification loop failed without new evidence; report the boundary instead of starting a third
- three failed fixes reveal new problems in different places
- user acceptance is required before push, protected-main integration, tag, or publish unless the current request already authorized that named action; local lane-custody commits under the accepted plan are not publication approval

The items above govern scheduling before approval or a changed goal. During already-approved execution, the narrower stop list in [Approved execution](#approved-execution) applies.

For external installed skills, stop with one or two candidates when matching is ambiguous; do not choose one on a weak keyword match.
