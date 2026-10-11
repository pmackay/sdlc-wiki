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

# principle-minimize-reader-load

**Core principle.** Count layers between question and answer, and hidden state in the reader's head; collapse one-caller wrappers and shrink mutable scope.

Applies when reviewing or shaping code that is hard to trace. The clearest pstack expression of [[pattern-deep-modules]] — it names the two costs (indirection depth, hidden state) as things to literally count.

## See Also
- [[pstack-poteto-mode]] — indexes this principle inline and reads the index at task start.
- [[pstack]] — the twenty-three-principle set this belongs to.
