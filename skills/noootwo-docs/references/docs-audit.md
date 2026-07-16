# Docs Audit

Use this when documentation may be missing, stale, duplicated, in the wrong layer, or making claims without evidence.

## Defect Categories

| Category | Meaning | Typical fix |
| --- | --- | --- |
| `missing` | a required fact or file is absent | add the smallest owning file/section |
| `stale` | docs contradict current files, commands, versions, or behavior | update or remove the old claim |
| `duplicated` | same fact is maintained in multiple places | keep one owner and link if needed |
| `wrong layer` | fact exists but in a document with the wrong responsibility | move to README/AGENTS/status/ADR/guide/reference/release owner |
| `unverified claim` | docs claim validation, readiness, release, or support without fresh evidence | add command/date/result or soften the claim |

## Audit Steps

1. Read the changed files and nearest docs that mention the same facts.
2. Classify each defect with one category.
3. Identify the owning layer using `docs-layering.md`.
4. Fix the owner first; update other layers only with links or short route hints.
5. Remove stale duplicates during the same pass.
6. Record validation claims with command, date, and result.

## Output Contract

```markdown
Docs Audit

Defects
- [missing|stale|duplicated|wrong layer|unverified claim] file: fact; impact; fix.

Owner Map
- fact -> owning layer.

Patch Plan
- file: minimal update.

Verification
- command/date/result, or `not verified` with reason.
```

## Workflow Interface

- `$noootwo-workflow` discovers process gaps and asks for docs placement.
- `$noootwo-product` may produce stable product decisions, user flows, states, or acceptance criteria that need one owning documentation layer.
- `$noootwo-docs` writes or cleans the documentation source of truth.
- `$noootwo-review` may report duplicated facts or unverified claims as project defects; docs fixes them without taking over code review.

## Red Flags

- Updating README because it is visible when status, ADR, guide, or release notes own the fact.
- Copying the same command list into README, AGENTS, and reference docs.
- Recording temporary progress as a durable decision.
- Leaving old version numbers in examples after a manifest/version bump.
- Claiming "validated", "ready", or "released" without a command or external evidence.
