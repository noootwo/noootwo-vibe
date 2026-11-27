# Design Probe Fixture

An operations settings page with five planted defects. The fixture is read-only
evidence for the design probe and review contract; do not treat a repair of this
copy as product work.

| ID | Defect |
| --- | --- |
| D1 | The blue summary outranks the editing task, and the primary action has no priority |
| D2 | `320x800` keeps a `536px` scroll width and clips the save action |
| D3 | The fixed save bar covers the focused time-zone select at `1440x900` |
| D4 | Helper and muted text measure `3.03–3.66:1` |
| D5 | Design-rationale copy leaks into the product surface |

Run:

```bash
python skills/noootwo-design/scripts/design_probe.py \
  docs/experiments/fixtures/design-probe \
  --out /tmp/design-probe --browser-channel chrome --allow-blockers
```

Expected blockers include `horizontal-overflow`, `fixed-bar-overlap`,
`focus-obscured`, `text-contrast`, and `control-contrast`. The repaired copy in
the measurement record must return zero blockers.
