---
type: capability
subtype: skill
belongs_to: "[[pstack]]"
implements: []
delegates_to: []
produces: []
applies: []
equivalent_to: []
sources: "pstack v0.15.2 — Lauren Tan (2026)"
raw: ["../../raw/pstack/2026-09-11-pstack-plugin.md"]
updated: 2026-09-11
---

# principle-outcome-oriented-execution

**Core principle.** Converge on the target architecture; do not preserve smooth intermediate states with throwaway compatibility code.

Applies during planned rewrites and migrations with explicit phase boundaries. It is what licenses planned, scoped breakage during [[pstack-architect]] fill-in, and the sibling of [[pstack-principle-migrate-callers-then-delete-legacy-apis]].

## See Also
- [[pstack-poteto-mode]] — indexes this principle inline and reads the index at task start.
- [[pstack]] — the twenty-three-principle set this belongs to.
