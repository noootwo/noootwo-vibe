# Build

Turn a settled path into one running artifact. This is the `build` command.

## Before editing

1. Read the current UI, its tokens, and the nearest component patterns.
2. If the surface, audience, or direction is unsettled, run `shape` first.
3. Read `references/craft.md` immediately before the first UI edit.
4. Read `references/system.md` only when the work touches tokens, a design system, or a new artifact family.
5. Read `references/translate.md` only when the target stack, assets, or handoff format is non-obvious.
6. Read `references/motion.md` only when motion or material is part of the brief.

Do not load the whole library. One artifact, one contract, one quality floor.

## Build

- Build the smallest complete artifact that satisfies the contract.
- Preserve the incumbent identity, content, behaviour, and scope on a repair.
- On a redesign, keep product truth and replace the visual world; do not split the difference into polish on the discarded look.
- Use real content and real states. Empty shells and placeholder cards hide layout defects.
- Let one element lead. Spend boldness in one place and keep the surrounding surface quiet.
- Name the implementation tool for motion; a named library is a commitment, not decoration.

## Render

Run the artifact at the sizes it ships at. For web, the minimum matrix is `320x800`, `390x844`, `768x1024`, and `1440x900`; include the platform's real device classes for native.

For every state the surface can enter, render and inspect the populated view. Drop the rest:

- default
- loading
- error
- empty, when the surface can be empty
- focus, when keyboard or assistive input matters
- long copy and localization, when the surface accepts user or translated text

Then run:

```bash
python scripts/design_probe.py <target> --out .noootwo/design
```

The probe writes screenshots and `probe.json`. A clean probe does not prove hierarchy or composition; it proves the mechanical floor.

## Review and close

Run `critique` once against the rendered artifact. Fix everything the first inspection shows in one batch, confirm with one more probe, and stop. Two full rounds maximum.

`ship` when the probe has no blockers and the review finds no blocking hierarchy, composition, type, state, copy, or accessibility defect. A builder-only review may ship local work with `local_only: true`. Production or publish needs an independent reviewer.

## Done

- The artifact runs and every contract item is visibly present.
- The required viewports and states have valid evidence.
- The probe has no blockers, or every remaining blocker has a named `fix` action.
- The review record has one disposition and one next action.

## Do not

- Read direction references when the incumbent direction is clear.
- Add motion, a font system, or a component library to make the work feel designed.
- Produce a document per gate.
- Call a source read a rendered review.
