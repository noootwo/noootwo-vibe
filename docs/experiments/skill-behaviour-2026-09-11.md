# Skill Behaviour Measurement — 2026-09-11

Evidence for the rewrite recorded in [ADR 0006](../adr/0006-skill-authoring-standard-and-router.md). Two measurements: a static conformance count, and a six-scenario behaviour probe comparing the previous skill text against the rewritten text.

## What this is, and what it is not

This is a **conformance probe**: each run was given one skill set — old or new — and one request, and asked only for the reply it would send. It measures whether the written instruction produces the intended next action.

It is **not** a field study. Each cell is a single run on a single model, and the probe supplies the skill text directly rather than relying on the harness to fire the skill. It supports no claim about rework rates, only about which behaviour the text produces when read.

## Static conformance

Measured from `HEAD` (old) and the worktree (new).

| Skill | Description chars | SKILL.md lines | Reference files | Bare `$noootwo-` refs | Load instructions | `default_prompt` |
| --- | --- | --- | --- | --- | --- | --- |
| `noootwo-workflow` | 525 → 180 | 161 → 91 | 5 → 3 | 31 → 0 | 0 → 1 | yes → no |
| `noootwo-product` | 584 → 188 | 266 → 83 | 3 → 2 | 7 → 0 | 0 → 1 | yes → no |
| `noootwo-design` | 568 → 195 | 121 → 102 | 45 → 9 | 3 → 0 | 0 → 1 | yes → no |
| `noootwo-review` | 497 → 174 | 151 → 90 | 4 → 4 | 12 → 0 | 0 → 1 | yes → no |
| `noootwo-docs` | 429 → 196 | 89 → 64 | 3 → 3 | 8 → 0 | 0 → 1 | yes → no |

Every value now sits inside the budget in `docs/agents/skill-authoring.md`, which the validator enforces. The five `default_prompt` blocks, which duplicated the description at 138–911 characters each, are gone.

## Behaviour probe

Six scenarios, each run against the old text and the new text. Three binary checks per scenario. `✓` = passed, `~` = partial, `✗` = failed.

| # | Scenario | Check | Old | New |
| --- | --- | --- | --- | --- |
| 1 | Vague feature list ("student learning app with AI practice, notes, community, courses, leaderboard, progress") | Asks the frontier in one round | ✗ | ~ |
| | | Each question carries options and a recommendation | ✓ | ✓ |
| | | Does not start building | ✓ | ✓ |
| 2 | Cross-file change plus docs ("add export-to-PDF to settings and update the docs") | Invokes the workflow before editing | ✗ | ✓ |
| | | Routes unsettled product questions to the product skill instead of asking them itself | ✗ | ✓ |
| | | Names the docs step | ✓ | ✓ |
| 3 | Vague UI request ("make the dashboard look better") | Treats the missing product path as the blocker | ✓ | ✓ |
| | | Asks the whole frontier in one round | ✗ | ✓ |
| | | Uses the fixed question format | ✗ | ✓ |
| 4 | Rework ("this is not what I meant at all") | Names the failed layer | ✗ | ✓ |
| | | Routes to the skill that owns that layer | ✗ | ~ |
| | | Avoids another cosmetic edit | ✓ | ✓ |
| 5 | Submit-bound change ("ship it") | Treats submit as a review gate | ✓ | ✓ |
| | | Names the lenses | ✓ | ✓ |
| | | Reports process rather than claiming a pass | ✓ | ✓ |
| 6 | Documentation-only change ("done?") | Checks the documentation impact | ✓ | ✓ |
| | | Classifies the fact into an owning layer | ✗ | ~ |
| | | Records the decision rather than closing silently | ~ | ✓ |

**Score: old 9.5/18, new 16.5/18.**

The gains concentrate where the rewrite aimed. Scenario 2 and 3 show the frontier round working: the old text asked one question per turn and the new text asked the whole answerable set in one round with options and recommendations. Scenario 2 also shows the difference between naming a skill and loading it: the old text asked the product question inside the workflow, the new text treated it as a product decision. Scenario 4 shows the rework table producing a layer diagnosis where the old text asked an open question.

## Where the new text is still weak

- **Scenario 1** asked one question where the new text permits a full round. The single question was arguably correct, because every other decision depended on it — the probe cannot distinguish correct frontier discipline from a missed round. Worth re-running with a scenario whose questions are genuinely independent.
- **Scenario 4 and 6** reached the right behaviour but did not name the owning skill or the target layer explicitly. Both are `~`, not `✓`.
- The probe never exercised the router (`noootwo-ask`), because the router is user-invoked and no probe step fired it. Router reachability is asserted by its `policy.allow_implicit_invocation: false` setting, not measured here.

## Re-running

Re-run when a skill's flow changes. Build the two skill sets, run the same six scenarios, score the same checks, and append the result here rather than replacing it.
