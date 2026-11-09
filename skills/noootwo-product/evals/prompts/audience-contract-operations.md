# Eval: Audience contract for a trained operations surface

Prompt: "Build an internal warehouse dispatch queue for night-shift operators who use 'ASN' and 'pick wave' every day. They need speed and keyboard control."

Expected:

- Records a primary user and moment, daily frequency, high throughput need, and the cost of a wrong dispatch.
- Allows high density, compact rows, keyboard shortcuts, batch actions, and the shared domain terms `ASN` and `pick wave`.
- Keeps service names, database fields, flags, and internal object names out of the operator UI.
- Places rare configuration behind a clear second layer and keeps the queue's primary action obvious.
- States how a first-time operator learns the domain terms without turning the queue into a tutorial.

Fails when: it makes the surface consumer-simple and slow; or treats "expert" as permission to show `order_sync_status`, `FF_PICKWAVE_V2`, `inventory-service`, or unexplained abbreviations.
