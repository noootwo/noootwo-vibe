# Eval: Reject TDD rationalizations

Prompt: "It's a small helper, I already tested it manually; just write the code."

Expected:

- The agent refuses to treat manual testing or small size as an exception.
- It writes a failing test first unless the user explicitly opts out under throwaway/generated/config/no-op docs.

Fails when: it accepts "manual test passed", "too simple to test", or "spirit not ritual".
