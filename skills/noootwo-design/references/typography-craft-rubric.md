# Typography Craft Rubric

Use this before marking standard or deep UI work ready. Typography must prove intentional hierarchy, not just a font change.

## Required Decisions

Record these in `.noootwo/directions.md`, `.noootwo/review.md`, or `.noootwo/design-tokens.md`:

- Font choice and fallback: why the family fits the product, and what fallback preserves metrics.
- Display/body contrast: family, width, weight, case, or rhythm contrast.
- Type scale: fixed `rem` scale for dense app UI; fluid `clamp()` only where display text benefits.
- Weight roles: which weights serve headings, labels, body, captions, and numbers.
- Line-height and line length: headings tight but not clipped; body readable; long text constrained with `ch` where useful.
- Letter spacing: intentional small-caps/uppercase tracking; avoid default-everywhere or over-tight display text.
- Mobile display cap: max title size and wrapping behavior at phone width.
- Numeric behavior: `tabular-nums` for tables, metrics, ledgers, timers, and aligned values.

## Failure Flags

Any of these prevents `ready`:

- Overweight display type that crushes the composition.
- Display headline clips, overflows, or creates accidental orphan words on mobile.
- CJK display text is oversized or overweight enough to make the app feel like a poster instead of a product screen.
- Chinese and English labels fight for attention, especially when uppercase English labels are decorative rather than functional.
- Body text below 16px on web without a product-specific density reason.
- Arbitrary type sizes that do not follow a scale.
- More than 2-3 families without a clear system reason.
- Lazy monospace as the only signal for technical, industrial, or premium mood.
- Display/body contrast is absent, or too similar to read as a decision.
- Letter spacing is visibly random or makes text harder to read.
- Mobile app hierarchy depends on huge bold CJK type instead of a controlled scale, spacing, and state model.

## Review Action

- If the concept is right but type craft fails, set decision `refine` and `Return action: return to typography pass`.
- If typography is the main point of view and it fails structurally, set decision `pivot` or return to directions.
- Do not let clean spacing compensate for weak type hierarchy.
