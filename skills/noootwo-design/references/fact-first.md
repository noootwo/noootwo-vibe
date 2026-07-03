# Fact First

Named products, brands, versions, launches, and recent technologies are facts, not vibes.

## When To Verify

Verify first if any of these are true:

- The task mentions a specific company, product, founder, launch, campaign, or versioned tool
- The task depends on current availability, release status, pricing, or specs
- You feel tempted to say "I think", "probably", or "as far as I remember"

## Workflow

1. Search authoritative sources first: official site, official newsroom, official docs, app stores, vendor changelog
2. Confirm the current state that matters to the design task:
   - existence
   - current version or product generation
   - positioning and announced capabilities
   - canonical naming
3. Write the result into `.noootwo/product-facts.md`
4. If the facts remain ambiguous, ask the user instead of inventing a premise

## Output Shape For `.noootwo/product-facts.md`

- `Status`
- `Project or brand`
- `Verified on`
- `Sources`
- `Current facts`
- `Design implications`
- `Unknowns that still need user input`

## Rules

- Do not start moodboards or prototypes on an unverified named product
- Record dates explicitly when the task depends on "latest" or "new"
- Prefer current official wording over remembered wording
