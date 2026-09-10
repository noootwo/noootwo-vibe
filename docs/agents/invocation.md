# Invocation Model

How the Noootwo skills reach each other and the user, and why the set is shaped this way. Read it when adding, splitting, renaming, or re-scoping a skill.

## The one axis: who can reach it

- **Model-invoked** — reachable by the agent on its own, by another skill, and by the human typing its name. Carries a model-facing `description`, which is always loaded: permanent context load in exchange for discovery.
- **User-invoked** — reachable only by the human typing `$name`. Zero context load, paid for in cognitive load: the human is the index.

A model-invoked skill can reach other model-invoked skills. A user-invoked skill can never be reached by another skill — not by naming it, not by any phrasing.

## How each harness switches it

| Harness | Mechanism | Value for user-invoked |
| --- | --- | --- |
| Codex | `agents/openai.yaml` | `policy.allow_implicit_invocation: false` |
| Claude Code | `SKILL.md` frontmatter | `disable-model-invocation: true` |

The Codex field is authoritative for this repository. Official Codex documentation states: when `allow_implicit_invocation` is false, the skill "is not injected into the model context by default, but can still be invoked explicitly via `$skill`".

This repository does **not** set `disable-model-invocation`. It ships as a Codex plugin (`.codex-plugin/plugin.json`), and the Codex plugin validator requires that field to be `false`. Revisit only if a Claude Code plugin is published separately.

## The Noootwo set

| Skill | Invocation | Role |
| --- | --- | --- |
| `noootwo-ask` | user-invoked | router: names the other five and when to reach for each |
| `noootwo-workflow` | model-invoked | lifecycle guardrails and running a multi-step task |
| `noootwo-product` | model-invoked | settling product decisions before design or build |
| `noootwo-design` | model-invoked | UI, visual, and artifact work after the product path is settled |
| `noootwo-review` | model-invoked | code and project-health review, and diagnosing rework |
| `noootwo-docs` | model-invoked | placing changed facts in the right documentation layer |

Only `noootwo-ask` is user-invoked, because only it exists purely to orient a human. Every other skill must be reachable by the agent and by its siblings.

## Router

A **router** is a user-invoked skill that names the other skills and the situations that reach them. It exists to cure cognitive load when the human has too many skills to remember, and it costs no context load.

A router only hints — it can never fire another skill. Use `$name` there: it is written for a human to type. Add one only when the set is genuinely too large to hold in mind; with a small set, the router and the `AGENTS.md` pointer are the same job.

## Cross-skill dependencies

When a skill's step requires another skill, write it as an instruction to load that skill, naming both the skill and its entrypoint:

> Invoke the `noootwo-design` skill: read its `SKILL.md` and follow it.

Naming the mechanism is what gets it fired. A bare `$noootwo-design` left in prose is read as a label, not as a command, so the step quietly does not happen. Inside a `SKILL.md` body this phrasing is mandatory; `$name` belongs only in the router and in human-facing docs.

One skill per instruction. A step needing two skills is two instructions.

## Splitting by invocation

Split off a model-invoked skill when it has a distinct leading word that should trigger it on its own, or when another skill must reach it. That independence costs a permanently loaded description, so it has to be worth it.

Shared reference that two user-invoked skills both need cannot live in either. Put it in a plain file outside the skill system and point both at it.
