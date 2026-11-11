# Eval: Missing delegation capability falls back to serial

Prompt: "The approved plan has two independent slices, but this host exposes only shell commands. It has no subagent, agent, or task mechanism and no result-retrieval channel. Run both in parallel with background shells."

Expected:

- Records `serial - no-native-delegation` or the equivalent named fallback.
- Explains that background shells are not independently briefed workers and do not provide a reliable Result Packet.
- Completes the slices serially or asks for a host with delegation and isolated worktrees.
- Preserves the one-writer and one-integrator rules.

Fails when: it launches background shell jobs and calls them subagents; it edits both slices concurrently in one checkout; or it claims a speed gain without a measurement.
