# Eval Prompt: Averaged References

Use `$noootwo-design` on a direction built from three strong references that disagree about density, type contrast, and motion speed, where the response takes the safe middle of all three.

Expected behavior:

- Pick one dominant direction and let the others contribute narrow details.
- Record the Reference Lock: build target, primaries, and what must not drift.
- Name the conflicting traits that were dropped and why.
- Keep the surviving direction's sharp traits rather than smoothing them.

Failure signals:

- Blends conflicting references into a compromise that resembles neither.
- Keeps every trait because each one seemed good.
- Records a lock that names a target without naming what must not drift.

Manual evaluation: pass only when the response shows the expected behavior and avoids all failure signals.
