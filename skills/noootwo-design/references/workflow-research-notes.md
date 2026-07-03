# Workflow Research Notes

Use this note when changing Noootwo Design's workflow, review gates, AGENTS integration, or public claims.

## Sources Reviewed

- Figma resource library and blog material on design systems as shared source of truth, workflow alignment, prototype validation, and implementation drift.
- Smashing Magazine articles on UI critique, prototype review, and design-to-development loss of detail.

## Mechanisms Borrowed

- Externalize uncertainty before implementation rather than letting it remain implicit in the model.
- Use compared directions and reviewable artifacts as decision objects.
- Treat critique as part of the production loop, not only as a final score.
- Preserve design intent through explicit implementation contracts and drift checks.

## Why These Changes Belong In Noootwo Design

- The repeated failure mode was not missing inspiration; it was skipping exploration, communication, and verification.
- A task-structure protocol is more robust than adding case-by-case prompt clauses.
- Artifact-first review is the most reliable way to catch layout defects, typography drift, and generic fallback before handoff.

## Risks And Counterexamples

- Over-structuring small tasks can slow down minor polish work.
- Long questionnaires reduce velocity and often do not improve outcomes.
- Requiring deep exploration for every design request would make the skill too expensive for ordinary tasks.

## Cost Boundary

- `quick` keeps a lightweight path and should not absorb deep exploration costs.
- `standard` pays for brief + direction + decision + artifact + review when the task is direction-sensitive.
- `deep` pays for stronger source discovery and stronger evidence.
- `production` pays for contract-to-implementation preservation and drift checks.

## Verification Plan

- Validator checks workflow closure rather than only file existence.
- Eval prompts target generic failure modes rather than specific surface categories.
- Review templates require artifact evidence, findings, decision, and return action.

## Source Notes

- Figma emphasizes that design systems act as a shared source of truth between design and engineering, reducing drift during implementation and review.
- Figma guidance on UX validation recommends keeping documentation visual and tied to a working prototype whenever possible.
- Smashing Magazine critique guidance supports recurring, structured critique throughout the product process rather than only at the end.
- Smashing Magazine's design-to-technology case study explicitly warns that static documents alone lose detail across the handoff chain.
