# Eval Prompt: Style Prose Without Visual Evidence

Use `$noootwo-design` when the user asks for a premium, niche, unusual app style and the draft response describes the style fluently but has no screenshots, references, visual sample, or spike.

Expected behavior:

- Run `Style Evidence Check` before treating the direction as implementation-ready.
- Mark confidence as low when visual evidence or implementation translation is missing.
- Ask for, find, or create a low-cost spike/artifact before claiming the style is understood.
- Return to style discovery when the evidence and proposed spec do not match.

Failure signals:

- Writes confident style rules from adjectives alone.
- Moves directly to Design Contract or UI edits without evidence.
- Calls the design ready because the prose sounds high-end.

Manual evaluation: pass only when the response shows the expected behavior and avoids all failure signals. The matching artifact check is `python scripts/eval_noootwo_artifacts.py <project> --scenario style-prose-without-visual-evidence`.
