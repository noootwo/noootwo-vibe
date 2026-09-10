# Noootwo Vibe

Noootwo Vibe is a multi-skill workspace for controlled AI-assisted software development.

It publishes five focused skills:

| Skill | Purpose | Version |
| --- | --- | --- |
| `noootwo-workflow` | Mandatory task-start routing with concrete triggers (feature, product idea, multi-file, bugfix, release, handoff, recovery, rejection loop), lifecycle guardrails, routing-as-invocation to Product/Design/Review/Docs, rework diagnosis, paused interview routing only for unresolved choices, compact handoff packets, project skill audits, foundation checks, planning, and closure | `0.8.0` |
| `noootwo-product` | Adaptive Product Clarity Gate, light single-question interview for one material gap, grilling-style deep Decision Interview with frontier rounds, fact self-serve, fixed question format, decision ledgers, frontier-empty confirmation gate, user-language presentation, product decision layers, greenfield discovery, real-user checkpoints, Product Reality Check, IA/main paths, interaction/state models, acceptance criteria, cognitive-cost review, product choices, and Product-to-Design Handoff | `0.6.0` |
| `noootwo-design` | UI/frontend Design Read, Style Evidence Check, style stability, semantic token contracts, quick polish, `.noootwo/` harness, artifact review, anti-slop hard bans, bounded verification, separated final review, and design handoff after product path clarity | `0.10.0` |
| `noootwo-review` | Tech Lead + QA Architect review, architecture-boundary lens, hard pre-submit/release gates, rework diagnosis, performance review, lean/context-cost review, project-health review, maintainability, and implementation review | `0.8.0` |
| `noootwo-docs` | Documentation state, hard docs-decision trigger for behavior/release/agent changes, docs audits, README/AGENTS/docs layering, product decision persistence, ADRs, context budgets, and release notes | `0.8.0` |

The repository root is not a published skill. It is the shared workspace for manifests, docs, validation, release helpers, and CI.

## Install

List all skills from the published repository:

```bash
npx -y skills add noootwo/noootwo-vibe --list --full-depth
```

Install all five skills globally for Codex:

```bash
npx -y skills add noootwo/noootwo-vibe --skill '*' --global --agent codex --yes
```

The command uses the `skills` CLI's standard Agent Skills layout and installs the
five child skills under `~/.agents/skills/`. Start a new task after installation
so the agent can discover them.

Install one skill:

```bash
npx -y skills add noootwo/noootwo-vibe --global --agent codex --skill noootwo-workflow --yes
```

From a local checkout:

```bash
npx -y skills add /path/to/noootwo-vibe --list --full-depth
npx -y skills add /path/to/noootwo-vibe --skill '*' --global --agent codex --yes
```

Update the globally installed Noootwo skills later with:

```bash
npx -y skills update noootwo-workflow noootwo-product noootwo-design noootwo-review noootwo-docs --global --yes
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

Use `noootwo-workflow` first for a new feature, product idea, multi-file or cross-skill change, bugfix, refactor, release, onboarding or handoff, recovery after repeated failed fixes, or a correction loop after user rejection. It owns lifecycle guardrails for read-first, product/design/review/docs routing, TDD/repro-first, verification, submit, and release decisions while keeping small direct work lightweight. Routing is an invocation: when a specialist trigger matches it explicitly invokes `noootwo-product`, `noootwo-design`, `noootwo-review`, or `noootwo-docs`. It routes product-shaped work to `noootwo-product` Clarity Gate, preserves explicit grill-style/deep-confirmation intent and its handoff ledger, pauses execution only while a material choice awaits an answer, diagnoses the failed layer on rework, then passes Product-to-Design Handoff and style-evidence risk to `noootwo-design` for non-quick UI work.

Use `noootwo-product` when a software product idea, blank-project start, broad product vision, requirements, feature scope, real users, user flows, information architecture, interaction models, onboarding, permissions, states, acceptance criteria, usability, cognitive cost, or product choices need clarification. It first classifies the brief as clear, one material gap, ambiguous/high-risk, or explicitly interview-driven. Clear, detailed requests move directly to the smallest useful artifact or implementation route; only unresolved material choices open an interactive Decision Interview. The interview uses light single questions for one material gap and grilling-style frontier rounds for deep confirmation: it asks every settled-prerequisite question per round with a recommended answer, resolves discoverable facts itself, keeps a decision ledger, and requires an explicit shared-understanding confirmation before handoff. It presents normal responses in the user's language, runs Product Discovery after material choices converge, and produces Product-to-Design Handoff.

Use `noootwo-design` for UI, visual systems, frontend design, screenshots, artifact review, `.noootwo/` deliverables, and design implementation handoff after the product path is clear. Non-quick work declares Design Read and maps design decisions into semantic tokens, component behavior, states, and artifact review paths. If real user, main path, states, acceptance, audience, or use context is still unresolved, route back to `noootwo-product` Decision Interview. High-character or previously rejected style work uses Style Evidence Check before trusting style prose; direction exploration runs only when style or structure is genuinely unresolved. Quick polish stays lightweight and does not require completing the full `.noootwo/` harness.

Use `noootwo-review` when code quality, pre-submit review, performance review, lean/context-cost review, over-engineering, dependency bloat, project health, refactoring, test strategy, architecture hygiene, or maintainability risk matters. It also flags broad skill triggers, fixed question lists, or default gates that make small tasks too expensive. Architecture remains a review lens here; there is no separate `noootwo-architecture` skill.

Use `noootwo-docs` when a change affects project state, user-facing instructions, repository layout, documentation audits, product decisions, ADRs, release notes, or agent instructions.

## Validation

Run the workspace validator:

```bash
python scripts/validate_skill_workspace.py .
```

Sync local installed skill copies when iterating locally:

```bash
python scripts/sync_local_install.py --no-dedupe-codex
python scripts/sync_local_install.py --target-root ~/.codex/skills --no-dedupe-codex
```

The default sync target is `~/.agents/skills`. When a synced Noootwo skill exists there, the script removes the same `noootwo-*` skill from `~/.codex/skills` so Codex does not show duplicate local skills.
For non-default targets, pass `--dedupe-codex` to apply the same duplicate cleanup.
For release batches that must keep both agent roots current, use `--no-dedupe-codex` and sync both roots explicitly.

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

Run opt-in high-risk design eval scenarios only when their prompt applies:

```bash
python skills/noootwo-design/scripts/eval_noootwo_artifacts.py <project> --scenario style-prose-without-visual-evidence
python skills/noootwo-design/scripts/eval_noootwo_artifacts.py <project> --scenario visual-direction-implemented-as-default-ui
```

## Release Model

Each child skill has its own `VERSION` file and tag prefix:

- `noootwo-workflow@v0.8.0`
- `noootwo-product@v0.6.0`
- `noootwo-design@v0.10.0`
- `noootwo-review@v0.8.0`
- `noootwo-docs@v0.8.0`

The root `VERSION` records the workspace version only. Do not use it as the release source for child skills.

## Research Basis

This workspace keeps the previous Noootwo Design research-first rule: workflow, design, documentation, review gates, AGENTS integration, and quality claims should be grounded in current evidence and validated behavior. Prefer repeatable mechanisms over large prompt text.

The repository-level basis is `references/research-basis.md`. Durable decisions live in `docs/adr/`; skill-specific details live in each skill's direct `references/` files.

## License

MIT
