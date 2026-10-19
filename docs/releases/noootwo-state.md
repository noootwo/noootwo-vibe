# noootwo-state Releases

## v0.3.0

- Added `spec` and `plan` fact types so accepted design contracts and their implementation sequences have explicit Noootwo-owned Markdown layers.
- Project specs now belong under `docs/specs/`; implementation plans belong under `docs/plans/`; `.noootwo/specs/active-design.md` remains the active task contract.
- Another installed skill's default output directory no longer overrides project document ownership. External paths remain read-only legacy unless the user approves a migration.
- Added `spec.recorded` and `plan.recorded` events and self-test coverage for spec and plan destinations.
- An omitted destination now defaults to `docs/specs/<request_id>.md` or `docs/plans/<request_id>.md`; relative custom destinations resolve from the project root.

## v0.2.0

- Added an abstract `migrate` command that ingests old files through a migration manifest and converts them into the current state format without interpreting their content.
- Each manifest entry supplies the old `path` plus `request_id`, `fact_type`, `query_profile`, `mutability`, and `lifespan`; the skill persists the content and records the old path as `replaces`.
- Moved sources are archived under `.noootwo/state/legacy/<path>` by default; `--keep` leaves the source in place.

## v0.1.0

- Replaced `noootwo-docs` with `noootwo-state`.
- Added abstract state/context persistence: a JSON current snapshot, an append-only JSONL event log, and a generated Markdown projection.
- Added property-only format selection for `state`, `event`, `decision`, `narrative`, `release`, `evidence`, and `procedure` facts.
- Added a POSIX shell query helper and a Python standard-library write/validate/render helper.
- Moved workflow state ownership out of `noootwo-workflow`; workflow now reads and records through `noootwo-state`.
- Kept `docs/releases/noootwo-docs.md` as a historical archive.
