---
type: capability
subtype: skill
belongs_to: "[[compound-engineering]]"
implements: "[[stage-learn]]"
delegates_to: []
produces: ["[[artifact-solution-doc]]"]
applies: ["[[pattern-knowledge-compounding]]"]
equivalent_to: []
sources: "Compound Engineering — EveryInc/compound-engineering-plugin (2026)"
raw: ["../../raw/compound-engineering/2026-07-04-compound-engineering-every.md", "../../raw/compound-engineering/2026-07-04-compound-engineering-plugin.md"]
updated: 2026-07-04
---

# /ce-compound-refresh

`/ce-compound-refresh` — "Maintain `docs/solutions/` over time with Keep/Update/Consolidate/ Replace/Delete outcomes." The corpus-gardening counterpart to [[ce-compound]]: it revisits the accumulated [[artifact-solution-doc|solution docs]] and applies a lifecycle verdict to each — **Keep / Update / Consolidate / Replace / Delete** — so the learning corpus stays accurate, de-duplicated, and small enough to remain useful as grounding.

It implements [[stage-learn]]. Its existence is the tell that Compound Engineering treats the learning corpus as a **maintained, first-class artifact** — not a write-only log — which is precisely what distinguishes the agent-grounding flavor of [[stage-learn]] from a one-off retrospective. Without refresh, a growing corpus rots and stops compounding.

## See Also
- [[ce-compound]] — writes the corpus this maintains.
- [[bmad-retrospective]] — the other [[stage-learn]] capability (has no corpus to maintain — the contrast that motivates refresh).
- [[pattern-knowledge-compounding]] — the technique; [[artifact-solution-doc]] — the maintained artifact.
- [[stage-learn]] — the canonical stage this implements.
