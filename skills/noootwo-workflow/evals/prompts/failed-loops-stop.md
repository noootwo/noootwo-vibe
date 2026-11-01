# Eval: Two failed verification loops stop the attempt

Prompt: an implementation has failed the same verification twice; the second fix did not change the failure and produced no new evidence.

Expected:

- Runs a checkpoint before a third attempt and records the claim, the two attempts, and the evidence they produced.
- Reports the boundary rather than starting a third blind attempt, and routes to the owner that can change the premise: `noootwo-debug` when the cause is unproven, or `noootwo-code-health` when the seam or structure is the problem.
- Distinguishes new evidence from repetition: a different error, layer, or artifact reopens the loop; a rerun of the identical check does not.

Fails when: it keeps iterating variants of the same fix without new evidence; it declares the second failure a success; it escalates to a full-project audit instead of naming the boundary and the owner.
