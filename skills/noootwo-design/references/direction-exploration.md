# Direction Exploration

Direction work explores materially different art directions before drafting. Use [structured-design-spec.md](structured-design-spec.md) so every direction can become a concrete design language, not a vibe.

## When

Produce 3 directions for `standard` and `deep` design work. Skip only for `quick`, `review`, `extract-system`, handoff-only, or explicit minor polish/stay-close requests.

Directions are a user-facing decision menu, not internal notes. Present the menu, recommend one direction, and wait for user selection before implementation unless the user explicitly delegates the choice.

For full redesign requests such as "redo all UI", "start over", "all design from scratch", or "do not use the current visual language", the direction menu is a hard blocking checkpoint.

## User-Facing Direction Shape

Write `.noootwo/directions.md` with:

- recommended direction and why
- full redesign trigger when relevant
- user selected direction, or `not selected yet`
- user decision gate: whether a choice is required, the exact question, options, recommendation, user selection, and whether the user delegated the choice
- 3 named directions
- surface type and why the chosen source pool fits
- for each direction: discovery method, case links the user can open, source evidence URL or screenshot, borrowed mechanisms, influence mechanism mix when used, mechanism-library match, rejected surfaces, calibration relationship, lineage/tone, unforgettable move, design-spec delta, type/color/density, typography craft, component/shape language, motion thesis, artifact strategy, why rare, what must never happen, mimicry risk to reject
- for each direction: must-preserve, allowed-variation, forbidden-substitution, signature-mechanism, token-target, component-target, and motion-target

## Internal Preflight

Before drafting, confirm:

- the 3 directions differ in type, structure, density, mood, component language, and motion
- each direction has a design-spec delta: color roles, type roles, layout model, component vocabulary, motion thesis, and forbidden moves
- each direction states what must survive translation into tokens and implementation, what may vary, and what must never be substituted
- product UI directions use product/design-system evidence, while campaign UI directions may use more experimental art-direction evidence
- each direction names how it becomes reviewable
- each direction includes at least one openable case link the user can inspect
- each direction has stack translation
- each direction defines font logic, scale, weight roles, line-height, letter-spacing, and mobile display cap
- no direction is only a palette swap
- no direction defaults to generic SaaS, shadcn-card-wall, or Flutter/native defaults without product reason
- no influence-led direction imitates a designer/artist signature style instead of translating mechanisms
- if options are materially different, `User selected option` or `User delegated choice to agent` is recorded before drafting

If 3 directions share the same opening structure or component skeleton, redo exploration.

If a direction cannot be summarized as implementation rules another agent could follow, return to directions before drafting.

If a required decision is unresolved, do not create artifacts, edit Flutter routes, write handoff, or enter production.
