# Dependency Fallback

Noootwo skills invoke one another, and any skill can be installed alone. When a named
skill is missing, do not guess, silently degrade, or pretend to be that skill.

## Order

1. Try to install the missing skill from the published workspace:

   ```bash
   npx -y skills add noootwo/noootwo-vibe --global --agent codex --skill <name> --yes
   ```

   If the checkout is local and installable, prefer the local path.

2. If install succeeds, invoke the newly installed skill and read its `SKILL.md`.

3. If install fails, take the smallest direct fallback the current skill already owns,
   then mark the record with `skill-missing: <name>`.

## Marker

Use exactly `skill-missing: <name>` in the produced record, note, or owning file. It is
the signal a later `noootwo-state` reconciliation pass looks for. Do not leave a silent
degradation with no marker.

## Persistence fallback

When `noootwo-state` is missing and install fails, a specialist writes its conventional
owning file directly and adds `skill-missing: noootwo-state`. The specialist still owns
its domain artifacts; only durable project state and context is affected. When the state
skill becomes available, absorb the marked record through a normal abstract request and
remove the marker.

## Routing fallback

When the missing skill is a routing target (for example a specialist `noootwo-workflow`
cannot schedule), name it, record `skill-missing: <name>` as an open blocker, and stop
for the user rather than running the target's method from memory.
