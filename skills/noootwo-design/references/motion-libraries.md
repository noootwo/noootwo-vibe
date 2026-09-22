# Motion Libraries And Platform Primitives

Read this only when a direction needs motion and the implementation choice is still open. `motion.md` owns the register, duration scale, easing, choreography, and bans; this file owns the smallest tool that can carry them.

## Register Gate

Choose the register before evaluating any library. A strong demo is not evidence of fit.

| Register | Allowed implementation | Usually reject |
| --- | --- | --- |
| Invisible | CSS state changes, platform-native state changes, no runtime | effect registries, scroll libraries, spring toys |
| Quiet | CSS/WAAPI, Motion layout and values, auto-animate, platform-native transitions | marquee, magnetic button, cursor trail, scroll hijack |
| Present | Motion, auto-animate, platform-native transitions, Rive or Lottie for an authored asset | several runtimes in one direction |
| Expressive | Motion, GSAP for scroll or timelines, copy-in registries, Rive or Lottie | using every available runtime at once |
| Theatrical | GSAP timelines, WebGL or Canvas, authored Rive or Lottie assets | any of these on a product screen without a product reason |

If the register is Invisible or Quiet, a copy-in effect component starts as a rejection unless the direction records a product reason and an exception.

## Selection Ladder

1. **Platform primitive** — use the framework's own transition, layout, gesture, or animation API first.
2. **Small runtime primitive** — add a focused library only when the platform API cannot express the gesture, layout, or physics cleanly.
3. **Copy-in registry component** — only at Present or above, and only when the source can be retuned to this direction.
4. **Authored asset runtime** — Rive or Lottie only when the motion is drawn or exported, not when it is a UI transition.

Never start at rung three or four. "The demo looked good" answers a different question from "this surface needs this motion".

## Intent Map

Use this as a starting point, then verify the current platform API against the target version.

| Intent | Web: React or Vue | Flutter | iOS | Android |
| --- | --- | --- | --- | --- |
| Hover, focus, press | CSS or WAAPI | implicit animation | SwiftUI animation or transition | `animate*AsState` |
| List enter, exit, reorder | auto-animate | `AnimatedList` or `AnimatedSwitcher` | `withAnimation` and transition | `AnimatedVisibility`, `animateItem` |
| Layout or shared element | Motion layout and `layoutId` | `Hero` plus the `animations` package | `matchedGeometryEffect` | shared element or `SharedTransitionLayout` |
| Route or page change | View Transitions or Motion presence | `animations` shared axis or fade through | native transition or navigation transition | `AnimatedContent` |
| Drag and gesture | Motion drag or Reorder | `ReorderableListView` or gesture APIs | native drag gesture | Lazy list reorder or gesture APIs |
| Scroll-linked marketing scene | GSAP ScrollTrigger or CSS scroll-driven | `CustomScrollView` plus a controller | SwiftUI scroll APIs | Compose scroll APIs |
| Number, label, or status change | CSS, WAAPI, or Motion number | `AnimatedSwitcher` or tween | `contentTransition` | `animateContentSize` or `AnimatedContent` |
| Authored character or illustration | Rive or Lottie | Rive or Lottie | Rive or Lottie | Rive or Lottie |

Scroll-linked staging belongs on marketing, launch, and portfolio surfaces. On product surfaces it competes with keyboard, assistive technology, and long lists; keep the page's own scroll behaviour unless the user has asked for an immersive experience.

## Tool Notes

| Tool | Licence and state | Best fit | Boundary |
| --- | --- | --- | --- |
| Motion | MIT; React, Vue, and JavaScript; active September 2026 | product-grade layout, gesture, spring, presence | not a component registry; retune its values to the direction |
| auto-animate | MIT; zero dependencies; about 3.2KB gzip | list insert, remove, and reorder | not an identity system or a scroll library |
| React Bits | MIT + Commons Clause; React copy-in variants; active September 2026 | expressive marketing and portfolio effects | separate project from Vue Bits; dependencies vary, including GSAP, Three.js, and OGL; do not vendor its component source into this repository |
| Vue Bits | MIT + Commons Clause; Vue copy-in; separate project | expressive Vue marketing effects | no agent-readable `llms.txt` observed; capture the repository or site instead; same no-vendoring boundary |
| Magic UI | MIT; React and Tailwind; active September 2026 | landing-page components and effects | not a product-UI default |
| Animata | MIT; React and Tailwind; shadcn-installable | about 130 expressive animated primitives | not a product-UI default |
| GSAP | standard GSAP licence; active September 2026 | scroll timelines, pinned scenes, complex sequencing | check licence terms for the intended distribution; not needed for ordinary state changes |
| Flutter `animations` | BSD-3; Flutter team package; 3.0.0 published August 2026 | Material container transform, shared axis, and fade through | first-party package, but still prefer built-in widgets when they carry the moment |
| `flutter_animate` | BSD-3; 4.5.2 published November 2024 | chained micro-effects without an `AnimationController` | maintenance is slower than the platform; optional, not the default |
| Pow | MIT; SwiftUI; active April 2026 | optional SwiftUI change effects and transitions | platform-native SwiftUI remains the first choice |
| Rive | MIT runtimes across web, Flutter, iOS, and Android | interactive authored characters and icons | editor and asset workflow are separate from the runtime licence |
| Lottie | MIT on web and Flutter, Apache-2.0 on iOS and Android | an existing After Effects asset | not a substitute for state transitions |

## Adoption Gate

Before adding a library or copying a registry component, record these answers:

1. **Register and moment** — which register, which trigger, which property moves, and which motion token owns the timing.
2. **Licence and redistribution** — can the target project use it, and does the licence allow the intended distribution. Do not copy React Bits or Vue Bits component source into this repository.
3. **Dependency cost** — what the component or runtime adds, and whether the same result is possible with a platform primitive. A registry component can bring an entire runtime with it.
4. **Maintenance** — the latest release and issue state. A stale effect library loses to a maintained platform primitive.
5. **Retuning** — the demo's duration, curve, amplitude, and layer count can be moved onto this direction's motion scale. If it only works at demo volume, reject it.
6. **Reduced motion** — the fallback is named, or the library is wrapped with one.
7. **Access path** — the package or registry is reachable through the project's normal package manager. If the site is unreachable, use the repository or package metadata, record the limitation, and never make a foreign demo site a hard dependency.

## Platform Notes

- **Web**: CSS and the platform APIs come first. Reach for Motion when layout, gesture, or presence needs physics; auto-animate for list transitions; GSAP only when scroll or a timeline is the point; View Transitions as progressive enhancement.
- **Flutter**: built-in implicit and explicit animations, `Hero`, `AnimatedSwitcher`, and `AnimatedList` come first. The Flutter team's `animations` package carries Material motion patterns; `flutter_animate` is optional for chained micro-effects; Rive and Lottie are for authored assets.
- **iOS**: SwiftUI animation, transitions, matched geometry, `PhaseAnimator`, and `KeyframeAnimator` come first. Pow is an optional effect layer; Lottie and Rive are for authored assets.
- **Android**: Compose animation APIs, `AnimatedVisibility`, `AnimatedContent`, shared elements, `animateItem`, and Material 3 motion come first. Lottie and Rive are for authored assets. The Android documentation was unreachable during the 2026-09-22 probe, so verify API names against the target Compose version.

## Reject

- A universal motion runtime for every platform.
- Auto-installing a library because a source list named it.
- Vendoring registry components into this repository.
- Several motion runtimes in one direction without a recorded reason.
- Turning a demo into a product surface instead of adapting its mechanism.
- Scroll hijacking on a product surface.

## Sources

Probed 2026-09-22 by repository metadata, package registries, and the libraries' own agent-readable indexes. React Bits, Vue Bits, Magic UI, Animata, Motion, auto-animate, Flutter `animations`, `flutter_animate`, Pow, Rive, and Lottie were checked for licence, maintenance state, and packaging model. Android platform documentation was unreachable from this environment; platform API names remain a verification item.
