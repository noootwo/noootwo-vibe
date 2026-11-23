# Eval Prompt: Layout Geometry Toolbar Miss

Use `$noootwo-design` on a dense desktop workspace after a toolbar change. The
top toolbar contains a second row of filter chips. At first glance the page
looks composed and clean, and the rest of the screen has no obvious defect. The
toolbar CSS contains `padding: 0 28px 14px`. The user points at the filter row
and says the tags are too close to the top and have more space below, then asks
for a real review rather than another pass over unrelated areas.

Expected behavior:

- Name the toolbar/filter row as the measured region and locate its owning
  container before proposing a repair.
- Inspect the populated rendered state and report the rendered top and bottom
  insets as numbers. Identify the `0px` versus `14px` vertical asymmetry.
- Check the region's inner gaps against its outer gaps, its left alignment
  anchors, sibling overlap, and clipping.
- Block `ready` on the measured geometry failure even if the overall screenshot
  looks calm.
- Choose `return to artifact` for the local layout defect, fix the owning
  container, and re-measure the same selector before finishing.
- Leave unrelated typography, copy, and composition alone unless measured
  evidence shows a separate defect.

Failure signals:

- Praises the overall composition and declares the page ready.
- Changes typography, copy, spacing elsewhere, or redesigns an unrelated area
  without locating the failing region.
- Treats the user's description as a style preference instead of checking the
  rendered inset.
- Reports only a screenshot impression with no top/bottom measurement.
- Fixes the toolbar but does not re-measure it or sweep the other geometry rows.
- Claims a geometry pass from source CSS alone when the populated rendered
  surface was available.

Manual evaluation: pass only when the response produces the measured region
evidence, blocks readiness on the asymmetry, and re-measures after the fix.
