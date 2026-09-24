# Noootwo Vibe

Noootwo Vibe is a multi-skill workspace for controlled AI-assisted software development.

It publishes ten focused skills — a router plus nine specialists:

| Skill | Invocation | Purpose | Version |
| --- | --- | --- | --- |
| `noootwo-ask` | user-invoked | Names the right skill for your situation and the order to run them in | `0.2.0` |
| `noootwo-workflow` | model-invoked | Reads current project state, matches the correct installed skill, and schedules one next step at a time | `0.14.0` |
| `noootwo-product` | model-invoked | Settles real user, first loop, scope, main path, states, and acceptance before design or build | `0.9.0` |
| `noootwo-design` | model-invoked | Turns a settled product path into direction, tokens, a Design Contract, and a reviewed artifact | `0.17.0` |
| `noootwo-tdd` | model-invoked | Owns red-green-refactor and test quality for behavior-changing code | `0.3.0` |
| `noootwo-review` | model-invoked | Judges code before it ships, owns the refactoring health loop, optimization review, re-testing, and user acceptance | `0.13.0` |
| `noootwo-state` | model-invoked | Reads and records project state and context, and chooses the storage form | `0.2.0` |
| `noootwo-debug` | model-invoked | Proves the cause of a failure before any fix, and bounds the fix to that cause | `0.2.0` |
| `noootwo-research` | model-invoked | Settles a decision that only outside evidence can settle, and borrows mechanisms instead of surfaces | `0.5.0` |
| `noootwo-onboard` | model-invoked | Enters an unfamiliar project and audits which skills it needs | `0.2.0` |

The repository root is not a published skill. It is the shared workspace for manifests, docs, validation, release helpers, and CI.

## Install

List all skills from the published repository:

```bash
npx -y skills add noootwo/noootwo-vibe --list --full-depth
```

Install all ten skills globally for Codex:

```bash
npx -y skills add noootwo/noootwo-vibe --skill '*' --global --agent codex --yes
```

The command uses the `skills` CLI's standard Agent Skills layout and installs the
ten child skills under `~/.agents/skills/`. Start a new task after installation
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
npx -y skills update noootwo-ask noootwo-workflow noootwo-product noootwo-design noootwo-tdd noootwo-review noootwo-state noootwo-debug noootwo-research noootwo-onboard --global --yes
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
    ├── noootwo-tdd/
    ├── noootwo-review/
    ├── noootwo-state/
    ├── noootwo-debug/
    ├── noootwo-research/
    └── noootwo-onboard/
```

`skills.json` is the source of truth for published child skills, versions, paths, and tag prefixes.

## Skill Responsibilities

`noootwo-ask` is the only user-invoked skill. Type it when you are unsure which skill fits; it names the right one and the order to run them in, at no context cost to the agent.

`noootwo-workflow` is the evidence-driven orchestrator. It reads current repo truth and project state through `noootwo-state`, matches the right owner from the available skill descriptions and artifact shape, and schedules one next step at a time. It owns order, scope, stop conditions, and handoffs; the specialists and matching installed skills own the work. It can invoke other installed skills for slides, documents, or media work without adding them to the Noootwo public set. When the owner is ambiguous or absent, it stops with one or two candidates instead of guessing.

`noootwo-product` settles what should exist before anything is designed or built. It reads discoverable facts itself, names what is unsettled, and then grills the frontier — the questions answerable now — one round at a time, each question carrying options and a recommendation. It ends when the frontier is empty and the user confirms a shared understanding, then produces the Product-to-Design Handoff.

`noootwo-design` turns a settled product path into a visual system. It declares a Design Read, compares directions when style or structure is unresolved, writes a Design Contract before editing, reads the craft floor immediately before building, and reviews the rendered artifact in bounded passes. For `deep` work it captures the references a direction leans on into `.noootwo/references/` with their provenance, extracts real values from a reachable page with its own zero-dependency Chrome extractor, locks the build target, and reports token and motion drift against that baseline afterwards. Motion is a language rather than a field: a personality archetype, a register set by the surface, a millisecond duration scale, an easing catalog, choreography budgets, and per-platform reduced-motion fallbacks. The craft floor also carries an interaction and accessibility gate, a data-presentation matrix, screenshot/design-image intake, a component state matrix, and an asset/performance budget, with Flutter and native equivalents rather than web-only rules. `ready` is never self-certified. When the real user, main path, states, or acceptance turn out to be unsettled, it invokes `noootwo-product`.

`noootwo-tdd` owns the test-first loop for behavior-changing code. It requires a failing test first, the minimal implementation, a full green test command, and refactoring only after green. Red and green are the adding-function hat; the post-green refactor is the refactoring hat, and the two never mix. It rejects production-first, tests-after, manual-test-only, and “too simple to test” reasoning.

`noootwo-review` judges the change and keeps the codebase healthy. It runs after every non-direct behavior change, before a hard implementation as preparatory refactoring, before submit or release, and during a triggered Structure Sweep. It follows Fowler's two hats, six refactoring workflows, small catalog moves, green-baseline safety, and economic payback; every structural finding is fixed, recorded as an opportunity or planned/long-term work, or accepted with a reason. It also owns optimization, re-testing, project health, and the user acceptance gate. Architecture remains a review lens; there is no separate `noootwo-architecture` skill.

`noootwo-state` owns project state and context persistence. It receives an abstract record request, chooses JSON/JSONL for queryable state and Markdown for narrative facts, then writes, validates, and reads the record. Other skills own content; this skill owns the form and location.

`noootwo-debug` turns a symptom into a proven cause before any file changes. It pins expected against actual with the raw failure, reproduces on demand, localizes with numbered checkpoints or bisection, then closes two gates: no edit until the cause is proven and competing hypotheses are refuted by named experiments, and no claim of a fix until a toggle test and a failing-first regression test prove it. It keeps the fix the size of the cause and hands anything larger back to the user as a decision.

`noootwo-research` settles a decision that only outside evidence can settle — a design direction, a stack or library choice, a competitor or user expectation, or prior art. It names the decision and what would flip it, sizes the pass into `quick`, `standard`, or `deep`, draws on domain source pools with an access record and a fallback ladder, extracts transferable mechanisms rather than surfaces, and requires two independent sources plus a counterexample before a claim decides anything. Its pools record what a probe actually observed: which case libraries are free, which need an account, which are paid, which are blocked, and which motion libraries publish a genuine agent-readable index. Every pass also surveys existing skills and public prior art against a four-part adoption gate.

`noootwo-onboard` enters a project you do not know. It reads the nearest evidence, audits which skills the project needs and which it deliberately does not, routes the foundation health judgment to `noootwo-review`'s project-health lens, and adds the single missing file that unblocks the work rather than scaffolding.

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
npx -y skills add ./skills/noootwo-tdd --list
npx -y skills add ./skills/noootwo-review --list
npx -y skills add ./skills/noootwo-state --list
npx -y skills add ./skills/noootwo-debug --list
npx -y skills add ./skills/noootwo-research --list
npx -y skills add ./skills/noootwo-onboard --list
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

- `noootwo-ask@v0.2.0`
- `noootwo-workflow@v0.14.0`
- `noootwo-product@v0.9.0`
- `noootwo-design@v0.17.0`
- `noootwo-tdd@v0.3.0`
- `noootwo-review@v0.13.0`
- `noootwo-state@v0.2.0`
- `noootwo-debug@v0.2.0`
- `noootwo-research@v0.5.0`
- `noootwo-onboard@v0.2.0`

The root `VERSION` records the workspace version only. Do not use it as the release source for child skills.

## Research Basis

This workspace keeps the previous Noootwo Design research-first rule, now owned by `noootwo-research`: design aesthetics, workflow modes, stack playbooks, review gates, stack or library choices, AGENTS integration, and quality claims are grounded in current evidence and validated behavior. Prefer repeatable mechanisms over large prompt text.

The repository-level basis is `references/research-basis.md`. Durable decisions live in `docs/adr/`; skill-specific details live in each skill's direct `references/` files.

## License

MIT
