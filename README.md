# Noootwo Vibe

Noootwo Vibe is a multi-skill workspace for controlled AI-assisted software development.

It publishes four focused skills:

| Skill | Purpose | Version |
| --- | --- | --- |
| `noootwo-workflow` | AI workflow control, task routing, planning, execution sequencing, and closure | `0.2.0` |
| `noootwo-docs` | Documentation state, README/AGENTS/docs layering, ADRs, and release notes | `0.2.0` |
| `noootwo-review` | Code quality, maintainability, refactoring discipline, and implementation review | `0.2.0` |
| `noootwo-design` | Research-backed UI/design workflow, `.noootwo/` harness, artifact review, and design handoff | `0.1.18` |

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

Use `noootwo-workflow` first when the task is broad, multi-step, release-bound, or needs routing. It decides when to bring in the other Noootwo skills.

Use `noootwo-docs` when a change affects project state, user-facing instructions, repository layout, ADRs, release notes, or agent instructions.

Use `noootwo-review` when code quality, refactoring, test strategy, architecture hygiene, or maintainability risk matters.

Use `noootwo-design` for UI, visual systems, frontend design, screenshots, artifact review, `.noootwo/` deliverables, and design implementation handoff.

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

## Release Model

Each child skill has its own `VERSION` file and tag prefix:

- `noootwo-workflow@v0.2.0`
- `noootwo-docs@v0.2.0`
- `noootwo-review@v0.2.0`
- `noootwo-design@v0.1.18`

The root `VERSION` records the workspace version only. Do not use it as the release source for child skills.

## Research Basis

This workspace keeps the previous Noootwo Design research-first rule: workflow, design, documentation, review gates, AGENTS integration, and quality claims should be grounded in current evidence and validated behavior. Prefer repeatable mechanisms over large prompt text.

The repository-level basis is `references/research-basis.md`. Durable decisions live in `docs/adr/`; skill-specific details live in each skill's direct `references/` files.

## License

MIT
