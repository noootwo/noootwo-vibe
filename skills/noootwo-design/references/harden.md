# Harden

States, errors, accessibility, localization, and copy. This is the `harden` command.

## States

Render each state that can occur:

- default
- loading
- error
- empty
- disabled
- focus
- long copy and localization

A state is not a spinner overlay. It preserves the reading order, the primary action, and the user's place in the task.

- Loading exposes `aria-busy`, disables actions that would fail, and does not collapse the page into a different layout.
- Error states say what happened, what was preserved, and what to do next. A technical code may appear as secondary, copyable detail.
- Empty states invite the next action instead of describing the absence.
- Disabled states explain why the action is unavailable when the reason is not obvious.

## Focus and keyboard

- Every interactive control has a visible focus indicator.
- The focused control is not hidden by a fixed, sticky, or overlay element.
- Focus order follows the reading order.
- A keyboard user can reach the primary action without traversing a hidden or duplicated control.
- Outline removal is paired with a visible replacement.

## Contrast and targets

- Normal text meets `4.5:1`; large text meets `3:1`.
- Control boundaries, focus rings, and meaningful icons meet `3:1` against their adjacent surface.
- Touch targets meet `24x24` CSS px; the product baseline is `40px` where the platform allows it.
- Color is not the only carrier of state or meaning.

## Copy

- Labels use the user's vocabulary or a domain term the audience already shares.
- Headings name the user's object, task, state, or next action.
- A note earns its place only when it prevents an error, explains a consequence, supports recovery, or teaches a term needed now.
- Design rationale, change summaries, quality claims, and evaluation notes stay out of the product surface.
- A setting names the user's outcome or a good default, not the mechanism that implements it.
- A layout-only request does not authorize new public copy.

## Localization

- Long CJK and mixed-language labels wrap without clipping or widening the document.
- The document language matches the visible copy.
- Dates, numbers, and plural forms use the platform's localization primitives.

## Done

- Every required state is rendered and inspected.
- Focus is visible and unobscured.
- Text, control, and focus contrast pass.
- Errors and empty states name a next action.
- Long copy and localization do not break the layout.
