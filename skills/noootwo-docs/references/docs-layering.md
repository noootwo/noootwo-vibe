# Docs Layering

Use this when a change affects more than one documentation layer.

## Ownership Rules

| File or directory | Owns | Does not own |
| --- | --- | --- |
| `README.md` | stable project purpose, install, skill list, basic usage | current task log, detailed architecture history |
| `AGENTS.md` | short always-on agent rules and routing | full skill bodies, long playbooks |
| `docs/status.md` | current state, active risks, validation status | durable decisions, historical release notes |
| `docs/adr/` | architecture/workflow decisions and consequences | operational checklists |
| `docs/guides/` | repeatable procedures | API/schema reference |
| `docs/reference/` | commands, manifests, schema, stable facts | narrative tutorials |
| `docs/releases/` | versioned release and migration notes | current active work |

## Update Pattern

1. Identify the changed fact.
2. Put it in exactly one owning layer.
3. Add links from other layers only when discoverability requires it.
4. Remove or revise stale claims in older layers.
5. Record validation evidence for release or status claims.

## ADR Template

```markdown
# ADR NNN: Title

- Status: proposed | accepted | superseded
- Date: YYYY-MM-DD

## Context

## Decision

## Consequences
```

Keep ADRs short. They explain why a durable choice exists; they are not implementation diaries.
