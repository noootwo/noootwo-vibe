# Product Interview Handoff

Use this packet when `$noootwo-workflow` routes a product request to `$noootwo-product`, especially when the user requests grill-style or detailed sequential confirmation.

```markdown
Product Interview Handoff
- Task class:
- Raw product idea:
- Explicit confirmation request:
- Clarity Gate: clear | one-material-gap | ambiguous/high-risk | explicit-interview
- Interview depth: none | light | deep
- Presentation language: infer from the user's latest message; preserve intentional technical terms
- Checked facts:
  - Fact:
    Source:
  - If none were found: state that explicitly.
- Decision ledger:
  - Confirmed:
  - Delegated assumptions:
  - Deferred:
  - Rejected:
  - Active risks:
    - Risk:
      Status: open | resolved | explicitly accepted | converted to scope cut
      Evidence:
      Owner:
- Intent fit: pending | confirmed | delegated
- Decision Interview needed: yes | no
- Waiting on:
- Execution status: blocked | ready_for_handoff | ready_for_execution
- Non-goals:
```

Rules:

- Initialize every ledger field, even when it is empty.
- Preserve the user's own wording for an explicit detailed-confirmation request.
- A `clear` result means Decision Interview is not needed. Do not create a waiting state or expose an interview template; continue with the smallest appropriate Product artifact or execution route.
- Every checked fact needs a source path, artifact, or an explicit `none found` note.
- An active risk is not resolved without a decision, owner, and evidence. Evidence may be a user confirmation, delegated assumption, checked artifact, or deliberate scope cut.
- `waiting on: user_answer` and `execution status: blocked` are the default while any material product choice is open. They explicitly stop implementation, design handoff, and implementation planning.
- `ready_for_handoff` requires explicit user selections or explicit delegated assumptions for every material choice. A recommended default alone never changes the status.
- `intent fit: pending` blocks Product-to-Design Handoff or implementation planning in deep mode until the user confirms or delegates the final fit.
- User-facing Product responses use the presentation language and natural localized labels. Keep canonical English field names in this packet only when they are useful for cross-skill interoperability.
- Workflow carries the packet to Product; Product owns the questions and updates the ledger.
