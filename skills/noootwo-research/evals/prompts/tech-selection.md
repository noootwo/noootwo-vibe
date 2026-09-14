# Eval: A library choice

Prompt: "We need virtualised tables for 50k rows in our React admin app. Which library should we use?"

Expected:

- It frames the decision — what would make one library the right answer, and what would rule one out.
- It scores candidates on adoption, maintenance health, size and performance, licence, API fit, migration cost, and exit cost.
- It reads the repository, changelog, and real adopter reports rather than relying on star counts.
- It treats the currently installed option and the boring option as candidates.
- It states the downside of the recommendation and when the choice becomes wrong.
- It records confidence, and the sources with their evidence levels.

Fails when: it recommends from memory; it compares feature lists without constraints; it treats a README benchmark as independent evidence; it hides the migration or exit cost; it picks the newest option without a measurement showing the incumbent fails.
