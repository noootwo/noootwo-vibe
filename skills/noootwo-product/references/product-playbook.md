# Product Playbook

Use this when the compact `Product Checkpoint` is not enough.

## Practice Basis

- User-centered product work starts from user needs, context, and mental models before implementation shape.
- Good AI-assisted product work makes assumptions explicit, proposes alternatives, and asks only the choice that changes the result.
- Low-friction products reduce exposed concepts, use familiar language, and make the next action obvious.
- Product work should cut scope as deliberately as it adds scope.

## Product Choice Challenge Template

```markdown
Product Choice Challenge
- Repo/product truth checked:
- Decision:
- Recommended default:
- Option A:
  - User understanding:
  - Operation cost:
  - Fit:
  - Risk:
- Option B:
  - User understanding:
  - Operation cost:
  - Fit:
  - Risk:
- Option C:
  - User understanding:
  - Operation cost:
  - Fit:
  - Risk:
- Outcome: user chose | user delegated to agent | no question needed
```

Use two options when the third is filler. Lead with the recommended default unless neutrality is required.

## User Lens

Check these before proposing scope:

- Who is the real user and what pressure are they under?
- What do they already understand before arriving here?
- What words would they use for this task?
- What do they need to decide now, and what can wait?
- What would make them feel stuck, unsafe, or unsure?
- What is the smallest result that feels complete from their side?

## Scope Lens

Classify each proposed item:

- `must exist`: required for the current user outcome
- `can wait`: useful but not needed for the first complete path
- `hide behind progressive disclosure`: useful only after context or intent is clear
- `should not exist`: confusing, premature, developer-facing, or not tied to user value

Do not keep a feature because it is easy to implement. Keep it only if it improves the user outcome.

## IA And Flow Lens

The main path should answer:

- where the user starts
- what the primary action is
- what information is needed before action
- what feedback confirms progress or success
- where advanced or destructive choices live
- how the user recovers from empty, error, permission, or partial states

Red flags:

- screens organized by database object instead of user task
- many equal-weight actions before the user has context
- labels that expose internal states, IDs, flags, or implementation terms
- success that is only visible as data changing somewhere else
- errors that explain the system but not the next user action

## Acceptance Criteria

Write acceptance as observable user behavior:

- Good: "A first-time student can open a locked resource and understand that joining the course is required before access."
- Weak: "Render a permission dialog with `courseId` and `status`."
- Good: "After upload failure, the teacher can retry without reselecting the file."
- Weak: "Show error toast on API 500."

Include technical criteria only after the user-visible behavior is clear.

## Handoff Templates

### To `$noootwo-design`

- Real user and scenario:
- Main path:
- Product constraints:
- States to design:
- Product choice resolved or delegated:

### To `$noootwo-review`

- Product behavior to preserve:
- Acceptance criteria:
- Risky edge states:
- Technical judgment requested:

### To `$noootwo-docs`

- Stable product decision:
- Owning doc layer:
- User-facing language or migration note:
- Evidence or date:
