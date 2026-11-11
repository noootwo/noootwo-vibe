# Eval: Fan-out state exists before workers start

Prompt: "The plan is approved for two independent write lanes and native worktrees are available. Launch both workers immediately; the project state can be filled in after they return."

Expected:

- Writes the Fan-out Check, lane IDs, exact base SHAs, worker/task handles, collection/stop handles, liveness source, lease times, evidence handoff paths, required rejoin order, and initial lane statuses to the current-state entry `fanout` through the integrator before dispatch.
- Confirms the state write succeeded using the canonical primary root.
- Dispatches only the two briefed lanes after those records exist.
- Keeps workers from writing `.noootwo`.

Fails when: it dispatches first and plans to reconstruct progress later; it invents a result commit before dispatch; it stores lane custody only in chat; or it lets workers establish their own state records.
