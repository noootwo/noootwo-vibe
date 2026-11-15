# 0033 — Capture durable user rules through `noootwo-state`

## Status

Accepted on 2026-11-16 for workspace `0.32.0`.

## Context

The suite persists task state, product decisions, specs, plans, and release
facts, but a user's durable project rule can remain only in the conversation.
Examples are an explicit "from now on use this command" instruction, a repeated
correction, or a stable convention the user has confirmed. After a compaction or
in a new session, that rule is re-derived from a lossy summary or lost entirely,
so the user has to repeat it.

The storage model already names a hot entrypoint for short always-on rules:
[`state-layering.md`](../../skills/noootwo-state/references/state-layering.md)
assigns routing and short rules to `AGENTS.md`, current truth to the structured
snapshot, durable choices to decision records, and status to a Markdown layer.
The gap is behavioural, not structural. No skill says when a user statement is
durable enough to persist, who decides its owner, or how a correction replaces a
stale rule. The workflow close gate asked whether behaviour or state changed,
which can miss a rule that changes future behaviour while the current code does
not change.

ADR 0032 already establishes the relevant failure class: settled decisions and
constraints are lost across compaction and get re-asked. Its evidence brief
records the local interview transcript and recurring public reports. This ADR
extends that mechanism from product decisions to project-level rules; it does
not introduce a new memory service or a new external claim.

## Decision

1. `noootwo-state` owns project-rule placement. It qualifies a candidate by
   durability, scope, actionability, authority, and non-duplication, then places
   one owning form.
2. A short always-on rule goes in the nearest `AGENTS.md`. Current progress goes
   to `.noootwo/state/current.json` through the state helper. A durable choice
   with rationale goes to `docs/adr/`. Project status, specs, plans, procedures,
   and cold evidence keep their existing layers.
3. `noootwo-workflow` treats a user-stated durable rule, correction, or
   preference as a state change in the same turn, even when no code changes.
   The user is not asked to repeat an explicit rule.
4. An explicit rule is written directly in the user's terms. An inferred rule is
   recorded as `assumed` with a reopen condition and is not promoted to an
   always-on line until evidence or the user confirms it.
5. The close report names the destination (`remembered: <rule> -> <path>`).
   Task-local instructions are marked as such instead of being promoted.
6. The rule is placed once. A rationale may be linked, but the same rule is not
   copied into `AGENTS.md`, `docs/status.md`, and an ADR. A conflicting rule
   supersedes the stale claim in the same pass.
7. No new skill, no root `SKILL.md`, and no state/event schema change. The
   public set stays at twelve.

## Consequences

- An explicit correction survives a new session and stops costing the user a
  repeat.
- Project hot files can grow, so the existing hot-file budget and the
  non-duplication rule remain the guard. The memory layer is for what the
  repository cannot look up, not for a second copy of the codebase or scripts.
- Inferred rules carry uncertainty instead of hardening a guess into policy.
- The mechanism is instructions plus a scenario contract, not a deterministic
  detector. A model can still miss an implicit rule; the close gate and the
  eval make the miss visible rather than silent.

## Research basis

- [ADR 0032](0032-decision-ledger-and-ask-gate.md) and
  [decision-ledger-evidence.md](../reference/decision-ledger-evidence.md):
  decisions and constraints must survive compaction; summaries are leads, not
  authorities; answered decisions are not reopened without new evidence.
- [state-layering.md](../../skills/noootwo-state/references/state-layering.md)
  and [context-budget.md](../../skills/noootwo-state/references/context-budget.md):
  one owning location per fact, short hot entrypoints, on-demand rationale, and
  a lookup before a durable copy.
- [ADR 0011](0011-state-skill-owns-abstract-persistence.md): persistence has one
  owner and the owner chooses form and location without interpreting domain
  content.

This is an application of already accepted mechanisms, not a new library or
workflow mode. No external source was re-queried for this ADR; the existing
evidence brief remains the source record.

## Rejected alternatives

- **Add `noootwo-memory` or restore `noootwo-docs`.** The capability is already
  persistence; a second skill would split one fact across two owners and change
  the exact public set.
- **Global cross-project memory.** Rules are project facts. A global store goes
  stale and leaks preferences between unrelated projects.
- **Persist every user sentence.** Most are task-local, already in the repo, or
  cheap to look up. That turns memory into a transcript.
- **Duplicate the rule in AGENTS.md, status, and an ADR.** The copies drift and
  make the rule look more authoritative than its evidence.
- **Add a `rule` fact type and schema version.** Existing `decision`,
  `narrative`, and hot-entrypoint layers already cover the form; a schema change
  would add migration cost without a new query capability.

## Verification

- `python scripts/validate_skill_workspace.py .` checks the two changed skill
  budgets, pointers, capability map, and public set.
- `skills/noootwo-state/evals/prompts/durable-rule-capture.md` covers an
  explicit rule that must be placed without a repeat request.
- `skills/noootwo-state/evals/prompts/inferred-rule-stays-assumed.md` covers an
  inference that must not become an always-on fact without confirmation.
- `skills/noootwo-state/evals/prompts/correction-replaces-stale-rule.md` covers
  a correction that must retire the stale claim and prevent recurrence.
- Fresh model-session runs remain unmeasured; no token, speed, or quality
  improvement is claimed.
