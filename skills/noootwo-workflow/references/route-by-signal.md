# Route by Signal

Match the task to the right owner from evidence, not from keyword aliases.

## Read the signal first

Collect the smallest useful set:

- latest user intent and requested artifact
- current stage from the `noootwo-state` helper, `docs/status.md`, and existing artifacts
- git status and recently changed files
- open blockers recorded by a previous specialist
- available skill names and descriptions

Do not load every installed `SKILL.md`. Read the inventory and candidate descriptions; open a full skill body only after it is the likely owner.

## Match by ownership, not keyword

For each candidate ask:

1. Does its description own this intent or output shape?
2. Does it produce the artifact the current step needs?
3. Is it the owner of the current blocker?
4. Would running it now repeat a settled stage?

Examples of artifact-shaped matching:

- a slide deck, PPT, keynote, or presentation brief → presentation/slide/ppt owner
- a document, report, README, or long-form written artifact → document/writing owner
- a visual UI or frontend change → design owner when direction is unsettled, implementation owner when design is settled
- behavior-changing code → `noootwo-tdd`, then `noootwo-review`
- a broken behavior or regression → `noootwo-debug` before implementation
- an unsettled product decision → `noootwo-product` before design or build

Do not write a permanent `keyword -> skill` table. Skill descriptions and trigger text are the registry.

## Decide one owner

- One clear owner → invoke it: read its `SKILL.md` and follow it.
- Two owners and one is a blocker for the other → run the blocker first.
- Two equally valid owners → stop and ask the user with one question.
- No owner → stop and report the gap with one or two closest candidates; do not invent a Noootwo skill or guess a wrong external skill.

## Return from a specialist

After the specialist returns, do not assume the next step from the original plan. Re-read current state and match again. The next owner may change because new evidence appeared.
