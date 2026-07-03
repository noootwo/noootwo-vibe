# Skills Manifest Reference

`skills.json` is the source of truth for public skills.

Fields:

- `repository`: GitHub owner/repo.
- `skillsRoot`: directory containing child skills.
- `releaseModel`: expected to be `independent-child-skills`.
- `skills[].name`: skill name and folder name.
- `skills[].path`: path to the skill folder.
- `skills[].version`: version mirrored from `skills/<skill>/VERSION`.
- `skills[].status`: currently `public` for published skills.
- `skills[].tagPrefix`: prefix used for release tags.

The workspace validator checks that the manifest matches the filesystem.
