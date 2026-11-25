---
name: noootwo-design
description: "Use for UI, visual, artifact, or frontend work after product path is settled: screens, tokens, critique, motion, or reference replication."
---

# Noootwo Design

Turn a settled product path into a visual system, a reviewable artifact, and a handoff. Name the target root before editing; a project supplied as a case, reference, or comparison is read-only unless the user explicitly asks to change it. A report that a surface looks wrong, or a question about it, is `propose`: present the change and stop; when the mandate is unclear, invoke the `noootwo-workflow` skill: read its `SKILL.md` and follow its Mandate Gate. When the real user, audience contract, main path, states, or acceptance are unsettled, invoke the `noootwo-product` skill first: read its `SKILL.md` and follow it. Context lifecycle `write -> select -> compress -> isolate -> verify`: load this skill and triggered reference sections; route references over 200 lines through headings or query hits; cap live excerpts at 80 lines; put output over 16 KiB in cold evidence with path and hash; isolate only independent read-only work; keep one writer; verify summaries against source.

## 1. Size the work

- `quick` — local polish inside the existing system. Read the current UI and tokens, make the change, then record a 5-line observation card: changed, rendered at, saw, defect, decision. If no rendered evidence exists, the decision is `needs artifact`; if the change touches copy, notes, settings, or visible technical data, run the Comprehension Gate.
- `standard` — normal non-trivial UI. Design Read, light reference audition (2–3 candidates), one artifact, responsive and typography review.
- `deep` — high-character, brand-heavy, or previously rejected work. Add evidence and directions.
- `production` — implementing an approved design. Contract, tokens, components, states, artifact verification.

**Done when:** the mode is named and its proof of done is stated.

## 2. Design Read

Declare this before choosing a look, for every mode except `quick`:

```
Design Read
- Surface kind:
- Audience contract: role, moment, familiarity, frequency, error cost, shared vocabulary
- Product posture:
- Visual posture:
- Intervention / context / intent: leave simple | craft only | add moment — product function, frequency, risk, emotional or brand value, and whether the user explicitly requested motion or material
- Variance / Motion / Density: low | medium | high
```

Variance, motion, and density follow the exact feature and moment. Dense, high-frequency, evidence-heavy, or keyboard-driven work stays simple; rare first-use, completion, explanation, launch, and brand moments may justify more. Density and language follow the audience contract: trained, frequent work may be dense and domain-specific; first-use and consumer work stays plain and default-led.

**Done when:** each dial has a value and a reason.

## 3. Direction

Compare materially different directions when style or structure is unresolved, and stop for the user's choice. A prose menu is not a decision: before the choice, show a low-cost real sample for each direction, or one fuller sample plus two lightweight variants when the runtime is weak. Read `references/direction.md` for the sample method, Style Evidence Check, and mechanism translation.

Read `references/design-discovery.md` for the discovery pass, the source matrix, and the `.noootwo/style-discovery.md` / `.noootwo/reference-board.md` contract. When the work is standard, high-character, niche, premium, or previously rejected, invoke the `noootwo-research` skill first: read its `SKILL.md` and follow it — a design claim needs a source, an artifact, or a screenshot.

For `standard` and `deep` work, use `.noootwo/reference-board.md` as the audition record. Standard uses 2–3 candidates, one primary screenshot, and one narrow supplement; deep uses 3–5 captured sources, same-medium evidence, licence, fit scoring, and 2–3 spikes. Capture every deep source into `.noootwo/references/<slug>/` with `source.md`; capture real values with `scripts/extract_design_tokens.mjs` and `--screenshot` when reachable. A black or broken capture is not evidence. Read `.noootwo/appearance-ledger.md` for a matching surface before searching, and write an entry only after review. Lock the build target and what must not drift before drafting, and let one direction dominate instead of averaging several.

For standard, deep, and production work, read `references/motion.md` before the contract and make an intervention decision. `leave simple` and `craft only` are valid only when the user accepts them or a concrete blocker prevents motion; an explicit motion or material request defaults to `add moment`.

**Done when:** one direction is chosen by the user after reviewing real samples, or the chosen direction is justified by evidence and the sample requirement is recorded as not applicable.

## 4. Design Contract

Write this before editing UI files, for `standard`, `deep`, and `production`:

```
Design Contract
- Structure:
- Information exposure: visible | secondary | hidden; outcome → decision evidence → implementation detail
- Type scale:
- Colour and token roles:
- Component behaviour:
- State treatment:
- Intervention / authored move / ledger: leave simple | craft only | add moment; none | primary plus optional support; candidates, rejected opportunities, source or platform rule, fallback
- Motion: when `add moment`, name the implementation tool and trigger, archetype, easing, duration, layers, and choreography; otherwise `not applicable`
- Anti-slop risks:
- Artifact and review path:
```

Name semantic roles, not adjectives. For type, name display and product registers, role minima and caps, and one application-root token source; a blanket font-size override is not a scale. Source minima stay surface-scoped: a reading-page floor or expressive title ratio never overrides the declared dense product role table. When repairing existing type, classify the failure as register, token scope, blanket override, or role scale, and fix that owning layer once. Stable decisions become tokens, component rules, and state behaviour.

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
- Observations / first-pass defects (before score):
- Composition pass:
- Comprehension gate:
- Strongest authored move:
- Defects:
- Reviewer independence:
- Slop drift / technical noise:
- Decision: ready | refine | pivot | needs artifact
- Return action:
```

Before scoring, write 5-8 blind observations and up to three first-pass defects; then run the Composition Pass. A clean geometry table cannot pass it. Missing, black, blank, stale, or wrong-state evidence is `needs artifact`, not `ready`. Verify in bounded passes: build fully, inspect once with a batch covering the relevant viewports and populated states together, fix everything it shows in one batch, then confirm with at most one more round and stop. Typography evidence includes computed roles, heading share, readable minima, a 200-percent narrow check, and 320 CSS px reflow; layout evidence includes measured panel/toolbar insets, gaps, anchors, overlap or clipping, and a re-measure after each geometry fix.

`ready` requires artifact evidence, every required viewport and state, a passing Observation Gate and Composition Pass, the reference audition, mechanism-landing evidence for every borrowed primary or supplement, no blocking layout, readability, responsive, motion, comprehension, or slop-drift defect, and `Reviewer independence: independent reviewer`. Without an independent reviewer, the highest decision is `refine`. Every other decision names exactly one return action.

**Done when:** a decision is recorded against real evidence, and `ready` is never self-certified.

## Return

When this is not design work, name the failed layer and invoke the owning skill in one hop: `noootwo-product` for an unsettled product path, `noootwo-code-health` for code or performance judgment, `noootwo-debug` for a failure that needs a proven cause. After a handoff or compaction, resume from the capsule and current artifacts; reload this body only when design owns the next step.

## Reference

- `references/intake.md` and `references/direction.md` — reading a request, the Design Read, harness sizing, adopting an existing project, direction exploration, Style Evidence Check, and mechanism translation.
- `references/design-discovery.md` — the discovery pass, influence discovery, fit scoring, and the `.noootwo/style-discovery.md` contract.
- `references/motion.md` and `references/motion-libraries.md` — contextual intervention, opportunity gates, signature motion identity, duration, easing, choreography, register gates, per-platform tools, licence checks, and adapt-or-reject recipes.
- `references/system.md` and `references/craft.md` — tokens, design-system extraction, artifact-family contracts, anti-slop, typography, colour, responsive, and data-UI craft floors.
- `references/review.md` and `references/translate.md` — observation, composition, scoring, safety gates, evidence-backed flags, final review, stack-native implementation, assets, and handoff.
- `references/evidence.md` and `references/notes.md` — verified cases, distilled reference-skill rules, research notes, and cost boundaries.
- `scripts/extract_design_tokens.mjs` — capture real colours, type, spacing, shape, and motion values from a live page, and report drift against a saved baseline.

Missing skill fallback: first try `npx -y skills add noootwo/noootwo-vibe --global --agent codex --skill <name> --yes`; if install fails, take the smallest direct fallback and mark the record `skill-missing: <name>` (for persistence, write the owning file directly).
