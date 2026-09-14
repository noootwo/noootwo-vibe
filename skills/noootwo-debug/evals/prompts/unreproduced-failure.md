# Eval: Unreproduced failure

Prompt: "Customers occasionally get a 500 on checkout. It has never happened locally, there is nothing useful in the logs, and it is happening more often. Please fix it."

Expected:

- It attempts a reproduction and records what it tried, rather than declaring the bug fixed by inspection.
- It recognizes intermittent failure as a measurement problem: it tries to establish a rate, and suspects order, time, concurrency, shared state, resource limits, or cache state rather than guessing at a line of code.
- It proposes instrumentation at the boundaries and leaves it to catch the next occurrence, or states the specific access, log, or reproduction it needs.
- It treats the failure as an incomplete evidence chain, and presents any interim mitigation as a mitigation rather than a proven fix.

Fails when: it ships a speculative fix for a bug it never reproduced; it blames the environment without checking the environment; it reports a cause it cannot support with evidence.
