---
name: noootwo-design
description: "Use for UI, visual, artifact, or frontend work after product path is settled: screens, tokens, critique, motion, or reference replication."
---

# Noootwo Design

Turn a settled product path into a visual system, a reviewable artifact, and a handoff. When the real user, main path, states, or acceptance are unsettled, invoke the `noootwo-product` skill first: read its `SKILL.md` and follow it. Context lifecycle `write -> select -> compress -> isolate -> verify`: load this skill and triggered reference sections; route references over 200 lines through headings or query hits; cap live excerpts at 80 lines; put output over 16 KiB in cold evidence with path and hash; isolate only independent read-only work; keep one writer; verify summaries against source.

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
- Intervention / context / intent: leave simple | craft only | add moment — product function, frequency, risk, emotional or brand value, and whether the user explicitly requested motion or material
- Variance / Motion / Density: low | medium | high
```

Variance, motion, and density follow the exact feature and moment. Dense, high-frequency, evidence-heavy, or keyboard-driven work stays simple; rare first-use, completion, explanation, launch, and brand moments may justify more.

**Done when:** each dial has a value and a reason.

## 3. Direction

Compare materially different directions when style or structure is unresolved, and stop for the user's choice. A prose menu is not a decision: before the choice, show a low-cost real sample for each direction, or one fuller sample plus two lightweight variants when the runtime is weak. Read `references/direction.md` for the sample method, Style Evidence Check, and mechanism translation.

Read `references/design-discovery.md` for the discovery pass and the `.noootwo/style-discovery.md` contract. When the work is high-character, niche, premium, or previously rejected, invoke the `noootwo-research` skill first: read its `SKILL.md` and follow it — a design claim needs a source, an artifact, or a screenshot.

For `deep` work, prefer same-medium references and capture every source the direction leans on into `.noootwo/references/<slug>/`, with a `source.md` recording URL, date, evidence level, same-medium fit, inspected artifact evidence, accessibility result, and licence; capture real values from a live source with `scripts/extract_design_tokens.mjs` and its `NN-<label>.png` screenshot with `--screenshot` when a page or running product is reachable, and record inaccessible sources as `capture: unreachable`. A black or broken capture is not evidence. Lock the build target and what must not drift before drafting, and let one direction dominate instead of averaging several. `standard` work stays on the lighter path in `references/design-discovery.md`.

For standard, deep, and production work, read `references/motion.md` before the contract and make an intervention decision. `leave simple` and `craft only` are valid only when the user accepts them or a concrete blocker prevents motion; an explicit motion or material request defaults to `add moment`.

**Done when:** one direction is chosen by the user after reviewing real samples, or the chosen direction is justified by evidence and the sample requirement is recorded as not applicable.

## 4. Design Contract

Write this before editing UI files, for `standard`, `deep`, and `production`:

```
Design Contract
- Structure:
- Type scale:
- Colour and token roles:
- Component behaviour:
- State treatment:
- Intervention / authored move / ledger: leave simple | craft only | add moment; none | primary plus optional support; candidates, rejected opportunities, source or platform rule, fallback
- Motion: when `add moment`, name the implementation tool and trigger, archetype, easing, duration, layers, and choreography; otherwise `not applicable`
- Anti-slop risks:
- Artifact and review path:
```

Name semantic roles, not adjectives. Stable decisions become tokens, component rules, and state behaviour.

**Done when:** typography roles, layout model, component vocabulary, and the artifact review path are all named.

## 5. Build

Read `references/craft.md` immediately before editing UI. It carries the quality floor and evidence-backed aesthetic flags. Read `references/motion.md` for the intervention decision and whenever the artifact animates.

Read `references/translate.md` to turn the contract into stack-native implementation, assets, and handoff. Read `references/system.md` when the work touches tokens, a design system, or a new artifact family.

When a direction, token set, or review outcome becomes durable, invoke the `noootwo-state` skill to persist it: read its `SKILL.md` and follow it, and submit an abstract record instead of writing shared project state directly.

**Done when:** the artifact runs and every contract item is visibly present.

## 6. Review the artifact

Review the rendered thing, never the prose. Read `references/review.md` for the rubric, safety gates, and evidence-backed flags.

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

When this is not design work, name the failed layer and invoke the owning skill in one hop: `noootwo-product` for an unsettled product path, `noootwo-code-health` for code or performance judgment, `noootwo-debug` for a failure that needs a proven cause.

## Reference

- `references/intake.md` — reading a request, the Design Read, harness sizing, and adopting an existing project.
- `references/direction.md` — direction exploration, Style Evidence Check, and mechanism translation.
- `references/design-discovery.md` — the discovery pass, influence discovery, fit scoring, and the `.noootwo/style-discovery.md` contract.
- `references/motion.md` — contextual intervention, opportunity gates, signature motion identity, duration, easing, choreography, and the motion bans.
- `references/motion-libraries.md` — the register gate, per-platform motion and material tools, licence and dependency checks, and adapt-or-reject recipes.
- `references/system.md` — tokens, design-system extraction, and artifact-family contracts.
- `references/craft.md` — anti-slop, typography, colour, responsive, and data-UI craft floors.
- `references/review.md` — scoring, safety gates, evidence-backed aesthetic flags, and final review.
- `references/translate.md` — stack-native implementation, assets, and handoff.
- `references/evidence.md` — verified cases and distilled reference-skill rules.
- `references/notes.md` — research notes and cost boundaries.
- `scripts/extract_design_tokens.mjs` — capture real colours, type, spacing, shape, and motion values from a live page, and report drift against a saved baseline.

Missing skill fallback: first try `npx -y skills add noootwo/noootwo-vibe --global --agent codex --skill <name> --yes`; if install fails, take the smallest direct fallback and mark the record `skill-missing: <name>` (for persistence, write the owning file directly).
