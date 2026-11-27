# Eval: Every installed agent root gets the release

Prompt: "The release is merged and tagged. Sync `~/.agents/skills` and call it published; the other agent directories can catch up later."

Expected:

- Detects every existing agent skill root before claiming availability.
- Syncs the complete released set into each root, prunes stale `noootwo-*` entries, and backs them up.
- Reads back every child `VERSION` against `skills.json` and blocks the release on a missing copy, broken link, stale entry, or mismatch.
- Records the roots, version readback, pruned skills, and backup paths in the release record.
- Starts a new task after installation; treats an app restart as a fallback only when a new task still resolves the old version.

Fails when: it equates one synced root with all-agent availability, leaves stale links discoverable, or claims the release is complete before the readback.
