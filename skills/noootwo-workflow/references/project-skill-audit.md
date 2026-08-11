# Project Skill Audit

Use this when entering an unfamiliar project, starting a broad change, or deciding which skills should govern the work.

## Goal

Produce a compact routing map from project facts, not from generic preference. The audit should say which Noootwo skills are required, which local mature skills are optional, what triggers each one, and which skills are not needed now.

## Inputs

Inspect only the nearest evidence first:

- `AGENTS.md`, README, `docs/status.md`, ADRs, release notes
- package/build files, CI workflows, scripts, test commands
- current changed files, issue/request text, recent git history
- session-provided installed skill list; if absent, inspect `~/.agents/skills/` and `~/.codex/skills/` names only before loading any skill body

Do not load every skill. Load a skill body only after a project fact makes it relevant.

## Noootwo Skill Decision Table

| Signal | Required skill | Trigger |
| --- | --- | --- |
| broad task, unclear sequence, release, takeover, missing process foundation | `$noootwo-workflow` | route, plan, audit, and close the loop |
| greenfield software product idea, blank-project product start, broad product vision, product brainstorming | `$noootwo-product` | run Clarity Gate; interview only for a material gap, otherwise emit the smallest useful product artifact |
| requirements, feature scope, real user, user flow, IA, interaction model, onboarding, permissions, states, acceptance criteria, confusion risk | `$noootwo-product` | clarify product path and challenge high-impact choices |
| UI, screenshots, visual system, `.noootwo/`, design handoff | `$noootwo-design` | inspect artifacts and design workflow evidence |
| code structure, refactor, tests, maintainability, architecture, AI-generated code risk | `$noootwo-review` | classify code/project defects and propose smallest fix |
| docs/status/README/AGENTS/ADR/release facts change or drift | `$noootwo-docs` | place facts in the right layer and remove stale claims |

## Local Skill Scan

Treat local skills as specialists, not as a checklist. Candidate categories:

- framework/runtime skills when package files prove the stack
- testing/debugging skills when failures, missing tests, or flaky checks appear
- git/release skills when branch, tag, PR, CI, or publishing is in scope
- document/presentation/pdf/spreadsheet skills when binary or structured office files are in scope
- design/polish/audit frontend skills only when UI evidence exists

Name an optional local skill only with a trigger, for example: `vitest` if the repo has Vitest config and test changes; `systematic-debugging` if a failure is reproducible but root cause is unknown.

## Output Contract

```markdown
Skill Audit

Required Noootwo Skills
- `$skill`: why needed; trigger; first file/evidence to inspect.

Optional Local Skills
- `skill-name`: why useful; trigger; load only if condition appears.

Not Needed Now
- `skill-name`: reason it is out of scope.

Missing Foundation
- item: impact; owner skill; minimal next step.

Routing Order
1. `$noootwo-workflow` ...
2. `$noootwo-product` / `$noootwo-design` / `$noootwo-review` / `$noootwo-docs` ...
```

## Red Flags

- Listing every installed skill without evidence.
- Loading many skill bodies before reading project files.
- Treating `$noootwo-design` as a general frontend code-quality review skill.
- Letting `$noootwo-design` define feature scope or user paths when `$noootwo-product` should clarify them first.
- Letting generic brainstorming own product discovery when `$noootwo-product` should identify the first user, first loop, and validation signal.
- Letting `$noootwo-review` write docs instead of handing defects to `$noootwo-docs`.
- Adding a new public Noootwo skill before proving a stable repeated trigger.
