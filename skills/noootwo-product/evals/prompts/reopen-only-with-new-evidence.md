# Eval: Reopen only with new evidence

Prompt: `balance_placement` was answered as `账号行内常显`. The user then says
the desktop always collapses the sidebar, so the account row is invisible at
first use. Two other settled decisions are untouched by this constraint.

Expected:

- Reopens only `balance_placement`, showing the old answer and naming the new
  constraint as the reason.
- Leaves the other settled decisions frozen.
- On the new answer, records it as superseding the old entry, keeping the old
  answer as history.

Fails when: it re-asks other settled decisions; it reopens without naming what
changed; it silently replaces the old answer; or it regenerates the whole
option set as if the decision were new.
