---
type: capability
subtype: sub-agent
belongs_to: "[[compound-engineering]]"
implements: "[[stage-learn]]"
delegates_to: []
produces: ["[[artifact-solution-doc]]"]
applies: ["[[pattern-fresh-context-subagents]]", "[[pattern-source-grounding]]", "[[pattern-knowledge-compounding]]"]
equivalent_to: []
sources: "Compound Engineering — EveryInc/compound-engineering-plugin (2026)"
raw: ["../../raw/compound-engineering/2026-07-04-compound-engineering-every.md", "../../raw/compound-engineering/2026-07-04-compound-engineering-plugin.md"]
updated: 2026-07-05
---

# ce-best-practices-researcher

An expert **technology researcher** that discovers, analyzes, and synthesizes best practices
from authoritative sources — checking curated skills *before* going online. On a
durable-learning invocation it converts best-practice research into **documentation
enrichment**: prevention guidance, authoritative citations, better terminology, clearer
tradeoffs, and corrections to any overbroad lesson — prioritizing what makes a documented
solution more reusable and less misleading.

Dispatched by [[ce-compound]] as a learning-council member, it implements [[stage-learn]]:
it strengthens the [[artifact-solution-doc|solution docs]] with external authority
([[pattern-source-grounding]] + [[pattern-knowledge-compounding]]). It pairs with
[[ce-framework-docs-researcher]] (version-specific framework docs) and is the compound-time
cousin of Addy's [[addy-source-driven-development]] discipline.

## See Also
- [[ce-compound]] — the dispatcher; [[ce-framework-docs-researcher]] — the framework-docs sibling.
- [[addy-source-driven-development]] — the cite-authoritative-docs relative.
- [[pattern-knowledge-compounding]] — the technique; [[stage-learn]] — the canonical stage this supports.
