# Minimal Foundation Templates

Use these only after `project-foundation-check.md` finds a real gap. Keep additions short and repo-specific.

## AGENTS Routing Section

```markdown
## Skill Routing

- Use `$noootwo-workflow` for task routing, project flow, release sequencing, and handoff closure.
- Use `$noootwo-docs` for README, AGENTS, docs/status, ADRs, guides, references, and release notes.
- Use `$noootwo-review` for maintainability, test strategy, refactoring, code review, and project-health defects.
- Use `$noootwo-design` for UI/design artifacts, screenshots, visual systems, and design handoff.
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

## Release Guide

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
- tag/push/sync install target if applicable
```

## Validation Checklist

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
- Prefer one missing file that unblocks the current project.
- Mark unknown facts as `unknown`, not invented certainty.
- Route content placement to `$noootwo-docs` before writing multi-layer docs.
