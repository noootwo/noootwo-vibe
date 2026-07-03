---
name: noootwo-design
description: Use when UI design, frontend design, visual redesign, agentic style discovery, influence discovery, existing-project UI adoption, design system extraction, artifact review, screenshot critique, React, Vue, Flutter, SwiftUI, Compose, native app UI, or implementation handoff work needs distinctive and non-generic product design.
---

# Noootwo Design

Noootwo Design is a design workflow protocol for non-trivial UI work. It routes by task structure, not by surface keywords. The goal is to keep design work inside a reliable loop:

`intake -> exploration -> directions -> decision -> design contract -> implementation plan -> artifact -> review -> handoff`

Use it for new UI pages, app screens, dashboards, workbenches, landing pages, visual redesign, typography, motion, art direction, screenshot review, design-system extraction, and implementation handoff. Do not use it for backend-only work, CLI tasks, pure logic bug fixes, or refactors with no UI impact.

## Project Context

Durable context lives in `.noootwo/`. If missing, bootstrap minimal context from `assets/noootwo-harness-template/` or run `python scripts/bootstrap_noootwo_harness.py`. Use `--profile deep`, `--profile production`, or `--profile full` only when those templates are needed.

Read only what the selected mode needs. Useful files include:

- `.noootwo/system.md`, `.noootwo/design-tokens.md`, `.noootwo/adoption.md`, `.noootwo/product-facts.md`
- `.noootwo/brief.md`, `.noootwo/style-calibration.md`, `.noootwo/style-discovery.md`, `.noootwo/reference-board.md`, `.noootwo/directions.md`
- `.noootwo/specs/active-design.md`, `.noootwo/plans/active-implementation.md`
- `.noootwo/review.md`, `.noootwo/handoff/implementation.md`, `.noootwo/handoff/acceptance.md`, `.noootwo/handoff/assets.md`

If a file is missing, stale, or `Status: pending`, refresh only the minimum needed for the current step. Write decisions as explicit contracts with evidence, constraints, unresolved uncertainty, preservation rules, artifact strategy, verification path, and return path.

## Task Classification

Before choosing a mode, classify the task on these dimensions:

- `change magnitude`: is this a local polish, or will it create a new visual structure, hierarchy, or system?
- `direction uncertainty`: are there multiple reasonable directions whose result depends on preference, brand, audience, use context, or product stance?
- `implementation commitment`: is the work still exploratory, or has a direction already been chosen and accepted for implementation?
- `artifact verifiability`: can the current environment produce a reviewable artifact, screenshot, preview, or nearest equivalent?
- `system continuity`: should the current system be preserved, or must it be reinterpreted or replaced?
- `artifact family`: is the target best treated as a UI surface, fixed-canvas graphic, slide deck, or live artifact?

Use those dimensions to route:

- `quick`: preserve the existing system, keep scope small, and avoid changing direction.
- `adopt-project`: first Noootwo pass on an existing project; establish baseline truth and preserve/improve boundaries.
- `standard`: non-trivial design work with meaningful visual decisions but ordinary cost.
- `deep`: high-character or high-risk work where stronger exploration is required.
- `production`: implementation-bound work with an accepted direction and a confirmed artifact/review path.
- `extract-system`: build or refresh durable design memory and tokens.
- `review`: inspect an artifact, diagnose drift or defects, and choose a return action.

Do not route by surface label alone. A poster, dashboard, landing page, route screen, or HTML prototype may all use the same workflow if the task structure is the same.

## Workflow Contract

For non-trivial UI work, follow this sequence:

`intake -> exploration -> direction brainstorm -> user decision -> design contract -> implementation plan -> artifact -> review -> handoff`

Stage meaning:

- `intake`: state the objective, audience/context, success criteria, constraints, and unresolved uncertainty.
- `exploration`: inspect existing UI/system truth, artifact constraints, and reference evidence.
- `direction brainstorm`: compare materially different paths and recommend one.
- `user decision`: resolve high-impact ambiguity or record explicit delegated choice.
- `design contract`: turn the chosen direction into implementation rules.
- `implementation plan`: map the contract into files/modules, tokens, components, verification, and drift risks.
- `artifact`: build the fastest reviewable artifact that can expose hierarchy, typography, density, layout behavior, and artifact-family-specific delivery constraints.
- `review`: judge the artifact, not the prose, and pick a concrete return action if not ready.
- `handoff`: only after the artifact passes review or the limitation is explicitly accepted.

Artifact-family implications:

- `ui surface`: responsive or platform-bound interface work; review needs viewport or device evidence.
- `fixed-canvas graphic`: poster, cover, social card, or other composition-first work; review needs final dimensions plus export-ready evidence.
- `slide deck`: presentation flows with page sequence and navigation logic; review needs structure, page flow, and export target evidence.
- `live artifact`: dashboard, decision room, or data/stateful artifact; review needs evidence that the live states or tweaks path actually work.

## Blocking Rules

These are hard stops, not recommendations:

- If the result depends on aesthetic, brand, audience, or use-context tradeoffs, do not implement before the direction decision is recorded.
- If the task introduces a new structure, new visual language, or new information hierarchy, do not implement before the exploration summary is recorded in `.noootwo/brief.md`.
- If the work is non-trivial UI implementation, do not edit UI files before `.noootwo/specs/active-design.md` and `.noootwo/plans/active-implementation.md` are completed and approved or explicitly delegated.
- If there is no reviewable artifact or explicit blocker, do not claim `ready`.
- If the artifact shows layout defects, responsive defects, unreadable typography, or generic drift, do not hide the issue under “polish”; return to the earliest stage that can actually fix it.

Allowed exceptions:

- `quick` polish that clearly preserves the current direction
- explicit handoff-only analysis
- explicit user approval to skip a gate

## Decision Protocol

Ask the user whenever a high-impact uncertainty can materially change the result. High-impact uncertainty includes:

- unclear goal priority
- unclear brand or taste posture
- unclear audience or use context
- unclear artifact form or review path
- unclear speed vs fidelity tradeoff
- unclear stack, preview, or verification path

The protocol:

1. externalize the uncertainty in `.noootwo/brief.md` or `.noootwo/directions.md`
2. present 2-3 meaningful options with one recommendation
3. record either the user choice or `User delegated choice to agent`
4. do not continue past the blocked stage until one of those is true

Do not turn this into a long questionnaire. Batch decisions and ask only what changes the output.

## Direction Brainstorm

Any `direction-sensitive` task must include a direction brainstorm before implementation. This is not a special mode; it is a required intermediate state whenever multiple viable directions exist.

Each compared direction must state:

- direction name
- key structural difference
- typography, color, and density stance
- signature mechanism
- why it fits the objective
- why it is not interchangeable with the other options
- at least one openable case link or evidence source

If three directions share the same structure and only swap palette or decoration, the brainstorm failed.

If the user has not selected a direction and has not delegated the choice, stop after the brainstorm.

## Mode Workflows

### Quick

- Read the current UI plus `.noootwo/system.md` and `.noootwo/design-tokens.md` when available.
- Preserve the existing direction unless the user explicitly asks to change it.
- Use artifact evidence when available; otherwise state the limitation.

### Adopt Project

- Use [adoption-playbook.md](references/adoption-playbook.md).
- Inspect current UI code, tokens, components, screenshots/previews, `AGENTS.md`, and `.noootwo/` status.
- Update `.noootwo/adoption.md` and `.noootwo/brief.md`, then route to the next mode.

### Standard

- Use [structured-design-spec.md](references/structured-design-spec.md).
- Complete the brief, compare directions, record the decision, then create the design contract and implementation plan before UI edits.
- Build the fastest reviewable artifact and review with typography and responsive gates.

### Deep

- Use deep only when stronger exploration is justified.
- Read discovery references only when needed: [agentic-style-discovery.md](references/agentic-style-discovery.md), [source-registry.md](references/source-registry.md), [reference-board.md](references/reference-board.md), [taste-fit-matrix.md](references/taste-fit-matrix.md), [workflow-cost-model.md](references/workflow-cost-model.md), and [anti-slop.md](references/anti-slop.md).
- Record source accessibility, evidence levels, rejected surfaces, mechanisms, and fit signals.
- Compare materially different directions and lower confidence if the evidence is weak or the spikes are too narrow.

### Production

- Read the approved design contract and implementation plan before UI edits.
- Map the chosen direction into `.noootwo/design-tokens.md` and stack-native implementation notes.
- For implementation-bound work that risks generic drift, run the detail-translation pass: surface inventory, component restyling matrix, default override pass, and micro-detail pass.

### Review

- Prefer lived artifacts: screenshot, running page, simulator preview, target-stack prototype, or recorded interaction.
- If no artifact evidence exists, mark `needs artifact` unless the user explicitly accepts the limitation.
- Use [review-rubric.md](references/review-rubric.md), [typography-craft-rubric.md](references/typography-craft-rubric.md), and [responsive-visual-gates.md](references/responsive-visual-gates.md). Use [data-ui-rubric.md](references/data-ui-rubric.md) for metric-heavy UI.
- Choose one return action: `return to exploration`, `return to directions`, `return to approved spec`, `return to implementation plan`, `return to artifact`, `return to responsive pass`, `return to typography pass`, `return to stack pass`, or `return to handoff`.

## Failure Recovery Map

Return to the earliest stage that can fix the problem:

- unclear goals, context, or success criteria: return to `intake`
- no real comparison between viable directions: return to `direction brainstorm`
- unresolved high-impact choice: return to `user decision`
- structure, hierarchy, or system rules missing: return to `design contract`
- artifact path, token mapping, or drift risks undefined: return to `implementation plan`
- structure is right but execution is weak: return to `artifact`
- overflow, clipping, or viewport failure: return to `responsive pass`
- type hierarchy, rhythm, or readability failure: return to `typography pass`
- stack-native craft failure: return to `stack pass`
- handoff written without passing review: return to `review`

## Hard Rules

- Establish design-system truth before inventing aesthetics.
- Visual evidence beats style adjectives.
- Never default to `Inter-only`, `system-only`, `hero + cards`, generic shadcn-like UI, or Flutter `Scaffold + AppBar + Card + ListView` without product reason.
- Do not replace one generic template with another.
- Do not imitate a specific designer or artist's signature look. Borrow mechanisms and reject mimicry.
- Do not present a direction menu without openable case links or inspectable evidence.
- Do not justify product UI using only campaign-gallery references.
- Flutter/native work needs stack-native preview evidence; HTML proxy is fallback only and cannot be stack-native ready.
- A design is not complete while required `.noootwo/` deliverables are pending, unresolved, or missing artifact evidence.

## Reference Map

- State: `python scripts/noootwo_status.py <project>`
- Artifact eval: `python scripts/eval_noootwo_artifacts.py <project> --scenario all`
- Core workflow: [workflow-cost-model.md](references/workflow-cost-model.md), [adoption-playbook.md](references/adoption-playbook.md), [project-integration.md](references/project-integration.md), [research-protocol.md](references/research-protocol.md)
- Discovery: [agentic-style-discovery.md](references/agentic-style-discovery.md), [source-registry.md](references/source-registry.md), [research-source-fallback.md](references/research-source-fallback.md), [reference-board.md](references/reference-board.md)
- System/spec/tokens: [system-extraction.md](references/system-extraction.md), [design-system-setup.md](references/design-system-setup.md), [structured-design-spec.md](references/structured-design-spec.md), [brief-expansion.md](references/brief-expansion.md)
- Directions/taste: [direction-exploration.md](references/direction-exploration.md), [taste-fit-matrix.md](references/taste-fit-matrix.md), [mechanism-library.md](references/mechanism-library.md), [style-lineages.md](references/style-lineages.md), [frontend-aesthetic-principles.md](references/frontend-aesthetic-principles.md), [impeccable-style-details.md](references/impeccable-style-details.md), [anti-slop.md](references/anti-slop.md)
- Artifacts/stacks/review: [artifact-family-contract.md](references/artifact-family-contract.md), [canvas-artifact-loop.md](references/canvas-artifact-loop.md), [target-stack-rules.md](references/target-stack-rules.md), [review-rubric.md](references/review-rubric.md), [review-gates.md](references/review-gates.md), [detail-translation-pass.md](references/detail-translation-pass.md), [handoff-bundle.md](references/handoff-bundle.md)
