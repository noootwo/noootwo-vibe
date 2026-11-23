# Releasing Skills

1. Update the changed skill's `skills/<skill>/VERSION`.
2. Mirror that version in `skills.json`.
3. Update `docs/releases/<skill>.md` with user-visible changes and migration notes.
4. Open or reconcile the Release Verification Ledger described in `skills/noootwo-release/references/release-verification-ledger.md`. Keep only release-bound checks, dedupe by evidence boundary, and record exact evidence.
5. Consume the reconciled ledger through the Release Check on the exact candidate, seal the completed ledger into the release record, then reset the open working ledger.
6. Run workspace validation and skill discovery checks from `README.md`, including a local clean install of all child skills with `--skill '*'`.
7. Commit the change.
8. Create a tag using the skill's `tagPrefix` from `skills.json`, for example `noootwo-code-health@vX.Y.Z`.
9. Push the branch and tags.
10. Verify the public clean install and sync both local install roots for a release batch:

```bash
python scripts/sync_local_install.py --no-dedupe-codex
python scripts/sync_local_install.py --target-root ~/.codex/skills --no-dedupe-codex
python scripts/sync_local_install.py --check
```

The default target is `~/.agents/skills`. Keeping `--no-dedupe-codex` while
syncing both roots prevents the first command from removing the Codex copy
before the second command refreshes it. Each sync verifies the installed
`VERSION` and `SKILL.md`; `--check` verifies both roots without copying.

After an install or update, start a new Codex task so it reloads the skill
catalog. Restart the app only when a new task still resolves the old installed
version. `VERSION` is metadata; the installed `SKILL.md` and references are the
content Codex reads.

The public installation contract is:

```bash
npx -y skills add noootwo/noootwo-vibe --skill '*' --global --agent codex --yes
```

The repository default branch must contain the published multi-skill workspace. A feature branch with the same files is not enough for the shorthand source above, because the `skills` CLI resolves `owner/repo` against the default branch.

Do not use the root `VERSION` as a child-skill release source.
