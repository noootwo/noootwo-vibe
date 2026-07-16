# Project Foundation Check

Use this when a project lacks clear operating instructions, when taking over an existing repo, or before broad AI-assisted development.

## Practice Basis

The check follows lightweight delivery practice: small batches, visible validation, clear ownership, and documentation that routes to deeper material instead of duplicating it.

## Audit Surface

| Area | Look for | Healthy enough |
| --- | --- | --- |
| Agent entry | `AGENTS.md` or equivalent | short always-on rules, skill routing, repo-specific constraints |
| Public usage | README | purpose, install/run basics, validation entrypoint |
| Current state | `docs/status.md` or equivalent | active state, risks, last validation, next actions |
| Decisions | `docs/adr/` or decision log | durable workflow/architecture choices separated from status |
| Releases | release notes or changelog | version history, migration notes, tag/publish model |
| Validation | scripts/package commands | one command or clear list that proves core health |
| Tests | test command/config | closest meaningful tests are discoverable |
| CI | `.github/workflows/` or equivalent | at least validates install/build/test/release-relevant checks |
| Run/preview | README or guide | how to start or inspect the project locally |
| Versions | manifest/version files | source of truth and release policy are explicit |
| Risks | status/review docs/issues | known gaps are visible, not hidden in chat |

## Classification

- `present`: exists and is usable.
- `weak`: exists but lacks an owner, command, date, or trigger.
- `missing`: absent.
- `stale`: contradicts current files, commands, or versions.
- `out of scope`: not needed for this project type now.

## Output Contract

```markdown
Foundation Check

Healthy
- item: evidence.

Gaps
- [missing|weak|stale] item: impact; owner skill; minimal fix.

Verification Entry
- command or missing path.

Recommended Minimal Patch
- file: one sentence describing the smallest useful addition.

Do Not Add
- heavy scaffold or process that lacks a current trigger.
```

## Ownership

- `$noootwo-workflow` owns the audit, routing order, and gap plan.
- `$noootwo-product` owns product path, real-user scope, states, and acceptance questions when the work depends on them.
- `$noootwo-design` owns design-specific harness and artifact readiness only when design work exists.
- `$noootwo-review` owns project-health defects tied to testability, maintainability, architecture boundaries, reviewability, release risk, and context cost.
- `$noootwo-docs` owns writing facts into README, AGENTS, status, ADRs, guides, references, and release notes.

## Stop Conditions

Ask or pause before creating process files when:

- the repo has a strong existing convention with different names
- adding files would conflict with framework tooling or package publishing
- the user asked for analysis only
- the missing foundation is not blocking the current change
