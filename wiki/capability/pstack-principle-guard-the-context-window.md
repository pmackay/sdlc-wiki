---
type: capability
subtype: skill
belongs_to: "[[pstack]]"
implements: []
delegates_to: []
produces: []
applies: ["[[pattern-context-engineering]]", "[[pattern-fresh-context-subagents]]"]
equivalent_to: []
sources: "pstack v0.15.2 — Lauren Tan (2026)"
raw: ["../../raw/pstack/2026-09-11-pstack-plugin.md"]
updated: 2026-09-11
---

# principle-guard-the-context-window

**Delegation principle.** Route bulk to subagents; keep summaries in the main thread, not raw payloads.

Applies when context is filling up: large outputs, long files, repeated reads, fan-out planning. Every fan-out skill obeys it structurally — [[pstack-how]] leaves raw exploration in the explorers, [[pstack-recall]] leaves raw transcripts in the miners, and [[pstack-swarm]] forbids pasting raw worker dumps into the report.

## See Also
- [[pstack-poteto-mode]] — indexes this principle inline and reads the index at task start.
- [[pstack]] — the twenty-three-principle set this belongs to.
