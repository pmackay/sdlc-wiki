---
type: capability
subtype: skill
belongs_to: "[[pstack]]"
implements: []
delegates_to: []
produces: []
applies: ["[[pattern-contract-first]]"]
equivalent_to: []
sources: "pstack v0.15.2 — Lauren Tan (2026)"
raw: ["../../raw/pstack/2026-09-11-pstack-plugin.md"]
updated: 2026-09-11
---

# principle-boundary-discipline

**Architecture principle.** Concentrate guards at system boundaries; trust internal types and keep business logic in pure functions.

Applies when wiring validation, error handling, or framework adapters. The boundaries named are the CLI, config, the network, and external APIs. Grounded in syntax by [[pstack-typescript-best-practices]], whose boundary-validation rule says `Record<string, unknown>` stops at the parse.

## See Also
- [[pstack-poteto-mode]] — indexes this principle inline and reads the index at task start.
- [[pstack]] — the twenty-three-principle set this belongs to.
