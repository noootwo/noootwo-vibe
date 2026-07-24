---
name: noootwo-design
description: "Use for UI/frontend/app visual execution after product path is clear: Design Read, Style Evidence Check, direction exploration when style or structure is unresolved, Design Contract, artifact review, semantic tokens, quick polish, design-system adoption, screenshot critique, and implementation handoff."
---

# Noootwo Design

Noootwo Design translates a clear product path into a stable visual system, implementation contract, reviewable artifact, and handoff. It does not define product scope. If `real user`, `main path`, `states`, or `acceptance criteria` are unclear, route to `$noootwo-product` Decision Interview before designing.

Use the lightest flow that can prove the result:

`intake -> design read -> optional evidence/directions -> design contract -> implementation plan -> artifact -> review -> handoff`

## First Pass

1. Read nearest truth first: request, `AGENTS.md`, current UI, screenshots, existing `.noootwo/` files, and the Product-to-Design Handoff when present.
2. Classify: `quick`, `adopt-project`, `standard`, `deep`, `production`, `extract-system`, or `review`.
3. For non-quick UI work, declare `Design Read` before choosing a look.
4. If high-character, niche, premium, unusual, user-selected, or previously rejected, run `Style Evidence Check` before trusting style prose.
5. If direction-sensitive, compare materially different directions and stop for user choice or explicit delegated choice.
6. If implementation-bound, create or update the Design Contract and implementation plan before UI edits.
7. Before handoff, review an artifact, screenshot, preview, simulator, recording, or explicit accepted limitation.

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
- `standard`: normal non-trivial UI work. Use Design Read, light exploration, directions only when the trigger applies, one artifact, responsive and typography review.
- `deep`: high-character, brand-heavy, niche, or previously generic work. Use evidence-backed discovery, Style Evidence Check, directions when style or structure is unresolved, stronger critique, and lower confidence when evidence is thin.
- `production`: approved design implementation. Translate the contract into tokens, components, states, stack notes, and artifact verification.
- `extract-system`: refresh durable system memory and semantic tokens from working UI evidence.
- `review`: judge artifact evidence and choose `ready`, `refine`, `pivot`, or `needs artifact`.

Do not route by surface label alone. Dashboards, native screens, landing pages, decks, posters, and live artifacts use the same decision flow when their risk shape is the same.

## Hard Stops

- Product path unclear: return to `$noootwo-product` Decision Interview.
- Audience, use-context, main path, state, or acceptance tradeoff unresolved: return to `$noootwo-product` Decision Interview.
- Taste or brand tradeoff unresolved after product path is clear: stop at directions or user decision.
- New structure, visual language, or hierarchy without exploration summary: do not implement.
- High-character style claim without visual evidence, anti-example, mechanism translation, or low-confidence label: return to style discovery.
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
- Style understanding fit:
- Product comprehension fit:
- Responsive/type/state findings:
- Decision: ready | refine | pivot | needs artifact
- Return action:
```

`ready` requires artifact evidence and no blocking layout, readability, responsive, product-comprehension, style-understanding, or generic-drift defects. Non-ready work needs exactly one return action, such as `return to style discovery`, `return to directions`, `return to design contract`, `return to implementation plan`, `return to artifact`, `return to responsive pass`, `return to typography pass`, `return to stack pass`, or `return to handoff`.

## Anti-Slop Rules

- Establish product-path truth before designing new UI structure.
- Establish design-system truth before inventing aesthetics.
- Prefer semantic tokens and component behavior over raw colors, decoration, or style adjectives.
- Do not default to `Inter-only`, `system-only`, `hero + cards`, generic shadcn-like UI, or Flutter `Scaffold + AppBar + Card + ListView` without product and UI reason.
- Do not replace one generic template with another.
- Do not imitate a specific designer or artist signature. Borrow mechanisms and reject mimicry.
- Do not let a polished style description replace visual evidence or a small spike when the requested taste is high-risk.
- Visual evidence beats claims about quality.

## Reference Map

- State: `python scripts/noootwo_status.py <project>` for adoption, production, handoff, or workflow debugging; not required for quick polish.
- Delivery validation: `python scripts/validate_noootwo_readiness.py <project>` and `python scripts/eval_noootwo_artifacts.py <project> --scenario all` for completed or implementation-bound `.noootwo/` work.
- Main path: `references/design-read-and-contract.md`, `references/style-evidence-check.md`, `references/direction-exploration.md`, `references/detail-translation-pass.md`, `references/review-rubric.md`, and `references/target-stack-rules.md`.
- Use local search in `references/` for stack, color, typography, data UI, responsive, artifact-family, adoption, or source-specific guidance only when the task names that need.
