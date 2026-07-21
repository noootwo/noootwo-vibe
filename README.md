# Noootwo Vibe

Noootwo Vibe is a multi-skill workspace for controlled AI-assisted software development.

It publishes five focused skills:

| Skill | Purpose | Version |
| --- | --- | --- |
| `noootwo-workflow` | AI workflow control, lifecycle guardrails, specialist-first routing, product-to-design handoff routing, project skill audits, foundation checks, task routing, planning, and closure | `0.7.3` |
| `noootwo-product` | Product decision layers, greenfield discovery, real-user checkpoints, IA/main paths, interaction/state models, acceptance criteria, cognitive-cost review, product choices, and Product-to-Design Handoff | `0.3.0` |
| `noootwo-design` | UI/frontend Design Read, style stability, semantic token contracts, quick polish, `.noootwo/` harness, artifact review, anti-slop checks, and design handoff | `0.8.0` |
| `noootwo-review` | Tech Lead + QA Architect review, architecture-boundary lens, pre-submit gates, performance review, lean review, project-health review, maintainability, and implementation review | `0.7.0` |
| `noootwo-docs` | Documentation state, docs audits, README/AGENTS/docs layering, product decision persistence, ADRs, context budgets, and release notes | `0.7.0` |

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
    ├── noootwo-product/
    ├── noootwo-design/
    ├── noootwo-review/
    └── noootwo-docs/
```

`skills.json` is the source of truth for published child skills, versions, paths, and tag prefixes.

## Skill Responsibilities

Use `noootwo-workflow` first when the task is broad, multi-step, release-bound, needs routing, or needs a project skill/foundation audit. It owns lifecycle guardrails for read-first, product/design/review/docs routing, TDD/repro-first, verification, submit, and release decisions while keeping small direct work lightweight. It routes greenfield product ideas and blank-project product starts to `noootwo-product`, then passes Product-to-Design Handoff to `noootwo-design` for non-quick UI work.

Use `noootwo-product` when a software product idea, blank-project start, broad product vision, requirements, feature scope, real users, user flows, information architecture, interaction models, onboarding, permissions, states, acceptance criteria, usability, cognitive cost, or product choices need clarification. It can run Product Discovery, challenge the request with 2-3 product options, converge on a recommended first loop, and produce Product-to-Design Handoff.

Use `noootwo-design` for UI, visual systems, frontend design, screenshots, artifact review, `.noootwo/` deliverables, and design implementation handoff after the product path is clear. Non-quick work declares Design Read and maps design decisions into semantic tokens, component behavior, states, and artifact review paths. Quick polish stays lightweight and does not require completing the full `.noootwo/` harness.

Use `noootwo-review` when code quality, pre-submit review, performance review, lean review, over-engineering, dependency bloat, project health, refactoring, test strategy, architecture hygiene, or maintainability risk matters. Architecture remains a review lens here; there is no separate `noootwo-architecture` skill.

Use `noootwo-docs` when a change affects project state, user-facing instructions, repository layout, documentation audits, product decisions, ADRs, release notes, or agent instructions.

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

The default sync target is `~/.agents/skills`. When a synced Noootwo skill exists there, the script removes the same `noootwo-*` skill from `~/.codex/skills` so Codex does not show duplicate local skills.
For non-default targets, pass `--dedupe-codex` to apply the same duplicate cleanup.

Run discovery checks:

```bash
npx -y skills add . --list
npx -y skills add . --list --full-depth
npx -y skills add ./skills/noootwo-workflow --list
npx -y skills add ./skills/noootwo-product --list
npx -y skills add ./skills/noootwo-design --list
npx -y skills add ./skills/noootwo-review --list
npx -y skills add ./skills/noootwo-docs --list
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

- `noootwo-workflow@v0.7.3`
- `noootwo-product@v0.3.0`
- `noootwo-design@v0.8.0`
- `noootwo-review@v0.7.0`
- `noootwo-docs@v0.7.0`

The root `VERSION` records the workspace version only. Do not use it as the release source for child skills.

## Research Basis

This workspace keeps the previous Noootwo Design research-first rule: workflow, design, documentation, review gates, AGENTS integration, and quality claims should be grounded in current evidence and validated behavior. Prefer repeatable mechanisms over large prompt text.

The repository-level basis is `references/research-basis.md`. Durable decisions live in `docs/adr/`; skill-specific details live in each skill's direct `references/` files.

## License

MIT
