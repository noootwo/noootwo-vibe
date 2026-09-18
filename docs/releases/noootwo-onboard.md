# noootwo-onboard Releases

## v0.1.1

- Made the trigger clearer for unfamiliar repositories and agent takeovers, and kept the "do not load every skill" boundary.

## v0.1.0

- Initial public skill: enter an unfamiliar repository, or decide which skills a project needs.
- Carries the skill decision table moved out of `noootwo-workflow`, extended to the full skill set including debug, research, and onboarding itself.
- Owns the minimal foundation templates, updated to the nine-skill routing block.
- The foundation health judgment is delegated to `noootwo-review`'s project-health lens, removing the duplicated audit surface that previously lived in both skills.
- Produces a routing map and a gap list, never a scaffold: one missing file that unblocks the current work.
- The templates and audit signals assume a software repository, with a stated rule for other kinds of project: keep the responsibility, let the file name follow the project.
