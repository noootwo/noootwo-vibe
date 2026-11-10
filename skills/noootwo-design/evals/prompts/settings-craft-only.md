# Eval Prompt: Settings Need Craft, Not A Spectacle

Use `$noootwo-design` on a settings or configuration screen whose real problems are grouping, hierarchy, terminology, control states, and feedback placement. The user has not asked for motion.

Expected behavior:

- Select `craft only` and explain why the product task does not justify an authored moment.
- Record that motion was not requested or that the user accepted no authored motion.
- Fix the actual hierarchy, grouping, copy, state, focus, validation, and responsive behavior.
- Keep any platform feedback immediate and compatible with keyboard and assistive technology.
- Record the rejected opportunities and why they would add cost without improving the task.
- Run the standard task/platform light audition with 2-3 candidates, including one real product or design-system source, then use the evidence for grouping and state conventions.
- Keep the expressive source lane closed unless a motion candidate passes the product, frequency, and function gates.

Failure signals:

- Adds animated backgrounds, shaders, elaborate transitions, or sound to make settings feel premium.
- Treats visual polish as a substitute for unclear controls or missing feedback.
- Scans expressive motion or effect libraries for visual inspiration instead of doing the task/platform light audition.
- Calls the result ready without evidence of the corrected states.

Manual evaluation: pass only when the response shows the expected behavior and avoids all failure signals. The matching artifact check is `python scripts/eval_noootwo_artifacts.py <project> --scenario craft-only-justified`.
