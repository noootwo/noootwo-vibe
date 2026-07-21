---
name: noootwo-design
description: Use when UI design, visual design, frontend design, quick UI polish, visual redesign, design read, design dials, style stability, semantic tokens, anti-slop checks, existing-project UI adoption, design system extraction, artifact review, screenshot critique, React, Vue, Flutter, SwiftUI, Compose, native app UI, or implementation handoff work needs distinctive and non-generic UI/frontend execution. Use after the product path is clear enough; route to noootwo-product when requirements, feature scope, user flow, IA, interaction model, states, acceptance criteria, usability, or cognitive-cost choices are unclear.
---

# Noootwo Design

Noootwo Design translates a clear product path into a stable visual system, implementation contract, reviewable artifact, and handoff. It does not define product scope. If `real user`, `main path`, `states`, or `acceptance criteria` are unclear, route to `$noootwo-product` before designing.

Use the lightest flow that can prove the result:

`intake -> design read -> exploration -> directions -> decision -> design contract -> implementation plan -> artifact -> review -> handoff`

## First Pass

1. Read nearest truth first: request, `AGENTS.md`, current UI, screenshots, existing `.noootwo/` files, and the Product-to-Design Handoff when present.
2. Classify: `quick`, `adopt-project`, `standard`, `deep`, `production`, `extract-system`, or `review`.
3. For non-quick UI work, declare `Design Read` before choosing a look.
4. If direction-sensitive, compare materially different directions and stop for user choice or explicit delegated choice.
5. If implementation-bound, create or update the Design Contract and implementation plan before UI edits.
6. Before handoff, review an artifact, screenshot, preview, simulator, recording, or explicit accepted limitation.

## Design Read

Use this for every non-quick UI task:

```markdown
Design Read
- Surface kind:
- Audience:
- Product posture:
- Visual posture:
- Variance:
- Motion:
- Density:
- Existing system to preserve:
```

The read turns brief signals into execution dials. `variance`, `motion`, and `density` should be low for operational tools and higher only when product context, audience, brand, or artifact family justifies it. Do not copy Antfu's UnoCSS taste by default; borrow the mechanism of explicit dials and stable tokens.

## Mode Routing

- `quick`: local polish that preserves the current system. Read current UI and existing system/tokens when present. No source mining, no three directions, no full harness.
- `adopt-project`: first Noootwo pass on an existing project. Capture current UI, tokens, screenshots, constraints, and `.noootwo/` baseline.
- `standard`: normal non-trivial UI work. Use Design Read, light exploration, directions when needed, one artifact, responsive and typography review.
- `deep`: high-character, brand-heavy, niche, or previously generic work. Use evidence-backed discovery, reference boards, stronger critique, and lower confidence when evidence is thin.
- `production`: approved design implementation. Translate the contract into tokens, components, states, stack notes, and artifact verification.
- `extract-system`: refresh durable system memory and semantic tokens from working UI evidence.
- `review`: judge artifact evidence and choose `ready`, `refine`, `pivot`, or `needs artifact`.

Do not route by surface label alone. Dashboards, native screens, landing pages, decks, posters, and live artifacts use the same decision flow when their risk shape is the same.

## Hard Stops

- Product path unclear: return to `$noootwo-product`.
- Taste, brand, audience, or use-context tradeoff unresolved: stop at directions or user decision.
- New structure, visual language, or hierarchy without exploration summary: do not implement.
- Non-trivial implementation without Design Contract and implementation plan: do not edit UI files.
- No reviewable artifact or accepted blocker: do not claim `ready`.
- Layout, responsive, unreadable typography, or generic drift defects: return to the earliest stage that can fix them.

Allowed exceptions: quick polish, explicit handoff-only analysis, or explicit user approval to skip a gate.

## Design Contract

Implementation-bound work must produce:

```markdown
Design Contract
- Structure:
- Type scale:
- Color/token roles:
- Component behavior:
- State treatment:
- Motion:
- Anti-slop risks:
- Artifact/review path:
```

Use semantic roles, not adjectives. Stable decisions should become tokens, component rules, state behavior, and forbidden substitutions. A design is not implementation-ready if it cannot name its typography roles, layout model, component vocabulary, and artifact review path.

## Artifact Review

Review the rendered thing, not the prose. Use:

```markdown
Artifact Review
- Evidence:
- Strongest authored move:
- Defects:
- Generic drift:
- Responsive/type/state findings:
- Decision: ready | refine | pivot | needs artifact
- Return action:
```

`ready` requires artifact evidence and no blocking layout, readability, responsive, or generic-drift defects. Non-ready work needs exactly one return action, such as `return to directions`, `return to design contract`, `return to implementation plan`, `return to artifact`, `return to responsive pass`, `return to typography pass`, `return to stack pass`, or `return to handoff`.

## Anti-Slop Rules

- Establish product-path truth before designing new UI structure.
- Establish design-system truth before inventing aesthetics.
- Prefer semantic tokens and component behavior over raw colors, decoration, or style adjectives.
- Do not default to `Inter-only`, `system-only`, `hero + cards`, generic shadcn-like UI, or Flutter `Scaffold + AppBar + Card + ListView` without product and UI reason.
- Do not replace one generic template with another.
- Do not imitate a specific designer or artist signature. Borrow mechanisms and reject mimicry.
- Visual evidence beats claims about quality.

## Reference Map

- State: `python scripts/noootwo_status.py <project>` for adoption, production, handoff, or workflow debugging; not required for quick polish.
- Delivery validation: `python scripts/validate_noootwo_readiness.py <project>` and `python scripts/eval_noootwo_artifacts.py <project> --scenario all` for completed or implementation-bound `.noootwo/` work.
- Core cost and integration: `references/workflow-cost-model.md`, `references/project-integration.md`, `references/research-protocol.md`.
- Product-to-design execution: `references/design-read-and-contract.md`, `references/structured-design-spec.md`, `references/handoff-bundle.md`.
- Discovery and directions: `references/agentic-style-discovery.md`, `references/source-registry.md`, `references/reference-board.md`, `references/direction-exploration.md`, `references/taste-fit-matrix.md`.
- Style stability: `references/design-system-setup.md`, `references/system-extraction.md`, `references/anti-slop.md`, `references/detail-translation-pass.md`, `references/color-system-calibration.md`.
- Review and stacks: `references/review-rubric.md`, `references/responsive-visual-gates.md`, `references/typography-craft-rubric.md`, `references/data-ui-rubric.md`, `references/target-stack-rules.md`, `references/artifact-family-contract.md`.
