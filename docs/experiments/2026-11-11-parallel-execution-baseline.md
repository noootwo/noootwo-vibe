# Parallel Execution Baseline

- Date: 2026-11-11
- Candidate: workspace `0.30.0`
- Decision: add a conditional Fan-out Gate, write-lane isolation, and one
  integrator/state-writer protocol
- Status: mechanism adopted; fresh-session speed, token, quality, and rework
  effects remain unmeasured

## Question

Subagent and parallel-task use is rare in local agent work. Is the low rate
caused by unavailable tools, or by discoverability and protocol gaps in the
Noootwo skills?

## Baseline

The scan read the local Codex session directories for October and November 2026
and deduplicated actual `function_call` records by `call_id` where present.
It did not send session content anywhere.

| Measure | Result |
| --- | --- |
| Codex session files | 62 |
| Session bytes | 2,746,899,054 (2.56 GiB) |
| Unique `spawn_agent` calls | 29 |
| Unique `wait_agent` calls | 50 |
| Unique `send_input` calls | 1 |
| Unique `close_agent` calls | 1 |
| Session files with a unique spawn | 9 |
| First spawn | `2026-10-26T16:58:30.401Z` |
| Last spawn | `2026-11-11T04:59:13.939Z` |
| Local Claude sample | 1 project session, 0 `Task`/`Agent` calls |

Limits:

- A session file is not a task; child sessions and repeated retries can inflate
  or obscure the distribution.
- The scan covers one local Codex installation and one tiny Claude sample.
- The presence of a tool definition is not a call; the count therefore uses
  `function_call` payloads and call IDs.
- No content, arguments, messages, or tool output are reproduced here.

The low rate is not explained by a missing host capability: at least one local
harness exposes delegation. The stronger explanation is a skill-protocol gap:

- `noootwo-workflow` did not advertise parallel work in its always-loaded
  description;
- the package lifecycle allowed isolation only for read-only work;
- accepted plans had `Interfaces`, assertions, verification, and `Review
  Focus`, but no execution mode;
- `noootwo-delivery` handled multiple requirements but not multiple write lanes
  inside one requirement;
- no worker brief, result packet, lane status, or explicit compaction recovery
  rule existed.

## Research Basis

The mechanism is intentionally conditional:

- Anthropic reports strong gains and a large token multiplier for isolated
  multi-agent research, not tightly coupled coding.
- Anthropic's guidance and Cognition's counterexample both warn against
  defaulting dependent decisions to separate agents.
- OpenAI Agents SDK defaults to three concurrent subagents.
- Claude Code recommends independent files, research, or review and names the
  overhead.
- Cursor and GitHub Copilot demonstrate that isolated parallel coding
  environments exist, while their details vary by host.
- Superpowers v7.0.2 contributes the independence gate, self-contained briefs,
  worker statuses, and progress ledger.
- Agentless is a counterexample to "more agents equals better."

Full sources and boundaries are in
[ADR 0031](../adr/0031-parallel-execution-protocol.md) and
[`borrowed-skills.md`](../reference/borrowed-skills.md).

## Change

The candidate adds:

1. A mandatory Fan-out Gate after a non-direct plan is drafted, before
   acceptance and the first write.
2. Four modes: `serial`, `read-fanout`, `write-fanout`, and
   `requirement-parallel`.
3. Four independence questions: contract, semantics/files, verification, and
   state/integration.
4. Write fan-out with 3 workers by default, 4 hard maximum, one linked worktree
   per lane, one integration branch, and one integrator.
5. Worker Brief and Result Packet contracts.
6. Delivery-owned Lane Map, executable rejoin order, blocked-lane handling,
   primary-root worktree creation, and cleanup.
7. State-owned evidence intake and strict single-writer serialization for
   snapshots, events, and evidence.
8. A plan field and eval coverage for missing Fan-out decisions.
9. A harness capability matrix with explicit serial fallback when delegation,
   collection, or isolation is absent; a branch alone is not isolation.
10. A drafted-versus-execution-ready plan boundary completed by the Fan-out Gate.
11. A bounded capsule projection for Fan-out Check and lane custody.
12. Integrator-maintained lease and liveness semantics, exact result commits from
    packets, and an outside-repository handoff for oversized worker evidence.
13. Worktree fallback ignore changes in the shared repository-local exclude, not
    the primary checkout's tracked `.gitignore`.

The candidate does not add a public skill, a root `SKILL.md`, a second state
root, a global scheduler, a full DAG, or a fixed multi-agent ceremony for every
task.

## Measurement Plan

Use fresh sessions with the same model, repository commit, and host capability.
Run each scenario with the `0.29.0`-equivalent serial instructions and the
candidate.

Record:

- whether a Fan-out Check appears before the first write;
- selected mode and the reason;
- number of workers actually dispatched;
- overlap or contract conflicts found before writing;
- first-pass lane acceptance rate;
- duplicate state writes and duplicate completed-unit dispatch after a
  simulated compaction;
- task duration, total tokens, tool calls, and user interventions;
- final correctness against a hidden verifier.

Scenarios:

- `fanout-read-two-unknowns`
- `fanout-write-disjoint-slices`
- `fanout-no-native-tool`
- `fanout-worker-blocked`
- `fanout-post-compaction-no-redispatch`
- `write-fanout-lanes-isolated`
- `write-fanout-shared-contract-serializes`
- `worker-results-are-evidence`

Pass conditions:

- candidate triggers fan-out for independent work more often than baseline;
- candidate does not trigger write fan-out for shared contracts;
- fewer than 1 in 5 runs duplicate a completed lane after compaction;
- no run uses a sibling copy or second `.noootwo`;
- task correctness does not regress;
- any speed or token claim is reported only from paired measurements.

## Verification

Deterministic checks for this candidate:

```bash
python3 scripts/validate_skill_workspace.py .
python3 -m py_compile scripts/validate_skill_workspace.py \
  skills/noootwo-state/scripts/noootwo_state.py \
  skills/noootwo-state/scripts/audit_codex_context.py
sh -n skills/noootwo-state/scripts/noootwo-state.sh
python3 skills/noootwo-state/scripts/noootwo_state.py --self-test
python3 skills/noootwo-state/scripts/audit_codex_context.py --self-test
git diff --check
```

The eval files are behavior contracts until fresh-session runs exist. This
experiment does not claim that the candidate already reduces latency, tokens,
conflicts, or rework.
