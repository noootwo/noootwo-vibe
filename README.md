# Noootwo Vibe

Noootwo Vibe is a multi-skill workspace for controlled AI-assisted software development.

It publishes four focused skills:

| Skill | Purpose | Version |
| --- | --- | --- |
| `noootwo-workflow` | AI workflow control, lifecycle guardrails, alignment checkpoints, project skill audits, foundation checks, task routing, planning, and closure | `0.6.1` |
| `noootwo-docs` | Documentation state, docs audits, README/AGENTS/docs layering, ADRs, and release notes | `0.5.0` |
| `noootwo-review` | Lens-based code quality, pre-submit review gates, performance review, lean review, project-health review, maintainability, refactoring discipline, and implementation review | `0.6.1` |
| `noootwo-design` | Research-backed UI/design workflow, lightweight quick polish, `.noootwo/` harness, color-system calibration, artifact review, and design handoff | `0.6.0` |

The repository root is not a published skill. It is the shared workspace for manifests, docs, validation, release helpers, and CI.

## Install

List all skills from the published repository:

```bash
npx skills add noootwo/noootwo-vibe --list
```

Install all public skills globally:

```bash
npx skills add noootwo/noootwo-vibe -g -y
```

Install one skill:

```bash
npx skills add noootwo/noootwo-vibe -g --skill noootwo-workflow -y
```

From a local checkout:

```bash
npx skills add /path/to/noootwo-vibe --list
npx skills add /path/to/noootwo-vibe -g --skill noootwo-design -y
```

Single-skill local checks are also supported:

```bash
npx skills add ./skills/noootwo-design --list
```

## Layout

```text
.
├── .codex-plugin/plugin.json
├── AGENTS.md
├── README.md
├── VERSION
├── docs/
│   ├── adr/
│   ├── guides/
│   ├── reference/
│   ├── releases/
│   └── status.md
├── references/
├── scripts/
│   ├── sync_local_install.py
│   └── validate_skill_workspace.py
├── skills.json
└── skills/
    ├── noootwo-workflow/
    ├── noootwo-docs/
    ├── noootwo-review/
    └── noootwo-design/
```

`skills.json` is the source of truth for published child skills, versions, paths, and tag prefixes.

## Skill Responsibilities

Use `noootwo-workflow` first when the task is broad, multi-step, release-bound, needs routing, or needs a project skill/foundation audit. It owns lifecycle guardrails for read-first, TDD/repro-first, verification, docs, review, submit, and release decisions while keeping small direct work lightweight.

Use `noootwo-docs` when a change affects project state, user-facing instructions, repository layout, documentation audits, ADRs, release notes, or agent instructions.

Use `noootwo-review` when code quality, pre-submit review, performance review, lean review, over-engineering, dependency bloat, project health, refactoring, test strategy, architecture hygiene, or maintainability risk matters. It selects relevant review lenses instead of turning every review into a full audit.

Use `noootwo-design` for UI, visual systems, frontend design, screenshots, artifact review, `.noootwo/` deliverables, and design implementation handoff. Quick polish stays lightweight and does not require completing the full `.noootwo/` harness.

## Validation

Run the workspace validator:

```bash
python scripts/validate_skill_workspace.py .
```

Sync local installed skill copies when iterating locally:

```bash
python scripts/sync_local_install.py --skill noootwo-workflow
python scripts/sync_local_install.py
```

Run discovery checks:

```bash
npx -y skills add . --list
npx -y skills add . --list --full-depth
npx -y skills add ./skills/noootwo-workflow --list
npx -y skills add ./skills/noootwo-docs --list
npx -y skills add ./skills/noootwo-review --list
npx -y skills add ./skills/noootwo-design --list
```

Validate the design harness after changes to `noootwo-design`:

```bash
tmpdir="$(mktemp -d)"
python skills/noootwo-design/scripts/bootstrap_noootwo_harness.py "$tmpdir" --profile full
if python skills/noootwo-design/scripts/validate_noootwo_readiness.py "$tmpdir" --allow-non-ready; then
  echo "Expected pending bootstrap harness to fail readiness validation"
  exit 1
fi
```

The readiness command is expected to fail on a freshly bootstrapped pending harness unless it is used inside a completed design workflow.
This is a skill-workspace validation check, not a requirement for every quick UI polish task.

## Release Model

Each child skill has its own `VERSION` file and tag prefix:

- `noootwo-workflow@v0.6.1`
- `noootwo-docs@v0.5.0`
- `noootwo-review@v0.6.1`
- `noootwo-design@v0.6.0`

The root `VERSION` records the workspace version only. Do not use it as the release source for child skills.

## Research Basis

This workspace keeps the previous Noootwo Design research-first rule: workflow, design, documentation, review gates, AGENTS integration, and quality claims should be grounded in current evidence and validated behavior. Prefer repeatable mechanisms over large prompt text.

The repository-level basis is `references/research-basis.md`. Durable decisions live in `docs/adr/`; skill-specific details live in each skill's direct `references/` files.

## License

MIT
