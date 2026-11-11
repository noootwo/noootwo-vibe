# Eval: Delivery records custody and merges frozen SHAs

Prompt: "Set up two write-fanout lanes, then rejoin them. The workers have task handles, but the plan only names their branch names."

Expected:

- Adds worker/task, collection/stop, liveness source, lease times, evidence handoff path, exact base SHA, and required rejoin order to the Lane Map before dispatch.
- Leaves the result commit unknown until the Result Packet; it never predicts the worker's exact commit.
- Collects a terminal Result Packet with an exact commit from each lane.
- Reviews and merges the frozen commit, not a later branch tip.
- Keeps state writes with the integrator and updates only when the frontier changes.

Fails when: it dispatches using branch names alone; it merges moving tips; or it lacks enough custody to recover a running or orphaned lane.
