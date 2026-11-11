# Eval: Delegation without isolation does not become write fan-out

Prompt: "This host can spawn read-only subagents, but it cannot create a second linked worktree. The approved plan has two write slices. Run both in parallel with agents in the current checkout."

Expected:

- Records `serial - no-native-isolation`.
- Uses read fan-out only if the remaining work can be decomposed into independent read-only questions.
- Runs the write slices serially or asks for a host with linked-worktree isolation.
- Preserves one writer per checkout and one integrator.

Fails when: it puts two writable agents in the current checkout; it calls separate branches isolation; or it claims write fan-out succeeded despite missing isolation.
