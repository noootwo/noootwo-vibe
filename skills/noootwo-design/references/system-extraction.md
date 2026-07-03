# System Extraction

Persistent design memory lives in `.noootwo/system.md`.

Read [design-system-setup.md](design-system-setup.md) first when the file is missing, stale, or still pending extraction.
Use [structured-design-spec.md](structured-design-spec.md) to write extracted facts as role-based design instructions.

## Source Priority

1. Existing `.noootwo/system.md`
2. Code and tokens in the current repo
3. Current live product or internal screenshots
4. Brand guidelines or component libraries
5. Design files, decks, annotated frames, or existing prototypes
6. User-provided references
7. Industry fallback patterns

## What To Extract

- Brand primitives: colors, marks, imagery, and visual materials
- Source of truth, extraction sources, confidence level, and missing evidence
- Published design system rules or token/component conventions
- Current `.noootwo/design-tokens.md` status or gaps
- Structured design spec: visual positioning, target qualities, anti-position, role rules, and agent guidance
- Preservation contract: permanent rules, variable expression, and task-specific exceptions
- Product purpose and audience
- Tone and writing posture
- Type system: confirmed fonts, fallback logic, hierarchy, and contrast strategy
- Color roles: canvas, surface, text, accent, semantic, and data roles with usage limits
- Component patterns: recurring shells, cards, rails, panels, forms, navigation, and evidence patterns
- Layout density: spacing rhythm, information density, and preferred structural moves
- Motion language
- Shape, material, depth, imagery, iconography, and language rules
- Platform constraints
- Target stack, rendering surface, stack-native component vocabulary, interaction grammar, and motion primitives
- Visual reference library and what each reference is allowed to influence
- Known generic fallbacks that would degrade the work
- Forbidden combinations and "never do this" constraints
- Preservation contract: what must survive implementation, what may vary, and what must never be substituted

## Output Shape For `.noootwo/system.md`

- `Status`
- `Updated From`
- `Source of truth`
- `Extracted from`
- `Confidence`
- `Missing evidence`
- `Published design system rules`
- `Structured design spec`
- `.noootwo/design-tokens.md` status
- `Brand primitives`
- `Product`
- `Audience and jobs`
- `Tone and language`
- `Type system`
- `Color roles`
- `Component patterns`
- `Layout density`
- `Motion language`
- `Shape, material, and depth`
- `Imagery, iconography, and language`
- `Agent design guidance`
- `Known generic fallbacks`
- `Forbidden combinations`
- `Platform constraints`
- `Target stack`
- `Rendering surface`
- `Stack-native component vocabulary`
- `Interaction grammar`
- `Motion primitives`
- `Visual reference library`
- `Refresh triggers`
- `Preservation contract`

## Rules

- Prefer exact values from code over inferred values from screenshots
- If the current file says `Status: pending extraction`, treat it as missing
- Keep project truth separate from task-specific experimentation
- Mark inferred values as inferred
- Update the file only when new information is concrete enough to persist
- Never promote a generated direction into durable system truth unless the user confirms it should become part of the product system
- A usable extraction should let a second agent implement the design without seeing the inspiration source
