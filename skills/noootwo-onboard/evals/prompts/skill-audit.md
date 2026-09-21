# Eval: Audit which skills a project needs

Prompt: "This is a small script repo with no tests and no CI. Which of your skills should I actually use?"

Expected:

- The audit is driven by project facts: no tests and no CI changes which skills are required and which are not needed now.
- It says plainly which skills are not needed yet, with the reason, instead of recommending the whole set.
- It names a trigger for each recommended skill.
- Foundation gaps go to `noootwo-review`'s project-health lens, with the smallest fix named.
- It routes any resulting content placement to `noootwo-state`.

Fails when: it recommends every skill; it treats a missing test suite as a reason to write one immediately without the user's decision; it invents project facts; it loads many skill bodies before reading the repository.
