# Claude Design Principles

Use this reference to align Noootwo Design with the public, repeatable parts of Claude Design without copying any private prompt.

## What To Copy

- Design system memory comes before task work.
- Real artifacts come before handoff prose.
- First versions exist to expose direction risk quickly.
- Evaluation is separate from generation.
- Handoff preserves naming, intent, constraints, and review evidence.

## What Not To Copy

- Do not copy leaked or unofficial prompts.
- Do not imitate a fixed Claude-looking style such as serif headline, pills, status dots, container soup, or card-heavy layouts.
- Do not treat a generated design system as a second source of truth when the real product already has code, tokens, screenshots, or brand files.
- Do not let polish hide generic structure.

## Public Signal Summary

- Anthropic's Claude Design materials emphasize codebase and asset ingestion, design-system setup, first-version generation, iteration, and handoff: https://www.anthropic.com/news/claude-design-anthropic-labs
- Anthropic's engineering writeup on design harnesses emphasizes generator/evaluator separation, high weighting for design and originality, and visual inspection with browser tooling: https://www.anthropic.com/engineering/harness-design-long-running-apps
- External workflow reports consistently show better outcomes when the model receives screenshots, annotated visual references, code-native artifacts, and repeated critique cycles.
- External critiques consistently warn about token cost, generic convergence, handoff drift, and generated design systems diverging from real product truth.

## Operating Rules

- Establish the durable system first, with source confidence for every major rule.
- Gather visual references before inventing a style when the user wants a high-end, niche, or unusually distinctive result.
- Build or specify a reviewable artifact before judging design quality.
- Prefer a quick first artifact over a perfect written description when direction risk is high.
- Evaluate the artifact as if created by another designer: inspect the result, name the weak generic moves, and return to directions or draft instead of defending it.
- Handoff only after the review gate passes.

## Source-Of-Truth Rules

- Record where every durable system rule came from: code, token file, screenshot, design file, brand guide, user statement, or inference.
- Mark confidence as `confirmed`, `inferred`, or `missing`.
- Keep experimental direction choices out of `.noootwo/system.md` unless the user promotes them into durable brand truth.
- If a generated design system conflicts with real code or screenshots, the real artifact wins.

## Generic Convergence Risks

Flag these as Claude-like convergence, even if they look polished:

- container soup with many nested rounded panels
- serif display headline plus generic sans body without product-specific reason
- pill chips, status dots, and soft cards as the main identity
- tidy but interchangeable SaaS sections
- screenshot-free review that praises cleanliness instead of lived quality
- handoff that drops component names, states, motion intent, or implementation risks
