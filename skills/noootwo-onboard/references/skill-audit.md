# Skill Audit

Use this when entering an unfamiliar project, starting a broad change, or deciding which skills should govern the work.

## Goal

Produce a compact routing map from project facts, not from generic preference. The audit says which Noootwo skills are required, which local mature skills are optional, what triggers each one, and which skills are not needed now.

## Inputs

Inspect the nearest evidence first:

- `AGENTS.md`, README, `docs/status.md`, ADRs, release notes
- package/build files, CI workflows, scripts, test commands
- current changed files, issue or request text, recent git history
- the installed skill list from the session; if absent, inspect `~/.agents/skills/` and `~/.codex/skills/` names only, before loading any skill body

Do not load every skill. Load a skill body only after a project fact makes it relevant.

The signals below are written for a software repository. For another kind of project, read the same responsibilities from that project's equivalents: what changes, how a change is verified, and who owns the record.

## Noootwo skill decision table

| Signal | Skill | Trigger |
| --- | --- | --- |
| broad task, unclear sequence, release, takeover, rework after a rejected fix | `$noootwo-workflow` | schedule the work: order, scope, stop conditions, handoffs |
| something broken, failing, flaky, or a reproducible failure with an unknown cause | `$noootwo-debug` | prove the cause before any fix, and bound the fix to it |
| a decision blocked by something only outside evidence can settle — a direction, a stack or library choice, a competitor or user expectation | `$noootwo-research` | settle it with sourced evidence, then record the confidence |
| entering an unfamiliar repository, or deciding which skills a project needs | `$noootwo-onboard` | audit the skill set and route the foundation health judgment |
| greenfield product idea, blank-project start, broad product vision, or unclear real user, first loop, scope, main path, states, acceptance | `$noootwo-product` | settle the product path with the smallest artifact |
| requirements, feature scope, user flow, IA, interaction model, permissions, states, acceptance criteria, confusion risk | `$noootwo-product` | clarify the product path and challenge high-impact choices |
| UI, screenshots, visual system, `.noootwo/`, design handoff | `$noootwo-design` | declare the Design Read, contract the design, review the artifact |
| code structure, refactor, tests, maintainability, architecture, performance and optimization work, AI-generated code risk | `$noootwo-review` | classify defects and judge before submit or release |
| docs, status, README, AGENTS, ADR, or release facts changed or drifted | `$noootwo-docs` | place facts in the owning layer and remove stale claims |

## Local skill scan

Treat local skills as specialists, not as a checklist. Candidate categories:

- framework and runtime skills when package files prove the stack
- testing, debugging, and performance skills when failures, missing tests, flaky checks, or a budget appear
- git, release, and CI skills when branch, tag, PR, or publishing is in scope
- document, presentation, PDF, and spreadsheet skills when binary or structured office files are in scope
- design and frontend-audit skills only when UI evidence exists

Name an optional local skill only with a trigger, for example: `vitest` when the repo has Vitest config and tests change; `systematic-debugging` when a failure reproduces but the cause is unknown.

## Output contract

```markdown
Skill Audit

Required Noootwo Skills
- `$skill`: why needed; trigger; first file or evidence to inspect.

Optional Local Skills
- `skill-name`: why useful; trigger; load only if the condition appears.

Not Needed Now
- `skill-name`: reason it is out of scope.

Foundation
- owned by `$noootwo-review` project-health lens: findings, evidence, gaps.

Routing Order
1. ...
2. ...
```

## Red flags

- Listing every installed skill without evidence.
- Loading many skill bodies before reading project files.
- Treating `$noootwo-design` as a general frontend code-quality review skill.
- Letting `$noootwo-design` define feature scope or user paths that `$noootwo-product` should settle first.
- Letting generic brainstorming own product discovery when `$noootwo-product` should find the first user and first loop.
- Letting `$noootwo-review` write docs instead of handing defects to `$noootwo-docs`.
- Running a bug fix here instead of routing to `$noootwo-debug`.
- Adding a new public skill before proving a stable, repeated trigger.
