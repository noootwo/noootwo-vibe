# 0030 — Source-fit reference audition and project-level appearance memory

## Status

Accepted on 2026-11-11. This is an unreleased implementation candidate, not a
published release.

## Context

Noootwo Design had a source pool but no stable model of what a source can prove.
Awwwards, Framer Gallery, Recent, React Bits, component libraries, platform
guidance, and real product screens could all influence the same decision without
an explicit role boundary. That produced three repeated failures:

- a visually strong gallery could outrank real product flow or data-density
  evidence;
- a component or effect demo could become the visual direction rather than an
  implementation resource;
- a selected reference could survive in the reference document while disappearing
  from the rendered artifact.

The old workflow also treated source lookup as conditional for `standard` work.
The model could therefore inherit its default component language and describe the
result as a designed direction. Deep work had stronger capture rules, but no
shared lightweight record for ordinary UI work and no reviewed project memory of
what had already been accepted or rejected.

## Research

The design source registry records the evidence and source boundaries. The key
mechanisms are:

- Separate the evidence job from site prestige: product evidence, platform
  convention, visual direction, motion mechanism, implementation resource, asset
  source, and research craft.
- Keep the free path complete. Mobbin and Refero provide useful structured
  screen/flow search on paid plans, but neither is required for the workflow.
- Treat a gallery as art-direction evidence, a component demo as implementation
  evidence, and a shipped-product pattern as a convention rather than proof of
  effectiveness.
- Capture the primary artifact and distinguish an inspected screenshot from a URL,
  a black capture, an unopened file, or a stated observation.
- Re-probe dynamic source access. A source conclusion older than 90 days is not a
  current access claim.
- Remember reviewed outcomes project-locally; current evidence still outranks an
  older preference.

The concrete source boundaries are recorded in
`skills/noootwo-research/references/design-source-registry.md`, with the
2026-11-11 probe results and limitations.

## Decision

1. Every `standard` and `deep` UI task runs a reference audition. `quick` does no
   external search. `production` uses the locked references and returns to
   discovery only when the surface changes or the mechanism drifts.
2. `standard` uses a light audition: 2-3 candidates from at least two roles, one
   inspected primary capture, one primary, and at most one narrow supplement.
3. `deep` uses 3-5 sources, at least one selected same-medium source, full capture
   and licence records, fit scoring, a reference lock, and 2-3 spikes.
4. Every candidate records its role, surface/audience, platform, access, evidence
   level, observed mechanism, fit, decision, capture, licence, landed result, and
   verification date.
5. Product UI needs a selected `product evidence` source and cannot let a gallery,
   component demo, effect library, or asset source carry the primary direction.
   Native work needs a selected native or platform-specific source.
6. The project-level `.noootwo/appearance-ledger.md` records accepted and rejected
   decisions only after review. It is read by matching surface/audience section
   and is never a global profile. Stable rules move into `system.md` and tokens.
7. Mechanism Landing QA verifies that every selected primary or supplement
   mechanism is present in the artifact and improves a named user outcome.
   `decoration`, `swallowed`, and `missing` block `ready`.
8. `validate_noootwo_readiness.py --reference-audition` enforces the contract;
   `--deep-mode` implies it. The flag is additive, and `Source N` headings remain
   readable for existing boards.
9. Asset sources have a separate record: asset type, source, licence,
   attribution, commercial use, access, and fallback. Gallery screenshots are not
   production assets.
10. The public skill set stays at twelve. The source registry lives in
    `noootwo-research`; Design extends existing references and harness templates.

## Rejected Alternatives

- **A global appearance profile.** It would silently transfer one project's taste
  and risk decisions into another project. Project-local memory plus current
  evidence is narrower and more honest.
- **A permanent ban or approval from the ledger.** A previous decision is a lead.
  The current audience, artifact, access result, and fit still decide.
- **A gallery-first workflow for product UI.** Galleries are useful for art
  direction, but they cannot supply product flow, information architecture, or
  dense worktable evidence.
- **A component-library style direction.** A clean demo proves implementation
  anatomy; it does not prove task fit or brand direction.
- **Mandatory paid source access.** The free path must work. Mobbin and Refero are
  optional accelerators only when the user already has access.
- **URL-only references.** An uninspected URL or broken capture is a lead, not
  visual evidence. The primary must be inspectable.
- **Pixel-level fidelity as the default.** `borrow-mechanism` needs translation
  evidence, not visual cloning. Source Fidelity QA remains only for `replicate`.
- **A second state root or a new public skill.** Both add ownership and recovery
  cost without improving the decision.

## Consequences

- Standard UI work now pays a bounded audition cost. The cost is capped at 2-3
  candidates and one primary capture; the full extractor stays optional.
- Deep work has a stricter, more expensive evidence record. A blocked source
  narrows the pass but does not become an invented observation.
- Existing boards with `Source N` headings remain parseable. A project that next
  claims `ready` or enters `deep` must add the new role, capture, licence, and
  landing fields.
- The readiness validator becomes stricter for `--deep-mode`: deep mode now
  implies the audition and requires at least three inspectable captures across
  the candidate set.
- The ledger adds one project-local file to the design harness. It does not add a
  dependency, a state root, a migration script, or a new public skill.

## Verification

- Workspace validation must pass after the new research reference, design
  references, templates, scripts, evals, fixtures, and versions change.
- The existing deep fixture must pass with old `Source N` headings still present.
- A standard positive fixture must pass `--reference-audition`; a negative
  fixture must reject candidate count, role coverage, product evidence, primary
  capture, licence, freshness, and ledger failures.
- Temporary probes must reject gallery-only primary, component-library primary,
  missing same-medium evidence, missing licence, unopened capture, and a selected
  mechanism that did not land.
- Seven prompt contracts cover consumer first use, operations tools, gallery
  boundaries, React Bits cross-platform use, component-library direction,
  mechanism landing, and ledger reuse.

The fixtures prove deterministic gate behavior, not that a model will always
choose the right source or that the resulting UI is better. Fresh-session
behaviour, screenshot quality, and cross-project outcomes remain separate
evidence.
