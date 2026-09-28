# Deployment Trace

Every deployed environment must expose enough identity to answer which release is running and where it came from.

## Minimum Fields

Use the platform's naming where it already exists; otherwise record these fields:

| Field | Meaning |
| --- | --- |
| `service.name` | deployed service or application |
| `service.version` | release version |
| `vcs.revision` | source commit or revision |
| `build.time` | build timestamp |
| `deployment.environment` | development, staging, production, or project equivalent |
| `artifact.digest` | immutable artifact identity |
| `release.id` | release ledger identifier |

For OpenTelemetry-compatible systems, use the resource semantic conventions such as `service.version` and deployment attributes. For other systems, map the same meaning to the platform's labels or metadata.

## Where The Trace Appears

At minimum, expose the release identity in:

- structured logs;
- metrics resource attributes or labels;
- traces or spans attached to the service;
- a health or build-info endpoint;
- an operator-visible diagnostic surface;
- an optional UI footer or debug panel when users and support need it.

## Verification

After deployment, verify the running environment reports the expected version, commit, artifact digest, and environment. A deployment that cannot report its identity keeps the release open until the gap is recorded.

## Handoff

The trace belongs to the release owner. `noootwo-debug` consumes it to localize a regression; it does not invent version labels or deployment markers.

## Done When

One query on any deployed environment identifies the release, source revision, artifact, configuration, and deployment time.
