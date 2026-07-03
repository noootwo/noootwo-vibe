# Responsive Visual Gates

Use this before `ready` on any non-trivial UI artifact. A design that clips on common viewports is not ready, even if the desktop screenshot looks strong.

## Required Viewports

Record screenshot, preview, or limitation evidence for:

- Phone: `390px` wide or nearest native device.
- Tablet or narrow desktop: `768px` wide.
- Desktop: `1440px` wide.
- Text scale or browser zoom: at least one check for 200% zoom, larger system text, or explicit limitation.

## Hard Fail Checks

Any of these forces `refine`:

- `document.documentElement.scrollWidth > window.innerWidth` on a web artifact.
- Key headline, nav, primary action, or critical data is clipped.
- Mobile display headline wraps into an unreadable block or pushes the task below an unreasonable first screen.
- Main navigation, primary action, or recovery action is inaccessible.
- Text scale breaks touch targets, state labels, or dense rows.
- Flutter/native preview ignores safe area, text scale, or platform chrome.

## Review Action

- Use `Return action: return to responsive pass` when the direction is good but viewport adaptation fails.
- Use `Return action: return to stack pass` when the failure is caused by target-stack layout behavior.
- If responsive evidence is unavailable, record the limitation and choose `needs artifact` or `refine`, not `ready`.

## Lightweight Automation

Use `scripts/check_visual_gates.py` when a local URL or static HTML file is available. The script checks overflow and obvious clipped text across the required viewports. It is a guardrail, not a substitute for design judgment.
