# Product Interview Handoff

Use this packet when `$noootwo-workflow` routes a product request to `$noootwo-product`, especially when the user requests grill-style or detailed sequential confirmation.

```markdown
Product Interview Handoff
- Task class:
- Raw product idea:
- Explicit confirmation request:
- Interview depth: light | deep
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
- Non-goals:
```

Rules:

- Initialize every ledger field, even when it is empty.
- Preserve the user's own wording for an explicit detailed-confirmation request.
- Every checked fact needs a source path, artifact, or an explicit `none found` note.
- An active risk is not resolved without a decision, owner, and evidence. Evidence may be a user confirmation, delegated assumption, checked artifact, or deliberate scope cut.
- `intent fit: pending` blocks Product-to-Design Handoff or implementation planning in deep mode until the user confirms or delegates the final fit.
- Workflow carries the packet to Product; Product owns the questions and updates the ledger.
