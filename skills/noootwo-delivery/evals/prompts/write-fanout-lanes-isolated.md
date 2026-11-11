# Eval: Write fan-out uses isolated lanes

Prompt: "One approved requirement has three disjoint slices: data import, an independent admin filter, and separate documentation. Each has its own files and acceptance command. Native worktrees and subagents are available. Set up parallel implementation."

Expected:

- Keeps one requirement integration branch and one eventual protected-main PR.
- Records a Lane Map with three lane branches, three linked worktrees, owned files, acceptance commands, and merge order.
- Keeps one integrator in the integration checkout and gives each lane one worker.
- Rejoins one lane at a time, rerunning the lane and combined checks after each.

Fails when: it creates three independent requirements or three main-bound PRs without saying why; it puts multiple writers in one worktree; it nests worktrees; or it leaves the current state to whichever worker finishes last.
