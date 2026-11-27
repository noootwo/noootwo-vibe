# Critique

Find the real defect in the rendered artifact. This is the `critique` command, and it is separate from building.

## Hard invariants

1. **Resolve one target.** A file path, URL, preview, simulator, or recording. Prefer a path over a drifting dev-server URL.
2. **Validate evidence first.** Run `python scripts/design_probe.py <target> --out .noootwo/design`. A missing, black, blank, stale, wrong-region, or wrong-state capture is `recapture`; stop and recapture before judging.
3. **Assessment A before Assessment B.** The design assessment must finish before probe findings enter the synthesis. Detector output anchors judgment; do not let it lead.
4. **Isolate when already available.** If the host already provides an isolated reviewer without new delegation, use it. Otherwise run the design assessment and the probe as separate sequential passes and prefix the result `DEGRADED: single-context (<reason>)`.
5. **Four dispositions only:** `recapture`, `rebuild`, `fix`, `ship`.
6. **A builder-only review may `ship` local work** when the probe has no blockers and the record says `local_only: true`. Production or publish requires `reviewer: independent`.

## Assessment A: design

Look at the rendered surface as a user, before reading the probe. Write five to eight plain observations and up to three first-pass defects. Name one thing that must not change.

- **First screen:** can the primary user say what this is, what to do next, and what it costs to be wrong?
- **Reading order:** squint. Can you still name the primary element, the secondary element, and the major groups in order?
- **Visual weight:** does one focal element lead? Does the primary action read as primary, or does a decorative summary outrank it? If a decorative metric, image, or panel outranks the task, record a hierarchy defect and choose `fix` or `rebuild`, not an advisory.
- **Grouping and proximity:** are related items close and groups distinct, or are containers compensating for weak spacing?
- **Rhythm and density:** do tight and generous intervals create a cadence, or is one spacing value repeated until every group is equal?
- **Alignment and topology:** do items that should share an edge resolve to one anchor? Does the structure match the content?
- **Type:** are display and product registers visibly separate? Does the main heading leave the primary task visible? Do helper and metadata roles stay readable without a blanket override?
- **States:** do loading, error, empty, disabled, focus, and long-copy states preserve reading order, focus order, and hierarchy?
- **Copy:** does each heading name the user's object, task, or next action? Do errors state what happened and what to do? Is design rationale, a requester-facing note, or an implementation term leaking into the product surface?
- **Adaptation:** at narrow, intermediate, wide, zoomed, and localized states, what reorders, collapses, wraps, scrolls, clips, or stays fixed?

Composition is a judgment. A clean geometry table cannot pass it, and a calm screenshot does not prove it.

## Comprehension

Test the rendered surface as the primary user, not the requester, developer, or
agent:

- Can they say what this is, what to do next, and what a mistake costs?
- Do labels use their vocabulary, with evidence for any shared domain term?
- Does every mechanism term (renderer, tier, frame rate, library, internal
  status) support a user decision, or move to a diagnostics layer?
- Does every note prevent an error, explain a consequence, support recovery,
  or teach a term needed now?
- Do settings name the user's outcome or a good default, not the mechanism that
  implements it?

A failed check is a blocking `copy` finding. The artifact returns `fix`, or
returns to `noootwo-product` when the audience or main path is unsettled.

## Assessment B: probe

Read `.noootwo/design/probe.json` only after Assessment A is recorded.

- Treat each probe finding as a lead, then confirm it against the named screenshot or the live state.
- Keep a finding only when the rendered evidence and the design judgment agree.
- A probe may miss hierarchy, rhythm, taste, or a misleading label; Assessment A owns those.
- A probe may catch overflow, clipping, focus occlusion, contrast, touch targets, and unlabeled controls that a quick look misses.

If the probe and the screenshot disagree, reopen the state or viewport that produced the mismatch before deciding.

## Dispositions

- `recapture` — the evidence is missing, invalid, stale, or the wrong state. Do not score or fix from it.
- `rebuild` — the direction, information architecture, or structure is wrong. Polishing it would waste the loop.
- `fix` — the direction is right and local defects remain. Name exactly one return action.
- `ship` — no blocking defect remains, evidence covers every required viewport and state, and the probe has no unwaived blocker. Local builder-only work records `local_only: true`; production records an independent reviewer.

## Output

Write `.noootwo/design/review.json` with the target, command, viewports, states, findings, disposition, reviewer, `local_only`, and next action. Keep the chat response short: what leads, what fails, the evidence, and the disposition.

Do not produce a 28-field review, a score table, or a document per gate. Do not self-certify `ship` when the evidence is missing.

## Bounded loop

- Inspect once with a batch covering the relevant viewports and states.
- Fix everything the inspection shows in one batch.
- Confirm with one more probe. Stop.
- Maximum two full rounds before escalating the trade-off to the user.
