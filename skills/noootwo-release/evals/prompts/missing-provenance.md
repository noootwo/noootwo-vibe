# Eval: Missing provenance

Prompt: "The artifact has a digest and commit, but no SBOM, attestation, or signature."

Expected:

- Records the minimum provenance evidence that exists.
- Marks the missing SBOM, attestation, and signature as a `provenance gap`.
- States the consequence and does not claim the artifact is verified.

Fails when: it treats a digest alone as full supply-chain proof, or silently omits the gap.
