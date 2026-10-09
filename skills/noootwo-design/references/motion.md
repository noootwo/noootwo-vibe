# Motion Language

The shared motion base: how this product behaves over time. Read it for `standard`, `deep`, and `production` work, and whenever a direction, token set, or artifact claims motion.

Motion is one design material among several, not a finishing pass or a default sign of effort. The still page and any motion must both be true at the end: a mechanic on a default-looking page has not solved the design, and a page that only feels authored while moving has no durable identity. Motion added after the layout has settled into a generic shape reads as garnish.

## Intervention Decision

Decide whether this product, feature, and moment should stay simple, receive craft-only work, or gain an authored moment before designing motion at all.

```markdown
Intervention Decision
- Product/feature and user:
- Frequency, task risk, emotional and brand value:
- Candidate moments:
- Decision: leave simple | craft only | add moment
- Why:
- Rejected opportunities:
```

Use this surface heuristic, then override it with product evidence:

| Surface or moment | Default | Why |
| --- | --- | --- |
| Keyboard path, command menu, batch action, high-frequency navigation | Leave simple | Delay and attention cost repeat on every use |
| Data table, monitor, analytics reading surface, control room | Leave simple or craft only | Motion competes with reading and comparison |
| Settings, form, configuration, maintenance flow | Craft only | Hierarchy, wording, validation, focus, and feedback carry the value |
| Occasional modal, sheet, toast, list change | Craft only or a small state move | Continuity helps only when the change is not frequent |
| First use, onboarding, empty state, success, completion | Consider add moment | Rare moments can carry explanation, orientation, or emotion |
| Launch, brand story, portfolio, campaign hero | Consider add moment | Expression is part of the product job when performance and fallback are proven |

`leave simple` and `craft only` are successful design decisions, not missing work. Record why the simpler treatment is better. `add moment` requires one primary authored move and at most one supporting move; it does not require every screen or feature to inherit the same spectacle.

Use the minimum intervention ladder:

1. Fix hierarchy, grouping, wording, and state clarity.
2. Use immediate platform feedback such as focus, pressed, validation, or status change.
3. Use state continuity when a change would otherwise teleport or lose context.
4. Add motion, material, sound, or haptics only when the first three cannot deliver the named user value.

Do not search for sources, tools, or effects until a candidate has passed the gates below. A missing authored moment is not a defect when the product context favors clarity, speed, or reading.

## Personality

When motion is selected, pick one archetype per direction and hold it. The archetype sets default duration, default easing, and how much overshoot is allowed.

| Archetype | Duration | Easing | Overshoot |
| --- | --- | --- | --- |
| Premium | 350-600ms | `cubic-bezier(0.4, 0, 0.2, 1)` | 0% |
| Corporate | 200-400ms | `cubic-bezier(0.2, 0, 0, 1)` | 0-3% |
| Playful | 150-300ms | `ease-out-back` | 10-20% |
| Energetic | 100-250ms | `ease-out-expo` | 15-30% |

## Register

Personality says how the motion feels. Register says how much attention it asks for. For a selected `add moment`, decide the register before looking for examples, because a reference only helps inside its own register.

| Register | What it does | Fits | Typical shape |
| --- | --- | --- | --- |
| Invisible | Confirms without being noticed | High-frequency controls, keyboard paths, dense tools | Instant state swap, or a 120ms colour change |
| Quiet | Softens a change so it reads as continuous | Settings, forms, lists, most product UI | 160-240ms fade and small settle, one property |
| Present | Gives a moment its own beat | Onboarding, empty states, first run, success | 240-400ms layered entrance, stagger under 400ms |
| Expressive | Carries the identity of the surface | Launches, hero moments, portfolio, brand pages | 400-600ms staged sequence, scroll-linked scenes |
| Theatrical | Is the experience | Campaign reveals, immersive microsites | Multi-scene choreography, authored assets |

The register follows the surface, not the mood of the moment. Product UI defaults to Quiet, with Invisible on anything the user triggers constantly. Marketing, launch, and portfolio surfaces may sit at Expressive. Theatrical is chosen deliberately and named in the direction.

Motion that is impressive in isolation usually belongs two registers above the surface it landed on. When a direction reaches for Expressive on a product screen, the reasoning has to be about the product, not about how the animation looks.

`references/craft.md` and the gates below keep the register honest. The register does not create an obligation to animate; the intervention decision determines whether motion exists at all.

## Lineage Mapping

Each style lineage carries one archetype. This is the default; a direction may override it and must record why.

| Lineage | Archetype | Signature move |
| --- | --- | --- |
| Neo Editorial | Premium | Paced reveals and restrained fades, no busy chrome |
| Industrial System | Corporate | State-driven transitions, instrument-like response |
| Quiet Luxury Product | Premium, ambient work on Gentle float | Soft tactile reveals, detail transitions |
| Precise Minimalism | Corporate on the Snappy curve | Quiet state transitions, near-invisible motion |
| Ceremonial Launch | Energetic, hero only on Playful | Reveal beats and bold staging |

## Signature Motion Identity

When a direction earns an authored motion moment, define three constants and reuse them everywhere:

1. **Signature easing** — one curve for about 80% of animations.
2. **Duration scale** — exactly three values: `quick`, `standard`, `slow`.
3. **Entrance pattern** — one entry style used consistently.

The authored move belongs to the product or flow, not automatically to every local feature. Component-library defaults can support it, but cannot be counted as the move. When no motion is selected, the authored move may instead be structural, typographic, material, or a state behavior.

## Duration Scale

Match duration to element type, then scale by distance.

| Element | Duration | Why |
| --- | --- | --- |
| Tooltip, micro-feedback | 80-120ms | Reads as instant |
| Button press, toggle | 120-180ms | Responsive feedback |
| Icon transition | 150-250ms | Clear state change |
| Card enter or exit | 200-350ms | Spatial awareness |
| Modal, dialog, sheet | 300-400ms | Focus shift |
| Page or route transition | 400-600ms | Context switch |
| Deliberate reveal | 600-1200ms | Theatrical build |

Interaction feedback budgets: hover under 100ms, press under 150ms, release and settle 200-300ms, error shake 300-400ms over two or three oscillations.

**Distance scales duration.** Treat 100px as the base, 200px as 1.3x, and 400px as 1.6x. **Entrances run 30-50% longer than exits**, because what appears carries more meaning than what leaves.

## Easing Catalog

Direction decides the family: entrances decelerate, exits accelerate, on-screen movement is smooth at both ends, and looping ambient motion uses a sine-based ease-in-out so the loop seam disappears.

| Name | Curve | Use |
| --- | --- | --- |
| Material 3 default | `cubic-bezier(0.2, 0, 0, 1)` | Default on-screen movement |
| Material 3 emphasized | `cubic-bezier(0.05, 0.7, 0.1, 1)` | Entrances and attention |
| Material 3 accelerate | `cubic-bezier(0.3, 0, 1, 1)` | Exits and dismissals |
| Apple HIG | `cubic-bezier(0.25, 0.1, 0.25, 1)` | Standard iOS-feeling transitions |
| Snappy | `cubic-bezier(0.2, 0, 0, 1)` | Fast, decisive, frequent interactions |
| Gentle float | `cubic-bezier(0.4, 0, 0.2, 1)` | Ambient and background motion |
| Bounce settle | `cubic-bezier(0.175, 0.885, 0.32, 1.275)` | Overshoot, playful contexts only |

## Material Modifiers

When a direction has a material thesis, scale its motion to match.

| Material | Duration | Overshoot |
| --- | --- | --- |
| Rigid: metal, stone | 1.2x | 0% |
| Elastic: rubber, gel | 0.8x | 15-25% |
| Fluid: water, paint | 1.5x | 5% |
| Paper: cards, sheets | 1.0x | 3-5% |
| Gas: smoke, fog | 2.0x | 0% |
| Glass: brittle | 0.9x | 0% |

## Three Layers

Flat animation reads as assembled. Every motion moment names three layers:

- **Primary** — the action the user follows.
- **Secondary** — supporting response: a shadow shifting, an icon settling.
- **Ambient** — background life: a slow gradient drift, a breathing indicator.

Not every moment needs all three at full strength, but a direction that can only describe the primary layer has no motion language yet.

## Choreography

- **Distance rule** — no motion crosses more than one third of the screen without an intermediate keyframe.
- **Element rule** — with three or more elements present, no more than one third may be in active motion at once.
- **Counter-motion** — when the hero moves one way, give ambient layers 20-30% of that speed in the opposite direction.

Stagger budgets, with the total staying under the stated ceiling:

| Pattern | Delay per element | Total budget | Use |
| --- | --- | --- | --- |
| Micro cascade | 20-40ms | under 200ms | List rows, grid cells |
| Standard | 50-100ms | under 400ms | Cards, panels, navigation |
| Dramatic | 100-200ms | under 600ms | Hero moments |
| Wave | 30-60ms | under 500ms | Data visualisation |

For a high-dynamic artifact, record a motion map before implementation: trigger, beat, primary change, supporting layers, hold, transition, settle, and exit. The map should show where the piece is still and where the motion carries meaning; a continuous effect with no rest beats is not a timeline.

## Opportunity Sweep

Use this only after the intervention decision names a relevant candidate. Sweep the seams that most often justify motion, then stop:

- **Feedback gaps** — press, hold, validation, or destructive confirmation.
- **Teleporting state** — content, routes, accordions, lists, and status changes that appear or disappear without continuity.
- **Missing spatial story** — popovers, sheets, drawers, and toasts whose origin or dismissal path is unclear.
- **Group entrance** — a rare grid or list that would otherwise arrive as an undifferentiated block.
- **Gesture seams** — drag, swipe, reorder, and dismissal that need physics or boundary feedback.
- **Delight budget** — first-run, empty, success, completion, and celebration.
- **Identity moment** — launch hero, product story, brand reveal, or authored illustration where expression is the job.

Apply these caps: at most 3 candidates for one view, 5-7 for a whole product. Keep the candidate ledger even when nothing survives. The required rejected section is what separates design judgment from an effects wishlist.

## Frequency Gate

Ask how often the user triggers the interaction before animating it.

| Frequency | Treatment |
| --- | --- |
| Rare, monthly | Expressive motion welcome |
| Occasional, daily | Subtle and fast |
| Frequent, hundreds per day | Instant, or no transition |
| Keyboard-initiated | No animation |

The best animation goes unnoticed. When users remark on the animation itself during routine work, it is too prominent for that surface.

## Purpose Gate

Every surviving candidate names one purpose. If none applies, reject it:

- **Feedback** — confirming that the interface heard the user.
- **Spatial consistency** — showing where something came from or went.
- **State indication** — making a change legible.
- **Preventing a jarring change** — bridging content that appears, disappears, or moves.
- **Explanation** — teaching how something works; marketing and onboarding only when it does not delay the task.
- **Delight** — allowed only at a rare or first-time moment.

"It looks cool" is not a purpose.

## Speed And Function Gates

The motion must work within the duration budget in this file. If it only works when slow and showy, reject it or reduce it.

Motion must help the task. Reject decoration on high-frequency controls, information the user is reading or comparing, critical error paths, and any interaction where movement reduces precision or accessibility. A simple state change, static composition, or typographic device may be the better intervention.

If any gate fails, return to `leave simple`, `craft only`, or a smaller platform-native move. Do not lower a gate to keep a visually attractive effect.

## Sourcing Motion Ideas

A direction gets better when it borrows a mechanism from a motion that already works, instead of inventing one from adjectives. Source the idea before writing the animation:

Source only after the intervention decision and gates have produced a surviving `add moment`. `leave simple` and `craft only` do not trigger a source search or a new tool.

1. **Fix the register and the archetype first.** A reference only transfers inside its own register; an Expressive reference will mislead a Quiet screen.
2. **Collect two or three examples, not one.** Look for the same moment handled differently — an entrance, a state change, a list reorder, a page transition.
3. **Name the mechanism.** For each example record what triggers it, which property moves, its duration and curve, how the layers relate, and what it communicates. "Cards settle 40ms after the shadow" is a mechanism; "smooth and premium" is not.
4. **Record the boundary.** What would count as copying the source's surface rather than its mechanism.
5. **Adapt, then prove it.** Map the mechanism onto this direction's duration scale and curve, and confirm it in the artifact.

The shared source pool — component and motion libraries that publish agent-readable indexes, curated inspiration sites, and the published platform guidance — lives in the `noootwo-research` skill. Invoke it: read its `SKILL.md` and follow it. Reference screenshots and captured pages land under `.noootwo/references/` like any other source.

Published libraries are strong evidence of craft and weak evidence of fit. A library demo is built to sell the effect; on a product surface the same effect is usually one register too loud. Take the technique and re-tune it, or leave it.

## Library Selection

Reach for the smallest tool that carries the direction.

Read [motion-libraries](motion-libraries.md) before adding a runtime or copying a registry component. It carries the register gate, the per-platform ladder, the licence and dependency checks, and the intent recipes. A copy-in component is the last rung, not the first.

| Need | Reach for |
| --- | --- |
| State change, hover, focus | CSS transitions and keyframes; no library |
| Enter, exit, layout shift in React or Vue | Motion for layout and gesture; `auto-animate` for list enter and exit |
| Scroll-linked staging, pinned scenes, SVG drawing | GSAP with ScrollTrigger |
| Authored character or illustration motion | Rive, or Lottie when the asset already exists as one |
| Expressive texture, material, distortion, or hero atmosphere | Shaders or Paper Shaders only after the register, fallback, and performance checks |
| Sound or haptic confirmation | Platform audio or haptic primitives; optional library only after product approval and licence review |
| Native screen transitions | Platform primitives before any third-party runtime |
| Cross-document or route transitions | The View Transitions API where the stack supports it |

Two cautions. Smooth-scroll libraries that take over the scroll wheel belong on marketing and portfolio surfaces, not on product screens, where they fight keyboard, assistive technology, and long scrolling lists. And "one library for everything" is not a direction: a stack carrying Motion, GSAP, Lottie, and a scroll hijack usually means the motion thesis was never decided. Check the licence and dependency cost before adopting a copy-in component; a registry demo is evidence of craft, not of fit.

## Reduced Motion

Every direction names a reduced-motion fallback in the same breath as its motion thesis: crossfades or instant state changes replacing spatial movement, ambient layers held still, and no loss of state information. Platform equivalents live in [translate](translate.md).

## Bans

Four rules are absolute and live with the quality floor in [craft](craft.md). Read it before editing UI; this file supplies the values, and that file decides what blocks `ready`.

## Troubleshooting

| Symptom | Likely cause | Fix |
| --- | --- | --- |
| Robotic | Linear easing, no arcs | Add an easing curve and a path |
| Too slow | Duration too long for the element | Check the duration table, favour ease-out |
| Cheap or flat | Missing secondary and ambient layers | Add shadow motion and background life |
| Distracting | Too many elements moving | Apply the element rule, reduce amplitude |
| No personality | Generic easing everywhere | Commit to one archetype |

## Motion Probe

When the artifact is heavy in motion or the user reports that a stretch feels dead, loose, or not following the pointer, capture evidence before changing curves. Use `scripts/extract_design_tokens.mjs --probe-motion <selector>` when the page is reachable, or record the limitation.

Read the probe as a timing measurement, not a style verdict:

- A high stillness ratio in a scroll-driven stretch is a timeline problem, not an easing problem.
- Steady-state lag behind a moving target is `speed / k`; tune the filter or lead, not the spring.
- An interaction can work without being discoverable. If a first-time visitor would not find a reveal or gesture, that is an affordance defect before it is a motion polish task.

## Sources

Distilled from the publicly published mechanisms of `LottieFiles/motion-design-skill` (MIT) for duration, easing, choreography, the three-layer model, and the register tables; `kylezantos/design-motion-principles` (MIT) for the frequency gate; `emilkowalski/skills` (MIT) for the opportunity sweep, four gates, output cap, and rejected-candidate ledger; `alchaincyf/huashu-art-motion` (MIT) for motion maps, style recipes, known weaknesses, and independent output review; Material 3 motion, M3 Expressive motion theming, and Apple HIG motion for the curve table and transition patterns. Values are starting points a direction adapts, never a house style to repeat.

`bendrape1-byte/silk-design` (MIT) takes the opposite stance — reach for motion by default and never ship a static page. Its transferable mechanism is consistency: one reveal configuration used everywhere reads as craft. Its default is not adopted here, because a product surface earns more from a lower register than from a smooth-scroll baseline, and scroll hijacking costs keyboard and assistive-technology behaviour.
