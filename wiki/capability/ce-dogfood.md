---
type: capability
subtype: skill
belongs_to: "[[compound-engineering]]"
implements: "[[stage-validate]]"
delegates_to: []
produces: []
applies: ["[[pattern-autonomous-loop]]"]
equivalent_to: ["[[addy-browser-testing]]"]
sources: "Compound Engineering — EveryInc/compound-engineering-plugin (2026)"
raw: ["../../raw/compound-engineering/2026-07-04-compound-engineering-every.md", "../../raw/compound-engineering/2026-07-04-compound-engineering-plugin.md"]
updated: 2026-07-04
---

# /ce-dogfood

`/ce-dogfood` — "Hands-off diff-scoped browser QA with autonomous small-breakage fixes and durable reporting." The autonomous cousin of [[ce-test-browser]]: it QAs the PR-affected surface end-to-end **without supervision**, *fixes small breakages on its own* ([[pattern-autonomous-loop]]), and writes a durable report of what it exercised and repaired.

It implements [[stage-validate]] and clusters with [[addy-browser-testing]] on live-runtime QA, but its signature is **autonomy + self-repair** — the same hands-off philosophy that [[lfg]] applies to the whole loop, scoped here to QA.

## Cross-framework equivalents
`ce-dogfood` ↔ [[addy-browser-testing]] (`equivalent_to`) on the live-browser-QA axis; unique in being **autonomous and self-fixing**.

## See Also
- [[ce-test-browser]] — the supervised sibling; [[lfg]] — the same autonomy applied loop-wide.
- [[addy-browser-testing]] — live-runtime-QA counterpart.
- [[stage-validate]] — the canonical stage this implements.
