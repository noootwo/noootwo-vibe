# Skills Manifest Reference

`skills.json` is the source of truth for the ten public skills.

Fields:

- `repository`: GitHub owner/repo.
- `skillsRoot`: directory containing child skills.
- `releaseModel`: expected to be `independent-child-skills`.
- `skills[].name`: skill name and folder name.
- `skills[].path`: path to the skill folder.
- `skills[].version`: version mirrored from `skills/<skill>/VERSION`.
- `skills[].status`: currently `public` for published skills.
- `skills[].dependencies`: sibling skills this skill may need; the runtime installs a missing one and falls back with a `skill-missing` marker if install fails.
- `skills[].tagPrefix`: prefix used for release tags.

The workspace validator checks that the manifest matches the filesystem.

The expected public skill order is `noootwo-ask`, `noootwo-workflow`, `noootwo-product`, `noootwo-design`, `noootwo-tdd`, `noootwo-code-health`, `noootwo-state`, `noootwo-debug`, `noootwo-research`, `noootwo-onboard`. The order is load-bearing: the validator compares the manifest against it. Do not add `noootwo-architecture` or a separate performance skill; architecture, technical judgment, tests, and performance remain `noootwo-code-health` lenses.

The capability map in [the invocation model](../agents/invocation.md) records which skill owns which capability, and the validator checks that every public skill appears there.

`noootwo-ask` is the only user-invoked skill; see [the invocation model](../agents/invocation.md).
