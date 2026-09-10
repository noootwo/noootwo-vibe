# Skills Manifest Reference

`skills.json` is the source of truth for the six public skills.

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

The expected public skill order is `noootwo-ask`, `noootwo-workflow`, `noootwo-product`, `noootwo-design`, `noootwo-review`, `noootwo-docs`. The order is load-bearing: the validator compares the manifest against it. Do not add `noootwo-architecture`; architecture remains a `noootwo-review` lens.

`noootwo-ask` is the only user-invoked skill; see [the invocation model](../agents/invocation.md).
