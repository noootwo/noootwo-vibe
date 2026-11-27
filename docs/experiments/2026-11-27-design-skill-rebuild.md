# Design Skill Rebuild Measurement — 2026-11-27

This record compares the old `noootwo-design` lifecycle with the command-routed
rebuild on one rendered operations-console fixture. It is a mechanism check, not
a statistical claim about defect recall.

## Fixture

`docs/experiments/fixtures/design-probe/index.html` is a notification-settings
page with five planted defects:

| ID | Defect |
| --- | --- |
| D1 | The decorative summary outranks the editing task, and the primary action has no priority |
| D2 | At `320` CSS px the page keeps a `536px` scroll width and clips the save action |
| D3 | The fixed save bar covers the focused time-zone select at `1440` |
| D4 | Helper and muted text measure `3.03–3.66:1` |
| D5 | “Configuration Surface”, “Signal density”, and “Optimized clarity” leak design rationale into the product surface |

The page supports `default`, `error`, `loading`, `focus`, and `long` states
through query parameters.

## Earlier Comparison

| Arm | Task | Defects | Time | Evidence / outcome |
| --- | --- | ---: | ---: | --- |
| A | Baseline critique | 5/5 | 342s | Short report |
| D | Old skill critique | 5/5 | 315s | Structured report; no extra recall |
| E | Baseline repair | 4/5 | 343s | Short report |
| F | Old skill repair | 5/5 | 335s | 80+ files, returned `refine`, readiness validator reported 22 errors |

The old skill added hierarchy and document volume. It did not add defect recall
on this fixture. Its own review format failed its readiness validator, and the
validator accepted a fake review with a nonexistent screenshot once the expected
documents were present.

## Rebuild Runs

| Arm | Task | Defects | Time | Evidence / outcome |
| --- | --- | ---: | ---: | --- |
| G | New skill critique | 5/5 plus navigation and mobile-header findings | 344s | No product files changed; 71 probe blockers |
| G2 | Final skill critique | 5/5 plus navigation, save-label wrapping, and loading-truthfulness findings | 347s | Hierarchy recorded as a release-blocking finding; 36 valid captures |
| H | New skill repair | Mechanical D2-D5 fixed; D1 primary action improved, summary weight still debatable | 517s | `ship`, builder review, `local_only: true`; 23 evidence files |

G used the design assessment before the probe and produced a `fix` disposition.
It recorded the `320` overflow, fixed-bar overlap, `1440` focus occlusion,
`3.03–3.67:1` text contrast, `1.47:1` control boundaries, and the design-rationale
copy. It also found missing navigation parity below `900px`.

G2 is the final hierarchy check. It names the saturated summary, the page title,
and the outlined save action as one hierarchy defect and returns `fix`; the new
reference now says a decorative metric that outranks the task is a hierarchy
defect, not an advisory.

H repaired the fixture and the final probe reported zero blockers. It made the
save action primary and removed the design-rationale copy, but the blue summary
still carries high visual weight. A builder can ship that local trade-off with
`local_only: true`; an independent reviewer may still send it back as `fix`.
This is the intended boundary: the probe cannot decide hierarchy, and `ship` is
not a universal quality certificate.

Its evidence set was one `probe.json`, one short `review.json`, one probe report,
and twenty captures. The final validator accepted `ship` with a builder review
and `local_only: true`.

## Probe Regression

| Target | Blockers | Captures |
| --- | ---: | ---: |
| Original demo | 71 | 36 |
| H repair | 0 | 20 |

The original demo still reports horizontal overflow, offscreen headings,
fixed-bar overlap, focus occlusion, text contrast, and input boundaries. The
repaired page reports none. Advisories remain for secondary-button boundaries,
small targets, and gradient contrast that the probe cannot resolve.

The G and H behavior runs used the command-routed skill before the final probe
fixes for nested scroll containers and evidence budgeting. H's repaired artifact
was re-probed and re-validated with the final code: zero blockers, 23 files, and
a passing builder-local `ship`. The defect result did not change.

## Validator Probes

The final validator passed a valid `ship` fixture and rejected:

- a missing capture;
- a finding whose evidence path does not exist;
- a builder review without `local_only: true`;
- a builder review under `--production`;
- `ship` with a remaining probe blocker;
- `fix` without a next action;
- a review matrix that does not match the probe.

## Limits

- One fixture, one model, and one host. The numbers are not a benchmark.
- The design assessment still depends on model judgment for hierarchy,
  composition, and taste.
- The probe is web-oriented. Flutter, SwiftUI, Compose, slides, and fixed-canvas
  artifacts need their own capture source and viewport names.
- No claim is made that the new skill reduces production rework outside this
  fixture.
