# noootwo-ask Releases

## v0.5.0

- Reordered the main flow so `noootwo-code-health` appears before `noootwo-tdd`: shape a non-obvious implementation, then write behavior-code, then return to code-health for review.
- Added the standalone and choosing-between cases for implementation shape, backend design, and frontend integration.

## v0.4.0

- Added `noootwo-release` to the main flow, on-ramps, standalone routing, and choosing-between table for version, tag, deployment, rollback, and release-trace work.

## v0.3.0

- Updated the router from `noootwo-review` to `noootwo-code-health`; the target capability is unchanged.

## v0.2.0

- Added `noootwo-tdd` to the main flow, choosing table, and standalone list.
- Replaced the `noootwo-docs` slot with `noootwo-state` for record and context placement, and updated the public set to ten skills.

## v0.1.3

- Sharpened the router description so it does not turn a UI mention into a product or design decision.

## v0.1.2

- Names eight specialists instead of six, adding `$noootwo-research` and `$noootwo-onboard`.
- Added the on-ramps and the choosing-between rows for outside evidence, project entry, and "something works but is too slow, too big, or too expensive" — the last routes to `$noootwo-review`, not `$noootwo-debug`.


## v0.1.1

- Names six specialists instead of five, adding `$noootwo-debug`.
- A broken thing now routes to `$noootwo-debug` as the on-ramp, with `$noootwo-workflow` added when the fix spans several files, skills, or a release.
- Added the debug row to the choosing-between-two table.


## v0.1.0

- Added the router: the only user-invoked skill in the suite, switched with `policy.allow_implicit_invocation: false` so it costs no context load.
- Names the five specialist skills, the order to run them in, and how to choose between two of them.
- Introduced alongside the authoring standard and invocation model in `docs/agents/`, per ADR 0006.
