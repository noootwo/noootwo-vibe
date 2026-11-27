---
name: noootwo-design
description: "Use for UI, visual, artifact, or frontend work after product path is settled: screens, tokens, critique, motion, or reference replication."
---

# Noootwo Design

Design is judged by the rendered artifact, not by the prose around it. Name the target root before editing; a project supplied as a case, reference, or comparison is read-only unless the user asks to change it. A report that a surface looks wrong, or a question about it, is `propose`: present the change and stop. When the mandate is unclear, invoke the `noootwo-workflow` skill: read its `SKILL.md` and follow its Mandate Gate. When the real user, audience contract, main path, states, or acceptance are unsettled, invoke the `noootwo-product` skill first: read its `SKILL.md` and follow it.

Context lifecycle `write -> select -> compress -> isolate -> verify`: load this body and one command reference; route references over 200 lines through headings or query hits; cap live excerpts at 80 lines; put output over 16 KiB in cold evidence with a path and hash; isolate the design assessment from the probe where possible; keep one writer for the review record; verify every claim against a rendered capture.

Read the current UI and its tokens before choosing a command. Load one command reference, not the whole library. `references/craft.md` is the shared quality floor; read it before any UI edit. `references/system.md` owns tokens and design systems; `references/translate.md` owns stack-native implementation.

## Commands

| Command | Use when | Reference |
|---|---|---|
| `shape` | The surface, audience, or direction is unsettled | `references/shape.md` |
| `build` | A new surface, redesign, or approved comp | `references/build.md` |
| `critique` | Review an existing rendered artifact | `references/critique.md` |
| `polish` | A local change inside an existing system | `references/polish.md` |
| `layout` | Spacing, rhythm, hierarchy, or responsive defects | `references/layout.md` |
| `typeset` | Type scale, roles, or readability | `references/craft.md` (typography) |
| `harden` | States, errors, i18n, accessibility, edge cases | `references/harden.md` |
| `motion` | Motion or material is part of the brief | `references/motion.md` |
| `system` | Tokens, components, or design-system extraction | `references/system.md` |
| `direction` | Direction is genuinely unresolved | `references/direction.md` and `references/design-discovery.md` |
| `translate` | Contract to stack-native implementation | `references/translate.md` |

Routing:

- No argument: name the command you infer and why, then proceed when the mandate allows. Ask only when two commands fit and the choice changes cost or direction.
- A critique, audit, or review request: `critique`.
- A small local change inside an incumbent system: `polish`.
- A mixed repair of an existing surface: `critique` once, then apply the findings as `polish` or the matching single-axis command.
- A new surface or redesign: `shape` when direction is unsettled, then `build`.
- A layout-only request: `layout`. A copy-only request: `harden`. A motion-only request: `motion`.
- Do not run `direction` or a reference audition when the incumbent direction is clear.

## Non-negotiables

- **Render before judging.** A source read, DOM query, or prose description is not evidence. Missing, black, blank, stale, or wrong-state evidence returns `recapture`.
- **Critique is separate from build.** Design judgment comes before detector or probe findings. If the host already provides an isolated reviewer without new delegation, use it. Otherwise run the design assessment and the probe as separate sequential passes and prefix the result `DEGRADED: single-context`.
- **Critique changes no product file.** It may write the probe and review record under `.noootwo/`; those are evidence, not a product edit.
- **Four dispositions only:** `recapture`, `rebuild`, `fix`, `ship`. Every other word is a finding, not a verdict.
- **Builder-only review may `ship` local work** when the probe has no blockers and the review records `local_only: true`. Production or publish requires `reviewer: independent`.
- **Bounded loop:** build or fix in one batch, inspect once, fix what the inspection shows in one batch, confirm once, stop. Two full rounds maximum.
- **Evidence budget:** one `probe.json`, one short review record, and the screenshots the probe names. Do not create a document per gate.

## Render gate

Before `ship`, run:

```bash
python scripts/design_probe.py <target> --out .noootwo/design
```

It writes `.noootwo/design/probe.json`, one primary capture per viewport and state, and a bottom capture only where fixed-bar overlap or focus occlusion is detected. The primary is full-page when the document scrolls, and the visible viewport for app-shell layouts. Drop states the surface cannot enter with `--state`; keep at least `default`. A missing or invalid capture is `recapture`. The probe is evidence, not judgment: a clean probe cannot prove hierarchy, composition, or taste.

## Review record

Write `.noootwo/design/review.json` (or `.noootwo/review.json` for a single-artifact project):

```json
{
  "target": "index.html",
  "command": "critique",
  "viewports": ["320x800", "390x844", "768x1024", "1440x900"],
  "states": ["default", "error", "loading", "focus", "long"],
  "findings": [
    {
      "severity": "blocking",
      "region": "settings grid",
      "evidence": ".noootwo/design/shots/320x800-default.png"
    }
  ],
  "disposition": "ship",
  "reviewer": "builder",
  "local_only": true,
  "next_action": "none"
}
```

`ship` requires no blocking finding, valid evidence for every required viewport and state, and a passing probe. `recapture` means the evidence is unusable. `rebuild` means direction or structure is wrong. `fix` means local defects remain.

Validate with:

```bash
python scripts/validate_design_evidence.py <root>
python scripts/validate_design_evidence.py <root> --production
```

## Return

When this is not design work, name the failed layer and invoke the owning skill in one hop: `noootwo-product` for an unsettled product path, `noootwo-code-health` for code or performance judgment, `noootwo-debug` for a failure that needs a proven cause. After a handoff or compaction, resume from the capsule and current artifacts; reload this body only when design owns the next step.

## Reference

- `references/shape.md` — intake, design read, direction only when unresolved, contract.
- `references/build.md` — new surface or redesign, one contract, render, bounded critique.
- `references/critique.md` — evidence validity, isolated assessments, four dispositions.
- `references/polish.md` — local change inside an incumbent system.
- `references/layout.md` — composition, geometry, responsive, extremes.
- `references/harden.md` — states, errors, i18n, accessibility, copy.
- `references/craft.md` — the shared quality floor, typography, colour, anti-slop.
- `references/system.md` — tokens, components, extraction.
- `references/motion.md` — motion and material decisions.
- `references/direction.md` and `references/design-discovery.md` — only when direction is genuinely unresolved.
- `references/translate.md` — stack-native implementation and handoff.

Missing skill fallback: first try `npx -y skills add noootwo/noootwo-vibe --global --agent codex --skill <name> --yes`; if install fails, take the smallest direct fallback and mark the record `skill-missing: <name>` (for persistence, write the owning file directly).
