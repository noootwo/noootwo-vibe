# Workflow Playbook

Use this only when the task is broad enough that a short direct path is not enough.

## Contents

- Practice Basis
- Project Entry
- Lifecycle Guardrails
- Alignment Checkpoint
- Routing Matrix
- Work Size
- Mode Details
- Default Loop
- Handoff Packet Templates
- Cost Controls
- Stop Conditions

## Practice Basis

- Mature process skills use hard gates, red flags, and completion evidence instead of vague encouragement.
- Agent skill guidance favors progressive disclosure: keep the entry file short and load deeper references only when useful.
- Modern delivery practice favors small batches, clear ownership, and fresh verification over large speculative plans.
- High-friction process lowers real usage. Add control only where it prevents a likely wrong decision, missed verification, or expensive rework.

## Project Entry

Use onboarding mode before normal execution when the project is unfamiliar, under-documented, or being taken over from another agent:

1. Run `project-skill-audit.md` to decide required Noootwo skills and optional local skills from repo evidence.
2. Run `project-foundation-check.md` if the project lacks obvious operating instructions, validation commands, release policy, or current state.
3. If gaps block safe work, use `minimal-foundation-templates.md` through `$noootwo-docs` to add the smallest useful file or section.
4. Continue with direct, planned, diagnostic, release, or recovery mode.

## Lifecycle Guardrails

Use guardrails at development, close, submit, release, and handoff points. They are required judgments, not required ceremony. Small direct work can pass them internally; non-trivial, submit-bound, or release-bound work should show a short result.

### Read-First Guard

Decide what repo truth must be checked before acting:

- `minimal`: current file, changed-file context, and nearest instructions
- `project`: `AGENTS.md`, README, active `docs/status.md`, package/build metadata, and nearest tests
- `decision`: ADRs, specs, release notes, public contracts, migrations, or design artifacts

Do not run a full doc crawl for small local edits. Do not skip source-of-truth docs when behavior, public usage, release, architecture, or handoff state can drift.

### Pre-Implementation Guard

Before editing, decide:

- whether an alignment checkpoint is needed
- whether TDD or repro-first is required
- which specialist skill owns product, design, docs, review, or release evidence
- what command or scenario will prove the change

Use TDD or repro-first when the task is a bugfix, behavior change, public interface change, regression risk, data/migration risk, or hard-to-prove shared code. If no practical test exists, record the manual scenario or verification gap before editing.

### During-Work Guard

Work in slices when the change is medium or larger:

- keep each slice independently reviewable and testable
- avoid new abstractions or dependencies unless current evidence requires them
- reroute to `$noootwo-product` when the real user, feature scope, interaction path, state model, or acceptance criteria becomes unclear
- update docs through `$noootwo-docs` when implementation changes user-visible behavior, state, release facts, or agent instructions
- reroute to `$noootwo-review` when code shape, dependency shape, or context cost becomes the risk

### Pre-Close / Pre-Submit Guard

Before finishing, committing, releasing, or handing off code changes, check:

- closest meaningful verification ran or the gap is explicit
- docs/status/ADR/release notes were updated or intentionally unchanged
- `$noootwo-product` checked product acceptance when user-visible behavior changed and the product path was unclear or newly defined
- `$noootwo-review` ran for submit-bound or release-bound code
- `$noootwo-design` reviewed UI/artifact quality when visual behavior changed

For small diffs, run a narrow self-review and directly fix local issues. For medium, broad, or risky diffs, run a structured review gate. Ask the user only when the fix would expand scope, alter product behavior, introduce a larger refactor, or choose between real tradeoffs.

Short output shape when visible:

```markdown
Lifecycle Guardrails
- Read first: files or docs checked.
- TDD/repro: used | not needed | gap recorded.
- Verification: command or scenario.
- Docs: updated | not affected | routed.
- Product: checked | not needed | routed.
- Review: self-review | structured gate | not needed for non-code.
```

## Alignment Checkpoint

Use this when a high-impact decision is unresolved and code inspection cannot decide it alone. It is intentionally smaller than a plan.

Trigger examples:

- unclear goal priority, success criteria, non-goal, real user, feature scope, or user path
- architecture boundary: which module, package, API, data store, or public contract owns the change
- release or migration risk
- design direction, artifact form, or review path
- missing verification path for a non-trivial change

Do not trigger for:

- one-file direct edits with an obvious check
- docs copy fixes that do not change project state
- local polish that preserves an existing UI direction
- decisions already made in AGENTS, status docs, ADRs, specs, or the user's latest message

Output shape:

```markdown
Alignment Checkpoint
- Repo truth checked: files/commands inspected.
- Decision: one question that changes implementation.
- Options: 2-3 choices with one recommended default.
- Outcome: user chose | user delegated to agent | no question needed.
```

If the user is unavailable and the risk is acceptable, proceed with the recommended default and list it as an assumption. If the wrong answer could cause migration, release, data, security, or product-direction damage, stop for the decision.

If the unresolved decision is product-shaped, use `$noootwo-product` for a Product Choice Challenge: real user, should/should-not build scope, main path, cognitive cost, states, and acceptance criteria.

## Routing Matrix

| Signal | Route |
| --- | --- |
| unfamiliar project, missing process foundation, unclear skill needs | `$noootwo-workflow` onboarding mode |
| requirements, feature scope, user flow, IA, interaction model, onboarding, permissions, states, acceptance criteria, confusion risk | `$noootwo-product` |
| UI, visual hierarchy, screenshots, `.noootwo/` | `$noootwo-design` |
| README, AGENTS, docs, ADR, status, release notes | `$noootwo-docs` |
| refactor, maintainability, architecture, code review | `$noootwo-review` |
| multi-step coordination, sequencing, release flow | `$noootwo-workflow` |
| bug, failing check, surprising runtime behavior | `$noootwo-workflow` diagnostic mode first, then specialist |

## Work Size

- `small`: one narrow file or behavior, existing tests/checks are clear.
- `medium`: several files, public behavior changes, docs likely affected.
- `large`: repo structure, release, migration, architecture, or multiple skills.

Small work can proceed directly after inspection. Medium work needs a short plan. Large work needs staged checkpoints and explicit validation.

## Mode Details

### Direct

Use for one narrow behavior or doc fix. State the file, change, and check. Avoid adding a multi-step plan unless uncertainty appears.

### Planned

Use for multi-file behavior, repo structure, public usage, or cross-skill work. Keep the plan short enough to fit in working memory:

- objective
- affected files/modules
- risks and non-goals
- execution slices
- verification commands
- docs/review/release handoffs

### Diagnostic

Use for test failures, bugs, regressions, broken installs, or unexpected behavior. Do not fix before identifying evidence:

- observed symptom and command/output
- reproduction path
- recent changes or likely boundary
- working comparison if one exists
- single hypothesis to test
- verifying command for the fix

### Release

Use when changing versions, tags, remotes, CI, local installs, or published packages. Always list:

- version source files
- manifests and README/docs that mirror versions
- validation commands
- tag names and conflict check
- install/sync target
- remote push evidence

### Onboarding

Use for unfamiliar repositories, missing process foundation, or skill-selection uncertainty. Output a short audit before implementation:

- required Noootwo skills and why
- optional local skills and exact triggers
- missing or weak foundation files
- minimal patch plan and owner skill
- skills or process that are intentionally not needed

### Recovery

Use after prior agent drift, repeated failed fixes, unclear half-finished work, or context compaction. First reconstruct current state from files, git, commands, and artifacts. Treat summaries as hints, not proof.

## Default Loop

1. Run lifecycle guardrails at the lightest useful level.
2. Inspect repo truth before deciding.
3. If skill needs or foundation are unclear, audit them before planning.
4. Run an alignment checkpoint only when one unresolved decision can change the work.
5. State the smallest viable path.
6. Implement in slices that can be tested independently.
7. Run the closest meaningful checks after each risky slice.
8. Route to `$noootwo-product` before design or implementation when the real user, product scope, main path, states, or acceptance criteria are unclear.
9. Update docs through `$noootwo-docs` when behavior, state, usage, product decision, or release changes.
10. Use `$noootwo-review` before submit/release for code changes, and for broad code structure, project-health gaps, architecture boundaries, or context-cost risk.
11. Before closing non-direct work, answer: verified, TDD/repro considered, docs affected, product/design/review needed.

## Handoff Packet Templates

### To `$noootwo-docs`

- Changed fact:
- Owning layer suspected:
- Files/commands touched:
- Validation or release evidence:
- Known stale docs to check:

### To `$noootwo-review`

- Behavior or structure changed:
- Files and nearest tests:
- Risk class:
- Verification command:
- Specific judgment requested:

### To `$noootwo-product`

- Real user or suspected user:
- User outcome:
- Unclear product choice:
- Current flow or artifact evidence:
- Acceptance or state question:

### To `$noootwo-design`

- UI/artifact surface:
- Product checkpoint or delegated product assumption:
- Current design evidence:
- Direction uncertainty:
- Reviewable artifact path:
- Implementation boundary:

## Cost Controls

- Load only files needed for the current slice.
- Prefer manifests, status files, and focused references over reading long docs.
- Do not paste large reference material into plans or summaries.
- Do not introduce new gates unless they prevent a repeated failure.
- Collapse repeated status into a single status file instead of rewriting the same fact in README, AGENTS, and release notes.
- Keep lifecycle guardrails as short decisions; only show them when the task, submit, release, or handoff risk justifies visibility.
- Prefer one short alignment checkpoint over a long intake form.
- Prefer one Product Choice Challenge over a full PRD unless the user asks for the larger artifact.

## Stop Conditions

Stop and ask or reroute when:

- a high-impact product or architecture choice is unresolved
- the verification path is missing and cannot be inferred
- the change would alter public behavior beyond the user's request
- three fix attempts reveal new problems in different places
- the work needs a specialist skill and continuing here would duplicate that skill
