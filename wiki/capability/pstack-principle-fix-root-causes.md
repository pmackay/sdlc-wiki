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

# principle-fix-root-causes

**Verification principle.** Trace each symptom to its root cause and fix it there.

Applies when debugging: reproduce first, ask why until you reach it, resist nil-check guards that silence crashes. pstack's member of the debugging cluster with [[gstack-investigate]], [[sp-systematic-debugging]], [[mp-diagnosing-bugs]], [[addy-debugging]], and [[ce-debug]]. [[pstack-no-comments]] cites it as intent-only authority — it guides the fix but never licenses widening the fence.

## See Also
- [[pstack-poteto-mode]] — indexes this principle inline and reads the index at task start.
- [[pstack]] — the twenty-three-principle set this belongs to.
