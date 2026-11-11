# 0031 - Conditional parallel execution and ordered rejoin

## Status

Accepted on 2026-11-11 for workspace `0.30.0`. Publication evidence is recorded
in `docs/status.md` after the protected-main merge and immutable tags.

## Context

The suite could ask a model to isolate independent read-only research or review,
but it had no positive trigger for subagents and no write-fanout protocol. In
practice, local history showed that delegation was rare:

- 62 Codex session files from October and November 2026 occupied 2.56 GiB;
- 29 unique `spawn_agent` calls appeared across 9 session files;
- 50 `wait_agent`, 1 `send_input`, and 1 `close_agent` call appeared;
- the first unique spawn was at `2026-10-26T16:58:30.401Z` and the latest was
  at `2026-11-11T04:59:13.939Z`;
- one local Claude project contained one session and zero `Task` or `Agent`
  calls.

These are machine-local session counts, not task counts or a controlled
sample. They still expose a product problem: the always-loaded workflow
description did not mention parallel work, the global context rule allowed
isolation only for read-only work, plans had no execution-mode field, and
delivery had no model for several write lanes inside one requirement.

Without a protocol, adding more delegation would invite the worse failure:
workers sharing one checkout, inventing incompatible contracts, duplicating
state, or overwriting each other's work.

## Research

The evidence supports conditional parallelism, not universal fan-out.

- Anthropic's multi-agent research system reports a large research-quality gain
  while using substantially more tokens than a single agent. Its result applies
  to breadth-first research with isolated context; it is not evidence that
  tightly coupled coding should fan out by default.
- Anthropic's "when and how to use multi-agent systems" guidance says most tasks
  remain single-agent and warns about overuse.
- OpenAI's Agents SDK defaults `max_concurrent_subagents` to 3, supporting a
  small default cap rather than an unbounded worker pool.
- Claude Code's subagent guidance recommends independent files, research, or
  review and notes the coordination overhead.
- Cursor and GitHub Copilot expose parallel agents and isolated coding
  environments, confirming that native worktree/task capability varies by host.
- `obra/superpowers` v7.0.2 contributes the independence test, a fresh
  self-contained worker brief, explicit worker statuses, and a progress ledger
  that prevents re-dispatch after compaction.
- Cognition's "Don't Build Multi-Agents" is the counterexample: dependent
  decisions need shared context, so a single writer remains the default.
- Agentless is a second counterexample: a simple staged pipeline can remain
  competitive without an agent swarm. More agents are not an outcome metric.

Sources:

- https://www.anthropic.com/engineering/multi-agent-research-system
- https://claude.com/blog/building-multi-agent-systems-when-and-how-to-use-them
- https://openai.github.io/openai-agents-python/multi_agent/
- https://code.claude.com/docs/en/sub-agents
- https://cursor.com/docs/agent/parallel-agents
- https://docs.github.com/en/copilot/concepts/agents/coding-agent/about-coding-agent
- https://github.com/obra/superpowers
- https://cognition.ai/blog/dont-build-multi-agents
- https://arxiv.org/abs/2407.01489

## Decision

1. `noootwo-workflow` owns a Fan-out Gate. After a non-direct plan is drafted,
   before acceptance and the first write, it chooses `serial`, `read-fanout`,
   `write-fanout`, or `requirement-parallel`.
2. The Gate re-runs when the next step exposes at least two independently
   answerable unknowns, review splits into independent lenses, another
   requirement becomes active, or compaction restores incomplete units.
3. `serial` remains the default. When a fan-out trigger exists, the record names
   why the units fail independence or why coordination cost wins.
4. Write fan-out requires four affirmative answers: contract, semantics/files,
   verification, and state/integration. Shared schemas, APIs, events,
   migrations, design tokens, manifests, lockfiles, generated clients, or
   release facts are contract-first or serial.
5. `read-fanout` uses 2-3 read-only workers in one checkout and returns bounded
   evidence to one lead.
6. `write-fanout` defaults to 3 workers and permits 4 as a hard maximum. One
   requirement keeps one integration branch and one eventual protected-main PR;
   every lane gets one linked worktree, one Worker Brief, one acceptance check,
   and one Result Packet. The integrator merges one lane at a time.
7. `requirement-parallel` remains delivery's existing Overlap Check across
   multiple requirements. Requirement branches do not replace write lanes
   inside one requirement.
8. Workflow owns the plan, mode, acceptance, and required rejoin constraint.
   The integrator schedules the Change Check; code health owns its verification
   decision. Delivery owns the executable Lane Map, isolation, merge mechanics,
   one-at-a-time rejoin, blocked-lane handling, and cleanup. A worker cannot
   spawn more workers, merge, write `.noootwo`, or change a shared contract.
9. The integrator owns the single current-state write. No worker or secondary
   worktree writes snapshots, events, or evidence directly; worker Result
   Packets return to the integrator because the state helper's read-modify-write
   path is not concurrency-safe. State owns the current snapshot; packets are
   evidence.
10. The integrator keeps the structured Fan-out Check and lane status in the
    current-state entry `fanout`; the capsule exposes a bounded projection plus a
    targeted `state --entry fanout` fallback, so compaction recovery does not
    depend on a full state-file load or silently lose custody.
11. `read-fanout` requires native delegation and collection. `write-fanout`
    additionally requires a distinct linked working directory per lane; a
    branch alone is not isolation. Missing capabilities record
    `serial - no-native-delegation`, `serial - no-native-collection`, or
    `serial - no-native-isolation`. Background shells and shared-checkout
    writers do not imitate fan-out.
12. Dispatch records the base SHA and expected acceptance result, never a
    predicted result commit. The Result Packet supplies the exact commit. The
    integrator maintains lease `acquired_at`, `last_seen_at`, `renew_by`, query
    handle, and orphan action; silence alone never proves completion.
13. Raw worker output above 16 KiB uses an integrator-assigned temporary path
    outside the repository. The integrator verifies and imports it into cold
    state evidence; the worker never writes `.noootwo`.
14. After compaction, a `done` lane is never re-dispatched. A `running` or
    orphaned lane is checked against its branch, commit, and latest packet
    before replacement.
15. A specialist invoked standalone remains serial unless it invokes workflow
    and the Gate selects a fan-out mode.
16. A non-direct plan is drafted first; Workflow's recorded Gate result completes
    it and makes it execution-ready. A missing Fan-out Check is a draft gap, not
    permission for TDD to invent an execution mode.
17. The public skill set stays at twelve. There is no separate orchestrator,
    subagent, parallel-work, or worktree skill.

## Interfaces

- The drafted plan gains an execution-completing `Fan-out Check` with mode,
  units, independence, shared meaning, worker/isolation capability, required
  rejoin order, and join condition.
- The Worker Brief records unit, method owner, read-only scope, custody handles,
  liveness source, oversized-evidence handoff, base/branch/worktree and owned
  files when writable, settled contracts, acceptance, and the Result Packet
  requirement.
- The Result Packet status is `done`, `done-with-concerns`, `needs-context`, or
  `blocked`, with evidence, decisions, and conflicts; write units add
  branch/commit/diff and files. Read units have no branch or commit obligation.
- Delivery adds a `Lane Map` with worker/task, collection/stop, lease, base SHA,
  and required rejoin order for one requirement's write lanes.
- State records lane status and packet handles in the `fanout` entry, projects a
  bounded view in the capsule, reads that exact entry when compression marks the
  view truncated, imports oversized evidence, and serializes all writes through
  the integrator.

## Rejected Alternatives

- **Universal parallel execution.** Coordination, token cost, and semantic
  conflict grow faster than the task when the work is coupled.
- **Read-only isolation as the permanent ceiling.** It prevents useful write
  fan-out even when all four independence questions pass.
- **Multiple writers in one checkout.** It cannot guarantee one writer per
  working tree and makes recovery ambiguous.
- **A new public orchestrator or subagent skill.** Workflow already owns
  scheduling, delivery already owns isolation/integration, and state already
  owns persistence. A new skill would duplicate descriptions and authority.
- **A full DAG before execution.** It front-loads decisions that the next
  evidence can invalidate. The Gate schedules only the current wave.
- **An unbounded worker pool.** The evidence and host defaults support a small
  cap. More lanes run in waves.
- **Background shells as workers.** They do not receive an independent brief,
  cannot reliably return structured results, and invite hidden shared writes.
- **Worker-owned or secondary-worktree `.noootwo` updates.** Multiple snapshots
  create a second authority, and concurrent read-modify-write calls can lose
  events even under the same canonical root.
- **Predicted result SHAs or worker-inferred completion.** They turn a branch
  tip into false custody evidence and cannot survive compaction safely.
- **Appending worktree ignores to the primary checkout's tracked `.gitignore`.**
  A fallback tool must not dirty the checkout it is trying to protect.
- **Vendor-specific hard-coding.** The protocol depends on capabilities
  (delegation, isolation, collection), not one tool name.

## Consequences

- Every non-direct plan runs a small Fan-out Check before acceptance. Direct work
  and tightly coupled one-slice work remain serial without extra ceremony.
- Workflow descriptions become discoverable for "parallel work" without adding
  an always-loaded skill.
- Write implementations can use more native agents while keeping one
  requirement, one integration branch, one integrator, and one state writer.
- Delivery has more work at the start and rejoin boundaries, but the same PR and
  protected-main policy remains.
- State records fewer, higher-signal updates because packets are evidence rather
  than separate snapshots.
- Existing public names, state/event schemas, and installation paths remain
  unchanged.

## Verification

- The eval contracts cover drafted-versus-execution-ready plans, Gate ordering,
  read and write fan-out, missing delegation/collection/isolation, branch-only
  false isolation, exact-base worktrees without primary-tree dirt, liveness and
  frozen SHAs, oversized evidence handoff, blocked rejoin, one integration
  branch feeding one main PR, and capsule-based post-compaction recovery.
- The Delivery contracts cover isolated lanes, primary-root worktree creation,
  shared-contract serialization, and required rejoin order.
- The State contracts and self-test cover worker packets as evidence, cold
  import of oversized output, the capsule's bounded fan-out projection, and
  strict single-writer serialization.
- The Decision-Complete Plan contract now requires a Fan-out Check.
- Workspace validation, all skill validators, discovery, syntax checks, state
  self-tests, and `git diff --check` must pass before publication.
- The eval contracts and local history are not a fresh-session behaviour
  measurement. No speed, token, quality, or rework improvement is claimed until
  paired baseline/candidate runs exist.
