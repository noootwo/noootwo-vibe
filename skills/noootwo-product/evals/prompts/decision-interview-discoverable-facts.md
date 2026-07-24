# Eval Prompt: Decision Interview Discoverable Facts

Use `$noootwo-product` in an existing repo where README, status docs, screenshots, or current UI already identify the user, platform, and existing entry points.

Expected behavior:

- Inspect discoverable product facts before asking the user.
- Ask only unresolved product tradeoffs that materially change the plan.
- Cite the checked repo/UI/doc facts in the Decision Interview context.
- Avoid asking for facts that are already present in the environment.

Failure signals:

- Asks "who is the user?" when the repo docs already answer it.
- Asks where the current UI or entry point is without searching.
- Treats Decision Interview as a generic intake form.

Manual evaluation: pass only when the response shows the expected behavior and avoids all failure signals.
