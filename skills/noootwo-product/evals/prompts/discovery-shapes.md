# Eval: Greenfield, feature list, and backend-shaped requests

Prompts (run each):

1. "I want to build something for teachers." (greenfield)
2. "Add a dashboard, a settings page, a report page, a team page, and notifications." (feature list)
3. "Give me a CRUD screen for the orders table with a status enum and an owner id." (backend-shaped)

Expected:

- Greenfield: the agent converges on a first loop with a real user and a proof signal, instead of a platform.
- Feature list: it finds the user outcome behind the list and treats most items as deferred.
- Backend-shaped: it replaces object names with user tasks, status flags with what the user sees and can do next, and groups fields by decision moment.
- All three run the same flow and stop at a shared understanding before building.

Fails when: it accepts the feature list as scope; it mirrors the table in the UI; it produces a full PRD.
