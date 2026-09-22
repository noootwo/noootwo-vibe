# Noootwo Skill Borrow Audit

This file records, per Noootwo skill, the external sources we have compared against, what we adopted, what we rejected, and the writing-quality gap the next pass is meant to close. It is a maintenance map, not a public skill. The owning process is `noootwo-research`; `docs/agents/skill-authoring.md` remains the writing standard.

Use this file before changing a skill's trigger, description, philosophy, or borrowed mechanism. Read the actual source, not just its README, before changing a row.

Project-centric companion: `docs/reference/borrowed-skills.md` lists every external source and where it landed; this file lists every Noootwo skill and what it adopted or rejected. Read the companion for the archive, this map for the next maintenance decision.

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

- Current role: evidence-driven re-entrant orchestration, one-next-step scheduling, scope, stop conditions, and external-skill discovery.
- Prior art: Superpowers orchestration/executing-plans, writing-plans, subagent-driven-development; skill-discovery routers.
- Adopt: read current project state before stage, match one owner by intent/artifact, keep direct cheap, stop on ambiguity, and persist `.noootwo/workflow-state.md`.
- Reject: fixed keyword routing tables, full DAG pre-planning, adding external skills to the Noootwo public set.
- Next pass: measure routing precision and mid-project resumption across eval scenarios.

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
- Next pass: keep expanding `source-pools.md` across product, stack, community, and domain-specific pools; the motion pool now carries licence and maintenance checks.

### noootwo-design

- Current role: UI, visual, artifact, and frontend work after product path is settled.
- Prior art: Anthropic frontend-design, impeccable, `ddruids/mobbin-skill`, `dembrandt`, `designlang`, `tinte`, `LottieFiles/motion-design-skill`, `kylezantos/design-motion-principles`, `Meet-Miyani/compose-skill`, Refero, `feitangyuan/motion-web`, `Leonxlnx/taste-skill`, `vercel-labs/web-interface-guidelines`, `antfu-design`, and `jakubkrehel/make-interfaces-feel-better`.
- Adopt: case capture, computed-style extraction, drift gate, motion language, reference lock, anti-averaging, interaction/accessibility gates, data-presentation rules, component-state matrix, and image-intake discipline.
- Reject: paid MCP as required, full motion-web cases/scripts/assets, mandatory image generation, mandatory scroll animation, and surface copying.
- Next pass: run the motion, interface-quality, and case-capture evals; turn any measured failure into a rule change before adding more guidance.

### noootwo-tdd

- Current role: red-green-refactor and test-quality discipline for behavior-changing code.
- Prior art: Superpowers `test-driven-development` and `writing-good-tests`.
- Adopt: must observe RED, minimal GREEN, full suite, mutation check, independent expectations, no mock-behavior assertions, explicit non-code exceptions.
- Reject: verbatim Superpowers wording, production-first, tests-after, manual-test rationalization.
- Next pass: measure feature/bugfix/refactor scenarios against hidden verifiers.

### noootwo-review

- Current role: code, architecture, performance, maintainability, refactoring, optimization, re-test, and user acceptance.
- Prior art: Ponytail lean-code-review ladder; Superpowers requesting/receiving code review and verification-before-completion; web.dev/vitals, Lighthouse, SRE, OpenTelemetry, k6, PostgreSQL docs, JMH and related benchmark guidance.
- Adopt: seven-rung lean review ladder, measurable performance evidence, severity output, behavior-preserving refactor loop, re-test gate, and explicit user acceptance before submit/publish.
- Reject: vendoring Ponytail or benchmark tools; adding a separate architecture or performance skill; allowing a refactor to ship without re-testing.
- Next pass: measure scope control, missing-test handoff, and acceptance-gate scenarios.

### noootwo-state

- Current role: own abstract project state/context persistence and choose the storage form.
- Prior art: Kungfu's JSON Schema and hash bindings, TRACE's append-only NDJSON, Claude Code's append/load SessionStore, and mnemo's JSONL source plus Markdown projection.
- Adopt: one owner per fact, property-only format selection, append-only events, schema/hash/idempotency validation, and cheap field/tail reads.
- Reject: domain-specific vocabulary inside this skill, a database as the source of truth, and Node/jq dependencies for the query path.
- Next pass: add eval coverage for format selection, stale-record replacement, and cross-session resume.

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
