# 0023 — Diagnosis Map and evidence authority

- Status: accepted
- Date: 2026-10-20
- Owners: `noootwo-debug`, `noootwo-workflow`, `noootwo-ask`, `noootwo-code-health`, `noootwo-research`

## Context

`noootwo-debug` was shaped for one reproducible failure: pin expected versus
actual, reproduce it, trace the path, prove the cause, then fix it. That is the
right Incident Path, but it omitted an earlier kind of work:

- confirm one or more suspected problems that have not been reproduced;
- find which evidence can decide a claim;
- explain a mixed-state observation across product, protocol, code, data,
  deployment, and agent behaviour;
- return a recommendation without editing anything.

A real run turned six independent claims into a multi-hour cross-system audit.
Before all six claims were confirmed, the agent began adding tests and changing
selection logic, invalidated existing patches and image evidence, and invested
in a long evidence package. The existing Gate A still forbade edits before a
proven cause, but the skill provided no bounded way to decide what each claim
needed, when a claim was settled, or when to stop.

The routing layer had the same gap. Workflow could route a known broken
behaviour to debug, but "confirm these suspected problems and give me options"
could fall into research, code-health, or implementation. Research could also
be mistaken for a way to establish live runtime or deployment state.

## Decision

1. Make the **Diagnosis Map** the entry artifact for every debug request. Each
   requested claim gets its own question, class, authority, decisive check,
   status, stop bound, and handoff.
2. Use an **evidence-authority matrix** by layer:
   `product | external | protocol | code-path | deployment | data | agent-process`.
   A source is authoritative only for its layer. Product decisions do not prove
   runtime behaviour, documentation does not prove a live deployment, and
   source code does not prove production state.
3. Keep confirmation **read-only by default**. No source edit, patch, rebuild,
   deployment, persistent config or data mutation, or broad evidence package
   before every requested claim has a verdict.
4. Lead with a **short per-claim verdict**: `confirmed`, `refuted`,
   `insufficient`, or `decision-needed`. A long report does not upgrade a
   status, and insufficient evidence is a complete result.
5. Give each claim one **decisive check**. A follow-up is allowed only for a
   conflict, ambiguity, or an untested required branch. Repetition without new
   discriminating power does not justify more investigation.
6. Keep multiple claims **independent** until evidence proves a shared cause.
   Order them by prerequisite, cost, and impact, not by code proximity or the
   temptation to amortise one large audit.
7. Stop before the next action enters a new system, source mutation, rebuild,
   deployment, persistent data change, or another evidence layer. Hand off the
   settled map row instead of doing the receiving skill's job.
8. If the user says "confirm and fix", still finish confirmation first. Only
   confirmed failures enter the Incident Path; refuted and insufficient claims
   do not earn a fix.
9. Route confirmation requests explicitly:
   `noootwo-workflow` and `noootwo-ask` send them to `noootwo-debug`;
   `noootwo-code-health` confirms a disputed premise before a Change Shape;
   `noootwo-research` treats runtime and deployment state as observations, not
   outside research.
10. Keep the public skill set and owners unchanged. This is a new entry and
    stop mechanism inside `noootwo-debug`, not a new diagnosis skill.

## Research basis

The mechanism was compared against current public skill implementations on
2026-10-20:

- `obra/superpowers` at `bb92a77`:
  `systematic-debugging` requires root-cause investigation before fixes,
  gathers boundary evidence in multi-component systems, changes one variable at
  a time, and questions the architecture after three failed fixes.
  `diagnosing-superpowers` adds intake before analysis, a read-only report,
  exact path/line citations, and the rule that a whole-session "why" is a
  complaint rather than a scoped problem.
- `mattpocock/skills` at `5beb35b`: `diagnosing-bugs` requires a tight,
  red-capable feedback loop and ranked falsifiable hypotheses; `triage` records
  confirmed, failed, or insufficient detail; `wayfinder` resolves one decision
  ticket at a time and keeps the frontier separate from unready fog and
  out-of-scope work.
- `pbakaus/impeccable` at `374a0e1`: audit is systematic and read-only, routes
  to stages without auto-running them, separates evidence from recommendations,
  and requires false positives to be verified.
- `anthropics/skills` at `dbd4588`: skill-creator measures with-skill versus
  baseline runs, records pass rate, time, tokens, and tool calls, and reads
  transcripts to find unproductive repeated work.

The adopted mechanisms prevent the observed failure directly: intake before
analysis, one question or ticket at a time, layer-specific evidence, a read-only
report, explicit statuses, and a named stop boundary. The observation that a
cost problem needs transcript and token measurement also sets the evaluation
boundary below.

## Rejected alternatives

- **A new diagnosis skill.** The capability already belongs to `noootwo-debug`;
  a second skill would split evidence ownership and add permanent context load.
- **Two full modes with duplicated methods.** The map is one entry shared by
  all requests. A reproducible failure expands one map row into the existing
  Incident Path; other rows may end at a verdict.
- **Requiring reproduction for every claim.** Some claims are facts about a
  deployment, data state, or external contract, not failures to reproduce.
- **A fixed time or tool-call budget.** It would stop arbitrary work without
  knowing whether the decisive evidence was obtained. The map's status and
  next-action boundary are the control.
- **Documentation as live-state evidence.** Official docs establish a protocol
  or capability; only deployment, configuration, runtime, or data evidence can
  establish the current instance.
- **A mandatory long report.** The user needs verdicts and options first; the
  evidence bundle is optional and must not precede the decision.

## Consequences

- `noootwo-debug/SKILL.md` now starts with the map, defaults confirmation to
  read-only, and limits the Incident Path to mapped failures.
- `noootwo-debug/references/diagnosis-map.md` owns the evidence matrix, output
  shape, stop rule, and handoff.
- Workflow, ask, code-health, and research gain narrow routing or boundary
  statements rather than copies of the debug method.
- Seven scenario prompts cover cross-system audit drift, evidence authority,
  mutation during confirmation, routing, independent frontiers, runtime facts
  mistaken for research, and shaping before a premise is settled.

## Verification

- The workspace, skill, script, state, and diff checks must pass.
- The new evals are written but not yet measured. No token, time, or rework
  reduction is claimed until with-skill and baseline transcripts are compared.
- What would change the answer: evals showing that the map over-triggers on a
  single obvious failure, or that agents still widen after a claim reaches a
  terminal status. The response would be to tighten the entry or stop rule,
  not to add another skill.
