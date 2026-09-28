# Eval: Classify the version change

Prompt: "We removed a public API field, added a new optional parameter, and fixed a bug. Pick the next version."

Expected:

- Treats the removed public field as a breaking change and commits to the resulting major or project-policy equivalent.
- Records the compatible feature and bug fix in the same release record.
- States the compatibility classification and migration notes.

Fails when: it picks a patch or minor version despite the incompatible removal, or omits the migration note.
