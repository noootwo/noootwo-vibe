# Eval: Preparatory refactoring before a hard change

Prompt: "Add a new payment provider. The current payment branch is a long conditional and the new provider does not fit it."

Expected:

- Switches to the refactoring hat before adding the provider.
- Confirms a green baseline, then uses a small catalog move such as Replace Nested Conditional with Guard Clauses, Replace Conditional with Polymorphism, or Introduce Parameter Object.
- Makes the behavior-preserving change first, runs tests, and only then adds the new provider.
- Does not bundle the provider behavior change with the structural change.

Fails when: it adds the provider first and cleans up afterward, or it changes behavior while wearing the refactoring hat.
