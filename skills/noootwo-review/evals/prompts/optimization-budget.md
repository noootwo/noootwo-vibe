# Eval: Optimization with a metric and a budget

Prompt: "The dashboard takes about four seconds to become interactive. Make it faster."

Expected:

- The agent treats this as optimization work in `noootwo-review`, not as a bug hunt in `noootwo-debug`, and does not demand a root cause before measuring.
- It names a metric and a budget before changing code, and says where the budget came from.
- It takes a reproducible baseline with a named command and records the conditions.
- It localizes with a profile, trace, or bundle report before choosing what to change.
- It changes the smallest thing that moves the metric, and proves before and after with the same command.
- It states the mechanism that explains the improvement, and leaves or records a guard.

Fails when: it optimizes before measuring; it micro-optimizes something the profile never shows; it declares a win from one noisy run; it hides the remaining cost instead of reporting it; or it routes the request to `noootwo-debug` because the page is "slow".
