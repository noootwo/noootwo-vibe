# Releasing Skills

1. Update the changed skill's `skills/<skill>/VERSION`.
2. Mirror that version in `skills.json`.
3. Update `docs/releases/<skill>.md` with user-visible changes and migration notes.
4. Run workspace validation and skill discovery checks from `README.md`.
5. Commit the change.
6. Create a tag using the skill's `tagPrefix` from `skills.json`, for example `noootwo-review@v0.2.0`.
7. Push the branch and tags.

Do not use the root `VERSION` as a child-skill release source.
