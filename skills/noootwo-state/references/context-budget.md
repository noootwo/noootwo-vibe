# Context Budget

Use this when a documentation source is becoming expensive to read, when a status document is turning into a timeline, or when an agent needs facts from a long document.

## Context lifecycle

`write -> select -> compress -> isolate -> verify`

1. **Write** the durable fact, decision, blocker, or evidence handle when it changes.
2. **Select** only the facts and files that constrain the current step.
3. **Compress** re-entry into a context capsule: goal, stage, settled and unsettled decisions, blockers, next trigger, provenance handles, and source hash.
4. **Isolate** only independent, read-only research or review work. Keep one writer and do not duplicate dependent decisions across agents.
5. **Verify** the capsule's claim against the named source before acting on it. Compression never upgrades uncertainty or replaces raw evidence.

The capsule is `noootwo.context-capsule/0.1`; state and event schemas remain authoritative and unchanged.

## Principle

Documentation should make the next task cheaper. If a file is read often, it must be short, scoped, and good at routing to deeper material. Long evidence, history, and raw material belong behind searchable names, not in always-read entrypoints.

## Heat Layers

| Layer | Owns | Budget |
| --- | --- | --- |
| Always-on entrypoints | `AGENTS.md`, skill `SKILL.md` files, short routing prompts | target under 200 lines |
| Status snapshot | `docs/status.md` or equivalent project status | target under 120 lines; hard stop at 200 lines |
| On-demand references | `references/`, `docs/reference/`, skill-specific playbooks | one topic per file; clear read trigger near the top |
| Durable history | `docs/releases/`, `docs/adr/` | concise dated records, not session transcripts |
| Cold evidence | raw evidence, long logs, screenshots, old task notes | searchable storage or out of repo; do not load by default |

## Live and cold

- A live excerpt defaults to 80 lines and never becomes the evidence record.
- Output above 16 KiB goes to a cold evidence file before the next reasoning step.
- The hot context carries the conclusion, file or URL, line or command, exit status, hash, and the path needed to reopen the source.
- Re-read a source slice when its hash, commit, environment, or claimed role is unclear; do not trust a summary that lost provenance.

## Placement Table

| Fact | Owner |
| --- | --- |
| Current repository state, current risks, current validation, next actions | `docs/status.md` |
| Version changes, user-visible migration notes, tag history | `docs/releases/` |
| Durable choices, boundaries, and role decisions | `docs/adr/` |
| Repeated workflows and how-to procedures | `docs/guides/` |
| Stable commands, schemas, manifests, field lists, API references | `docs/reference/` |
| Raw evidence, old process notes, transcripts, long command output | cold storage, archive, or deletion |

## Status Compression Rules

When `docs/status.md` grows past the target budget:

1. Keep only the current project identity, live validation surface, active risks, and next actions.
2. Replace older validation runs with the current verified command set and date.
3. Remove completed risks from status after their release note, ADR, or reference owner exists.
4. Move historical version details to release notes.
5. Move stable decisions to ADRs.
6. Move reusable procedures to guides or references.
7. Move, link, or mark stale process notes; delete only non-authoritative scratch after its owner confirms no historical or evidentiary value.

Do not preserve a complete landed-work timeline in status. If historical traceability matters, create a concise release note or ADR and link to it only when discovery would otherwise fail.

## Retrieval Rules

Before reading a long document, locate the relevant slice locally:

1. Use `rg --files` to identify candidate files.
2. Use `rg -n` on headings, paths, identifiers, dates, errors, commands, or domain terms.
3. Read only the matching section with a bounded command such as `sed -n 'start,endp'`.
4. Prefer file headers, summaries, frontmatter, tables of contents, and heading lists before body text.
5. Read the whole document only for whole-document audits, consistency checks, or when targeted search fails.

Never use a long file as a context dump when a local search can isolate the relevant evidence.

## State helper

- `capsule` returns a bounded re-entry view in Markdown or JSON and never changes state; both forms default to 80 lines and 6,000 characters.
- `inspect` returns metadata, headings, and matching lines; it never needs to dump a long file.
- `capture` writes complete command output to cold evidence and returns only its exit status, hash, path, and bounded tail.
- Read the append-only event tail only when reconstructing change history; use the capsule for ordinary re-entry.
- An unchanged structured-state request creates no event; a changed request names what changed and stores the evidence hash and size.

## Maintenance Gate

Before adding material to a hot file, ask:

- Will most future sessions need this fact before doing any work?
- Can this fact be verified or acted on directly?
- Is this the only owner for the fact?
- Would a search term plus an on-demand reference be cheaper?

If the answer is not clearly yes for the first three questions, route it out of the hot file.
