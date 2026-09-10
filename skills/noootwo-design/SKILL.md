---
name: noootwo-design
description: "Use for UI, visual, artifact, or frontend work: a new screen, a redesign, a restyle, tokens, components, screenshot critique, or responsive and typography polish. Requires a settled product path."
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

Read `references/research.md` first when the work is high-character, niche, premium, or previously rejected — a design claim needs a source, an artifact, or a screenshot.

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
- Motion:
- Anti-slop risks:
- Artifact and review path:
```

Name semantic roles, not adjectives. Stable decisions become tokens, component rules, and state behaviour.

**Done when:** typography roles, layout model, component vocabulary, and the artifact review path are all named.

## 5. Build

Read `references/craft.md` immediately before editing UI. It carries the quality floor and the hard bans.

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

`ready` requires artifact evidence and no blocking layout, readability, responsive, product-comprehension, or slop-drift defect. Every other decision names exactly one return action.

**Done when:** a decision is recorded against real evidence, and `ready` is never self-certified — prefer a reviewer that did not build the artifact.

## Reference

- `references/intake.md` — reading a request, the Design Read, harness sizing, and adopting an existing project.
- `references/direction.md` — direction exploration, Style Evidence Check, and mechanism translation.
- `references/research.md` — the research pass and its source pools.
- `references/system.md` — tokens, design-system extraction, and artifact-family contracts.
- `references/craft.md` — anti-slop, typography, colour, responsive, and data-UI craft floors.
- `references/review.md` — scoring, gates, hard bans, and final review.
- `references/translate.md` — stack-native implementation, assets, and handoff.
- `references/evidence.md` — verified cases and distilled reference-skill rules.
- `references/notes.md` — research notes and cost boundaries.
