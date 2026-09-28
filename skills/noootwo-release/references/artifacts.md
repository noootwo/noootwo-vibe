# Artifacts And Release Identity

Separate build, release, and run. A release must be identifiable after the build environment is gone.

## Build, Release, Run

- **Build**: transform a commit into an immutable executable artifact and its metadata.
- **Release**: bind one artifact to one configuration version, release ID, and deployment plan.
- **Run**: execute that release in an environment without rebuilding or mutating the artifact.

Build once and promote the same artifact through environments. Environment differences belong in configuration, not in a new build.

## Minimum Artifact Identity

Record:

- artifact name and immutable digest;
- commit SHA and source reference;
- release ID and tag;
- build time and build system identity;
- configuration version;
- target environments;
- provenance, SBOM, signature, or the explicit gap.

Do not use a mutable branch name or a floating tag as the release identity.

## Provenance And Supply Chain

The minimum provenance record is artifact digest + commit SHA + build identity. When available, add SBOM, attestation, signature, and reproducibility evidence.

If provenance is unavailable, record `provenance gap` with the missing artifact and the consequence. Do not describe an unverified build as proven. Link the available evidence from the Release Plan through `noootwo-state`.

## Release Ledger

Treat releases as append-only. A release cannot be mutated after creation; any change creates a new release ID. The ledger should answer:

- what artifact is running;
- which source commit produced it;
- which configuration was bound to it;
- when and where it was built;
- who or what approved the release;
- which release it replaced.

## Done When

One artifact can be traced from source commit to release ID, digest, configuration, and environment without rebuilding or guessing.
