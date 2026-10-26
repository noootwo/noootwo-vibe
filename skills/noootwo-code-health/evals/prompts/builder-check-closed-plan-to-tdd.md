# Eval: A closed plan goes directly to TDD

Prompt: "Implement this approved local plan. Interfaces, file scope, assertions, verification commands, and Review Focus are complete, and no new boundary is crossed."

Expected:

- Recognizes that the plan is decision-complete and the seam is obvious.
- Skips a ceremonial fresh builder review when the handoff is not cross-session, expensive, or cross-boundary.
- Does not invent new product or architecture questions.
- Hands the first behavior assertion to TDD.

Fails when: it reruns product discovery; it creates a second implementation plan; or it blocks on ordinary naming or test-file organization.
