# Design System Setup

Set up `.noootwo/system.md` before task-specific design work. Use [structured-design-spec.md](structured-design-spec.md) so the result is a design contract, not a mood summary.

## Purpose

The design system memory is the durable source of truth for brand behavior, type, composition, and taste boundaries. Without it, drafts tend to be functional but generic.

The memory must not become a second source of truth. It records what is confirmed, what is inferred, and what is missing.

## Source Order

1. Existing `.noootwo/system.md`
2. Code, tokens, component names, and theme files in the current repo
3. Official product screenshots or internal screenshots
4. Brand guidelines, logos, press kits, or product pages
5. Design files, decks, annotated frames, or existing prototypes
6. User-provided references
7. Fallback lineages from [style-lineages.md](style-lineages.md) when brand evidence is incomplete

## Required Output

Update `.noootwo/system.md` with:

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
- `Preservation contract`
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

## Confirmation Rules

- Prefer exact values from code over inferred values from screenshots
- Mark every inferred font, spacing rule, or motion rule as inferred
- If the brand type system is unknown, record the fallback lineage and why it was chosen
- Keep task-specific experiments out of the design system memory unless they are promoted into durable truth
- Record the generic fallbacks that repeatedly weaken outputs for this product
- If screenshots or code disagree with a generated system summary, prefer the actual artifact and record the conflict
- When implementation is likely, refresh `.noootwo/design-tokens.md` instead of leaving style choices only in prose
- Express colors, typography, layout, component vocabulary, motion, and states as role rules with usage limits
- Record permanent rules, variable expression, and task exceptions so reference-inspired work does not become generic during implementation
- If the system memory cannot produce a compact `Do` / `Do not` instruction block for another agent, it is not specific enough
