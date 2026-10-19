# Eval: A durable product spec uses the project's owning layer

Prompt: "The account-settings decisions are settled. Persist them as the project spec, and keep the small acceptance checklist in the reply."

Expected:

- Persists the settled contract through `noootwo-state` as a `spec` fact.
- Uses `docs/specs/` rather than another installed skill's default directory.
- Keeps the small acceptance checklist in the reply instead of manufacturing a larger document.

Fails when: it writes under `docs/superpowers/`, treats the active `.noootwo/` design contract as the durable project spec, or turns every settled checkpoint into a spec.
