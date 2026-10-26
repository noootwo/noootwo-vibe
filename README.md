# Noootwo Vibe

Noootwo Vibe is a multi-skill workspace for controlled AI-assisted software development.

It publishes eleven focused skills — a router plus ten specialists:

| Skill | Invocation | Purpose | Version |
| --- | --- | --- | --- |
| `noootwo-ask` | user-invoked | Names the right skill for your situation and the order to run them in | `0.6.1` |
| `noootwo-workflow` | model-invoked | Chooses read depth, loads one owner at a time, and schedules shape-before-implementation, scoped Change Checks, Release Verification Ledger handoffs, and the full Release Check | `0.21.0` |
| `noootwo-product` | model-invoked | Settles real user, first loop, scope, main path, states, and acceptance before design or build | `0.12.0` |
| `noootwo-design` | model-invoked | Turns a settled product path into a contextual visual intervention, tokens, a Design Contract, and a reviewed artifact | `0.20.0` |
| `noootwo-tdd` | model-invoked | Owns red-green-refactor and relevant-test evidence for behavior-changing code | `0.6.1` |
| `noootwo-code-health` | model-invoked | Shapes a non-obvious change, runs a scoped Change Check after each requirement, and a full Release Check before release | `0.18.0` |
| `noootwo-release` | model-invoked | Owns the Release Verification Ledger, Release Check consumption, versioning, tags, immutable artifacts, deployment traces, provenance, rollback, and release health | `0.3.1` |
| `noootwo-state` | model-invoked | Reads and records project state and context, produces bounded capsules, inspects files, captures cold evidence, and chooses the storage form and owning layer | `0.4.0` |
| `noootwo-debug` | model-invoked | Confirms claims with layer-appropriate evidence, proves a failure's cause, bounds the fix, and closes systemically | `0.6.1` |
| `noootwo-research` | model-invoked | Settles a decision that only outside evidence can settle, and borrows mechanisms instead of surfaces | `0.7.1` |
| `noootwo-onboard` | model-invoked | Enters an unfamiliar project, audits context health and the skills it needs | `0.5.0` |

The repository root is not a published skill. It is the shared workspace for manifests, docs, validation, release helpers, and CI.

## Context Budget

The eleven skills share one lifecycle: `write -> select -> compress -> isolate -> verify`. It does not add a twelfth skill; `noootwo-workflow` chooses reading depth and `noootwo-state` owns the bounded read view and evidence handles.

- `direct` work reads the current file context, not project state.
- `resume` reads a context capsule, current commit/worktree, and at most three frontier entry points.
- `decision/evidence` work reads only the ADRs, specs, release records, contracts, or local evidence that can settle the step.
- References above about 200 lines are entered through headings or query hits. Live excerpts stay at 80 lines or fewer. Raw output above 16 KiB goes to cold evidence first; the hot context carries its path and hash.
- One writer owns dependent changes. Only independent read-only research or review is isolated to a subagent.
- After compaction or when the goal changes, the capsule is checked against the current commit, worktree, and latest evidence. An unrelated new goal after completion gets a new-session recommendation unless the user explicitly continues.

Useful state reads:

```bash
skills/noootwo-state/scripts/noootwo-state.sh capsule
skills/noootwo-state/scripts/noootwo-state.sh inspect docs/status.md --query release
skills/noootwo-state/scripts/noootwo-state.sh capture --name failing-check -- npm test
python3 skills/noootwo-state/scripts/audit_codex_context.py --cwd "$PWD" --since 2026-10-01 --json
```

The capsule is a read view, never a new source of truth. Append-only events and cold evidence remain the history. The design and evidence boundary are recorded in [ADR 0024](docs/adr/0024-bounded-context-lifecycle.md) and [the context-cost research brief](docs/reference/context-cost.md).

## Install

List all skills from the published repository:

```bash
npx -y skills add noootwo/noootwo-vibe --list --full-depth
```

Install all eleven skills globally for Codex:

```bash
npx -y skills add noootwo/noootwo-vibe --skill '*' --global --agent codex --yes
```

The command uses the `skills` CLI's standard Agent Skills layout and installs the
eleven child skills under `~/.agents/skills/`. Start a new task after installation
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
npx -y skills update noootwo-ask noootwo-workflow noootwo-product noootwo-design noootwo-tdd noootwo-code-health noootwo-release noootwo-state noootwo-debug noootwo-research noootwo-onboard --global --yes
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
    ├── noootwo-code-health/
    ├── noootwo-release/
    ├── noootwo-state/
    ├── noootwo-debug/
    ├── noootwo-research/
    └── noootwo-onboard/
```

`skills.json` is the source of truth for published child skills, versions, paths, and tag prefixes.

## Skill Responsibilities

`noootwo-ask` is the only user-invoked skill. Type it when you are unsure which skill fits; it names the right one and the order to run them in, at no context cost to the agent.

`noootwo-workflow` is the evidence-driven orchestrator. It chooses `direct`, `resume`, or `decision/evidence` reading depth, verifies a restored capsule against the current commit and worktree, matches the right owner from available skill descriptions and artifact shape, and schedules one next step at a time. It treats a named current spec, ADR, issue, or evidence record as an authority rather than a reason to re-run its authoring skill, and loads at most one specialist body before evidence. Plan-only work receives one bounded identifier search and no preloaded downstream owners. It owns order, verification depth, scope, stop conditions, and handoffs; the specialists and matching installed skills own the work. It records state only when the goal, decision, blocker, evidence, or next trigger changes, and recommends a new session for an unrelated goal after completion. A request to confirm several suspected problems goes to `noootwo-debug`'s Diagnosis Map, with independent claims and a read-only verdict before any fix. For a non-obvious code change, it schedules `noootwo-code-health` to shape the seam before `noootwo-tdd`; an obvious local edit skips that pass. After one requirement, code-health runs a Change Check scoped to the diff and blast radius; before release, it runs one Release Check with the full suite or CI evidence, a full Structure Sweep, and release evidence. Once a plan is approved, reversible ambiguities are decided from the spec, plan, and evidence, recorded as rulings with their error cost and reopen trigger, and continued. User-owned decisions, irreversible changes, security or privacy impact, external side effects or spend, and plan invalidation still stop. A newly discovered release-bound check or gap is routed to `noootwo-release` for the Release Verification Ledger instead of being carried as every requirement's full audit. It can invoke other installed skills for slides, documents, or media work without adding them to the Noootwo public set. When the owner is ambiguous or absent, it stops with one or two candidates instead of guessing.

`noootwo-product` settles what should exist before anything is designed or built. It reads discoverable facts itself, names what is unsettled, and then grills the frontier — the questions answerable now — one round at a time, each question carrying options and a recommendation. An unresolved first round starts from observed facts and proposals stated separately, then asks one controlling question or all independent root questions together. It records user-owned how decisions separately from agent defaults, including each default's reason and reopen condition. It ends when the frontier is empty and the user confirms a shared understanding, then produces the Product-to-Design Handoff.

`noootwo-design` turns a settled product path into a contextual visual intervention. It declares a Design Read, decides whether the exact feature and moment should `leave simple`, use `craft only`, or `add moment`, and only then considers motion, shaders, sound, or haptics. A candidate must pass frequency, purpose, speed, and function gates before source research or a new tool starts; rejected opportunities stay visible. When a direction choice remains materially unresolved, it presents real low-cost samples rather than a prose menu, and the user chooses after seeing them. `leave simple` and `craft only` remain valid outcomes when the product needs clarity or speed, but an explicit user request for motion or material defaults to `add moment` and cannot be silently downgraded. The implementation must name its tool and trigger; an installed or user-named library or shader is selected, replaced by a recorded equivalent, or rejected with a concrete reason. The skill writes a Design Contract before editing, reads the craft floor immediately before building, and reviews the rendered artifact in bounded passes. Deep references prefer the target medium and must have been inspected; broken captures are not evidence. Repeated aesthetic patterns are evidence flags, while accessibility, readability, real content, state integrity, and interaction recovery remain hard gates. For `deep` work it also extracts real values from a reachable page with its zero-dependency Chrome extractor, locks the build target, and reports drift against that baseline afterwards. When an authored moment is selected, motion is a language rather than a field: personality, register, millisecond scale, easing, choreography, and reduced-motion fallback. `ready` is never self-certified. When the real user, main path, states, or acceptance turn out to be unsettled, it invokes `noootwo-product`.

`noootwo-tdd` owns the test-first loop for behavior-changing code. It requires a failing test first, the minimal implementation, relevant-test proof, and refactoring only after green. Red and green are the adding-function hat; the post-green refactor is the refactoring hat, and the two never mix. The full suite is a Release Check, not the TDD exit. When the implementation shape or seam is unsettled, it returns to workflow instead of inventing architecture inside the loop. It rejects production-first, tests-after, manual-test-only, and “too simple to test” reasoning.

`noootwo-code-health` keeps code elegant and healthy in two passes. Before implementation, when a change's seam or integration is non-obvious, it runs an Integration Read and produces a compact Change Shape: seam and ownership, contracts, reuse, reversibility, test seam, smallest first slice, and rejected alternatives. It skips that pass for an obvious local change with no contract, data, or migration impact. A non-obvious, cross-session, expensive, or cross-boundary handoff gets a conditional Builder Check; a closed local plan goes directly to TDD. Decision-complete plans record file scope, interfaces, ordered steps, observable assertions, verification, review focus, and a ruling ledger. After one requirement, it runs a Change Check on the current diff, changed behavior, nearest callers, affected tests, and one to three lenses; it escalates only when blast radius requires it. Before release, it runs one Release Check with the full suite or CI evidence, a full Structure Sweep, release evidence, and named gaps. It follows Fowler's two hats, six refactoring workflows, small catalog moves, green-baseline safety, and economic payback, and disposes of every structural finding as fixed, opportunity, planned, long-term, or accepted. It also owns optimization, re-testing, project health, and the user acceptance gate. Architecture and integration design remain code-health lenses; there is no separate `noootwo-architecture` skill.

`noootwo-release` owns release engineering. It turns a ready change into an identified, immutable release: version source and compatibility, tag semantics, artifact identity and provenance, changelog and release notes, deployment markers, rollback or forward-fix, and release health by version. It keeps one Release Verification Ledger for checks that must be decided at the release boundary, dedupes them by evidence boundary, consumes each once through the Release Check, and seals the result into the release record. It persists release facts through `noootwo-state` and uses existing CI or deployment tools as execution resources without binding the suite to one vendor. The append-only Release Ledger remains the release-identity history; the verification ledger is the open queue that feeds it.

`noootwo-state` owns project state and context persistence. It receives an abstract record request, chooses JSON/JSONL for queryable state and Markdown for narrative facts, then writes, validates, and reads the record. Its capsule is a bounded 80-line/6,000-character re-entry view with source hash and evidence handles; `inspect` returns metadata, headings, and local hits instead of dumping long files; `capture` writes complete command output to cold evidence and returns only status, hash, path, and a bounded tail. The optional Codex audit reports aggregate token, compaction, and tool-output cost without emitting message content. Append-only history and state/event schemas stay authoritative and unchanged. Other skills own content; this skill owns the form and location.

`noootwo-debug` turns a claim into a verdict before any file changes. Every request starts with a Diagnosis Map: each claim gets a problem class, the evidence authority that can settle it, one decisive check, a terminal status, a stop bound, and a handoff. Product decisions, official protocol evidence, runnable code paths, live deployment state, data state, and agent transcripts are not interchangeable; confirmation stays read-only, and a long report never upgrades an uncertain status. If a mapped row is a reproducible failure, it expands into the Incident Path: expected versus actual, reproduce, localize with checkpoints, prove the cause, bound the fix, then prove it with a toggle and failing-first regression test. After the fix it writes a Systemic Close covering sibling and near-miss paths, the recurrence barrier and owner, and the learning loop. Larger structural work is handed to the owning skill instead of expanded inside the fix.

`noootwo-research` settles a decision that only outside evidence can settle — a design direction, a stack or library choice, a competitor or user expectation, or prior art. It names the decision and what would flip it, sizes the pass into `quick`, `standard`, or `deep`, draws on domain source pools with an access record and a fallback ladder, extracts transferable mechanisms rather than surfaces, and requires two independent sources plus a counterexample before a claim decides anything. Live runtime, configuration, and deployment state are observations for the owning evidence skill, not research findings. Its pools record what a probe actually observed: which case libraries are free, which need an account, which are paid, which are blocked, and which motion libraries publish a genuine agent-readable index. Every pass also surveys existing skills and public prior art against a four-part adoption gate.

`noootwo-onboard` enters a project you do not know. It reads the nearest evidence, audits context health for whole-read entrypoints, long-file retrieval routes, stale skill names, status timelines, and missing short-term state, then audits which skills the project needs and which it deliberately does not. It routes the foundation health judgment to `noootwo-code-health`'s project-health lens, routes a missing release path to `noootwo-release`, and adds the smallest AGENTS/status/state adapter that unblocks the work rather than scaffolding. Existing history is preserved.

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
npx -y skills add ./skills/noootwo-code-health --list
npx -y skills add ./skills/noootwo-release --list
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
python skills/noootwo-design/scripts/eval_noootwo_artifacts.py <project> --scenario leave-simple-justified
python skills/noootwo-design/scripts/eval_noootwo_artifacts.py <project> --scenario craft-only-justified
python skills/noootwo-design/scripts/eval_noootwo_artifacts.py <project> --scenario add-moment-proof
python skills/noootwo-design/scripts/eval_noootwo_artifacts.py <project> --scenario explicit-motion-request-honored
```

## Release Model

Each child skill has its own `VERSION` file and tag prefix:

- `noootwo-ask@v0.6.1`
- `noootwo-workflow@v0.21.0`
- `noootwo-product@v0.12.0`
- `noootwo-design@v0.20.0`
- `noootwo-tdd@v0.6.1`
- `noootwo-code-health@v0.18.0`
- `noootwo-release@v0.3.1`
- `noootwo-state@v0.4.0`
- `noootwo-debug@v0.6.1`
- `noootwo-research@v0.7.1`
- `noootwo-onboard@v0.5.0`

The root `VERSION` records the workspace version only. Do not use it as the release source for child skills.

## Research Basis

This workspace keeps the previous Noootwo Design research-first rule, now owned by `noootwo-research`: design aesthetics, workflow modes, stack playbooks, review gates, stack or library choices, AGENTS integration, and quality claims are grounded in current evidence and validated behavior. Prefer repeatable mechanisms over large prompt text.

The repository-level basis is `references/research-basis.md`. Durable decisions live in `docs/adr/`; skill-specific details live in each skill's direct `references/` files.

## License

MIT
