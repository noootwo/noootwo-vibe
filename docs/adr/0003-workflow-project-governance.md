# ADR 0003: Workflow as Project Governance Entry

- Status: accepted
- Date: 2026-07-03

## Context

`noootwo-workflow` could route individual tasks, but it did not yet answer a takeover question: what skills does this project need, and is the basic development process healthy enough for AI-assisted work? That left gaps in unfamiliar projects: missing validation entrypoints, unclear documentation ownership, duplicated truth sources, and no compact way to decide whether local mature skills should be involved.

External skill guidance favors concise entry files with deeper supporting files loaded only when needed. Delivery and review practice favors small batches, fast feedback, clear ownership, and concrete defects over broad speculative process.

## Decision

Upgrade `noootwo-workflow` from task commander to project governance entry for onboarding and takeover work. It now owns project skill audits, foundation health checks, gap plans, and multi-skill handoff closure.

Keep the public skill set unchanged: `noootwo-workflow`, `noootwo-docs`, `noootwo-review`, and `noootwo-design`.

`noootwo-docs` owns documentation placement and cleanup for discovered gaps. `noootwo-review` owns engineering-health defects such as missing verification, CI gaps, release risk, unstable module boundaries, and context cost. `noootwo-design` remains unchanged.

## Consequences

- Project onboarding has a repeatable audit path without adding a new public skill.
- Skill bodies stay concise; detailed audits live in direct `references/` files.
- Future projects can be checked for required Noootwo skills, optional local skills, and missing foundation before implementation starts.
- The workflow can recommend minimal templates, but docs remains responsible for writing facts into the correct layer.
