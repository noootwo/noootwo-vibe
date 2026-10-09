# Eval Prompt: Settings Need Craft, Not A Spectacle

Use `$noootwo-design` on a settings or configuration screen whose real problems are grouping, hierarchy, terminology, control states, and feedback placement.

Expected behavior:

- Select `craft only` and explain why the product task does not justify an authored moment.
- Fix the actual hierarchy, grouping, copy, state, focus, validation, and responsive behavior.
- Keep any platform feedback immediate and compatible with keyboard and assistive technology.
- Record the rejected opportunities and why they would add cost without improving the task.

Failure signals:

- Adds animated backgrounds, shaders, elaborate transitions, or sound to make settings feel premium.
- Treats visual polish as a substitute for unclear controls or missing feedback.
- Requests external research before a candidate has passed the product and frequency gates.
- Calls the result ready without evidence of the corrected states.

Manual evaluation: pass only when the response shows the expected behavior and avoids all failure signals. The matching artifact check is `python scripts/eval_noootwo_artifacts.py <project> --scenario craft-only-justified`.
