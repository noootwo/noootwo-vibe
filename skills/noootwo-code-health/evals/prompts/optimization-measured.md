# Eval: Optimization is measured, not intuitive

Prompt: "This page feels slow; optimize it."

Expected:

- Review names a metric and budget, takes a reproducible baseline, and localizes with a profile/trace/report before changing code.
- It changes the smallest thing, proves before/after, and leaves a guard.
- It re-runs tests and waits for user acceptance before release.

Fails when: it guesses the hot path, rewrites code without a baseline, or claims a speedup from a single noisy run.
