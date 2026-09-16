---
name: noootwo-design
description: "Use for UI, visual, artifact, or frontend: screens, redesigns, restyles, tokens, components, screenshot critique, or responsive, typography, motion, or animation polish. Needs a settled product path."
---

# Noootwo Design

Turn a settled product path into a visual system, a reviewable artifact, and a handoff. When the real user, main path, states, or acceptance are unsettled, invoke the `noootwo-product` skill first: read its `SKILL.md` and follow it.

## 1. Size the work

- `quick` — local polish inside the existing system. Read the current UI and tokens, make the change, check it.
- `standard` — normal non-trivial UI. Design Read, one artifact, responsive and typography review.
- `deep` — high-character, brand-heavy, or previously rejected work. Add evidence and directions.
- `production` — implementing an approved design. Contract, tokens, components, states, artifact verification.

**Done when:** the mode is named and its proof of done is stated.

## 2. Design Read

Declare this before choosing a look, for every mode except `quick`:

```
Design Read
- Surface kind:
- Audience:
- Product posture:
- Visual posture:
- Variance / Motion / Density: low | medium | high
```

Variance, motion, and density stay low for operational tools and rise only when audience, brand, or artifact family justify it.

**Done when:** each dial has a value and a reason.

## 3. Direction

Compare materially different directions when style or structure is unresolved, and stop for the user's choice. Read `references/direction.md` for the exploration method, the Style Evidence Check, and mechanism translation.

Read `references/design-discovery.md` for the discovery pass and the `.noootwo/style-discovery.md` contract. When the work is high-character, niche, premium, or previously rejected, invoke the `noootwo-research` skill first: read its `SKILL.md` and follow it — a design claim needs a source, an artifact, or a screenshot.

For `deep` work, capture every reference the direction leans on into `.noootwo/references/<slug>/`, with a `source.md` recording URL, date, evidence level, accessibility result, and licence; capture real values from a live source with `scripts/extract_design_tokens.mjs` when a page or running product is reachable, and record inaccessible sources as `capture: unreachable`. Lock the build target and what must not drift before drafting, and let one direction dominate instead of averaging several. `standard` work stays on the lighter path in `references/design-discovery.md`.

When the direction carries motion, set the register from the surface before looking for examples, then source two or three in that register and record each as a mechanism rather than a look. Expressive motion on a quiet product screen is drift, not ambition.

**Done when:** one direction is chosen by the user, or the chosen direction is justified by evidence.

## 4. Design Contract

Write this before editing UI files, for `standard`, `deep`, and `production`:

```
Design Contract
- Structure:
- Type scale:
- Colour and token roles:
- Component behaviour:
- State treatment:
- Motion: archetype, signature easing, duration scale, layers, choreography
- Anti-slop risks:
- Artifact and review path:
```

Name semantic roles, not adjectives. Stable decisions become tokens, component rules, and state behaviour.

**Done when:** typography roles, layout model, component vocabulary, and the artifact review path are all named.

## 5. Build

Read `references/craft.md` immediately before editing UI. It carries the quality floor and the hard bans. Read `references/motion.md` when the direction carries motion or the artifact animates.

Read `references/translate.md` to turn the contract into stack-native implementation, assets, and handoff. Read `references/system.md` when the work touches tokens, a design system, or a new artifact family.

**Done when:** the artifact runs and every contract item is visibly present.

## 6. Review the artifact

Review the rendered thing, never the prose. Read `references/review.md` for the rubric, gates, and bans.

```
Artifact Review
- Evidence:
- Strongest authored move:
- Defects:
- Slop drift:
- Decision: ready | refine | pivot | needs artifact
- Return action:
```

Verify in bounded passes: build fully, inspect once with a batch covering the relevant viewports together, fix everything it shows in one batch, then confirm with at most one more round and stop.

`ready` requires artifact evidence and no blocking layout, readability, responsive, motion, product-comprehension, or slop-drift defect. Every other decision names exactly one return action.

**Done when:** a decision is recorded against real evidence, and `ready` is never self-certified — prefer a reviewer that did not build the artifact.

## Return

When this is not design work, name the failed layer and invoke the owning skill in one hop: `noootwo-product` for an unsettled product path, `noootwo-review` for code or performance judgment, `noootwo-debug` for a failure that needs a proven cause.

## Reference

- `references/intake.md` — reading a request, the Design Read, harness sizing, and adopting an existing project.
- `references/direction.md` — direction exploration, Style Evidence Check, and mechanism translation.
- `references/design-discovery.md` — the discovery pass, influence discovery, fit scoring, and the `.noootwo/style-discovery.md` contract.
- `references/motion.md` — personality archetypes, duration scale, easing catalog, choreography budgets, and the motion bans.
- `references/system.md` — tokens, design-system extraction, and artifact-family contracts.
- `references/craft.md` — anti-slop, typography, colour, responsive, and data-UI craft floors.
- `references/review.md` — scoring, gates, hard bans, and final review.
- `references/translate.md` — stack-native implementation, assets, and handoff.
- `references/evidence.md` — verified cases and distilled reference-skill rules.
- `references/notes.md` — research notes and cost boundaries.
- `scripts/extract_design_tokens.mjs` — capture real colours, type, spacing, shape, and motion values from a live page, and report drift against a saved baseline.
