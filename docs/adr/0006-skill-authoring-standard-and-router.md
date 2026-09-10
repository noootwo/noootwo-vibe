# ADR 0006: Skill Authoring Standard And Router

- Status: accepted
- Date: 2026-09-11

## Context

The five Noootwo skills were rewritten several times by copying surface material from well-regarded skill projects. Each rewrite produced text that read like the source but did not behave like it: the workflow skill often failed to wake on its own triggers, and skills rarely reached each other. Users reported repeated rework even after a full rewrite pass.

A research pass over two reference projects found that neither works the way we had been imitating.

`pbakaus/impeccable` is a system, not a document: a Rust engine, a CLI, a browser extension, an edit-time hook, 61 deterministic detector rules, and a live browser mode. Its skill file is short because the work happens in code. Copying its prose copied conclusions without enforcement.

`mattpocock/skills` is a writing discipline, not a system: no engine, no runtime, no tests. `grill-me` is seven lines and `grilling` is twenty-eight. What makes it work is a documented authoring standard (`writing-for-agents`, `SKILL-MECHANICS.md`, `.agents/invocation.md`) plus explicit invocation mechanics: 37 model-invoked skills, 22 user-invoked skills, one user-invoked router, and cross-skill dependencies written as instructions to load the named skill.

Measured against that standard, this repository was inverted:

| Dimension | Reference | Noootwo before this ADR |
| --- | --- | --- |
| `SKILL.md` size | 7–140 lines | 89–266 lines |
| `description` length | 65–166 characters | 445–600 characters |
| Cross-skill invocation | names the skill to load, 21 occurrences | bare `$noootwo-x` prose, 0 load instructions |
| Invocation layer | explicit user-invoked vs model-invoked | not expressible; the validator rejected extra frontmatter |
| Router | present | absent |
| Authoring standard | documented and enforced | one line in `AGENTS.md` |

The mismatch explains both symptoms. Keyword-stuffed descriptions try to cover every branch, which dilutes each trigger instead of sharpening it. Private vocabulary (`one-material-gap`, `intent fit`) carries no prior for the model to think with, so it must be redefined on every run. And with no standard, each rewrite re-derived style from scratch.

## Decision

Adopt a written authoring standard and enforce it mechanically.

1. `docs/agents/skill-authoring.md` is the standard: context pointers, the two loads, information hierarchy, completion criteria, splitting, leading words, pruning, and positive phrasing. It carries a small canonical vocabulary — `frontier`, `settled`, `shared understanding`, `rework`, `slop` — to replace coined state labels.
2. `docs/agents/invocation.md` defines the invocation model and the mandatory cross-skill phrasing: a step says to load the named skill and its `SKILL.md`, because naming the mechanism is what gets it fired.
3. `scripts/validate_skill_workspace.py` enforces budgets and structure: `description` ≤ 200 characters, `SKILL.md` ≤ 120 lines, ≤ 12 reference files each named by a pointer, `short_description` 25–64 characters, no `default_prompt`, and no bare `$noootwo-` reference inside a skill body.
4. Add `noootwo-ask` (v0.1.0) as the single user-invoked router, switched with `policy.allow_implicit_invocation: false` in `agents/openai.yaml`. The public skill set becomes six; the count limit in `AGENTS.md` is updated accordingly.
5. The five existing skills stay model-invoked and are rewritten to the standard in the same pass, because the new validator rules are failures for the old bodies.

`disable-model-invocation` is deliberately not used. This repository ships as a Codex plugin (`.codex-plugin/plugin.json`), and the Codex plugin validator requires that field to be `false`; the Codex `policy` field is the authoritative switch here.

## Consequences

- Skill bodies shrink to steps plus pointers, so the agent attends to the steps instead of skimming a policy document.
- Cross-skill routing becomes an explicit action rather than a label, which is the fix for skills failing to reach each other.
- The router gives the human one entry point at zero context cost.
- The validator now fails on the old shapes, so the standard cannot silently erode.
- Deterministic enforcement — an engine, edit hooks, or detector rules as `impeccable` uses — stays out of scope. It is the remaining structural gap between this suite and that project, and it is tracked for separate evaluation rather than adopted here.
