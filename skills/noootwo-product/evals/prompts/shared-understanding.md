# Eval: Shared understanding

Prompt: a grilling session where the user has just answered the last open frontier question.

Expected:

- The agent recomputes the frontier, finds it empty, and stops asking new questions.
- It summarises what is settled, assumed, deferred, rejected, and any risk still carried.
- It states the check in plain words: this first loop solves X for Y and deliberately does not solve A or B.
- It asks once whether that matches what the user meant, unless the user already delegated the final call.
- It waits for that confirmation before handing off or planning implementation.
- On "no", it reopens only the mismatched branch.

Fails when: it continues asking settled questions; it treats its own summary as confirmation; it hands off with a carried risk that would change the main path, scope, trust boundary, or acceptance.
