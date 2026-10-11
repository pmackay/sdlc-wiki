---
type: capability
subtype: skill
belongs_to: "[[pstack]]"
implements: []
delegates_to: []
produces: []
applies: ["[[pattern-systematic-debugging]]"]
equivalent_to: []
sources: "pstack v0.15.2 — Lauren Tan (2026)"
raw: ["../../raw/pstack/2026-09-11-pstack-plugin.md"]
updated: 2026-09-11
---

# principle-attack-the-premise

**Core principle.** Question the shared premise instead of writing another fix that assumes it.

Applies when two or more fixes sharing one premise have failed the same gate. Distinctive instruction: take a census of which actors hold the imbalance before the next fix. This is the escalation rung above [[pstack-principle-fix-root-causes]], and the counterpart of the stop-after-three-fixes rule in [[gstack-investigate]] and [[sp-systematic-debugging]] — but framed as a move to make rather than a stop to take.

## See Also
- [[pstack-poteto-mode]] — indexes this principle inline and reads the index at task start.
- [[pstack]] — the twenty-three-principle set this belongs to.
