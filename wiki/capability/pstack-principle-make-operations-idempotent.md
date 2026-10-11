---
type: capability
subtype: skill
belongs_to: "[[pstack]]"
implements: []
delegates_to: []
produces: []
applies: ["[[pattern-idempotent-operations]]"]
equivalent_to: []
sources: "pstack v0.15.2 — Lauren Tan (2026)"
raw: ["../../raw/pstack/2026-09-11-pstack-plugin.md"]
updated: 2026-09-11
---

# principle-make-operations-idempotent

**Architecture principle.** Converge to the same end state regardless of partial prior runs.

Applies when designing commands, lifecycle steps, or processing loops that run amid crashes, restarts, and retries. This is the principle that makes long autonomous runs survivable, and the wiki's first framework-level statement of [[pattern-idempotent-operations]] — [[pstack-setup-pstack]] applies it literally by overwriting its whole rule file so re-runs stay idempotent.

## See Also
- [[pstack-poteto-mode]] — indexes this principle inline and reads the index at task start.
- [[pstack]] — the twenty-three-principle set this belongs to.
