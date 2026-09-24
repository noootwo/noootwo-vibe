# Invocation Model

How the Noootwo skills reach each other and the user, and why the set is shaped this way. Read it when adding, splitting, renaming, or re-scoping a skill, and when one skill needs another's capability.

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
| `noootwo-ask` | user-invoked | router: names the other skills and when to reach for each |
| `noootwo-workflow` | model-invoked | lifecycle guardrails and running a multi-step task |
| `noootwo-product` | model-invoked | settling product decisions before design or build |
| `noootwo-design` | model-invoked | UI, visual, and artifact work after the product path is settled |
| `noootwo-tdd` | model-invoked | red-green-refactor and test quality for behavior-changing code |
| `noootwo-review` | model-invoked | change review, the refactoring health loop, structure sweeps, optimization, and acceptance |
| `noootwo-state` | model-invoked | recording and reading project state/context and choosing storage format |
| `noootwo-debug` | model-invoked | proving a cause and bounding the fix when something is broken |
| `noootwo-research` | model-invoked | settling a decision that only external evidence can settle |
| `noootwo-onboard` | model-invoked | entering an unfamiliar project and auditing which skills it needs |

Only `noootwo-ask` is user-invoked, because only it exists purely to orient a human. Every other skill must be reachable by the agent and by its siblings.

`noootwo-workflow` may discover and invoke other installed skills as execution resources when the task belongs outside the Noootwo set, such as slides, documents, or media work. Those skills are not added to the public set or the capability map.

## Router

A **router** is a user-invoked skill that names the other skills and the situations that reach them. It exists to cure cognitive load when the human has too many skills to remember, and it costs no context load.

A router only hints — it can never fire another skill. Use `$name` there: it is written for a human to type. Add one only when the set is genuinely too large to hold in mind; with a small set, the router and the `AGENTS.md` pointer are the same job.

## Cross-skill dependencies

When a skill's step requires another skill, write it as an instruction to load that skill, naming both the skill and its entrypoint:

> Invoke the `noootwo-design` skill: read its `SKILL.md` and follow it.

Naming the mechanism is what gets it fired. A bare `$noootwo-design` left in prose is read as a label, not as a command, so the step quietly does not happen. Inside a `SKILL.md` body this phrasing is mandatory; `$name` belongs only in the router and in human-facing docs.

One skill per instruction. A step needing two skills is two instructions.

## Missing-skill fallback

A skill can be installed alone. When a named skill is missing, follow
`docs/agents/dependency-fallback.md`: try to install it from the published workspace,
and if install fails take the smallest direct fallback and mark the record
`skill-missing: <name>`. Do not silently degrade or impersonate the missing owner.

## The capability bridge

Every capability has exactly one owner. A caller invokes the owner; it never re-implements the capability itself.

### Capability map

| Capability | Owner | Callable by | Returned |
| --- | --- | --- | --- |
| proving the cause of a failure, and bounding the fix to it | `noootwo-debug` | `noootwo-workflow`, `noootwo-product`, `noootwo-design`, `noootwo-review`, `noootwo-state`, `noootwo-research`, `noootwo-onboard` | the evidence chain, the proven cause, the fix scope, the toggle and regression proof, and what remains unproven |
| settling a decision that external evidence decides, and surveying prior art | `noootwo-research` | `noootwo-workflow`, `noootwo-product`, `noootwo-design`, `noootwo-review`, `noootwo-state`, `noootwo-debug`, `noootwo-onboard` | sources with evidence levels, the mechanisms found, applicability and boundaries, counterexamples, and a `deep` brief persisted through `noootwo-state` |
| entering an unfamiliar project and auditing its skill set | `noootwo-onboard` | `noootwo-ask`, `noootwo-workflow`, `noootwo-product` | required, optional, and not-needed skills with triggers; foundation gaps; the smallest unblocking patch |
| settling product decisions | `noootwo-product` | `noootwo-workflow`, `noootwo-design`, `noootwo-review`, `noootwo-state`, `noootwo-debug`, `noootwo-research`, `noootwo-onboard` | settled, delegated, deferred, and rejected decisions, plus the Product-to-Design Handoff |
| turning a settled product path into a reviewed artifact | `noootwo-design` | `noootwo-workflow`, `noootwo-product`, `noootwo-review`, `noootwo-state`, `noootwo-research`, `noootwo-onboard` | Design Read, Design Contract, and an Artifact Review decision against artifact evidence |
| running red-green-refactor and keeping tests honest | `noootwo-tdd` | `noootwo-workflow`, `noootwo-review` | the green test evidence, the minimal implementation, and the behavior-preserving refactor baseline |
| judging the change and keeping code structure healthy, including performance work | `noootwo-review` | `noootwo-workflow`, `noootwo-product`, `noootwo-design`, `noootwo-state`, `noootwo-debug`, `noootwo-research`, `noootwo-onboard` | severity-ordered findings, the lenses applied, evidence read, verification gaps, structural dispositions, and the owning skill for each handoff |
| recording and reading project state/context and choosing storage format | `noootwo-state` | `noootwo-workflow`, `noootwo-product`, `noootwo-design`, `noootwo-tdd`, `noootwo-review`, `noootwo-debug`, `noootwo-research`, `noootwo-onboard` | the stored record, the chosen form and location, the read result, or a recorded decision that nothing changed |
| ordering, scope, stop conditions, and handoffs | `noootwo-workflow` | the human, `noootwo-ask`, and every specialist handing sequencing back: `noootwo-product`, `noootwo-design`, `noootwo-review`, `noootwo-state`, `noootwo-debug`, `noootwo-research`, `noootwo-onboard`, `noootwo-tdd` | mode, sequence, handoffs, and the close report |

A skill body may name a sibling only when that sibling's row lists the caller. Naming a skill is the instruction to load it, so an undeclared name is a call the bridge never authorized. `noootwo-ask` is exempt: it names skills as hints for the human and can never fire one.

### Call contract

- Write a call as one instruction naming the mechanism: invoke the owning skill, read its `SKILL.md`, and follow it. A step needing two skills is two ordered instructions.
- Hand over the minimum: the question or artifact, the evidence already gathered, and the constraint the answer must respect. Do not paste a sibling's method back to it.
- The callee owns its method and its decision. The caller owns order, scope, stop conditions, and the final report.
- The callee returns its own artifact plus what it did not decide. Silence about the boundary is how two skills both claim a decision.
- When the work is not the callee's, it names the failed layer and re-routes in one hop instead of doing the job itself.

### Loop rules

- A callee never calls back the caller for the same decision.
- Re-entry needs new evidence or a genuinely unanswered question; dissatisfaction is not a reason to re-enter.
- One round trip per layer per trigger. A second bounce goes to `noootwo-workflow`'s layer diagnosis, not into another call.
- `noootwo-ask` is never fired by a skill. It exists for the human, and a skill that hints at it wastes the turn.

### Shared material

- A capability's method lives in exactly one place: the owning skill.
- Material that two or more skills need, and that belongs to none of them, lives in a plain file outside the skill system — `docs/agents/` or the repository's `references/` — and each skill points at it.
- A skill body names the loader instruction, never a bare `$name`.
- `scripts/validate_skill_workspace.py` enforces the mechanical half: every skill named in a `SKILL.md` must exist, every public skill must appear in the capability map, every skill named in the map must exist, and every sibling named in a skill body must be listed as a caller in the map row it points at.

## Splitting by invocation

Split off a model-invoked skill when it has a distinct leading word that should trigger it on its own, or when another skill must reach it. That independence costs a permanently loaded description, so it has to be worth it.

Shared reference that two user-invoked skills both need cannot live in either. Put it in a plain file outside the skill system and point both at it.
