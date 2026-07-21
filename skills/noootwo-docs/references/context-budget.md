# Context Budget

Use this when a documentation source is becoming expensive to read, when a status document is turning into a timeline, or when an agent needs facts from a long document.

## Principle

Documentation should make the next task cheaper. If a file is read often, it must be short, scoped, and good at routing to deeper material. Long evidence, history, and research belong behind searchable names, not in always-read entrypoints.

## Heat Layers

| Layer | Owns | Budget |
| --- | --- | --- |
| Always-on entrypoints | `AGENTS.md`, skill `SKILL.md` files, short routing prompts | target under 200 lines |
| Status snapshot | `docs/status.md` or equivalent project status | target under 120 lines; hard stop at 200 lines |
| On-demand references | `references/`, `docs/reference/`, skill-specific playbooks | one topic per file; clear read trigger near the top |
| Durable history | `docs/releases/`, `docs/adr/` | concise dated records, not session transcripts |
| Cold evidence | raw research, long logs, screenshots, old task notes | searchable storage or out of repo; do not load by default |

## Placement Table

| Fact | Owner |
| --- | --- |
| Current repository state, current risks, latest validation, next actions | `docs/status.md` |
| Version changes, user-visible migration notes, tag history | `docs/releases/` |
| Durable product, workflow, architecture, or role-boundary decisions | `docs/adr/` |
| Repeated workflows and how-to procedures | `docs/guides/` |
| Stable commands, schemas, manifests, field lists, API references | `docs/reference/` |
| Raw research, old process notes, transcripts, long command output | cold storage, archive, or deletion |

## Status Compression Rules

When `docs/status.md` grows past the target budget:

1. Keep only the current project identity, live validation surface, active risks, and next actions.
2. Replace older validation runs with the latest verified command set and date.
3. Remove completed risks from status after their release note, ADR, or reference owner exists.
4. Move historical version details to release notes.
5. Move stable decisions to ADRs.
6. Move reusable procedures to guides or references.
7. Delete stale process notes that no longer change present work.

Do not preserve a complete landed-work timeline in status. If historical traceability matters, create a concise release note or ADR and link to it only when discovery would otherwise fail.

## Retrieval Rules

Before reading a long document, locate the relevant slice locally:

1. Use `rg --files` to identify candidate files.
2. Use `rg -n` on headings, paths, identifiers, dates, errors, commands, or domain terms.
3. Read only the matching section with a bounded command such as `sed -n 'start,endp'`.
4. Prefer file headers, summaries, frontmatter, tables of contents, and heading lists before body text.
5. Read the whole document only for whole-document audits, consistency checks, or when targeted search fails.

Never use a long file as a context dump when a local search can isolate the relevant evidence.

## Maintenance Gate

Before adding material to a hot file, ask:

- Will most future sessions need this fact before doing any work?
- Can this fact be verified or acted on directly?
- Is this the only owner for the fact?
- Would a search term plus an on-demand reference be cheaper?

If the answer is not clearly yes for the first three questions, route it out of the hot file.
