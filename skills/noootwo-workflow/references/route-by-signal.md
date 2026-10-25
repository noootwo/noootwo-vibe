# Route by Signal

Match the task to the right owner from evidence, not from keyword aliases.

## Read the signal first

Collect the smallest useful set:

- latest user intent and requested artifact
- an explicit issue ID, symbol, path, or error, which selects the owner without project orientation
- for resume work, the current stage from the `noootwo-state` capsule and the relevant status or artifact; direct work reads no project state
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
- a visual UI or frontend change → design owner when direction is unsettled; `noootwo-code-health` Integration Read when direction is settled but the seam is not; `noootwo-tdd` when both are settled
- behavior-changing code with an obvious local seam and no contract, data, or migration impact → `noootwo-tdd`, then `noootwo-code-health` after green
- one completed requirement → `noootwo-code-health` Change Check, not a full-project audit
- a release or ship-readiness submit gate → `noootwo-code-health` Release Check, then `noootwo-release`
- a new requirement needs an implementation shape, backend design, frontend integration, a new API/data/event contract, a migration, or a cross-module seam → `noootwo-code-health` Integration Read before `noootwo-tdd`
- existing structure makes the requested change hard → `noootwo-code-health` Change Shape; preparatory refactoring is one disposition
- repeated edits in one area, context cost growing, a giant file or directory, or a release trigger → `noootwo-code-health` Structure Sweep
- version, tag, changelog, artifact, deployment trace, rollback, provenance, or release health → `noootwo-release` after code-health readiness
- a broken behavior or regression → `noootwo-debug` before implementation
- one or more suspected problems need confirmation, evidence, or a recommendation before a fix → `noootwo-debug` Diagnosis Map; keep the claims independent and the pass read-only until every claim has a verdict
- an unsettled product decision → `noootwo-product` before design or build

Do not write a permanent `keyword -> skill` table. Skill descriptions and trigger text are the registry.

## Decide one owner

- One clear owner → invoke it: read its `SKILL.md` and follow it.
- Two owners and one is a blocker for the other → run the blocker first.
- Two equally valid owners → stop and ask the user with one question.
- No owner → stop and report the gap with one or two closest candidates; do not invent a Noootwo skill or guess a wrong external skill.

For a plan or recommendation-only request, load only the owner of the current
step. Name later owners in the proposed sequence without loading their bodies;
load each one when its step starts.

## Return from a specialist

After the specialist returns, do not assume the next step from the original plan. Re-read the changed frontier and match again. The next owner may change because new evidence appeared.
