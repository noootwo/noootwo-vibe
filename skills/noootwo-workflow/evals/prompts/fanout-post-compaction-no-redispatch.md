# Eval: Compaction does not re-dispatch completed lanes

Prompt: "A session compacts during a three-lane write fan-out. The recovered Fan-out Check says Lane A is done, Lane B is running with a branch and commit, and Lane C is unstarted. The user says 'continue'."

Expected:

- Recovers the Fan-out Check and lane statuses from the capsule's bounded `fanout` projection before dispatching anything.
- Does not re-dispatch Lane A.
- Inspects Lane B's branch and commit to determine whether it completed, failed, or is still running before replacing it.
- Dispatches only Lane C, or a demonstrably incomplete Lane B unit with a fresh brief.
- Keeps one integrator and one current-state writer.

Fails when: it starts all three lanes again; it loads or invents a second state record because the capsule omitted fan-out custody; it trusts the stale capsule without checking the worktrees; it marks Lane B done from the status alone; or it creates a second state root.
