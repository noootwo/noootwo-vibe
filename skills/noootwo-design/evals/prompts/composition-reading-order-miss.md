# Eval Prompt: Composition Reading Order Miss

Use `$noootwo-design` on a dense dashboard where three panels have equal visual
weight, the primary task sits below the first viewport, and the only action is
the same size and colour as the filters. There is no overflow, clipping, or
overlap, so a geometry-only pass is clean. The user says the page looks fine and
asks whether it is ready.

Expected behavior:

- Write 5-8 plain observations and up to three first-pass defects before
  reading the probe findings or describing the page as shippable.
- Run the design assessment: squint test, primary and secondary reading order,
  grouping, focal weight, rhythm, and density.
- Name the equal-weight panels and buried primary action as composition
  defects, with the viewport and rendered evidence.
- Keep the clean geometry result as supporting evidence, not as a pass for
  composition.
- Return to the artifact, rebalance the focal hierarchy, and re-inspect the
  populated state before claiming `ship`.

Failure signals:

- Reports only overflow, clipping, and spacing because those checks pass.
- Calls the page shippable because the geometry table is clean.
- Changes typography, colour, or copy elsewhere without naming the reading-order
  defect.
- Reads the probe before recording the design assessment.
- Claims production `ship` without an independent reviewer.

Manual evaluation: pass only when the response records the observations,
catches the reading-order and visual-weight defects, and blocks `ship`.
