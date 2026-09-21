# noootwo-state Releases

## v0.1.0

- Replaced `noootwo-docs` with `noootwo-state`.
- Added abstract state/context persistence: a JSON current snapshot, an append-only JSONL event log, and a generated Markdown projection.
- Added property-only format selection for `state`, `event`, `decision`, `narrative`, `release`, `evidence`, and `procedure` facts.
- Added a POSIX shell query helper and a Python standard-library write/validate/render helper.
- Moved workflow state ownership out of `noootwo-workflow`; workflow now reads and records through `noootwo-state`.
- Kept `docs/releases/noootwo-docs.md` as a historical archive.
