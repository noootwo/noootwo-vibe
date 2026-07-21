# Docs Layering

Use this when a change affects more than one documentation layer.

## Practice Basis

- Diataxis separates documentation by user need: learning, solving a task, looking up facts, and understanding decisions.
- ADR practice keeps durable architectural decisions short, dated, and separate from operational logs.
- Agent-facing docs work best when always-on files stay small and route to deeper references instead of duplicating them.
- Large-context agent work stays cheaper when hot files are snapshots and indexes, while long evidence is found through local search and read in slices.

## Ownership Rules

| File or directory | Owns | Does not own |
| --- | --- | --- |
| `README.md` | stable project purpose, install, skill list, basic usage | current task log, detailed architecture history |
| `AGENTS.md` | short always-on agent rules and routing | full skill bodies, long playbooks |
| `docs/status.md` | current state, active risks, latest validation status, active product decisions, next actions | durable decisions, historical release notes, completed risks, work diaries |
| `docs/adr/` | architecture/workflow/product role-boundary decisions and consequences | operational checklists |
| `docs/guides/` | repeatable procedures | API/schema reference |
| `docs/reference/` | commands, manifests, schema, stable facts | narrative tutorials |
| `docs/releases/` | versioned release and migration notes | current active work |

## Fact Classifier

Use this classifier before editing:

| Fact type | Owning layer |
| --- | --- |
| What the project is and how to install/use it | `README.md` |
| What agents must always know before acting | `AGENTS.md` |
| What is true right now but may change soon, including active product choices | `docs/status.md` |
| Why a durable product, architecture, or workflow decision exists | `docs/adr/` |
| How to repeat a workflow | `docs/guides/` |
| Exact fields, commands, manifests, schemas | `docs/reference/` |
| What changed in a version and how to migrate | `docs/releases/` |
| Raw research, old process notes, long logs, or historical evidence | cold storage, archive, or deletion |

If a fact seems to belong in several places, pick one owner and link from the others only when discovery would otherwise fail.

## First Adoption Flow

When a project has weak or missing documentation foundation, add the smallest durable set before writing detailed guides:

1. `AGENTS.md`: always-on repo rules and skill routing only.
2. `docs/status.md`: current state, latest validation entry, active risks, next actions.
3. First ADR: durable repo/workflow decision that explains why the foundation exists.
4. Release notes or release guide: only if versioning, publishing, or install flow is in scope.
5. README update: stable purpose, install/run, and links to the owning layers.

If the repo already uses equivalent locations, map to those responsibilities instead of forcing these names.

## Update Pattern

1. Identify the changed fact.
2. Search for existing claims about the same fact.
3. Put the new truth in exactly one owning layer.
4. Add links from other layers only when discoverability requires it.
5. Remove or revise stale claims in older layers.
6. Record validation evidence for release or status claims.
7. If the destination is a hot file, keep the update within its budget or move detail to an on-demand layer.

## Change-To-Docs Matrix

| Change | Check |
| --- | --- |
| Command, script, install path, CLI behavior | README, guides, reference |
| Repo/package/skill layout | README, AGENTS, ADR, status |
| Version, tag, release, local install | release notes, status, manifest reference |
| Product, architecture, or workflow decision | ADR, status if currently active |
| Agent behavior or routing | AGENTS, skill body, relevant reference |
| Public API, schema, manifest field | reference docs, release notes if user-visible |
| Project foundation or skill audit | AGENTS, status, ADR, guide only if repeated |
| Old validation runs, completed risks, historical task notes | release notes, ADR, archive, or delete from status |

## Status Budget

`docs/status.md` is a current-state snapshot. Target 120 lines or fewer and treat 200 lines as a hard stop: compress or move facts before adding more.

Keep only:

- current repository or product state
- latest validation evidence with date or command
- active risks that still affect next work
- next actions

Move old version changes to `docs/releases/`, durable decisions to `docs/adr/`, repeated steps to `docs/guides/` or `docs/reference/`, and raw research or process history out of the hot path.

## Stale-Doc Cleanup

When changing docs, also scan nearby files for:

- old repository names, package names, and URLs
- obsolete commands or paths
- version numbers copied outside the manifest or release notes
- planned language that now describes shipped behavior
- validation claims without a command or date
- duplicated instructions that should route to a skill or guide
- project state facts copied into README instead of status
- Product Checkpoints copied into multiple places instead of one owning layer
- status documents that keep completed risks, old validation runs, or chronological work diaries

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

## Quality Gate

Before handoff, verify:

- every changed fact has one owner
- volatile state is not in README or AGENTS
- durable decisions are not only in status or chat
- install/release commands were checked or clearly marked unverified
- stale references from the old state were removed or intentionally retained with a migration note
- first-adoption docs were kept minimal instead of generating a full handbook
- hot files stayed within budget or were split before new detail was added
