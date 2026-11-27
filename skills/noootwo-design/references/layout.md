# Layout

Composition first, geometry second. This is the `layout` command.

## Composition

Judge the rendered surface, not the source.

- **Squint:** with detail blurred, can you name the primary element, the secondary element, and the major groups in order?
- **Weight:** does one focal element lead, with supporting elements stepping down? If everything has the same weight, nothing leads.
- **Grouping:** are related items close and distinct groups separated? If a container is doing the work, proximity is weak.
- **Rhythm:** do tight and generous intervals create a cadence, or is one spacing value repeated until every group feels equal?
- **Density:** does information per region match task frequency, decision complexity, audience, and error cost?
- **Topology:** do items that should share an edge resolve to one anchor? Does the structure match the content rather than a framework default?

## Geometry

Measure the regions that changed, the regions the user named, and the regions the contract declares. For `build` and `direction` work, also measure one representative region per visible group.

Record per region and state:

```text
Surface / state | Region | Selector | Container | Inset T/R/B/L | Inner gap | Outer gap | Alignment anchor | Overlap / clip | Verdict
```

- Single-row regions such as toolbars, tabs, filter rows, and control clusters have matching top and bottom insets unless an intentional attachment is recorded.
- When spacing alone communicates grouping, the space around a group exceeds the space inside it.
- Items expected to share an edge resolve to one alignment anchor within tolerance.
- Siblings do not overlap; child content stays inside its container.
- A source padding value is a lead. The rendered inset is evidence.

## Responsive and extremes

Check `320`, the shipped phone width, tablet, desktop, and roughly `200%` zoom or an equivalent narrow viewport.

- No horizontal overflow.
- No critical heading, navigation item, or button off-screen.
- No clipped or orphaned text.
- The primary action stays visible and reachable.
- A fixed or sticky bar does not cover the last field, its focus ring, or the final copy.
- Long CJK and mixed-language text wraps without widening the document.

## Fix and close

Fix the composition and geometry findings in one batch. Re-measure every closed finding with the same selector, then sweep all rows once.

`layout` is done when the reading order holds, the measured regions pass, the required viewports reflow, and the primary action remains visible.
