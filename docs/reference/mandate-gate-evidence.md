# Mandate Gate Evidence

Supporting sources for [ADR-0036](../adr/0036-mandate-gate.md). The decision is
to separate "the user described a problem" from "the user authorized a change",
and to fail closed when the mandate cannot be read.

## Access limits

- The web-search provider was rate-limited during this pass; sources were
  fetched directly.
- `developers.openai.com` returned HTTP 403 and `raw.githubusercontent.com`
  reset the connection. GitHub HTML pages, the Spec Kit documentation site,
  and the HN and GitHub issue APIs were reachable.
- Because the official Codex manual was unreachable, this decision makes no
  claim about whether Codex has a native plan mode.

## Sources

| Source | Level | What it shows | What transfers | Boundary |
| --- | --- | --- | --- | --- |
| Claude Code docs, common workflows — plan mode | official | "Claude reads files and proposes a plan but makes no edits until you approve." | Read-only deliberation before an explicit approval. | Harness-specific switch; not required. |
| Claude Code docs, best practices — "Brainstorm with Claude first" | official | Interview until a spec exists, then build from it in a fresh session. | Write the intent down before executing. | The fresh-session detail is a cost choice, not a requirement. |
| Cursor docs — Plan Mode | official | Clarifying questions, a reviewable plan, and building only when the user starts the build; quick changes skip it. | Proportional cost: gate complex or ambiguous work, not every edit. | UI affordance is Cursor's. |
| Kiro docs — Specs | official | Three-phase requirements/design/tasks flow with approval gates; `Quick Spec` is explicitly "without approval gates". | Default gate plus an explicit cheap path. | Phase count is Kiro's process choice. |
| GitHub Spec Kit docs | official | "Assessment can stand alone; a decision to proceed does not automatically start implementation." | A diagnosis or approach decision is not a build order. | Artifact names and slash commands are not adopted. |
| Microsoft HAX Guideline 10 | official design guidance | "Engage in disambiguation or gracefully degrade... In ambiguous situations, less can be more." | Ask or narrow scope when the goal is uncertain. | Written for AI product UX, not coding agents. |
| OpenAI Agents SDK — human-in-the-loop | official | Per-tool approval, and rules fail closed when arguments cannot be safely inspected. | Fail-closed authority on unreadable intent. | The SDK interrupt mechanism is not adopted. |
| `openai/codex` issue #2101 | community | "It will often dive into making changes right away and lacks a good way to manage or edit a plan before executing." | The failure is recurrent and user-visible, not local to one prompt. | Anecdotal; one issue thread. |
| Armin Ronacher, "What Actually Is Claude Code's Plan Mode?" | credible hands-on analysis | Plan mode is mostly prompting plus read-only reminders; a reviewable on-disk plan can replace the mode; some tools removed it. | Implement the mechanism in the process, not the harness. | One practitioner's reading of one implementation. |

## Counterexample

Tools that removed plan mode still keep a reviewable plan artifact and an
explicit go step. That is evidence against requiring a UI mode, not against
gating writes.

## Not claimed

- No controlled measurement of fewer rework rounds, lower token use, or faster
  delivery.
- No claim that every critique is ambiguous; the diff-summary test exists to
  keep unambiguous changes on the direct path.
