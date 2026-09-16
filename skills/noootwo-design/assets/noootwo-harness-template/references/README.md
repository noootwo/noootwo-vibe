# Captured References

One directory per source the direction leans on:

```
.noootwo/references/<slug>/
  source.md      provenance: url, date, evidence level, accessibility, licence
  NN-label.png   the captured screen or section
```

`source.md` shape:

```markdown
# <Source name>

- url:
- captured:
- tool:
- evidence level: real product flow | design system | curated gallery | community signal | single shot
- accessibility: reachable | login required | fallback | unreachable
- attribution and licence:
- capture: ./01-screen.png
```

When a source cannot be opened, record `accessibility: unreachable`, keep the URL and the reason, and move on. A blocked source narrows the evidence; it does not cancel the discovery pass.

This directory holds personal reference. It stays out of version control, is never redistributed, and is never a target to reproduce pixel for pixel. Borrow the mechanism — space, density, rhythm, state grammar, motion behaviour — and leave the artwork, brand assets, and exact composition behind.

Capture values from a reachable page with `scripts/extract_design_tokens.mjs` from the `noootwo-design` skill, then map what was borrowed into `.noootwo/reference-board.md` under `Landed as`.
