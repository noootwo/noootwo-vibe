# Project Status

- Repository: `noootwo/noootwo-vibe`
- Branch model: feature work on `codex/*`, default branch `main`
- Public skill set: `noootwo-workflow`, `noootwo-docs`, `noootwo-review`, `noootwo-design`
- Release model: independently versioned child skills listed in `skills.json`
- Root `SKILL.md`: intentionally absent so default skill discovery lists all child skills

## Current Validation Surface

Last verified: 2026-07-03 on `codex/noootwo-vibe-monorepo` after aligning all public skills to `v0.3.0`.

- `python scripts/validate_skill_workspace.py .`
- `npx -y skills add . --list`
- `npx -y skills add . --list --full-depth`
- per-skill `npx -y skills add ./skills/<skill> --list`
- `python /Users/notwo/.codex/skills/.system/skill-creator/scripts/quick_validate.py skills/<skill>`
- temporary incomplete-project simulation for workflow/docs/review audit contracts
- Noootwo Design harness checks under `skills/noootwo-design/scripts/`

Latest result: workspace validation and aggregate/design discovery passed after aligning `noootwo-design` to `0.3.0`. The earlier v0.3.0 governance pass also passed full-depth discovery, per-skill discovery, Python compile, skill quick validation, incomplete-project audit contract, and design harness bootstrap checks.

## Active Risks

- GitHub plugin-style ingestion is treated as packaging metadata; `skills` CLI discovery is the verified installation surface.
- `noootwo-design` contains the previous design workflow and must remain self-contained for single-skill publishing.
- Workflow/docs/review `v0.3.0` should stay concise at the entry point and keep project-governance guidance in direct references.
- The new project audit templates should stay minimal; do not turn them into automatic full scaffolding without evidence from repeated use.

## Next Actions

- Run full validation after every skill layout or metadata change.
- Update `docs/releases/` and per-skill tags when publishing changed skills.
