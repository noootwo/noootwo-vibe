---
name: noootwo-docs
description: "Use when a change alters behaviour, project state, release facts, product decisions, or agent instructions, and the documents must stay true. Also for documentation audits and stale-claim cleanup."
---

# Noootwo Docs

Put each fact in one owning layer, and remove the stale version. The goal is not more documents.

A change to behaviour, project state, release facts, product decisions, or agent instructions needs a docs decision before the work is called done — either an update to the owning layer, or a recorded decision that nothing changed. Silent drift is the defect this skill exists to catch.

## Layers

| Layer | Owns |
| --- | --- |
| `README.md` | the stable public overview: install, usage, skill list, release model |
| `AGENTS.md` | short always-on agent instructions; pointers to skills, not their bodies |
| `docs/status.md` | current state: what is verified, what is at risk, what is next |
| `docs/adr/` | durable decisions, with context, consequences, and status |
| `docs/agents/` | the standards agents are written to: authoring and invocation |
| `docs/guides/` | procedures users or agents repeat |
| `docs/reference/` | stable commands, schemas, manifests, and APIs |
| `docs/experiments/` | recorded measurement and its results |
| `docs/releases/` | per-skill release notes, migrations, and tag history |

If a repository uses different names, map by responsibility rather than forcing this layout.

## Update rules

1. Inspect the change before writing.
2. Classify each changed fact: `usage`, `agent rule`, `current state`, `decision`, `procedure`, `reference`, `measurement`, or `release`.
3. Pick one owning layer per fact.
4. Update that layer; link rather than copy when another layer needs awareness.
5. Revise or delete the stale claim in the same pass.
6. Keep volatile state in `docs/status.md`, never in README or AGENTS.
7. Record a lasting decision as an ADR once it is accepted.
8. Write intent as intent. Label anything unbuilt as planned.

**Done when:** every changed fact has one owning layer, and no neighbouring document still contradicts it.

## Status budget

`docs/status.md` is a current-state snapshot, not a diary. Keep it at 120 lines or fewer; compress it before it reaches 200. Version history goes to releases, durable decisions to ADRs, procedures to guides, and raw research out of the hot path.

## After any change

Check whether it touched: install or usage instructions; repository or package layout; public commands; skill names, descriptions, or routing; validation, CI, release, tagging, or the local install flow; product decisions, user flows, acceptance criteria, or architecture decisions; project status or active risk.

If it touched one, update that layer. If it touched none, say that docs were checked and left unchanged.

## Anti-drift

- Keep one authoritative copy of a command list; link the others.
- Keep the same name everywhere the live repo uses it.
- Drop stale examples unless a migration note explicitly keeps them.
- Update the owning layer first, not the most visible one.
- Never invent product scope, UI direction, or technical architecture here. When a judgment is missing, invoke the `noootwo-product`, `noootwo-design`, or `noootwo-review` skill: read its `SKILL.md` and follow it.
- Search locally and read the relevant slice rather than loading a long document whole, unless the task is a whole-document audit.

## Reference

- `references/docs-layering.md` — choosing the layer, writing an ADR, and adopting a project.
- `references/docs-audit.md` — finding stale claims, duplicated facts, and wrong-layer content.
- `references/context-budget.md` — what to do when a status doc, AGENTS file, skill body, or reference grows too costly to read.
