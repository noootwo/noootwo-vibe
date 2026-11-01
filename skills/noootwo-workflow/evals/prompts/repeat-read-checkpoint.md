# Eval: A second read of the same source is a checkpoint

Prompt: an agent is mid-investigation and is about to read the same architecture file again and rerun the same failing verification command with the same inputs, because the first attempt felt inconclusive.

Expected:

- Stops before the repeat and runs a checkpoint: refresh the capsule, restate the current claim, the proven facts, and the open frontier.
- Names what would make the second read different — a changed hash, commit, claimed role, or a new question the first read could not answer.
- Without that change, reports the boundary and moves to a different evidence source or the owning skill instead of repeating.
- Keeps any durable change in `noootwo-state`; a repeat with no new evidence creates no new event for its own sake.

Fails when: it silently re-reads the same slice or reruns the same command; it treats a repeated read as progress; it broadens the read (whole file, whole repo, full suite) to escape the inconclusive state.
