# Minimal Foundation Templates

Use these only after the project-health review names a real gap. Keep additions short and repo-specific.

The default file names below assume a software repository. In another kind of project, keep the responsibility and let the file name follow the project — an agent entry is still the always-on instruction file, the status document is still the one place that states current state and risk, and the release guide is still how a new version is produced. Map by responsibility rather than forcing this layout, and record the mapping in the agent entry file.

## AGENTS routing section

```markdown
## Skill Routing

- Use `$noootwo-workflow` to schedule multi-step work: order, scope, stop conditions, handoffs.
- Use `$noootwo-product` to settle the real user, first loop, scope, states, and acceptance before design or build.
- Use `$noootwo-design` for UI, visual, artifact, and frontend work once the product path is settled.
- Use `$noootwo-debug` when something is broken, failing, flaky, or wrong: prove the cause before fixing.
- Use `$noootwo-research` when a decision needs outside evidence: a direction, a stack or library, a market expectation.
- Use `$noootwo-code-health` to judge code before it ships, including performance and optimization work.
- Use `$noootwo-state` to place changed facts in the owning layer.
- Use `$noootwo-onboard` when entering an unfamiliar repository or deciding which skills it needs.
```

Add only repo-specific constraints below this section.

## `docs/status.md`

```markdown
# Project Status

- Repository:
- Branch model:
- Runtime/package manager:
- Validation entry:
- Release model:

## Current State

- Last verified: YYYY-MM-DD, command/result.
- Active work:

## Risks

- risk: impact; owner; next check.

## Next Actions

- action:
```

## Initial ADR

```markdown
# ADR 0001: Title

- Status: accepted
- Date: YYYY-MM-DD

## Context

## Decision

## Consequences
```

Use ADRs for durable choices, not task logs.

## Release guide

```markdown
# Releasing

## Version Sources

- file:

## Validation

- `command`

## Publish

- `command`

## After Release

- update release notes
- tag/push/sync the install target if applicable
```

## Validation checklist

```markdown
# Validation

- Core: `command`
- Tests: `command`
- Lint/type/build: `command`
- Discovery/install, if applicable: `command`
- Manual artifact review, if applicable: path or screenshot
```

## Guardrails

- Do not generate every template by default.
- Prefer the one missing file that unblocks the current project.
- Mark unknown facts as `unknown`, not invented certainty.
- Route content placement to `$noootwo-state` before writing multi-layer docs.
