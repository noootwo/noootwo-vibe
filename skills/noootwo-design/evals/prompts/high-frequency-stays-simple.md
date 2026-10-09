# Eval Prompt: High-Frequency Surface Stays Simple

Use `$noootwo-design` on a command palette, data table, or monitor that is used hundreds of times per day and already has clear hierarchy and state feedback.

Expected behavior:

- Record an intervention decision of `leave simple` or `craft only` from the product function, frequency, task risk, and existing evidence.
- Improve real usability issues through hierarchy, density, state clarity, or platform feedback instead of adding decoration.
- Reject motion for keyboard-initiated, high-frequency, or data-reading moments.
- State why no authored moment is needed and what evidence shows the surface is already sufficient.

Failure signals:

- Scans external effect libraries because the task is visually ordinary.
- Adds a signature animation, shader, sound, or new runtime to prove design effort.
- Treats any no-motion result as incomplete.
- Calls the work ready without checking real states or the nearest artifact.

Manual evaluation: pass only when restraint is justified by the product context and the response avoids every failure signal. The matching artifact check is `python scripts/eval_noootwo_artifacts.py <project> --scenario leave-simple-justified`.
