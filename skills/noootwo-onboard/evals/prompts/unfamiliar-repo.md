# Eval: Enter an unfamiliar repository

Prompt: "I just took over this repo from another agent. Where do I start?"

Expected:

- The agent invokes the `noootwo-onboard` skill by loading its `SKILL.md`.
- It reads the nearest evidence — `AGENTS.md`, README, status, package files, CI, tests — before loading any skill body.
- It produces the required, optional, and not-needed skill map, each with a trigger or a reason.
- It hands the foundation health judgment to `noootwo-code-health`'s project-health lens instead of classifying health itself.
- It proposes at most the one missing file that unblocks the first piece of work, and does not scaffold.

Fails when: it lists every installed skill without evidence; it writes a full documentation scaffold; it classifies foundation health itself and duplicates the review surface; it starts implementing a change before the map exists.
