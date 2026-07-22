# Style Evidence Check

Use this when a requested direction is high-character, premium, niche, unusual, user-selected, or previously rejected. The goal is to avoid confident style prose that the agent cannot actually draw or implement.

This is not a new full workflow. It tightens `agentic-style-discovery.md`, `direction-exploration.md`, `detail-translation-pass.md`, and `review-rubric.md`.

## Check Shape

```markdown
Style Evidence Check
- Style claim:
- Visual evidence:
- Anti-example:
- Borrowed mechanism:
- Implementation translation:
- Confidence: high | medium | low
- Artifact/spike required:
```

## Field Rules

- `Style claim`: the user's taste target in concrete terms, not only adjectives.
- `Visual evidence`: real screenshot, reference case, visual sample, user-provided image, or spike artifact. If none exists, say `missing`.
- `Anti-example`: a visible pattern that would prove the agent misunderstood the direction.
- `Borrowed mechanism`: transferable layout, type, material, density, interaction, or state behavior.
- `Implementation translation`: how that mechanism becomes tokens, components, spacing, motion, native controls, or artifact structure.
- `Confidence`: `low` unless evidence and translation are both clear.
- `Artifact/spike required`: what visual proof must exist before `ready`.

## Hard Rules

- Do not turn "premium", "niche", "unique", or "advanced" into a confident design spec without visual evidence.
- If evidence contradicts the proposed spec, return to style discovery instead of polishing implementation.
- If only one weak reference exists, mark low confidence and require a spike or artifact review.
- For product UI, product-flow evidence outranks pure art-direction shots.
- For campaign or editorial surfaces, visual novelty can weigh more, but implementation translation still must be named.
