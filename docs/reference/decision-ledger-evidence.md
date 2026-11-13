# Decision Ledger Evidence

Research brief for ADR 0032: how the product interview keeps answered decisions
from being asked again across rounds, sessions, and compactions.

## Decision

Which mechanism should `noootwo-product` use to keep a settled answer settled:

```
Decision:   How the interview records answers so no round, session, or
            compaction re-asks a decision the user already made.
Would flip: Evidence that a durable ledger plus per-round recitation costs more
            than it saves, or that a host already guarantees answer survival.
Not enough: Opinion posts without a transcript, issue, or artifact; a single
            unreplicated report.
```

Size: `deep`. The change alters the shipped interview protocol and its evals,
so it is persisted here and through ADR 0032.

## Problem Evidence (local and public)

The failure is reproducible, not hypothetical.

- Local artifact: session
  `rollout-2026-11-13T11-39-14-01a1d2fc...` (kungfu-harness) ran 9 compactions
  in 2h22m; every question round except one fired within ~1.5 minutes after a
  compaction. `balance_placement` was asked three times with a different option
  set each time; the answers drifted from "账号行内常显" to "账号入口常驻" to
  "顶栏胶囊 + 账户菜单", and `onboarding_shape` drifted from "轻量三步" to
  "轻量两步". The 13:57 summary listed already-answered items under
  `尚需用户确认`, which produced the next two duplicate rounds. The project's
  `.noootwo/state/current.json` (2026-10-29) contains none of these decisions.
- `openai/codex` issues: #54544 *repeats settled questions*; #42611
  *auto-compaction replays an already-answered user message as a new turn*;
  #49022 *Active Goal is lost after automatic context compaction and Codex
  resumes previously completed tasks*; #58369 *agent reopens explicit user
  decisions*; #46175 *returns to earlier clarification state after answers*;
  #44648 shows the question tool has no resolve/withdraw lifecycle. User
  reports, unverified by maintainers, but mutually consistent.
- `anthropics/claude-code` issues: #80938 *compaction silently drops
  custom working-mode directives*; #96422 *custom instructions are lost across
  context compaction with no signal*; #26771 documents data that still exists
  on disk being dropped and re-requested from the user; #97906 asks for
  "conversation anchors ... a ledger of finished items". Same evidence level.

## Solution Evidence (mechanisms, by source)

Official guidance and product docs:

- Anthropic, *Effective context engineering for AI agents*: compaction "preserves
  architectural decisions, unresolved bugs, and implementation details while
  discarding redundant tool outputs"; warns that overly aggressive compaction
  loses context whose importance appears later; recommends maximizing recall in
  the compaction prompt.
- Kiro docs, Compaction and IDE 1.0 compaction: "Your goals, decisions, and
  technical progress are preserved"; key decisions and constraints sit in the
  always-preserved table; the summary persists as a session checkpoint; the
  documented recovery when a detail is lost is to restate it.
- Claude Code docs, costs and memory: `/compact` accepts custom preservation
  instructions and CLAUDE.md can carry them; CLAUDE.md and auto memory load at
  the start of every session.
- GitHub Spec Kit, `clarify` command template: "Exclude questions already
  answered"; answers are encoded back into the spec, and follow-up commands read
  the spec instead of re-asking; the session budget is capped at five questions.
- Rasa forms: the agent requests the first required slot that is not yet
  filled; filled slots are not asked again. The classic slot-filling
  mechanism, stated generically.

Community and methodology sources:

- Superpowers `v7.0.2` `brainstorming`: "Never ask what the project or their
  context already answers, or reopen what they've already decided"; the design
  doc is written and approved before planning. `executing-plans`: "the ledger is
  your memory"; "leave a record that survives your own forgetting"; rulings are
  recorded as decision, reason, and cost if wrong.
- Manus, *Context Engineering for AI Agents*: rewriting `todo.md` each step
  "recites its objectives into the end of the context", countering drift and
  "lost-in-the-middle"; it also warns that uniform context creates ruts.
- ACE (arXiv 2510.04618): iterative rewriting suffers "brevity bias" and
  "context collapse"; the fix is structured, incremental updates that preserve
  detail. This names the exact regression seen in the local transcript.
- Cline Memory Bank: a small file hierarchy read at the start of every task keeps
  project context stable across resets.
- 12-Factor Agents: own your context window; unify execution and business state;
  resume "from any point by just loading the thread" instead of re-deriving it.
- MADR ADR template: a decision's status carries `superseded by ADR-XXXX`.
  Changing a settled decision happens through an explicit new record, never by
  silently re-asking.

## Adopted Mechanism

One protocol with five rules, owned by `noootwo-product`:

1. **Ledger.** Every answer becomes one entry: stable `id`, question, the user's
   answer in their words, `status`, and the condition that reopens it.
2. **Ask gate.** A round asks only ids with no entry or a met `reopen-if`
   condition; the frontier is recomputed as *answerable now minus answered*.
3. **Frozen wording, explicit supersede.** An answered decision keeps its
   wording and options; a reopen shows the old answer, names the new evidence,
   and records the new answer as superseding the old entry.
4. **Recitation.** Every asking round, shared-understanding summary, and plan
   repeats the full settled list as `id: answer` lines, so the recent context
   always carries the record. This is the Manus recitation mechanism applied to
   decisions.
5. **Append, don't rewrite.** Entries and status changes are appended; the
   ledger is never regenerated from memory. Durable work persists it through
   `noootwo-state`; a read-only or plan-only turn carries it in the recited list
   and the plan's settled section.

## Boundaries and Counterexamples

- No independent controlled study measures the ask gate. Evidence is the local
  transcript plus recurring public reports plus mechanism-level official
  guidance. Confidence: medium.
- Host asymmetry: Claude Code offers compaction instructions and hooks; Codex
  offers neither, and Plan Mode forbids file writes, so the skill-level
  recitation and the plan-embedded ledger are the only transferable mechanisms.
  This brief does not claim host behavior changes.
- Cost boundary: the ledger stays one line per decision. Cline-style full reads
  and Manus-style recitation both cost tokens; Anthropic's "smallest set of
  high-signal tokens" caps the size. Recitation repeats compact lines, not the
  transcript.
- Uniformity counterexample: Manus warns that repeated identical context
  produces ruts; recitation stays a short list, not a scripted replay.
- Cheap modes stay cheap: direct edits and settled requests never build a
  ledger; the protocol only runs while an interview is open.
- Rejected alternatives: global cross-project memory (stale, unsafe);
  re-reading full transcripts after compaction (cost, and the Compact
  Laundering lesson from the context-cost pass); copying Spec Kit's five-question
  cap or Cline's file hierarchy wholesale; treating a compaction summary as
  authoritative over the ledger.

## Source Index

- Anthropic context engineering:
  `https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents`
- Kiro Compaction: `https://kiro.dev/docs/compaction.md`
- Kiro IDE 1.0 compaction: `https://kiro.dev/docs/ide/whats-new-v1/compaction.md`
- Kiro Memory: `https://kiro.dev/docs/memory.md`
- Claude Code costs (compact instructions): `https://docs.claude.com/en/docs/claude-code/costs.md`
- Claude Code memory: `https://docs.claude.com/en/docs/claude-code/memory.md`
- GitHub Spec Kit clarify template:
  `https://github.com/github/spec-kit/blob/main/templates/commands/clarify.md`
- Superpowers brainstorming and executing-plans:
  `https://github.com/obra/superpowers`
- Manus context engineering:
  `https://manus.im/blog/Context-Engineering-for-AI-Agents-Lessons-from-Building-Manus`
- ACE: `https://arxiv.org/abs/2510.04618`
- Cline Memory Bank: `https://docs.cline.bot/prompting/cline-memory-bank`
- 12-Factor Agents: `https://github.com/humanlayer/12-factor-agents`
- MADR: `https://github.com/adr/madr`
- Rasa forms: `https://rasa.com/docs/rasa/forms/`
- Codex issues: `openai/codex` #54544, #42611, #49022, #58369, #46175, #44648
- Claude Code issues: `anthropics/claude-code` #80938, #96422, #26771, #97906

Access note: Kiro's HTML pages render client-side; the `.md` endpoints listed
above served the full text and were read directly. All GitHub issue bodies were
read through the GitHub API on 2026-11-13.
