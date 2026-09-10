# Design Working Notes

Research notes and cost boundaries behind the design workflow.


## Workflow Research Notes

Use this note when changing Noootwo Design's workflow, review gates, AGENTS integration, or public claims.

### Sources Reviewed

- Figma resource library and blog material on design systems as shared source of truth, workflow alignment, prototype validation, and implementation drift.
- Smashing Magazine articles on UI critique, prototype review, and design-to-development loss of detail.

### Mechanisms Borrowed

- Externalize uncertainty before implementation rather than letting it remain implicit in the model.
- Use compared directions and reviewable artifacts as decision objects.
- Treat critique as part of the production loop, not only as a final score.
- Preserve design intent through explicit implementation contracts and drift checks.

### Why These Changes Belong In Noootwo Design

- The repeated failure mode was not missing inspiration; it was skipping exploration, communication, and verification.
- A task-structure protocol is more robust than adding case-by-case prompt clauses.
- Artifact-first review is the most reliable way to catch layout defects, typography drift, and generic fallback before handoff.

### Risks And Counterexamples

- Over-structuring small tasks can slow down minor polish work.
- Long questionnaires reduce velocity and often do not improve outcomes.
- Requiring deep exploration for every design request would make the skill too expensive for ordinary tasks.

### Cost Boundary

- `quick` keeps a lightweight path and should not absorb deep exploration costs.
- `standard` pays for brief + direction + decision + artifact + review when the task is direction-sensitive.
- `deep` pays for stronger source discovery and stronger evidence.
- `production` pays for contract-to-implementation preservation and drift checks.

### Verification Plan

- Validator checks workflow closure rather than only file existence.
- Eval prompts target generic failure modes rather than specific surface categories.
- Review templates require artifact evidence, findings, decision, and return action.

### Source Notes

- Figma emphasizes that design systems act as a shared source of truth between design and engineering, reducing drift during implementation and review.
- Figma guidance on UX validation recommends keeping documentation visual and tied to a working prototype whenever possible.
- Smashing Magazine critique guidance supports recurring, structured critique throughout the product process rather than only at the end.
- Smashing Magazine's design-to-technology case study explicitly warns that static documents alone lose detail across the handoff chain.


## Plugin Architecture Notes

Use this note when changing how `noootwo-design` fits inside `noootwo-vibe`.

### Current State

- `noootwo-design` is one public child skill under the `noootwo-vibe` workspace.
- The repository root has no `SKILL.md` so default skill discovery lists all public child skills.
- Design-specific references, scripts, assets, and eval prompts live inside `skills/noootwo-design/` so the design skill can be installed or published independently.
- Former public design child skills are now internal Noootwo Design responsibilities:
  - style discovery
  - artifact review
  - detail translation

### Mechanisms Preserved

- Keep one design front door that classifies design work.
- Keep high-cost research and detail-preservation flows optional and mode-bound.
- Share design resources inside the `noootwo-design` skill package, not at the monorepo root.
- Split future design artifact families only when the artifact contract, evidence surface, or review gates materially differ.

### Boundaries

- Do not reintroduce `noootwo-style-discovery`, `noootwo-design-review`, or `noootwo-detail-translation` as public skills without an explicit product decision.
- Do not move design harness scripts back to the workspace root; that would break single-skill publishing.
- Do not add root compatibility `SKILL.md`; that would hide child skills in default `skills` CLI discovery.


## Plugin Vs Skill Research Notes

Use this note when deciding whether a Noootwo capability should become a public skill, an internal reference, or an integration/plugin.

### Stable Distinction

- `skill`: reusable workflow, sequencing, review, formatting, or judgment.
- `plugin/integration`: external tool access, app connection, MCP server, or connected data source.
- `AGENTS.md`: short always-on project guidance and routing hints.

### Current Noootwo Vibe Decision

Noootwo Vibe publishes five workflow skills:

- `noootwo-workflow`
- `noootwo-product`
- `noootwo-design`
- `noootwo-review`
- `noootwo-docs`

Noootwo Design remains a skill because its value is workflow and judgment, not external system access. If future design work needs Figma, Slides, Drive, asset search, or other connected systems, add those as integrations around the skill family instead of making the design skill a giant tool manual.

### Split Test

Before adding any new public skill, require a clear yes for most of these:

- It has a distinct workflow contract.
- It has a distinct review or evidence surface.
- It reduces trigger ambiguity or context weight.
- It is reusable across many prompts.
- It can be validated independently.

If not, keep the behavior as an internal reference or mode inside an existing skill.


## Workflow Cost Model

Use this to prevent Noootwo Design from becoming too expensive for ordinary UI work.

### Modes

- `quick`: local polish. No source mining, no 3 directions, no spike comparison, no full harness completion. Use current UI, existing system/tokens when present, and one artifact or screenshot when available.
- `standard`: normal UI design. Light calibration, 3 directions, 1 artifact, typography and responsive review before ready.
- `deep`: high-end, niche, brand-heavy, Claude Design-like, or major redesign work. Source accessibility, evidence-backed discovery, 2-3 artifact spikes, screenshot comparison, typography and responsive gates.
- `production`: approved design implementation. Token mapping, stack playbook, screenshot or preview acceptance.
- `detail-translation`: not a standalone mode. It is an implementation-stage reinforcement layer for surfaces that otherwise drift back to defaults.
- `adopt-project`: first use in an existing project. Capture baseline and constraints before redesigning.

### Cost Controls

- Do not run deep mode just because a task is visual.
- Do not bootstrap or complete the entire `.noootwo/` harness for quick polish.
- Do not add a new mode for full redesign. Use the full redesign checkpoint inside `deep` or `adopt-project -> deep`.
- If the user asks for minor polish or to preserve the current system, use `quick`.
- If the user path, feature scope, interaction model, states, or acceptance criteria are unclear, route to `$noootwo-product` before design escalation.
- If the user asks to redo all UI or abandon the current visual language, the cost of discovery and user direction selection is intentional. Stop at the direction menu before implementation.
- For non-quick UI implementation, the approved design spec and implementation plan are intentional cost controls. They are cheaper than reworking a bad UI after code is written.
- Use the detail-translation layer only for implementation-bound work, production review, or post-review drift. Do not make it the default cost of quick polish or early direction exploration.
- Use readiness validation for delivery and handoff confidence, not as the first step of ordinary UI work.
- Skip the spec/plan gate only for quick polish, explicit handoff-only work, or explicit user approval to proceed without the gate.
- If time or environment blocks source mining, screenshots, or target-stack previews, record the limitation and reduce readiness confidence.
- If only 1 deep spike is possible, mark the exploration as low-confidence and do not claim full territory comparison.
- Prefer existing project preview tools before adding new dependencies.

### Escalation

Escalate from standard to deep only when the user asks for strong taste, niche/high-end direction, brand shift, or a previous standard result was too generic.

De-escalate from deep when the user prioritizes speed, implementation certainty, or staying close to an existing shipped interface.
