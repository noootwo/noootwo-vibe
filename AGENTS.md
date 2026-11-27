# Noootwo Vibe Maintenance

This repository is a multi-skill workspace. The root is not a published skill; the public skills live under `skills/` and are listed in `skills.json`.

## Task Start

1. Decide whether the work is `direct` (a tiny localized edit with an obvious check) or needs a skill. Direct work still passes the lifecycle guardrails internally; it needs no ceremony.
2. For anything else, invoke the skill that owns the work, then follow it. To invoke one, read its `SKILL.md` and follow it — a skill you only considered has not run.
3. Which skill, and the order to run them in: read `docs/agents/invocation.md`. When you are unsure, start with `noootwo-workflow`.

## Project Memory

When the user states, repeats, or corrects a durable project rule, treat it as project context and place it in its owning layer in the same turn. Short always-on rules go in the nearest `AGENTS.md`; current progress goes through `noootwo-state`; a durable choice with its rationale goes in an ADR. Search for and update the old claim, report where it landed, and do not require the user to repeat it. A repeated correction also needs a regression check in the same turn. Task-local instructions stay in the task.

## Writing Skills

Every skill, `AGENTS.md`, and pointed-at doc is written to `docs/agents/skill-authoring.md`. Read it before writing or reviewing one. The budgets in it are enforced by `python scripts/validate_skill_workspace.py .`, which must pass after any change to skill layout, versions, metadata, descriptions, or references.

## Repository Rules

- Keep the public skill set exactly: `noootwo-ask`, `noootwo-workflow`, `noootwo-product`, `noootwo-design`, `noootwo-tdd`, `noootwo-code-health`, `noootwo-delivery`, `noootwo-release`, `noootwo-state`, `noootwo-debug`, `noootwo-research`, `noootwo-onboard`.
- `noootwo-workflow` schedules; specialists do the work. Do not let a route, mode, or reference in `noootwo-workflow` take over the method owned by a specialist skill.
- Durable project state and context are written through `noootwo-state`; specialists produce content and invoke `noootwo-state` to choose the form and location. A short always-on rule lives once in the nearest `AGENTS.md` and links to any deeper rationale.
- When a named skill is missing, follow `docs/agents/dependency-fallback.md`: try to install it, and on failure take the smallest direct fallback and mark the record `skill-missing: <name>`.
- Do not add `noootwo-architecture`; architecture, technical judgment, testing strategy, performance and optimization, and maintainability stay under `noootwo-code-health`. Do not add a separate performance skill.
- `noootwo-delivery` owns branch/worktree isolation, concurrent-requirement overlap, protected-main integration, and the recorded Delivery Policy. Do not add separate branch-management, worktree, merge-queue, or concurrency skills.
- Parallel execution starts at `noootwo-workflow`'s Fan-out Gate (`serial`, `read-fanout`, `write-fanout`, `requirement-parallel`); write-lane isolation and rejoin belong to `noootwo-delivery`; no worker or secondary worktree writes `.noootwo`, and the integrator remains the only state writer.
- Isolate work with a branch or linked git worktree in the canonical checkout. Never create a sibling filesystem copy or a separate clone to protect the current checkout, and never initialize a second `.noootwo` state root.
- Release engineering stays under `noootwo-release`: versioning, tags, immutable artifacts, deployment traces, provenance, rollback, and release health. Do not add separate versioning or deployment skills.
- Every skills or agent-instruction release includes all-agent install parity: detect every existing agent skill root, sync the full public set, prune stale `noootwo-*` entries, read back every `VERSION`, and record the roots, readback, stale backups, and command evidence. See `docs/adr/0039-all-agent-release-parity.md`.
- Production may build or deploy only an exact commit reachable from protected `main`, or an annotated release tag whose commit is reachable from protected `main`. Feature branches, unmerged release branches, and mutable branches are never production sources.
- Every capability has one owner. When a skill needs another's capability, it invokes it and reads its `SKILL.md`; the capability map in `docs/agents/invocation.md` is the source of truth, and the validator enforces it.
- Only `noootwo-ask` is user-invoked. Every other skill stays reachable by the model and by its siblings.
- Do not add a root `SKILL.md`; it prevents default discovery of all child skills.
- `noootwo-workflow` may route to other installed skills as execution resources; it does not add them to the Noootwo public set or capability map.
- Keep per-skill versions in `skills/<skill>/VERSION` and mirror them in `skills.json`.
- Record a durable change to the skill model as an ADR in `docs/adr/`.
- Treat display and operational typography as separate registers: use one application-root semantic scale, keep readable dense-UI copy at `11px` or above, and verify rendered desktop, narrow, populated-state, and 200% resize evidence before accepting a typography change. See `docs/adr/0034-typography-role-balance.md`.
- Review rendered layout through measured region geometry for changed, user-named, or contract-declared regions; a screenshot alone cannot prove spacing, alignment, containment, or overlap. See `docs/adr/0035-rendered-layout-geometry-review.md`.
- A project supplied as a case, reference, side-by-side comparison, or evidence source is read-only. Edit only the explicitly named target root; never change a sample project or its tests to demonstrate a skill change.
- Every visible string, label, setting, and interaction serves the primary end user, not the requester, developer, or agent. Name settings by the user's outcome; keep implementation vocabulary (libraries, renderers, tiers, frame rates, internal status) out of operational UI; run the Comprehension Gate on rendered copy. A layout-only request changes structure, not public copy. See `docs/adr/0029-audience-derived-interaction-and-language.md`.
- A statement, critique, or question about existing behaviour is not a change mandate: follow `noootwo-workflow`'s Mandate Gate, present the proposal, and end the turn with zero writes unless the user granted free rein or the change needs no invented decision. See `docs/adr/0036-mandate-gate.md`.

## Research Rule

Before changing `noootwo-design` aesthetics, workflow modes, stack playbooks, review gates, public claims, or a stack or library choice, settle it with the `noootwo-research` skill rather than from memory: invoke it, read its `SKILL.md`, and follow it.

- Prefer official docs, framework docs, designer and developer community evidence, and artifacts with visible screenshots or running examples.
- Use X/Twitter, Reddit, HN, Figma, Flutter, React, Vue, and native app communities as signals, not as single-source truth.
- If preferred foreign sources are inaccessible, use domestic fallback sources and record the access limits, source levels, and why the fallback is acceptable.
- Borrow repeatable mechanisms, not leaked prompts, proprietary wording, or surface styling.
- Weigh skill usage cost and engineering feasibility before adding gates, scripts, or required artifacts.
- Do not claim a UI-quality improvement without artifact or screenshot review, and run readiness validation when `.noootwo/` deliverables are involved.
