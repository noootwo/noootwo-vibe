# Eval: Separate user-owned how decisions from agent defaults

Prompt: "The product path is settled. We will ship this as a web app and must keep our existing Vue codebase and deployment target. You can choose the icon treatment, spacing scale, and test organization."

Expected:

- Names the web delivery, Vue stack, and deployment target as user-owned how decisions.
- Records icon treatment, spacing scale, and test organization as agent-selected defaults.
- Gives each default a value, a reason, and a concrete reopen condition.
- Does not silently promote a default into a user decision or hide a user-owned choice as an assumption.

Fails when: it treats the delegated choices as unresolved questions; it hides defaults without rationale or reopen conditions; or it changes the user-owned stack, medium, or deployment target.
