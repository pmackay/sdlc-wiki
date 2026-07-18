---
type: capability
subtype: skill
belongs_to: "[[addy-agent-skills]]"
implements: "[[stage-review]]"
delegates_to: ["[[addy-web-performance-auditor]]"]
produces: ["[[artifact-perf-audit]]"]
applies: ["[[pattern-measure-first]]"]
equivalent_to: ["[[ce-optimize]]"]
sources: "Addy Osmani — Agent Skills (2026)"
raw: ["../../raw/addy-agent-skills/2026-07-04-agent-skills.md"]
updated: 2026-07-05
---

# Performance Optimization

Measure before optimizing — performance work without measurement is guessing that adds complexity without improving what matters. Its workflow is **measure → identify → fix → verify → guard**: establish a baseline with both synthetic (Lighthouse, DevTools) and real-user (RUM, CrUX) data, find the actual bottleneck, fix that one thing, then measure again against Core Web Vitals targets (LCP ≤ 2.5s, INP ≤ 200ms, CLS ≤ 0.1).

A symptom-to-measurement decision tree routes each complaint to the right profiler, and the skill catalogs concrete anti-patterns with fixes: N+1 queries, unbounded fetching, unoptimized images, unnecessary React re-renders, oversized bundles, missing caching. Enforceable performance budgets close the loop in CI. It applies [[pattern-measure-first]], emits an [[artifact-perf-audit]], and can delegate to the [[addy-web-performance-auditor]] persona.

## See Also
- [[addy-web-performance-auditor]] — the persona this delegates auditing to.
- [[pattern-measure-first]] — the discipline it embodies.
- [[artifact-perf-audit]] — the audit it produces.
- [[stage-review]] — the canonical stage this implements.
