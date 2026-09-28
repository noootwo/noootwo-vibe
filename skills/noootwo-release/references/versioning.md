# Versioning

Versioning makes compatibility visible and gives every release a stable identity.

## Version Source Of Truth

Choose one authoritative source and record it as a decision through `noootwo-state`. Default precedence when the project has no policy:

1. A declared release policy or release document.
2. Package or application manifest.
3. `VERSION` file.
4. Git tag.

A tag points to a version; it never creates one. Mirror files and manifests are caches, not additional authorities. When sources disagree, name the conflict, choose the owner, update the mirrors, and record the migration.

## Semantic Versioning

Use Semantic Versioning by default for libraries and services:

- `MAJOR` for incompatible public API changes.
- `MINOR` for backward-compatible functionality.
- `PATCH` for backward-compatible bug fixes.
- Pre-release and build metadata are extensions, not replacements for the core version.

The public API must be declared and precise enough to classify changes. For applications, a SemVer plus build number is acceptable when the product has a different release cadence. API, schema, config, and data versions are separate versions linked from the Release Plan.

If a project uses a non-SemVer scheme, record why, how compatibility is communicated, and how rollback identifies the previous release.

## Changelog And Release Notes

- Keep an append-only changelog with categories such as Added, Changed, Deprecated, Removed, Fixed, and Security.
- Release notes name user-visible changes, migration steps, deprecations, known risks, and the previous release.
- Do not rewrite a released entry. A correction creates a new entry and, when necessary, a new patch release.
- The changelog may be generated from commits, but the release record is the authority.

## Compatibility And Deprecation

For every release, record:

- what changed in the public API, schema, config, or data contract;
- who must migrate and by when;
- the compatibility window and the fallback path;
- the deprecation notice and removal version;
- the verification that old and new forms coexist safely.

## Done When

One version source is authoritative, the next version follows from compatibility, the changelog and notes are complete, and every mirror or tag agrees with the chosen source.
