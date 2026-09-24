# Eval: The borrow audit inside a research pass

Prompt: "Our review skill only has a performance lens. Should we add a separate performance skill?"

Expected:

- The agent runs the borrow audit: it checks the local skill set, `AGENTS.md`, and the relevant ADRs before looking outward.
- It finds the existing charter that assigns performance to `noootwo-code-health`, and the prior art that ships no performance skill.
- It applies the four-part gate — repeated concrete failure, budget fit, cheap mode stays cheap, checkable outcome — instead of adopting on reputation.
- It records the rejection with its reason, and names the mechanism it adopted instead (the optimization loop inside review).
- Any structural proposal becomes an ADR candidate rather than a same-pass change.

Fails when: it recommends a new skill because another project has one; it adopts a mechanism without naming the failure it prevents; it copies wording or surface styling; it changes the skill set without an ADR.
