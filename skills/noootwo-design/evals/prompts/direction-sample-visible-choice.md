# Eval: Choose from viewed samples

Prompt: "The three dashboard skeletons are ready. Which one should we build, and why?"

Context: The samples show different hierarchy, density, and interaction models.

Expected:

- Opens or screenshots each sample before evaluating it.
- Describes observed structural differences, not just aesthetic labels.
- Prints a recommendation tied to the product objective.
- Waits for the user to select or delegate before implementation.

Fails when: it recommends from filenames; it treats metadata as proof of the rendered result; or it proceeds without a recorded selection.
