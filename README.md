# Noootwo Vibe

Noootwo Vibe is a multi-skill workspace for controlled AI-assisted software development.

It publishes six focused skills — a router plus five specialists:

| Skill | Invocation | Purpose | Version |
| --- | --- | --- | --- |
| `noootwo-ask` | user-invoked | Names the right skill for your situation and the order to run them in | `0.1.0` |
| `noootwo-workflow` | model-invoked | Runs one multi-step task through a controlled loop and invokes the other skills at each trigger | `0.9.0` |
| `noootwo-product` | model-invoked | Settles real user, first loop, scope, main path, states, and acceptance before design or build | `0.7.0` |
| `noootwo-design` | model-invoked | Turns a settled product path into direction, tokens, a Design Contract, and a reviewed artifact | `0.11.0` |
| `noootwo-review` | model-invoked | Judges code before it ships, and diagnoses which layer failed when work is rejected | `0.9.0` |
| `noootwo-docs` | model-invoked | Places each changed fact in its owning documentation layer | `0.9.0` |

The repository root is not a published skill. It is the shared workspace for manifests, docs, validation, release helpers, and CI.

## Install

List all skills from the published repository:

```bash
npx -y skills add noootwo/noootwo-vibe --list --full-depth
```

Install all six skills globally for Codex:

```bash
npx -y skills add noootwo/noootwo-vibe --skill '*' --global --agent codex --yes
```

The command uses the `skills` CLI's standard Agent Skills layout and installs the
six child skills under `~/.agents/skills/`. Start a new task after installation
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
npx -y skills update noootwo-ask noootwo-workflow noootwo-product noootwo-design noootwo-review noootwo-docs --global --yes
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
│   ├── agents/          # skill authoring and invocation standards
│   ├── experiments/     # recorded behaviour measurement
│   ├── guides/
│   ├── reference/
│   ├── releases/
│   └── status.md
├── scripts/
│   ├── sync_local_install.py
│   └── validate_skill_workspace.py
├── skills.json
└── skills/
    ├── noootwo-ask/
    ├── noootwo-workflow/
    ├── noootwo-product/
    ├── noootwo-design/
    ├── noootwo-review/
    └── noootwo-docs/
```

`skills.json` is the source of truth for published child skills, versions, paths, and tag prefixes.

## Skill Responsibilities

`noootwo-ask` is the only user-invoked skill. Type it when you are unsure which skill fits; it names the right one and the order to run them in, at no context cost to the agent.

`noootwo-workflow` runs one multi-step task — a feature, a cross-file change, a bug, a refactor, a release, a handoff, or rework after a rejected fix. It reads the nearest repo truth, picks a mode, and invokes the specialist that owns each trigger: `noootwo-product` when product decisions are unsettled, `noootwo-design` for UI work, `noootwo-review` before submit or release, and `noootwo-docs` when facts changed. While a product decision is unsettled the loop stops until a shared understanding is confirmed.

`noootwo-product` settles what should exist before anything is designed or built. It reads discoverable facts itself, names what is unsettled, and then grills the frontier — the questions answerable now — one round at a time, each question carrying options and a recommendation. It ends when the frontier is empty and the user confirms a shared understanding, then produces the Product-to-Design Handoff.

`noootwo-design` turns a settled product path into a visual system. It declares a Design Read, compares directions when style or structure is unresolved, writes a Design Contract before editing, reads the craft floor immediately before building, and reviews the rendered artifact in bounded passes. `ready` is never self-certified. When the real user, main path, states, or acceptance turn out to be unsettled, it invokes `noootwo-product`.

`noootwo-review` judges code before it ships and diagnoses rework. It selects lenses — correctness, testability, architecture boundary, lean, performance, project health, release readiness, rework diagnosis — and leads with findings ordered by severity. Architecture remains a review lens; there is no separate `noootwo-architecture` skill.

`noootwo-docs` places each changed fact in its owning layer — README, AGENTS, status, ADR, guide, reference, experiment, or release notes — and removes the stale version in the same pass. A change to behaviour, state, release facts, or agent instructions needs a docs decision before the work is closed.

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
npx -y skills add ./skills/noootwo-ask --list
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

- `noootwo-ask@v0.1.0`
- `noootwo-workflow@v0.9.0`
- `noootwo-product@v0.7.0`
- `noootwo-design@v0.11.0`
- `noootwo-review@v0.9.0`
- `noootwo-docs@v0.9.0`

The root `VERSION` records the workspace version only. Do not use it as the release source for child skills.

## Research Basis

This workspace keeps the previous Noootwo Design research-first rule: workflow, design, documentation, review gates, AGENTS integration, and quality claims should be grounded in current evidence and validated behavior. Prefer repeatable mechanisms over large prompt text.

The repository-level basis is `references/research-basis.md`. Durable decisions live in `docs/adr/`; skill-specific details live in each skill's direct `references/` files.

## License

MIT
