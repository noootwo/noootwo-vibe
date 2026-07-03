# Verified UI Casebook

Use this reference for evidence-backed patterns. Borrow the mechanism, not the surface decoration.

## Case Selection Rules

- Prefer official docs, public repositories, credible hands-on writeups, or posts with visible artifacts.
- A case is useful only if it reveals a repeatable mechanism: design-system setup, visual reference use, code-native artifact, screenshot review, motion primitive, or stack-native component vocabulary.
- Do not copy brand styling, layout, artwork, or proprietary product language.

## Claude Design Official Flow

- Evidence: Anthropic launch and help-center material describe design system setup from codebase, design files, screenshots, decks, brand assets, and iteration on first versions.
- Source links: https://www.anthropic.com/news/claude-design-anthropic-labs and https://support.claude.com/en/articles/14604397-set-up-your-design-system-in-claude-design
- Mechanism to borrow: durable system memory, first artifact, conversational iteration, inline/direct editing, and structured handoff.
- Risk to avoid: treating generated rules as brand truth when real product evidence exists.

## Anthropic Harness Engineering

- Evidence: Anthropic's design harness writeup describes generator/evaluator separation, design and originality as high-value criteria, and visual inspection through browser tooling.
- Source link: https://www.anthropic.com/engineering/harness-design-long-running-apps
- Mechanism to borrow: independent evaluator, screenshot/live artifact review, explicit `refine` and `pivot` decisions, and repeated loops when the direction is promising.
- Risk to avoid: loops that only rewrite prose without looking at the actual artifact.

## Anthropic Frontend Design Skill

- Evidence: Anthropic's public skill asks for an explicit aesthetic direction, a memorable visual move, strong typography, deliberate motion, and avoidance of generic AI aesthetics.
- Source link: https://raw.githubusercontent.com/anthropics/skills/main/skills/frontend-design/SKILL.md
- Mechanism to borrow: make the aesthetic point of view concrete before implementation and reject safe default font/layout choices.
- Risk to avoid: copying the wording without requiring a real artifact or stack translation.

## Paper Plus Claude Code

- Evidence: public workflow reports show better design iteration when a visual canvas, screenshots, or drawn annotations are paired with Claude Code.
- Source links: https://x.com/felixleezd/status/2039731306612060186 and https://aifounderkit.com/ai-tools/paper-ai-design-tool/
- Mechanism to borrow: visual canvas as shared state, fast directional variants, and annotation-driven refinement.
- Risk to avoid: assuming a text-only brief can replace visible design evidence.

## Thoughtbot Design Sprint With Claude Code

- Evidence: Thoughtbot describes rapid prototyping with Claude Code inside a design sprint context, using prototypes to move from concept to decision.
- Source link: https://thoughtbot.com/blog/rapid-prototyping-with-claude-code-how-we-transformed-our-design-sprint-process
- Mechanism to borrow: prototype early, test assumptions through artifact review, and let the artifact reveal missing states and content.
- Risk to avoid: over-investing in polish before validating the core interaction and hierarchy.

## Flutter Wonderous And gskinner Work

- Evidence: `flutter-wonderous-app` and gskinner Flutter showcases demonstrate high visual fidelity, custom transitions, effects, and authored motion in Flutter.
- Source links: https://github.com/gskinnerTeam/flutter-wonderous-app and https://flutter.gskinner.com/
- Mechanism to borrow: Flutter can support premium visual systems when the design uses slivers, custom painting, rich motion, careful imagery, and stack-native layout primitives.
- Risk to avoid: defaulting to `Scaffold + AppBar + Card + ListView` and then expecting prompt adjectives to create high-end output.

## Rive Across Product Stacks

- Evidence: Rive supports interactive animation assets across Web, Flutter, iOS, Android, React, and React Native.
- Source link: https://rive.app/
- Mechanism to borrow: use authored motion assets as product identity when static components are not enough.
- Risk to avoid: treating animation as garnish on a generic layout.

## React Motion And GSAP

- Evidence: Motion for React and GSAP/ScrollTrigger provide production-grade primitives for layout transitions, gesture motion, and scroll-driven staging.
- Source links: https://motion.dev/docs/react-layout-animations and https://gsap.com/docs/v3/Plugins/ScrollTrigger/
- Mechanism to borrow: make motion part of the direction thesis: reveal, compare, unfold, inspect, stage, or transform.
- Risk to avoid: adding low-value fade/slide presets after the page already looks generic.

## SwiftUI And Jetpack Compose Native Motion

- Evidence: platform docs expose native animation and transition primitives such as matched geometry, shared elements, and adaptive Material motion.
- Source links: https://developer.android.com/develop/ui/compose/animation/shared-elements and platform animation documentation for the target Apple framework.
- Mechanism to borrow: preserve platform idioms while using native transitions, surface layering, typography, and haptics to express the art direction.
- Risk to avoid: forcing a web landing-page composition into a native app shell.

## How To Use The Casebook

- Pick 1-2 cases as mechanism references before direction exploration.
- Record the selected mechanisms in `.noootwo/brief.md` or `.noootwo/directions.md`.
- During review, check whether the implementation actually used the mechanism, not whether it superficially resembles the case.
