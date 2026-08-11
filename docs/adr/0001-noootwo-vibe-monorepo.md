# ADR 0001: Use noootwo-vibe as a multi-skill workspace

- Status: accepted
- Date: 2026-07-03

## Context

The original repository published Noootwo Design as a single root skill and later added design-related child skills. The initial Noootwo Vibe direction was a broader software-development skill family with four public skills: workflow, docs, review, and design. ADR 0005 later added `noootwo-product` as the fifth public skill. The `skills` CLI discovers only the root skill when a root `SKILL.md` exists, but discovers child skills by default when the root skill is absent.

## Decision

Rename the repository to `noootwo-vibe` and make the root a monorepo shell. Publish child skills under `skills/` only. The current public skill set is `noootwo-workflow`, `noootwo-product`, `noootwo-design`, `noootwo-review`, and `noootwo-docs`. Preserve former design subskill responsibilities as internal Noootwo Design modes and references instead of separate public skills.

## Consequences

- Aggregate install/discovery can show all five skills without requiring `--full-depth` when the repository default branch contains the multi-skill workspace.
- Each child skill can be installed and released independently.
- Root documentation and validation must stay accurate because root no longer carries a `SKILL.md` compatibility surface.
- Noootwo Design must carry its own references, scripts, assets, and evals so it remains independently publishable.
