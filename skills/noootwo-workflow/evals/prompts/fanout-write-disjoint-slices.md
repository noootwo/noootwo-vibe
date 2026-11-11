# Eval: Write fan-out for disjoint implementation slices

Prompt: "Implement this approved plan. Slice A changes the parser in `src/parser/` with its own tests; slice B changes the settings screen in `src/settings/` with its own tests. They share no interface, migration, generated output, or acceptance command. Native subagents and linked worktrees are available."

Expected:

- Records a Fan-out Check whose four independence questions pass and chooses `write-fanout`.
- Gives each lane a Worker Brief with one base, owned files, settled constraints, and its acceptance command.
- Uses one linked worktree per lane, one integrator, and one merge order.
- Reviews and merges one lane at a time, rerunning the lane and combined checks.

Fails when: both workers share a checkout; one worker merges without integrator review; the plan silently changes a shared interface; or the lead dispatches more than four lanes at once.
