# Release Health

Release health is observed by version, not only by service aggregate.

## Signals

Track at least:

- adoption or traffic share by release;
- error rate and crash-free sessions or requests;
- latency and saturation by release;
- deployment failures and rollback events;
- user-visible regressions introduced by the release;
- time to restore after a failed release.

For process health, DORA's four keys are useful evidence: deployment frequency, lead time for changes, change failure rate, and time to restore. They describe the release system, not an individual change.

## Diagnosis Handoff

When a regression appears:

1. Confirm the affected release ID and environment from the deployment trace.
2. Compare the release against its predecessor.
3. Hand the evidence to `noootwo-debug` for a proven cause.
4. Preserve the release record and do not rewrite earlier entries.

## Done When

The release can be identified in production, compared with its predecessor, evaluated for user impact, and handed to debugging or rollback with evidence.
