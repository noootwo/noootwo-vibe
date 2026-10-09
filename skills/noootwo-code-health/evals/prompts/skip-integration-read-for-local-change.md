# Eval: Skip the Integration Read for an obvious local change

Prompt: "Fix a typo in this component's error message. The nearest test covers the message and there is no contract, data, or migration impact."

Expected:

- Treats the change as a local, obvious-seam edit.
- Routes directly to `noootwo-tdd` or the local edit; it does not run the Integration Read.
- Does not create a Change Shape, ADR, or architecture discussion.

Fails when: it triggers an Integration Read, asks for a design document, or expands the scope into nearby cleanup.
