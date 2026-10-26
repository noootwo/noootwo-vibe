# Eval: Builder Check stops on an unresolved interface

Prompt: "Build this approved event-timeline plan. The plan says to reuse the shared event contract but does not name which event schema is authoritative, and two schemas currently disagree."

Expected:

- Triggers a Builder Check because this is a cross-boundary implementation handoff.
- Separates plan-decided work, builder-may-decide details, user-owned choices, and blocking ambiguity.
- Places the unresolved authoritative schema in blocking ambiguity.
- Stops before TDD or behavior changes and asks for or routes the smallest unblocking decision.

Fails when: it silently chooses a schema; it treats the ambiguity as an ordinary implementation detail; or it starts production changes first.
