# Eval: Capture an explicit durable rule without being asked again

Prompt: "This project uses pnpm for every package command. Remember that; don't make me repeat it."

Expected:

- Classifies the instruction as a durable project rule, not a task-local instruction.
- Searches the nearest `AGENTS.md`, ADRs, status, specs, and state for an existing claim.
- Writes one short always-on rule in the owning hot layer, with its scope and trigger.
- Links one on-demand rationale only when a tradeoff or decision needs it; does not copy the rule into several files.
- Reports `remembered: <rule> -> <path>` and does not ask the user to confirm their own explicit words.
- Keeps the rule project-local and does not create a global memory store.

Fails when: it leaves the rule only in chat; writes a transcript; duplicates it across `AGENTS.md`, status, and an ADR; overgeneralizes it to every project; or asks the user to repeat the instruction.
