# 0014 — Motion library map and cross-platform interface-quality gates

## Status

Accepted.

## Context

`noootwo-design` already owned a motion language, but it did not say which modern
library or platform primitive should carry a motion moment, and it did not have a
single interface-quality gate for accessibility, component states, data
presentation, asset cost, or screenshot-to-implementation intake. The gap was
easiest to see on Flutter and native work: the web path had an extractor and a
small visual gate, while the native path relied on prose.

Open-source effect registries such as React Bits, Vue Bits, Magic UI, and
Animata are useful execution resources, but they are not design defaults. Their
licences, dependency weight, maintenance state, and register fit differ, and
copying a demo into a quiet product surface is a regression rather than an
upgrade.

## Decision

- Add `references/motion-libraries.md` as an on-demand map from motion register
  to the smallest tool that can carry it, with web, Flutter, SwiftUI, and
  Compose entries, licence and dependency checks, and explicit rejection rules.
- Keep `motion.md` as the owner of personality, register, duration, easing,
  choreography, and bans; `motion-libraries.md` only owns implementation choice.
- Add a platform-neutral Interaction and Accessibility Gate and a Data
  Presentation Matrix to `craft.md`.
- Add a Component State Matrix and an Asset and Performance Budget to
  `translate.md`, with Flutter and native equivalents.
- Add screenshot and design-image intake to `design-discovery.md` so an image
  source is extracted before implementation and its missing interaction,
  accessibility, responsive, and data evidence stays explicit.
- Extend the web-only `check_visual_gates.py` with advisory interface checks.
  Findings require source, accessibility-tree, or keyboard confirmation and
  never block `ready` by themselves.

## Consequences

- A motion moment now has one path from register to platform primitive to
  optional library, without making any third-party component a required
  dependency.
- Flutter and native work receive the same contract depth as web work, while the
  automated artifact checks remain explicitly web-only.
- The design skill stays within its `SKILL.md` and reference budgets: the
  interface-quality pass extends existing references rather than adding another
  one.
- React Bits and Vue Bits are compared and referenced, not vendored; their
  MIT + Commons Clause boundary remains visible.
