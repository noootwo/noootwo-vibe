# Eval: Technical evidence for a technical buyer

Prompt: "Create a security review page for enterprise buyers evaluating our API. They need architecture, data residency, authentication, and incident history."

Expected:

- Names the buyer, the evaluation moment, and the decision the page must support.
- Leads with the outcome and scope of the service, then presents architecture, data residency, authentication, and incident evidence in a scannable second layer.
- Keeps the technical terms because they are the buyer's domain, and defines any product-specific term the buyer may not share.
- Does not delete evidence the buyer needs in order to approve the service.
- Keeps implementation detail that has no decision role out of the first screen.

Fails when: it opens with an architecture dump before stating what the service does; hides data residency or authentication behind generic marketing copy; or treats "enterprise" as permission for unexplained internal names.
