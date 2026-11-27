# Shape

Settle the surface before building. This is the `shape` command, not a universal lifecycle: a clear repair or polish skips it.

## Intake

Read the request, the current UI, and the nearest project context. Answer only what the work needs:

- **Target:** the one root that may be edited.
- **Surface:** page, panel, form, deck, simulator screen, or artifact.
- **Audience:** the primary end user's role, moment, frequency, error cost, and shared vocabulary. The requester is not the audience unless they are also the daily user; their taste is evidence about the product, not the user's vocabulary.
- **Job:** the first loop the user completes, and the decision or action it supports.
- **Constraints:** platform, stack, brand, data, permissions, and what must not drift.
- **Acceptance:** the rendered viewports, states, and observable outcome.

If a missing fact would change the design, ask one question that resolves it. Do not interview for facts the repository already answers.

## Design Read

Write this before choosing a look:

```text
Design Read
- Surface kind:
- Audience contract:
- Product posture:
- Visual posture:
- Intervention: leave simple | craft only | add moment
- Variance / motion / density: low | medium | high
```

Each value needs a reason from the audience, task, frequency, risk, or brand. A row of defaults is not a read.

- Dense, frequent, keyboard-driven, or error-costly work stays simple and legible.
- Rare first-use, completion, explanation, launch, and brand moments may carry more variance or one authored move.
- Density follows the audience: trained operators may get dense domain UI; first-use users get plain defaults.

## Direction

Preserve the incumbent direction when it is clear. Do not run a reference audition merely because the work is new.

Run `direction` only when at least one is true:

- No visual world exists yet.
- The user rejected the incumbent direction.
- The brief asks for a materially different character.
- The current direction cannot carry the product's subject or audience.

When direction is unresolved, read `references/direction.md` and `references/design-discovery.md`. Show a low-cost real sample for each viable path, or one fuller sample plus two lightweight variants when the runtime is weak. A prose menu is not a choice. Stop for the user's choice when the choice changes the visual world.

For build work, two or three candidates are enough. For direction or brand-heavy work, capture three to five same-medium sources, record licence and fit, and build two or three spikes. A black or broken capture is not evidence.

## Contract

Write one contract before editing. It is a decision record, not a document set:

```text
Design Contract
- Structure:
- Information exposure: visible | secondary | hidden
- Vocabulary: the user's terms for the object, state, and next action; mechanism terms that stay in code or diagnostics
- Type roles:
- Colour and token roles:
- Component behaviour:
- States:
- Motion: not applicable | one authored move and its trigger
- Must not drift:
- Artifact and evidence path:
```

Name semantic roles, not adjectives. A blanket font-size override is not a type scale. Stable decisions become tokens, component rules, and state behaviour.

## Done

- Target, surface, audience, job, and acceptance are named.
- The design read changes at least one decision, or the work is a direct preserve-and-repair.
- Direction is preserved with a reason, or chosen by the user after real samples.
- One contract names structure, type, colour, states, motion, and non-drift.

## Do not

- Force a reference board on a clear local change.
- Turn the design read into eight fields of boilerplate.
- Ask the user to choose a direction when the incumbent direction is already accepted.
- Write a separate document for every contract field.
