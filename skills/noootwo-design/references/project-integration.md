# Project Integration

Use this reference when installing Noootwo Design into a project workflow.

## Standard `AGENTS.md`

Agents commonly read a root `AGENTS.md` as project context. Integrate the short `UI/Design Workflow` guidance from `assets/AGENTS.md` into the target project's root `AGENTS.md`.

The bootstrap script creates or merges this section by default:

```bash
python scripts/bootstrap_noootwo_harness.py /path/to/project
```

Use `--skip-agents` when the caller explicitly does not want `AGENTS.md` touched.

If the project has no `AGENTS.md`, create it from `assets/AGENTS.md`.
If the project already has `AGENTS.md`, merge in only the `## UI/Design Workflow` section from `assets/AGENTS.md`. Preserve existing project instructions and avoid overwriting unrelated sections.

## Purpose

The `AGENTS.md` snippet is only a project-level pointer. It tells agents that UI-related work is led by `$noootwo-design` and that project design context lives in `.noootwo/`. Detailed workflow rules stay inside the skill.

## Integration Rules

- Do not create custom project-guide filenames for agent context.
- Prefer the root `AGENTS.md`.
- Create `AGENTS.md` when it is missing unless `--skip-agents` is used.
- Merge the `## UI/Design Workflow` section when `AGENTS.md` already exists.
- Make merging idempotent; repeated bootstrap runs must not duplicate the section.
- Do not overwrite unrelated existing project instructions.
- Keep the snippet short; do not duplicate the skill's workflow.
- Mention `$noootwo-design` explicitly in UI/UX/frontend/app design instructions.
- If Noootwo is introduced mid-project, record adoption baseline in `.noootwo/adoption.md` before broad redesign.

## Good Trigger Language

Use concrete trigger words:

- UI design
- frontend design
- visual redesign
- screenshot review
- app screen
- React, Vue, Flutter, SwiftUI, Compose
- design system
- handoff

Avoid vague language like "make it better" without saying when to call the skill.
