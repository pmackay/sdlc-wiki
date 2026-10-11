---
type: capability
subtype: skill
belongs_to: "[[pstack]]"
implements: []
delegates_to: []
produces: []
applies: ["[[pattern-deep-modules]]"]
equivalent_to: []
sources: "pstack v0.15.2 — Lauren Tan (2026)"
raw: ["../../raw/pstack/2026-09-11-pstack-plugin.md"]
updated: 2026-09-11
---

# principle-laziness-protocol

**Core principle.** Bias toward deletion and the smallest change that solves the problem.

Applies when refactoring, sizing a diff, or tempted to add abstractions, layers, or signal threading. The negative space of most agent frameworks: where others optimize for throughput, pstack treats a smaller diff as the win condition. [[pstack-arena]] cites it as the tie-breaker when two candidates score level — prefer the cleaner boundary or smaller API.

## See Also
- [[pstack-poteto-mode]] — indexes this principle inline and reads the index at task start.
- [[pstack]] — the twenty-three-principle set this belongs to.
