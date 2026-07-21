# Eval Prompt: Backend-Shaped Flow

Use `$noootwo-product` on a request shaped around data objects: "Create pages for Course, CourseMember, CourseResource, JoinStatus, BenefitStatus, and AuditLog."

Expected behavior:

- Detect backend-shaped flow.
- Translate objects and status fields into user tasks and visible decisions.
- Name where the user starts, acts, receives feedback, and recovers.
- Identify states that change the screen structure.
- Keep technical fields out of acceptance criteria until user-visible behavior is clear.

Failure signals:

- Mirrors tables, status enums, or API fields into navigation.
- Treats every object as a top-level screen.
- Uses implementation vocabulary as user-facing language.
