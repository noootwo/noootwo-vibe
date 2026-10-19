# 0022 — Project specs and plans use Noootwo-owned document layers

## Status

Accepted.

## Context

External installed skills can contribute useful methods, but some also prescribe
their own project directory, such as `docs/superpowers/specs/` and
`docs/superpowers/plans/`. A project that follows Noootwo document ownership
must not let an execution resource silently become the authority for its
durable product, design, or implementation records.

The gap existed because `noootwo-state` owned persistence but did not name a
layer for accepted specifications or their implementation plans. When no
Noootwo-owned destination exists, an external skill's default path becomes the
path of least resistance and the two conventions mix.

## Decision

1. Accepted cross-functional product, UX, and system design contracts are
   `spec` facts and live in `docs/specs/`.
2. Implementation sequences tied to an accepted spec are `plan` facts and live
   in `docs/plans/`.
3. `.noootwo/specs/active-design.md` remains the active task design contract,
   not durable project-wide truth.
4. External skills remain valid execution resources, but their default output
   directories do not override the project's document layers. Durable output is
   persisted through `noootwo-state`.
5. Existing directories created by an external skill are read-only legacy.
   Migrating them requires explicit project-owner approval, moves the current
   facts into the owning layers, and updates every reference in the same pass.
   A mixed layout is not an accepted end state.
6. `noootwo-product` may persist a settled result as a spec, but a small
   checkpoint does not require a document merely because a spec path exists.
7. `noootwo-workflow` checks external-skill output at close time and routes
   durable artifacts to the Noootwo layer.

## Consequences

- Project specs and plans have stable, skill-neutral locations.
- A borrowed workflow can still be used without importing its project layout.
- The owner may approve one complete path migration; until then, legacy
  directories stay read-only and new work uses the canonical layers.
- The state protocol gains `spec` and `plan` fact types, so the placement is
  explicit rather than inferred from file names.
