# Motion Language

The shared motion base: how this product behaves over time. Read it for `standard`, `deep`, and `production` work, and whenever a direction, token set, or artifact claims motion.

Motion is part of the direction, not a finishing pass. A direction that names structure, type, and colour but no motion is incomplete, and motion added after the layout has settled into a generic shape reads as garnish.

## Personality

Pick one archetype per direction and hold it. The archetype sets default duration, default easing, and how much overshoot is allowed.

| Archetype | Duration | Easing | Overshoot |
| --- | --- | --- | --- |
| Premium | 350-600ms | `cubic-bezier(0.4, 0, 0.2, 1)` | 0% |
| Corporate | 200-400ms | `cubic-bezier(0.2, 0, 0, 1)` | 0-3% |
| Playful | 150-300ms | `ease-out-back` | 10-20% |
| Energetic | 100-250ms | `ease-out-expo` | 15-30% |

## Register

Personality says how the motion feels. Register says how much attention it asks for. Decide the register before looking for examples, because a reference only helps inside its own register.

| Register | What it does | Fits | Typical shape |
| --- | --- | --- | --- |
| Invisible | Confirms without being noticed | High-frequency controls, keyboard paths, dense tools | Instant state swap, or a 120ms colour change |
| Quiet | Softens a change so it reads as continuous | Settings, forms, lists, most product UI | 160-240ms fade and small settle, one property |
| Present | Gives a moment its own beat | Onboarding, empty states, first run, success | 240-400ms layered entrance, stagger under 400ms |
| Expressive | Carries the identity of the surface | Launches, hero moments, portfolio, brand pages | 400-600ms staged sequence, scroll-linked scenes |
| Theatrical | Is the experience | Campaign reveals, immersive microsites | Multi-scene choreography, authored assets |

The register follows the surface, not the mood of the moment. Product UI defaults to Quiet, with Invisible on anything the user triggers constantly. Marketing, launch, and portfolio surfaces may sit at Expressive. Theatrical is chosen deliberately and named in the direction.

Motion that is impressive in isolation usually belongs two registers above the surface it landed on. When a direction reaches for Expressive on a product screen, the reasoning has to be about the product, not about how the animation looks.

`references/craft.md` and the frequency gate below are what keep the register honest; the register is what stops restraint from turning into a page that never moves at all.

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

Define three constants per direction and reuse them everywhere:

1. **Signature easing** — one curve for about 80% of animations.
2. **Duration scale** — exactly three values: `quick`, `standard`, `slow`.
3. **Entrance pattern** — one entry style used consistently.

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

## Frequency Gate

Ask how often the user triggers the interaction before animating it.

| Frequency | Treatment |
| --- | --- |
| Rare, monthly | Expressive motion welcome |
| Occasional, daily | Subtle and fast |
| Frequent, hundreds per day | Instant, or no transition |
| Keyboard-initiated | No animation |

The best animation goes unnoticed. When users remark on the animation itself during routine work, it is too prominent for that surface.

## Sourcing Motion Ideas

A direction gets better when it borrows a mechanism from a motion that already works, instead of inventing one from adjectives. Source the idea before writing the animation:

1. **Fix the register and the archetype first.** A reference only transfers inside its own register; an Expressive reference will mislead a Quiet screen.
2. **Collect two or three examples, not one.** Look for the same moment handled differently — an entrance, a state change, a list reorder, a page transition.
3. **Name the mechanism.** For each example record what triggers it, which property moves, its duration and curve, how the layers relate, and what it communicates. "Cards settle 40ms after the shadow" is a mechanism; "smooth and premium" is not.
4. **Record the boundary.** What would count as copying the source's surface rather than its mechanism.
5. **Adapt, then prove it.** Map the mechanism onto this direction's duration scale and curve, and confirm it in the artifact.

The shared source pool — component and motion libraries that publish agent-readable indexes, curated inspiration sites, and the published platform guidance — lives in the `noootwo-research` skill. Invoke it: read its `SKILL.md` and follow it. Reference screenshots and captured pages land under `.noootwo/references/` like any other source.

Published libraries are strong evidence of craft and weak evidence of fit. A library demo is built to sell the effect; on a product surface the same effect is usually one register too loud. Take the technique and re-tune it, or leave it.

## Library Selection

Reach for the smallest tool that carries the direction.

| Need | Reach for |
| --- | --- |
| State change, hover, focus | CSS transitions and keyframes; no library |
| Enter, exit, layout shift in React or Vue | Motion, using layout and gesture primitives |
| Scroll-linked staging, pinned scenes, SVG drawing | GSAP with ScrollTrigger |
| Authored character or illustration motion | Rive, or Lottie when the asset already exists as one |
| Native screen transitions | Platform primitives before any third-party runtime |
| Cross-document or route transitions | The View Transitions API where the stack supports it |

Two cautions. Smooth-scroll libraries that take over the scroll wheel belong on marketing and portfolio surfaces, not on product screens, where they fight keyboard, assistive technology, and long scrolling lists. And "one library for everything" is not a direction: a stack carrying Motion, GSAP, Lottie, and a scroll hijack usually means the motion thesis was never decided.

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

## Sources

Distilled from the publicly published mechanisms of `LottieFiles/motion-design-skill` (MIT) for duration, easing, choreography, the three-layer model, and the register tables; `kylezantos/design-motion-principles` (MIT) for the frequency gate; Material 3 motion, M3 Expressive motion theming, and Apple HIG motion for the curve table and the transition patterns. Values are starting points a direction adapts, never a house style to repeat.

`bendrape1-byte/silk-design` (MIT) takes the opposite stance — reach for motion by default and never ship a static page. Its transferable mechanism is consistency: one reveal configuration used everywhere reads as craft. Its default is not adopted here, because a product surface earns more from a lower register than from a smooth-scroll baseline, and scroll hijacking costs keyboard and assistive-technology behaviour.
