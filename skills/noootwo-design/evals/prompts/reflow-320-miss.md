# Eval Prompt: Reflow 320 Miss

Use `$noootwo-design` on a settings surface that looks correct at `1440px` and
`390px`, but at `320` CSS px the toolbar and a two-column form force horizontal
scrolling and clip the save action. There is no text overflow at the wider
viewports, so the usual desktop and phone screenshots look calm. The user asks
for a final readiness check.

Expected behavior:

- Inspect the `320` CSS px reflow state, not only the `390px` phone viewport or
  a `200%` zoom of a wide window.
- Record the unintended two-dimensional scrolling and the clipped primary
  action as blocking defects with measured evidence.
- Run the responsive check and choose `fix`.
- Keep the desktop and phone evidence, but do not let it override the narrower
  failure.
- Re-check the repaired state at `320` before `ship`.

Failure signals:

- Treats `390px` or `200%` zoom as a substitute for `320` CSS px reflow.
- Declares shipping from desktop and phone screenshots alone.
- Calls the failure a cosmetic issue because only one viewport is affected.
- Fixes an unrelated typography or copy issue instead of the reflow defect.

Manual evaluation: pass only when the response catches the `320` reflow failure
and blocks `ship`.
