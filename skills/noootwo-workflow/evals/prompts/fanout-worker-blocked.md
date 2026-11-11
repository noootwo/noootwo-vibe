# Eval: A blocked lane stops dependent rejoin

Prompt: "A two-lane write fan-out is running. Lane A is done and passes its checks. Lane B discovers that both lanes need a new shared event schema and reports `blocked`. The accepted plan did not define that schema."

Expected:

- Preserves Lane A and Lane B work and does not re-dispatch either with the same brief.
- Treats the new shared schema as a contract change that requires the owning decision or plan revision.
- Stops dependent rejoin, or serializes/contract-firsts the schema before resuming.
- Records the block and its reopen trigger; the integrator remains the only state writer.

Fails when: it merges Lane A as if Lane B's contract did not affect it; it lets a worker invent the event schema; it starts more lanes; or it retries the blocked lane without new context.
