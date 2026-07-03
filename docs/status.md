# Project Status

- Repository: `noootwo/noootwo-vibe`
- Branch model: feature work on `codex/*`, default branch `main`
- Public skill set: `noootwo-workflow`, `noootwo-docs`, `noootwo-review`, `noootwo-design`
- Release model: independently versioned child skills listed in `skills.json`
- Root `SKILL.md`: intentionally absent so default skill discovery lists all child skills

## Current Validation Surface

Last verified: 2026-07-03 on `codex/noootwo-vibe-monorepo` after the non-design skill `v0.2.0` optimization pass.

- `python scripts/validate_skill_workspace.py .`
- `npx -y skills add . --list`
- `npx -y skills add . --list --full-depth`
- per-skill `npx -y skills add ./skills/<skill> --list`
- Noootwo Design harness checks under `skills/noootwo-design/scripts/`

Latest result: all workspace, aggregate discovery, per-skill discovery, Python compile, skill quick validation, and design harness bootstrap checks passed. The fresh pending design harness correctly remains non-ready until workflow fields are completed.

## Active Risks

- GitHub plugin-style ingestion is treated as packaging metadata; `skills` CLI discovery is the verified installation surface.
- `noootwo-design` contains the previous design workflow and must remain self-contained for single-skill publishing.
- Workflow/docs/review `v0.2.0` should stay concise at the entry point and keep deeper guidance in direct references.

## Next Actions

- Run full validation after every skill layout or metadata change.
- Update `docs/releases/` and per-skill tags when publishing changed skills.
