# Eval: Worker results are evidence, not a second state authority

Prompt: "Three write-fanout workers return Result Packets. Each changed files in its own linked worktree and has a green lane check. One also produced a 20 KiB test log and returned the integrator-assigned temp path instead of inlining it. The integrator needs to record progress before merging them."

Expected:

- Treats each Result Packet as evidence with its branch, commit, files, checks, decisions, and conflicts.
- Has the integrator verify the packets and write one current-state update at the canonical root.
- Uses `--root <primary>` from any linked worktree and creates no second `.noootwo`.
- Verifies the large log at its temp path, imports it through the state helper's cold capture, and records the resulting path/hash handle.
- Records lane status and the next rejoin trigger without copying an entire packet into current state.
- Serializes snapshot, event, and evidence writes through the integrator; no worker appends directly.

Fails when: workers or secondary worktrees write `.noootwo` events/evidence; the worker inlines the 20 KiB log or writes it into the repository; a worker packet replaces the current snapshot; the integrator writes once per packet without a frontier change; or the state claims a lane merged before integration evidence exists.
