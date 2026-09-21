# 0012 — Install-first dependency fallback with a missing-skill marker

## Status

Accepted.

## Context

The Noootwo skills are published as independent child skills, so a specialist can be
installed alone. When it needs a sibling that is not installed — for example a design
step that must persist durable state through `noootwo-state` — the sibling is absent and
the step cannot run the normal way.

Silently degrading would break the one-owner invariant, and hard-failing without a trace
would make a single-skill install unusable for otherwise independent work.

## Decision

- Record each skill's dependencies in `skills.json`.
- When a named skill is missing, first try to install it from the published workspace:
  `npx -y skills add noootwo/noootwo-vibe --global --agent codex --skill <name> --yes`.
- If install succeeds, invoke the newly installed skill normally.
- If install fails, take the smallest direct fallback the current skill already owns and
  mark the record `skill-missing: <name>`.
- For persistence, the fallback is to write the conventional owning file directly and add
  `skill-missing: noootwo-state`; a later reconciliation absorbs the marked record.

## Consequences

- Every skill that invokes a sibling carries a one-line install-first fallback rule.
- Missing dependencies are visible in `skills.json` and reconcilable via the marker.
- The one-owner invariant holds: fallback happens only while the owner is absent and is
  always recorded, never a silent second authority.
