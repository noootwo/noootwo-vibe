# Eval Prompt: Explicit Motion Request Cannot Collapse To Zero Motion

Use `$noootwo-design` after the user explicitly asks for motion, animation, liveliness, fancy treatment, or a named motion library on a product surface. The user also says the result should stay appropriate and not become noisy.

Expected behavior:

- Record `User motion intent: requested` and treat the requested scope as `add moment`; moderation changes register and count, not whether motion exists.
- Choose one primary authored move and at most one supporting move.
- Name the actual trigger, implementation tool, duration, curve, layers, and reduced-motion fallback.
- Produce an artifact-visible result; an explanation, a rejected-ideas list, or a generic component transition does not satisfy the request.
- If no surface can safely carry motion, stop and ask the user to accept no authored motion instead of silently choosing `craft only`.

Failure signals:

- Records `craft only` or `leave simple` without the user accepting no authored motion.
- Treats "适度" as permission for zero motion.
- Says a library was considered but never selects it, replaces it with a recorded equivalent, or rejects it with a concrete reason.
- Calls the result ready when no rendered motion exists.

Manual evaluation: pass only when the response shows the expected behavior and avoids all failure signals. The matching artifact check is `python scripts/eval_noootwo_artifacts.py <project> --scenario explicit-motion-request-honored`.
