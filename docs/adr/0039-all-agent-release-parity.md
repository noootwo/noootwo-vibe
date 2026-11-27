# 0039 — All-agent installation parity is a release gate

## Status

Accepted on 2026-11-27.

## Context

The published release was verified in `~/.agents/skills` and
`~/.codex/skills`, but this machine also exposes Claude, Cursor, and Gemini
skill roots. Those roots were not part of the release check.

- `~/.claude/skills` contained symlinks to only part of the public set, plus
  broken `noootwo-docs` and `noootwo-review` links.
- `~/.cursor/skills` and `~/.gemini/skills` had no Noootwo skills.
- The checker treated a broken symlink as absent because it tested the target
  with `is_dir()`, so stale links could survive `--prune`.

The artifact was therefore published while some installed agents could not
discover the current suite. A two-root check proved two roots, not the machine.

## Decision

1. A release that publishes skills or agent instructions must detect every
   existing agent skill root on the release machine.
2. The release installs the full public set into every detected root, prunes
   stale `noootwo-*` entries, and reads back every child `VERSION` against
   `skills.json`.
3. A missing copy, stale entry, broken link, or version mismatch blocks the
   release. The release cannot claim all-agent availability from one root.
4. The release record lists every detected root, the readback for each child,
   the pruned skills, and their backup paths.
5. `scripts/sync_local_install.py --all-known` performs the sync and
   `--all-known --check --json` produces the release evidence. The known set
   covers the standard Agent Skills and Codex roots plus Claude, Cursor, Gemini,
   Windsurf, and Codeium roots when present; an additional path is passed with
   `--target-root`.
6. Installed content is reloaded by starting a new agent task. An app restart is
   required only when a new task still resolves the old installed version.

## Consequences

- A local release now depends on the machine's installed agent roots, not only
  on CI and the public registry.
- The checker fails on partial and stale installations, which can make a
  previously green release require cleanup.
- The known-root list needs maintenance when an agent introduces another
  standard path. An unknown path is covered only when passed explicitly.
- CI cannot prove a developer machine's roots; the post-merge local check is
  part of release evidence rather than a portable CI gate.

## Rejected Alternatives

- **Keep checking two roots.** It cannot support the claim that every installed
  agent sees the release.
- **Publish first and sync later.** The release would be observable in a mixed
  state that users can hit.
- **Delete every stale directory without backup.** It makes cleanup fast but
  destroys the evidence needed to diagnose an accidental prune.
- **Require an app restart after every release.** A new task reloads the skill
  catalog; restart is the fallback only when stale content persists.

## Verification

- `python scripts/sync_local_install.py --all-known --prune`
- `python scripts/sync_local_install.py --all-known --check --json`
- `python scripts/validate_skill_workspace.py .`
