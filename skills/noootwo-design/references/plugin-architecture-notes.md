# Noootwo Design Packaging Notes

Use this note when changing how `noootwo-design` fits inside `noootwo-vibe`.

## Current State

- `noootwo-design` is one public child skill under the `noootwo-vibe` workspace.
- The repository root has no `SKILL.md` so default skill discovery lists all public child skills.
- Design-specific references, scripts, assets, and eval prompts live inside `skills/noootwo-design/` so the design skill can be installed or published independently.
- Former public design child skills are now internal Noootwo Design responsibilities:
  - style discovery
  - artifact review
  - detail translation

## Mechanisms Preserved

- Keep one design front door that classifies design work.
- Keep high-cost research and detail-preservation flows optional and mode-bound.
- Share design resources inside the `noootwo-design` skill package, not at the monorepo root.
- Split future design artifact families only when the artifact contract, evidence surface, or review gates materially differ.

## Boundaries

- Do not reintroduce `noootwo-style-discovery`, `noootwo-design-review`, or `noootwo-detail-translation` as public skills without an explicit product decision.
- Do not move design harness scripts back to the workspace root; that would break single-skill publishing.
- Do not add root compatibility `SKILL.md`; that would hide child skills in default `skills` CLI discovery.
