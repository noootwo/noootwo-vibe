# Noootwo Design

Type once, get a design worth shipping.

Noootwo Design is an open skill for UI design, frontend design, app-screen design, visual redesign, design-system extraction, artifact review, screenshot critique, token mapping, and implementation handoff.

Current version: `v0.1.17`
Version source: repository tag plus the root `VERSION` file.

## What It Does

- Helps agents choose the right workflow mode: `adopt-project`, `quick`, `standard`, `deep`, `production`, `extract-system`, or `review`
- Routes by task structure: change magnitude, direction uncertainty, implementation commitment, artifact verifiability, and system continuity
- Establishes durable `.noootwo/` design system memory before substantial UI work
- Writes design systems and selected directions as structured design contracts with layout grammar, type rules, color roles, component vocabulary, verification paths, and return actions
- Captures baseline context when adopted into an existing project midway through development
- Externalizes unresolved uncertainty instead of hiding it in the model's internal reasoning
- Explores 3 directions when useful, then blocks implementation until the user selects a direction or delegates the choice
- Stops for user decisions whenever a high-impact ambiguity can materially change the result
- Captures the selected direction in an approved design contract before implementation
- Requires an implementation plan before non-quick UI file edits
- Uses stage roles and agentic style discovery for deep high-character design work
- Uses optional influence discovery to find designer, artist, studio, product, movement, or spatial-system mechanisms without copying signature style
- Preserves the discovered style through an explicit translation contract so the direction survives tokens, components, motion, and handoff
- Adds an optional detail-translation pass for implementation-stage drift: surface inventory, component restyling, default overrides, and micro-detail review
- Mines product flows, design systems, curated galleries, domestic fallback sources, and community signals, then transfers mechanisms instead of copying surfaces
- Requires artifact, typography, and responsive evidence before calling non-trivial design work ready
- Keeps high-cost deep workflow limited to high-end, niche, brand-heavy, or major redesign tasks
- Maps approved design decisions into reusable design tokens and stack-specific implementation notes
- Produces handoff only after artifact evidence, readiness checks, or an explicit limitation is recorded

## Install

This repository currently supports two installation shapes:

- `single-skill compatibility`: install the root `SKILL.md` exactly as before
- `multi-skill plugin skeleton`: the repository also contains a `.codex-plugin/` manifest plus `skills/` child skills for front-door routing, style discovery, design review, and detail translation

The single-skill path is the stable default today.

The plugin skeleton is architectural groundwork, not the default verified install contract yet. On this repository's current validation path, `npx skills add . --list` still discovers one root skill from the repo checkout, and the local Codex CLI verified during this refactor was `codex-cli 0.116.0`, which did not expose a usable `codex plugin add/list` flow in the shell. Until that changes, treat the root `SKILL.md` as the release surface and the plugin skeleton as the internal expansion path.

From a published repository:

```bash
npx skills add noootwo/noootwo-design -g -y
```

From a local checkout:

```bash
npx skills add /path/to/noootwo-design -g -y
```

To sync the latest repo state into the local installed skill copy used by Codex/Cursor-style workflows today, update the installed directory under `~/.agents/skills/noootwo-design/`.

## Plugin Skeleton

The repository now includes a multi-skill plugin skeleton:

- `.codex-plugin/plugin.json`
- `skills/noootwo-design/`
- `skills/noootwo-style-discovery/`
- `skills/noootwo-design-review/`
- `skills/noootwo-detail-translation/`

These child skills share the same root-level `references/`, `scripts/`, `assets/`, and `evals/` directories instead of duplicating them. This is the intended expansion path for future artifact-specific skills such as poster or slides.

Current status:

- `verified now`: the skeleton validates structurally inside this repository
- `not yet verified as the default local install path`: multi-skill plugin ingestion from this repo checkout in the current local Codex CLI
- `recommended compatibility strategy`: keep the root `SKILL.md` as the stable front door until plugin installation and discovery are verified end-to-end

Current responsibility split:

- `noootwo-design`
  Front-door workflow and task routing
- `noootwo-style-discovery`
  Research-heavy direction discovery and mechanism transfer
- `noootwo-design-review`
  Artifact critique, defect diagnosis, and return-action decisions
- `noootwo-detail-translation`
  Late-stage implementation preservation and anti-default drift

The root `SKILL.md` remains in place as the compatibility entrypoint for environments that still install the repository as a single skill.

Do not split by surface keyword alone. Future poster, slides, or other graphic-design additions should become child skills only when they represent a stable workflow/artifact contract that differs materially from the core UI workflow.

## Split Criteria

Keep behavior in the root front-door skill when the task still shares the same:

- task-classification logic
- direction and decision protocol
- design-contract shape
- implementation gate
- artifact-review loop

Create a child skill only when the specialization introduces a durable, reusable contract that changes how the work must be produced or reviewed. In practice, that means most of the following should be true:

- the artifact form changes materially
- the evidence or review surface changes materially
- the return-action map changes materially
- the implementation or export constraints change materially
- the specialization is reusable across many topics, not tied to one theme or industry prompt

Good split examples:

- `poster` if the work needs fixed-canvas composition, export-ready assets, print or bleed rules, and poster-specific hierarchy/review checks
- `presentation/slides` if the work needs slide masters, deck narrative flow, speaker or presenter context, and slide-by-slide review rules
- `other graphic-design artifacts` when they require their own artifact grammar rather than the core UI artifact loop

Bad split examples:

- `tcm-poster`, `campaign-page`, `flutter-page`, or other topic/stack labels that do not create a different workflow contract by themselves

## Shared Core

To keep child skills lightweight and consistent, the plugin root should remain the shared core for:

- task classification and blocking rules
- decision protocol and delegated-choice rules
- direction brainstorm requirements
- `.noootwo/` templates and workflow closure
- readiness validation and eval prompts
- research protocol, source weighting, and fallback rules
- review language and return-action vocabulary

Child skills should add only the artifact-specific layer on top of that shared core.

## Best Expansion Path

For this repository, the best default expansion path is:

1. keep the root `SKILL.md` as the stable install surface and front-door router
2. keep shared workflow logic at plugin root
3. add child skills only for durable artifact families such as poster or presentation design
4. move to plugin-first distribution only after local multi-skill plugin discovery is verified end to end in the target Codex runtime

If future poster or PPT work also needs external systems such as Figma, Google Drive, Slides, or asset libraries, that should be handled as plugin or MCP capability on top of the skill family, not by overloading the root workflow skill itself.

## Project AGENTS.md Integration

For best model discovery, integrate a short Noootwo Design note into the target project's root `AGENTS.md`.

Bootstrap creates or merges that short section by default:

```bash
python scripts/bootstrap_noootwo_harness.py /path/to/project
```

If the project already has `AGENTS.md`, bootstrap preserves existing project instructions and only adds or replaces the short `## UI/Design Workflow` section from [assets/AGENTS.md](assets/AGENTS.md). Repeated runs are idempotent.

Use `--skip-agents` when you only want `.noootwo/` files:

```bash
python scripts/bootstrap_noootwo_harness.py /path/to/project --skip-agents
```

This is only a small project-level pointer. Keep the detailed workflow rules inside the `$noootwo-design` skill.

## Use

Examples:

- `Use $noootwo-design in deep mode to redesign this launch page with a more niche, high-end direction.`
- `Use $noootwo-design to redo all UI design in this Flutter app; show 3 directions before implementing.`
- `Use $noootwo-design in deep mode and run style discovery before drafting this dashboard.`
- `Use $noootwo-design in adopt-project mode to introduce Noootwo into this existing Flutter app before redesigning.`
- `Use $noootwo-design in standard mode to design a new workbench home page and show 3 directions before building.`
- `Use $noootwo-design in quick mode to polish spacing and type while staying close to the current UI.`
- `Use $noootwo-design in production mode to map this approved design into React tokens and implementation notes.`
- `Use $noootwo-design to review these screenshots and decide ready, refine, pivot, or needs artifact.`

## Harness

Noootwo Design stores durable context in `.noootwo/`.

Bootstrap the template into a project with:

```bash
python scripts/bootstrap_noootwo_harness.py
```

The default profile is `minimal` to reduce pending/TBD noise. Profiles:

- `minimal`: baseline system, adoption, brief, tokens, directions, review
- `deep`: minimal plus discovery, reference board, calibration
- `production`: minimal plus approved spec, implementation plan, handoff
- `full`: all templates

```bash
python scripts/bootstrap_noootwo_harness.py /path/to/project --profile deep
```

## Readiness Validation

Check that the required Noootwo deliverables are no longer pending before claiming a design is ready:

```bash
python scripts/validate_noootwo_readiness.py /path/to/project
```

The validator fails when `.noootwo/directions.md`, `.noootwo/review.md`, or `.noootwo/design-tokens.md` is missing, still `Status: pending`, contains unresolved `TBD` placeholders, or when `.noootwo/review.md` does not record a `ready` decision.

Use `--allow-non-ready` only when you want to verify that the workflow documents are complete but the design is still expected to be `refine`, `pivot`, or `needs artifact`.

Use `--deep-mode` when validating a deep-mode deliverable. It also requires `.noootwo/style-discovery.md` and `.noootwo/reference-board.md` to be complete.

For full redesign work, keep the same `--deep-mode` validator. If `.noootwo/directions.md` records `Full redesign trigger: yes`, it must also record `User selected direction` before the work can be ready.

For implementation work, require the approved spec and plan gate:

```bash
python scripts/validate_noootwo_readiness.py /path/to/project --implementation-gate
```

For a stricter workflow-closure check, require the brief, direction decision, implementation verification path, and evidence-backed review:

```bash
python scripts/validate_noootwo_readiness.py /path/to/project --strict-workflow
```

When a design is directionally correct but keeps drifting into default components or AI-looking detail, add the optional detail-translation gate after the implementation gate. This gate is intended for implementation-bound work and only checks handoff files if those files already exist and are no longer left as untouched templates:

```bash
python scripts/validate_noootwo_readiness.py /path/to/project --implementation-gate --detail-translation-gate
```

To inspect the workflow state without reading every markdown file:

```bash
python scripts/noootwo_status.py /path/to/project
```

Run lightweight workflow pressure tests against completed `.noootwo/` artifacts:

```bash
python scripts/eval_noootwo_artifacts.py /path/to/project --scenario all
```

For local web artifacts, run the lightweight visual gate:

```bash
python scripts/check_visual_gates.py http://localhost:3000 --screenshot-dir /tmp/noootwo-shots
```

The visual gate checks common viewport overflow and obvious clipped text. If browser automation is unavailable, record manual screenshot evidence and the limitation in `.noootwo/review.md`.

## Eval Prompts

The lightweight prompts in [evals/prompts](evals/prompts) are release pressure tests. They are not automated benchmarks; use them to check failure modes such as:

- missing exploration before build
- missing user decision under ambiguity
- artifact built but not reviewable
- directionally right but generic drift
- layout defects after fast delivery

## Package Layout

```text
.
├── .codex-plugin/plugin.json
├── SKILL.md
├── agents/openai.yaml
├── skills/
│   ├── noootwo-design/
│   ├── noootwo-style-discovery/
│   ├── noootwo-design-review/
│   └── noootwo-detail-translation/
├── assets/AGENTS.md
├── assets/noootwo-harness-template/
├── evals/prompts/
├── references/
└── scripts/
```

## Claude Design Alignment

This project does not copy private prompts. It implements public, repeatable mechanisms that make Claude Design-like workflows stronger:

- durable design-system memory before task work
- standard project `AGENTS.md` guidance for model discovery
- task-structure routing instead of surface-keyword routing
- stage roles so research, art direction, implementation, and evaluation do not blur together
- agentic style discovery before deep high-character drafts
- influence discovery for mechanism transfer, not designer/artist mimicry
- source weighting and mechanism transfer instead of surface copying
- structured design contracts instead of vague style adjectives or external template dependencies
- foreign-source accessibility checks with domestic fallback when needed
- full redesign checkpoint before implementation when the user asks to redo all UI
- approved design spec and implementation plan gates before non-quick UI file edits
- explicit externalization of unresolved uncertainty before implementation
- minimal bootstrap plus profile-based expansion to reduce default context noise
- artifact structure evals for workflow pressure tests
- typography, responsive, and spike-comparison gates for high-cost deep work
- optional detail-translation gate for implementation-stage polish when previous output drifted generic
- explicit but compact style calibration
- code-native or stack-native artifacts before final judgment
- token mapping before production handoff
- independent review using screenshots, previews, readiness validation, or explicit artifact limitations

## Research Basis

This workflow revision is grounded in public sources that emphasize:

- workflow and communication as part of the design system, not separate from it
- critique and review throughout the design/development process
- prototypes/artifacts as shared comparison objects when choosing between approaches
- the risk of design detail loss between guidelines, implementation, and release

See [references/research-protocol.md](references/research-protocol.md) and [references/workflow-research-notes.md](references/workflow-research-notes.md).

## License

MIT
