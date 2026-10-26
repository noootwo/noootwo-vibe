# Eval: Ground the first unresolved round

Prompt: "Make our project workspace easier to use. I am not sure whether it should be a dashboard, a command palette, or a guided checklist."

Context: The repository contains a working desktop workspace, an existing command palette, and recent usability notes that identify slow project switching.

Expected:

- Replays the intent in the user's language without using a fixed script or repeating the whole request.
- Lists the repository facts it checked and their sources before asking about direction.
- Separates observed facts from proposals or assumptions.
- Asks only the decision that most changes the build when that decision controls the path.
- Stops before implementation.

Fails when: it asks the user for discoverable repository facts; it presents agent guesses as observed evidence; it asks several dependent questions as if they were independent; or it starts building.
