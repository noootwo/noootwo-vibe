# 0013 — `noootwo-state` owns migration of legacy records

## Status

Accepted.

## Context

The persistence model changed from several specialist-owned Markdown files to a single
abstract state standard. Existing projects still have the old files, and taking them over
manually would require each specialist to re-read and re-write its own history.

`noootwo-state` must stay abstract and cannot decide from the content whether an old file
is a decision, narrative, evidence, or current state.

## Decision

- Add a `migrate` command to `noootwo_state.py` that consumes a migration manifest.
- The manifest supplies only abstract properties for each old file: `path`, `request_id`,
  `fact_type`, `query_profile`, `mutability`, `lifespan`, and optional `owner_skill`,
  `domain`, and `destination`.
- The skill reads the old file as content, persists it through the normal form selection,
  records the old path as `replaces`, and archives the source under
  `.noootwo/state/legacy/<path>` unless `--keep` is passed.
- The caller supplies the classification; `noootwo-state` never interprets content.

## Consequences

- Old specialist files can be migrated in one pass without re-embedding persistence logic
  in the specialists.
- The migration is non-destructive by default: the source moves to the legacy archive.
- The abstract-only boundary is preserved; no domain-specific field names or judgments
  enter `noootwo-state`.
