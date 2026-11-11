# Eval: Every shared-root state write serializes through the integrator

Prompt: "Two write-fanout workers finish together. Each wants to append an `evidence.recorded` event and update `.noootwo/state/current.json` through the primary root before releasing the lane."

Expected:

- Stops both workers from writing state even though they pass the same `--root`.
- Returns each Result Packet and evidence handle to the integrator.
- Has the integrator verify the packets, then serialize snapshot, event, and evidence writes in one process.
- Updates current state only when the goal, decision, blocker, evidence, or next trigger changed.

Fails when: it assumes an atomic file replace makes concurrent read-modify-write safe; it lets workers append events; or it mirrors both packets as independent snapshots.
