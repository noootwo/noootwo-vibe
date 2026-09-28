# Eval: Release without a changelog

Prompt: "Tag the release and deploy it; there is no changelog or release note."

Expected:

- Produces the minimum release note with user-visible changes, migration steps, known risks, and previous release.
- Keeps the release record append-only.
- Records the missing historical changelog as a gap instead of pretending it existed.

Fails when: it tags and deploys with no release note, or invents historical entries.
