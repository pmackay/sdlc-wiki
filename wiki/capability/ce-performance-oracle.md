---
type: capability
subtype: sub-agent
belongs_to: "[[compound-engineering]]"
implements: "[[stage-review]]"
delegates_to: []
produces: ["[[artifact-perf-audit]]"]
applies: ["[[pattern-fresh-context-subagents]]", "[[pattern-measure-first]]"]
equivalent_to: ["[[addy-web-performance-auditor]]"]
sources: "Compound Engineering — EveryInc/compound-engineering-plugin (2026)"
raw: ["../../raw/compound-engineering/2026-07-04-compound-engineering-every.md", "../../raw/compound-engineering/2026-07-04-compound-engineering-plugin.md"]
updated: 2026-07-05
---

# ce-performance-oracle

The **Performance Oracle** — a performance-optimization expert covering algorithmic complexity, database optimization, memory management, caching, and scalability. Its mission is to identify bottlenecks before they hit production → [[artifact-perf-audit]].

It implements [[stage-review]] (performance quality gate) and is a **direct** counterpart to Addy's [[addy-web-performance-auditor]] (and clusters with the [[ce-optimize]] ↔ [[addy-performance]] pair, [[pattern-measure-first]]). Like [[ce-security-sentinel]], it is also a [[ce-compound]] council member: on a durable-learning invocation it converts perf analysis into lesson validation (bottleneck class, proving measurements, scaling assumptions) for [[artifact-solution-doc]].

## Cross-framework equivalents
`ce-performance-oracle` ↔ [[addy-web-performance-auditor]] (`equivalent_to`) — both are measure-first performance auditors producing a perf scorecard.

## See Also
- [[addy-web-performance-auditor]] — the direct counterpart persona.
- [[ce-optimize]] — the metric-driven optimization skill; [[ce-compound]] — dispatches this agent to mine perf lessons.
- [[stage-review]] — the canonical stage this supports; [[stage-learn]] — its compound-council role.
