# Brief Expansion

Turn a short ask into a design brief before building.

## Purpose

The brief defines the problem, audience, and constraints. It does not prescribe every solution detail.

## Output Shape For `.noootwo/brief.md`

- `Status`
- `Task`
- `Audience`
- `Primary job to be done`
- `Desired outcome`
- `Surface or flow`
- `Artifact expectation`
- `Reference sources`
- `Stack constraints`
- `Allowed implementation complexity`
- `Constraints`
- `Non-goals`
- `Tone extreme`
- `Aesthetic ambition`
- `Novelty target`
- `Brand-safety tolerance`
- `Motion appetite`
- `One unforgettable thing`
- `Must feel like`
- `Must not feel like`
- `Design objectives`
- `Success signals`
- `Open questions`

## Rules

- Keep the brief strategic and implementation-light
- Separate hard constraints from preferences
- If the user asks for "better" or "more polished", translate that into explicit design objectives
- If the ask is ambiguous, the brief should expose the ambiguity instead of hiding it
- If the user does not specify style ambition, default to a strong, opinionated direction and record that assumption explicitly
- If the user does not specify a memorable move, write a provisional `one unforgettable thing` so the draft has a non-generic center of gravity
- If the user wants high-end, niche, rare, or Claude Design-like work, require visual references or select credible mechanism references from [verified-ui-casebook.md](verified-ui-casebook.md)
- If the target stack is Flutter, SwiftUI, Compose, React, Vue, or another app framework, record the artifact expectation before direction work begins
- If the brief contains taste adjectives but no concrete style choices, run [style-calibration.md](style-calibration.md) before direction exploration
