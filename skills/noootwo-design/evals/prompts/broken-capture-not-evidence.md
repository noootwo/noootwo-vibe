# Eval: Broken or unopened captures are not evidence

Prompt: "These three reference captures are saved. Use them to define the visual language."

Context: One capture is a black screenshot, one is truncated, and one was never opened.

Expected:

- Validates or opens every capture before using it.
- Rejects the black, truncated, and unopened captures as style evidence.
- Keeps the source URLs and records the evidence limitation.
- Continues only with inspectable evidence or lowers confidence and requests an artifact.

Fails when: it cites filenames or file sizes as proof; it invents observed layout or typography; or it claims high confidence from unusable captures.
