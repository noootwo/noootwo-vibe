# Eval: A correction replaces the stale rule instead of adding a duplicate

Prompt: "The earlier rule says `npm test`; the user now says: 'I already told you this project uses pnpm. Stop using npm here.'"

Expected:

- Searches the owning layers and finds the stale `npm test` claim.
- Replaces or supersedes it in the same pass and records the correction's trigger, new rule, and prevention check.
- Keeps the shortest positive rule in the owning always-on layer and does not leave both commands active.
- Reports `remembered: <new rule> -> <path>` and does not ask the user to restate the correction.
- Routes a recurring failure to the owning diagnosis skill instead of stacking another rule.

Fails when: it adds a second contradictory rule; leaves the stale claim in place; records only the transcript; or asks the user to repeat a correction they already made.
