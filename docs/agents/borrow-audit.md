# Noootwo Skill Borrow Audit

This file records, per Noootwo skill, the external sources we have compared against, what we adopted, what we rejected, and the writing-quality gap the next pass is meant to close. It is a maintenance map, not a public skill. The owning process is `noootwo-research`; `docs/agents/skill-authoring.md` remains the writing standard.

Use this file before changing a skill's trigger, description, philosophy, or borrowed mechanism. Read the actual source, not just its README, before changing a row.

## Evaluation axes

For every candidate source we ask four questions:

1. **Trigger quality** — does the source's description make it easier for the model to reach for it at the right moment?
2. **Philosophy sharpness** — does it name the first principle in one sentence better than the current Noootwo text?
3. **Progressive disclosure** — does it load only the reference the current branch needs?
4. **Mechanism fit** — does it prevent a repeated concrete failure, keep cheap modes cheap, and become checkable?

A "we already have it" conclusion is not valid unless the writing is also as sharp. A better description with the same mechanism is a real improvement.

## Skill-by-skill map

### noootwo-ask

- Current role: user-invoked router.
- Prior art: Codex/Claude skill routers, Product Design index skill, motion-web intent-detection map.
- Adopt: negative routing per skill, one hop per trigger, router never does the specialist's work.
- Reject: model-invoking the router automatically; duplicating skill bodies inside the router.
- Next pass: make each `$noootwo-*` entry answer "when not to use it".

### noootwo-workflow

- Current role: one controlled loop, routing, scope, stop conditions.
- Prior art: mature process skills; agent skill guidance; obra/superpowers-style gate wording.
- Adopt: hard gates as judgments, bounded modes, read-first ladder, specialist handoff.
- Reject: adding a heavyweight plan for direct edits; turning guardrails into ceremony.
- Next pass: tighten the read-first ladder and mode table, keep `direct` nearly free.

### noootwo-product

- Current role: settle what should exist before design or build.
- Prior art: OpenAI Product Design plugin (`product-design`), especially `get-context`, `ideate`, `audit`, and `critical-overrides`.
- Adopt:
  - Minimum brief before frontier questions.
  - Project-local product context snapshot instead of global user context.
  - Product-flow audit for existing UX when the user asks to audit or critique a live flow.
  - Explore / Design / Build boundary at the product-to-design handoff.
- Reject:
  - Global `user-context` outside a project.
  - Product Design's Sites/Browser-specific workflow and prototype templates.
  - Product Design's asset-generation and share/deploy paths; those belong to design or integrations.
- Next pass: add trigger phrases for existing-flow audit, minimum brief, and product context.

### noootwo-research

- Current role: settle decisions with outside evidence and audit prior art.
- Prior art: `dzhng/deep-research`, `mvanhorn/last30days`, `obra/superpowers`, `pbakaus/impeccable`, `mattpocock/skills`, `anthropics/skills`, OpenAI Product Design, `feitangyuan/motion-web`.
- Adopt: breadth/depth control, evidence ladder, mechanism extraction, borrow-audit gate.
- Reject: copying source wording, paid MCP as default path, dependencies that tax cheap modes.
- Next pass: turn `source-pools.md` into a broader prior-art map for every Noootwo skill, not only design and motion.

### noootwo-design

- Current role: UI, visual, artifact, and frontend work after product path is settled.
- Prior art: Anthropic frontend-design, impeccable, `ddruids/mobbin-skill`, `dembrandt`, `designlang`, `tinte`, `LottieFiles/motion-design-skill`, `kylezantos/design-motion-principles`, `Meet-Miyani/compose-skill`, Refero, and `feitangyuan/motion-web`.
- Adopt: case capture, computed-style extraction, drift gate, motion language, reference lock, anti-averaging.
- Reject: paid MCP as required, full motion-web cases/scripts/assets, surface copying.
- Next pass: sharpen motion philosophy, add source-fidelity QA for explicit replication, and add a light motion probe without new dependencies.

### noootwo-review

- Current role: code, architecture, performance, maintainability, and release review.
- Prior art: Ponytail lean-code-review ladder; web.dev/vitals, Lighthouse, SRE, OpenTelemetry, k6, PostgreSQL docs, JMH and related benchmark guidance.
- Adopt: seven-rung lean review ladder, measurable performance evidence, severity output, separated review.
- Reject: vendoring Ponytail or benchmark tools; adding a separate architecture or performance skill.
- Next pass: sharpen the "Tech Lead / QA Architect, not style critique" trigger.

### noootwo-docs

- Current role: keep documents true and place changed facts in the owning layer.
- Prior art: docs-as-code and technical-writing practice; Diátaxis-style separation of tutorial, how-to, reference, and decision material.
- Adopt: single owner per fact, context budget, stale-claim audit.
- Reject: more documents as the default answer.
- Next pass: add a first principle that documents exist to prevent future drift, not to record activity.

### noootwo-debug

- Current role: prove the cause before fixing.
- Prior art: root-cause analysis and debugging skills; scientific-method and falsification practice.
- Adopt: hypothesis ledger, evidence chain, toggle, bounded fix.
- Reject: fixing from stack-trace inference before a reproducible cause.
- Next pass: make description include user complaint phrases like intermittent, CI-only, or previously working.

### noootwo-onboard

- Current role: enter an unfamiliar repo and audit which skills it needs.
- Prior art: onboarding/skill-discovery skills; local installed-skill scan practice.
- Adopt: read nearest evidence first, load skills only after a project fact makes them relevant.
- Reject: loading every installed skill; adding a project-independent setup ritual.
- Next pass: sharpen the "new repo" and "takeover" trigger.

## Adoption gate

Before implementing a candidate, confirm all four:

1. It prevents a repeated concrete failure.
2. It fits the description/SKILL/reference budget.
3. It keeps the cheap mode cheap.
4. It becomes checkable through a rule, template, script, or eval.

Record rejections in this file so the same proposal does not return every quarter.

## License boundaries

- OpenAI Product Design is a private plugin. Borrow mechanisms and description technique; do not copy its plugin structure, workflows, prompts, or brand wording.
- `feitangyuan/motion-web` is CC BY-NC 4.0. Borrow mechanisms and ideas; do not copy its SKILL, cases, scripts, or assets into a commercial skill.
- Named open-source skills may be MIT or otherwise permissive; still borrow mechanisms, not leaked prompts or surface styling.
