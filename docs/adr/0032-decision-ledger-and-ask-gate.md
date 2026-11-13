# 0032 — Decision ledger and ask gate

## Status

Accepted on 2026-11-13 as the candidate for the next release batch.

## Context

A read-only audit of one real product interview
(`rollout-2026-11-13T11-39-14-01a1d2fc...`, kungfu-harness) showed the interview
loop failing in a way the existing rules did not catch:

- 9 compactions in 2h22m; every question round except one fired within about
  1.5 minutes after a compaction.
- `balance_placement` was asked three times with a regenerated option set each
  time; the recorded answer drifted from "账号行内常显" to "账号入口常驻" to
  "顶栏胶囊 + 账户菜单", and `onboarding_shape` drifted from "轻量三步" to
  "轻量两步". The 13:57 summary moved answered decisions back under
  `尚需用户确认`, which produced the next duplicate rounds.
- The project's `.noootwo/state/current.json` (2026-10-29) contained none of
  these decisions: answers lived only in the transcript and in rolling
  summaries. Plan Mode forbids file writes, so the interview could not persist
  them at the moment they arrived.

The same class recurs publicly: `openai/codex` #54544, #42611, #49022, #58369,
#46175, #44648 and `anthropics/claude-code` #80938, #96422, #26771, #97906 all
report settled questions or directives being re-opened or re-asked after
compaction. The previous ledger in `product-flow.md` was a display template
with four status buckets; it had no ids, no ask gate, no reopen rule, and no
recovery path, so a compacted model could re-derive the frontier from a lossy
summary and ask again.

## Decision

1. `noootwo-product` owns a Decision Ledger protocol. Every settled decision
   becomes one entry with a stable id, the user's answer quoted in their words,
   a status (`answered`, `assumed`, `deferred`, `rejected`, or
   `superseded by <id>`), and the condition that reopens it.
2. An ask gate recomputes the frontier as *answerable now minus answered*.
   A round asks only ids with no entry or a met `reopen-if` condition. Answered
   decisions keep their wording and options; reopening shows the old answer,
   names the new evidence, and records the new answer as a supersede.
3. Every asking round, shared-understanding summary, handoff, and plan recites
   the settled list as `id: answer` lines, so the recent context always carries
   the record. A compaction summary is a lead; the ledger is the authority.
4. Entries are appended, never regenerated from memory. Work that outlives the
   session or crosses a handoff persists the ledger through `noootwo-state`.
   Read-only and plan-only turns recite it, and the plan's settled section
   becomes the durable copy.
5. `SKILL.md` carries the gate, the recitation, and the re-entry rule; the full
   protocol and the compact shape live in `references/product-flow.md`. Three
   eval contracts cover answered stays answered, post-compaction recovery, and
   reopen-only-with-evidence.
6. No host feature is required. Claude Code offers compaction instructions and
   hooks; Codex offers neither, and Plan Mode forbids writes, so recitation and
   the plan-embedded ledger are the transferable mechanisms.
7. No new skill, no schema change, and no change to the public set. Direct
   edits and already-settled requests never build a ledger.

## Research basis

Anthropic's context-engineering guidance requires compaction to preserve
decisions, constraints, and unresolved detail; Kiro's compaction docs place
goals, decisions, and constraints in the always-preserved set with a
checkpoint; Spec Kit's `clarify` states "exclude questions already answered"
and encodes answers back into the spec; Rasa forms re-ask only unfilled slots;
Superpowers `brainstorming` says never to reopen what the user already decided
and `executing-plans` treats the ledger as memory; Manus recites objectives to
counter drift; ACE (arXiv 2510.04618) names brevity bias and context collapse
as the rewrite failure; MADR records changed decisions as `superseded by`.

Full source levels, boundaries, and counterexamples live in
[`docs/reference/decision-ledger-evidence.md`](../reference/decision-ledger-evidence.md)
and the decision-continuity pass in
[`references/research-basis.md`](../../references/research-basis.md). No
independent controlled study measures the ask gate; the local transcript,
recurring public reports, and mechanism-level official guidance support
adoption without a token, speed, or quality claim.

## Rejected alternatives

- **Global cross-project decision memory.** Decisions are project facts; a
  global store goes stale and leaks context between unrelated work.
- **Re-reading full transcripts after compaction.** Cost, and the
  context-cost pass already rejected transcript replay; the Compact Laundering
  finding argues against flattening provenance.
- **Copying Spec Kit's five-question cap or Cline's file hierarchy.** The cap
  is Spec Kit's process choice, and the hierarchy is Cline's storage layout;
  only the dedupe and persistence mechanisms transfer.
- **Depending on host compaction hooks or instructions.** Codex has no
  equivalent surface today, and Plan Mode forbids the file write the hook would
  need.
- **Letting a summary reopen a decision.** Summaries compress by design; the
  append-only ledger preserves the answer and the reopen condition.

## Consequences

- The interview gains one small always-on rule set and a slightly longer
  reference; each round pays a few recitation tokens and buys answer durability
  across rounds, sessions, and compactions.
- The ledger stays one line per decision; it is not a transcript and not a
  second spec.
- Residual risk: recitation can be skipped, or the ledger can silently diverge
  from the project state. The eval contracts cover the first; the second is
  handled by the existing single-writer and verify rules in `noootwo-state`.

## Verification

- `python scripts/validate_skill_workspace.py .` enforces the `SKILL.md` line
  budget and reference pointers after the new text.
- The product skill validator runs over `skills/noootwo-product`.
- Three new eval prompts join the existing product contracts:
  `answered-decisions-stay-answered`, `post-compaction-frontier-recovery`,
  `reopen-only-with-new-evidence`.
- The next paired-session measurement uses the same protocol as the
  context-cost pass; no improvement is claimed until it is measured.
