# Skill Authoring Standard

The standard every Noootwo skill is written to, and the standard the validator enforces. Read it before writing or reviewing a skill, an `AGENTS.md`, or any document an agent reaches through a pointer.

A skill is not an essay about design or product work. It is a set of steps an agent runs, plus the reference those steps reach for. The writing below is what makes it run the same way twice.

## Context pointers

A **context pointer** is a reference held in the agent's context that names out-of-context material and the condition for reaching it. A skill's `description` is one; a line in `AGENTS.md` naming a doc is the same object. The pointer's wording, not its target, decides when the agent reaches it.

A pointer does two jobs: say what the material is, and name the **branches** that reach it. Branch rules:

- Front-load the leading word; the pointer is where the triggering happens.
- One trigger per branch. Synonyms that rename one branch are one branch written twice; collapse them.
- Cut identity the body already carries.
- Every word is always-loaded, so the pointer earns harder pruning than the body.

Budget: `description` ≤ 200 characters. If it does not fit, the skill covers too many branches and should split.

## The two loads

- **Context load** is always-loaded material: an `AGENTS.md` line, a skill description. It costs tokens and attention every turn whether or not it fires.
- **Cognitive load** is the human remembering which document exists and when to reach for it. Not a cost to minimise — it is the price of human agency.

Material behind a pointer escapes context load at the price of the pointer's line. Material with no pointer rides entirely on cognitive load.

## Information hierarchy

Rank every piece of content by how immediately the agent needs it:

1. **In-file step** — what the agent does, in order. The primary tier.
2. **In-file reference** — consulted on demand; a flat peer-set of rules is fine.
3. **Disclosed reference** — a separate file behind a pointer, loaded only when the pointer fires.

**Progressive disclosure** is the move down the ladder so the top stays legible. Inline what every branch needs; disclose what only some branches reach. When a skill has steps, in-file reference that should be disclosed buries them and turns attending to them into a coin-flip.

**Co-location**: keep a concept's definition, rules, and caveats under one heading so reading one part brings its neighbours.

**Sprawl** is the failure: a body too long even when every line is live. Attention thins across the excess. Cure it with the ladder — disclose, or split by branch.

Budget: `SKILL.md` ≤ 120 lines, of which the steps come first.

## Steps and completion criteria

Every step ends on a **completion criterion**: the condition that says the work is done. Two properties make it a lever:

- **Clarity** — can the agent tell done from not-done? A vague bound ("understanding reached", "ready") invites **premature completion**: the agent ends the step early because the visible steps ahead pull it forward.
- **Demand** — how much the criterion requires. "Every modified model accounted for" forces thorough work; "produce a change list" does not.

The strongest criteria are both checkable and exhaustive. Sharpen the bound before reaching for anything heavier.

## Splitting

Split only when the cut earns its cost:

- **By sequence** — when the later steps tempt the agent to rush the current one. Only hides them across a real context boundary (a handoff or a subagent); an inline call leaves them in context.
- **By invocation** — see [invocation.md](invocation.md).

## Leading words

A **leading word** is a compact concept already in the model's pretraining that the agent thinks with while running the document. Repeated as a token, never as a sentence, it accumulates definition and anchors a region of behaviour in few tokens by recruiting priors the model already has.

A coined word recruits no priors: you pay in definition tokens what a pretrained word gives free. Reach for an existing word first.

**Canonical Noootwo vocabulary.** Use these tokens; do not invent synonyms for them.

| Word | Means |
| --- | --- |
| **frontier** | the questions that are answerable now, because their prerequisites are settled |
| **settled** / **unsettled** | a decision is made and confirmed, or it is not; replaces ad-hoc state enums |
| **shared understanding** | the exit condition of an interview: the agent's summary matches what the user meant |
| **rework** | work redone because an earlier layer failed; the failure this suite exists to prevent |
| **slop** | output that is generic, decorative, or assembled rather than designed |

Anchored words already in use — `artifact`, `trace`, `layer`, `seam` — stay.

## Pruning

- **Single source of truth**: one authoritative place per meaning. Duplication costs maintenance and inflates a meaning's prominence past its rank.
- **The environment is a source of truth too** (`package.json` scripts, config, directory layout). A document that restates it is a cache; cache only what the agent cannot look up.
- **Relevance**: does the line still bear on what the document does? Shorter documents are easier to keep relevant; the default fate otherwise is **sediment** — stale layers that settle because adding feels safe and removing feels risky.
- **No-ops**: an instruction the model already obeys by default pays load to say nothing. The test is model-relative: does it change behaviour versus the default? If not, delete the sentence.

## Positive phrasing

Steering by prohibition drags the forbidden behaviour into context and makes it more available. State the target behaviour instead ("write one-line comments"), so the banned one is never spoken.

A prohibition earns its place only as a hard guardrail that cannot be phrased positively — and even then, pair it with the positive target so attention lands on what to do.

## Budgets the validator enforces

| Rule | Limit |
| --- | --- |
| `description` length | ≤ 200 characters |
| `SKILL.md` length | ≤ 120 lines |
| `references/` files per skill | ≤ 12 |
| Every reference named by a pointer in `SKILL.md` | required |
| `agents/openai.yaml` `interface.short_description` | 25–64 characters |
| `interface.default_prompt` | not used; the description already carries the trigger |
| Cross-skill reference in a `SKILL.md` body | must name the skill and its `SKILL.md`, never a bare `$name` |
