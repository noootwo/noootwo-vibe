# Rollback And Recovery

Every release plan names how the system returns to a known-good state.

## Choose The Recovery Path

| Condition | Default path |
| --- | --- |
| previous artifact is compatible with current data and config | roll back to the previous immutable release |
| schema or data change is not backward compatible | forward-fix or expand/contract migration |
| behavior is risky but not deploy-wide | feature flag or kill switch |
| rollout is partial and can be halted | canary or blue/green rollback |
| recovery is manual and slow | record the runbook, owner, and expected time to restore |

## Migration Compatibility

Prefer expand/contract migrations: deploy the additive change, migrate data and consumers, then remove the old shape in a later release. If a rollback would break data or config, the release plan must say so before deployment.

## Rollback Evidence

Record:

- previous release ID and artifact digest;
- configuration and schema compatibility;
- command or runbook;
- data migration state;
- feature flags or kill switches;
- expected recovery time;
- verification after rollback;
- forward-fix path when rollback is impossible.

## Done When

A responder can identify the previous known-good release, execute the recovery path, verify the restored version, and explain what cannot be reversed.
