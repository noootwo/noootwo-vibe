# Eval: Grill the frontier

Prompt: a broad request — "Build a student learning app with AI practice, notes, community, courses, leaderboard, and progress."

Expected:

- The agent reads repo and product truth before asking, and never asks the user for a fact it could find.
- It names the unsettled decisions, then asks the whole frontier in one round — every independent question at once.
- Each question is numbered, carries 2-3 options, and ends with a `➡️` recommendation and its reason.
- Questions whose prerequisites are still unsettled are parked for a later round, not guessed.
- It waits. "Continue", "start", or "build it" does not settle a decision.
- It does not produce a PRD, an implementation plan, or a design handoff in the same turn.

Fails when: it asks one question per turn although several are independent; it asks about low-impact or technical details; it answers its own questions; it assumes an unanswered branch.
