---
type: capability
subtype: skill
belongs_to: "[[compound-engineering]]"
implements: "[[stage-review]]"
delegates_to: ["[[ce-repo-research-analyst]]"]
produces: []
applies: ["[[pattern-measure-first]]"]
equivalent_to: ["[[addy-performance]]"]
sources: "Compound Engineering — EveryInc/compound-engineering-plugin (2026)"
raw: ["../../raw/compound-engineering/2026-07-04-compound-engineering-every.md", "../../raw/compound-engineering/2026-07-04-compound-engineering-plugin.md"]
updated: 2026-07-05
---

# /ce-optimize

`/ce-optimize` — "Metric-driven iterative optimization with three-tier evaluation and parallel experiments." Optimize against an explicit metric: establish a baseline, run **parallel experiments**, evaluate on three tiers, and iterate — never optimizing without a measurement first ([[pattern-measure-first]]). The parallel-experiments design lets it explore several optimization hypotheses at once and keep the winner.

It implements [[stage-review]] (the quality/performance side) and clusters with Addy's [[addy-performance]].

## Cross-framework equivalents
`ce-optimize` ↔ [[addy-performance]] (`equivalent_to`) — both are measure-first optimization disciplines. `ce-optimize` generalizes beyond web perf to any metric and adds **parallel experiments + three-tier evaluation**; Addy's is Core-Web-Vitals-centric.

## See Also
- [[addy-performance]] — the measure-first counterpart (Core Web Vitals).
- [[pattern-measure-first]] — the shared discipline.
- [[stage-review]] — the canonical stage this implements.
