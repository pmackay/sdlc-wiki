---
type: capability
subtype: command
belongs_to: "[[gstack]]"
implements: "[[stage-review]]"
delegates_to: []
produces: "[[artifact-perf-audit]]"
applies: ["[[pattern-measure-first]]"]
equivalent_to: ["[[addy-performance]]", "[[addy-web-performance-auditor]]", "[[ce-optimize]]", "[[ce-performance-oracle]]"]
sources: "gstack — Garry Tan (2026)"
raw: ["../../raw/gstack/2026-07-05-gstack-framework.md"]
updated: 2026-07-05
---

# /benchmark

`/benchmark` — the **Performance Engineer**. Baselines page-load times, **Core Web Vitals**, and
resource sizes via the browse daemon, then compares before/after on every PR to catch **performance
regressions** ([[artifact-perf-audit]]).

gstack's member of the cross-framework **performance** cluster ([[pattern-measure-first]]) —
alongside Addy's [[addy-performance]] / [[addy-web-performance-auditor]] and Compound Engineering's
[[ce-optimize]] / [[ce-performance-oracle]]. Distinctive: it is regression-oriented (before/after
per PR against a stored baseline) rather than one-shot optimization. The gstack-native
`gstack-model-benchmark` CLI is a *different* thing — a cross-model benchmark of gstack's own skills
([[gstack-benchmark-models]]).

## See Also
- [[addy-web-performance-auditor]] · [[ce-optimize]] · [[ce-performance-oracle]] — performance-cluster counterparts.
- [[gstack-benchmark-models]] — the unrelated cross-model skill benchmark (meta).
- [[stage-review]] — the canonical stage this implements.
