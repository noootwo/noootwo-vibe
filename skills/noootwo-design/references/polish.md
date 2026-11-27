# Polish

A local change inside an existing system. This is the `polish` command.

## Scope

Polish preserves the current visual world. It may tighten spacing, type, hierarchy, states, or local layout. It does not:

- replace the palette, type system, navigation, or component language;
- add a new page, feature, or motion language;
- rewrite public copy unless the request is about that copy;
- turn a local defect into a redesign.

If the probe reveals a structural, contrast, or copy defect outside the requested scope, report it. Do not fix it silently.

## Copy

When the change adds, removes, or rewrites a visible string, test it as the
primary user before accepting it:

- does it name the user's object, state, or next action?
- does it expose a mechanism term (renderer, tier, frame rate, library, or
  internal status) that the user does not need to decide?
- would a good default remove the setting or the explanation entirely?

A failed check is `fix`. Record the result in the card.

## Process

1. Read the current UI and its tokens.
2. Run `design_probe.py` once to capture the before state at the shipped width and `320`.
3. Make the smallest change that addresses the named problem.
4. Run the probe again at the shipped width and `320`, including the long-copy state when text changed.
5. Record a five-line card in the conversation:

```text
Changed:
Rendered at:
Saw:
Defect:
Decision: keep | fix | recapture
```

## Done

- The change is rendered and inspected.
- The probe has no new blocker.
- The card names what changed, where it was rendered, what was seen, and the remaining defect.
- The current visual system is intact.

## Do not

- Run a reference audition, three directions, or a full harness for a local polish.
- Claim `ship` from source inspection alone.
- Change colour, navigation, component language, or copy without saying so.
