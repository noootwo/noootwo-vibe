# 0029 — Audience-derived interaction and language

## Status

Accepted on 2026-11-09.

## Context

The product and design skills already named a "real user" and preferred
progressive disclosure, but the handoff did not turn user characteristics into
concrete interaction decisions. Models therefore defaulted to an
engineering-shaped surface: implementation names, model and framework details,
internal statuses, explanatory notes, and settings for choices a good default
could handle.

The failure is not "too much information" in the abstract. It is information
that does not help the primary user complete the current task, make the current
decision, or recover from the current error.

The existing split remains correct:

- Product owns the user, moment, outcome, main path, states, acceptance, and the
  audience-derived interaction posture.
- Design owns the translation into layout, copy, components, disclosure, and the
  rendered-artifact review.

## Research

The deciding evidence is recorded in
`docs/reference/audience-language-evidence.md`.

The strongest mechanisms:

- NN/g's novice/expert work supports conditional density and expert affordances,
  not a universal simple or dense UI.
- NN/g's plain-language analysis supports concise language for experts too, while
  allowing domain terms that the audience genuinely shares.
- NN/g's progressive-disclosure work supports a first layer of frequent core
  content and one clear second layer for rare or advanced content; more than two
  levels tends to lose users.
- W3C COGA independently supports removing unnecessary content, short chunks,
  no unexplained jargon, and clear page purpose.
- GOV.UK and Microsoft independently support starting from user needs,
  context, and simple words with precise meanings.
- ISO 24495-1 frames plain language by reader outcome: relevant, findable,
  understandable, and usable.

The counterexamples are equally important: trained operators can use high
density and shared domain terms; technical buyers need architecture, security,
performance, and compatibility evidence; and hiding the main path or required
evidence behind progressive disclosure is a comprehension defect.

## Decision

1. `noootwo-product` adds an **Audience Contract** to the Product-to-Design
   Handoff: primary user and moment, familiarity and shared vocabulary, usage
   frequency, error or decision cost, learning-versus-throughput stance, and
   visible/secondary/hidden information.
2. Product derives one **Interaction Posture** from that contract: density,
   language, main-path shape, settings stance, expert affordances, and help
   stance.
3. One primary audience is named per surface. Multiple audiences get separate
   paths or layers rather than a generic average.
4. `noootwo-design` carries an **Information exposure** field in the Design
   Contract and a **Comprehension Gate** in artifact review. The gate checks
   first-screen purpose and next action, user vocabulary, technical-term
   justification, note budget, density fit, settings stance, and error recovery.
5. Visible information follows **outcome -> decision evidence -> implementation
   detail**. Implementation names, service or database details, framework or
   model names, internal IDs or flags, and design rationale stay in code, docs,
   or a diagnostics layer unless they are the user's work object.
6. Every visible note must prevent an error, explain a consequence, support
   recovery, or teach a term needed now. A note that changes no decision is
   deleted.
7. A missing audience contract that would change the first screen returns to
   Product. A missing contract that would not change the screen is recorded as
   an assumption.

## Rejected alternatives

- **B2C/B2B as the audience model.** It does not distinguish a first-time
  customer from a trained operator, or a consumer from a technical buyer.
- **A full persona or research matrix for every task.** Too costly for small
  work. The six-field contract is the minimum that changes interaction.
- **A separate UX-writing skill.** Copy is part of the interface. Product owns
  the user and vocabulary decision; Design owns the rendered copy and review.
  Adding another public skill would split one capability across two owners.
- **Delete all technical language.** Technical evidence is required for
  integration, security, performance, compatibility, and risk decisions. The
  rule is placement and justification, not blanket removal.
- **Make every surface simple and low-density.** High-frequency operational
  tools legitimately trade learnability for throughput, keyboard control, and
  batch actions.
- **Treat "expert user" as permission for internal names.** Expertise is
  domain-specific. A shared domain term is valid; an implementation name is not.
- **Rely on visual review alone.** A beautiful first screen can still fail the
  user's comprehension. The gate is a separate review result.

## Consequences

- Product handoffs now carry audience and interaction posture explicitly, so
  Design does not invent density or vocabulary from the surface label.
- Design review can block `ready` for technical noise, unexplained internal
  terms, note-heavy UI, or settings that should be defaults.
- The existing `.noootwo` harness templates carry the new fields; no new state
  root or artifact family is created.
- The public skill set stays at twelve. No new skill, schema migration, or
  dependency is introduced.
- The change adds no mandatory research pass for small work. The contract can be
  satisfied from the request, repository evidence, or a recorded assumption.

## Verification

- Workspace validation must pass after the skill, template, and reference changes.
- Four Product eval contracts cover consumer, operations, technical-buyer, and
  missing-audience cases.
- Three Design eval contracts cover consumer technical noise, operations density
  with internal jargon, and a failed comprehension gate blocking `ready`.
- No fresh-session behavior, comprehension, time, token, or rework improvement
  is claimed until those contracts are run against a no-skill baseline.
