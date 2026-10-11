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

# principle-model-the-domain

**Architecture principle.** Encode the domain in a structure instead of scattered conditionals.

Applies when writing stateful logic, or when code branches a lot or repeats a shape assumption across files. The structure may be a state machine, a typed model, a table or registry, a reducer, a boundary, or simply the right collection. [[pstack-poteto-mode]] promotes this to a standing trigger: any code at all means naming the data shape first.

## See Also
- [[pstack-poteto-mode]] — indexes this principle inline and reads the index at task start.
- [[pstack]] — the twenty-three-principle set this belongs to.
