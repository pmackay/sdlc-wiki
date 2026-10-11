---
type: pattern
sources: "Addy Osmani — Agent Skills (2026); Tessl docs (2026)"
updated: 2026-09-12
---

# Pattern: Measure first (profile before optimizing)

Never optimize on a hunch. Take a measurement — a profile, a bundle analysis, a Core Web Vitals reading — locate the actual bottleneck, then fix that and re-measure to confirm the win. Findings without measurement are labeled **potential impact**, never presented as fact (the metric-honesty rule). Prevents speculative complexity that trades readability for imaginary performance.

## Applied by (backlinks)

Addy Osmani — Agent Skills:

- [[addy-performance]] — Core Web Vitals targets, profiling workflows, bundle analysis.
- [[addy-web-performance-auditor]] — Quick mode ("potential impact") vs Deep mode (measured, from Lighthouse/PSI/CrUX/trace data).

Compound Engineering:

- [[ce-optimize]] — baseline → parallel experiments → three-tier evaluation; never optimize without a metric.
- [[ce-performance-oracle]] — bottleneck analysis backed by measurements; [[ce-repo-research-analyst]] — finds the metrics/benchmark surfaces first.

gstack:

- [[gstack-benchmark]] — baseline Core Web Vitals / load, then compare before/after on every PR.

Tessl:

- [[tessl-observability]] — measures where skills **activate** across real agent sessions, not where they are installed. The first capability here that measures agent behavior in production rather than in a test, and the distinction matters: a skill deployed everywhere and firing nowhere looks identical to a working one from any install-side view.

## See Also
- [[artifact-perf-audit]] — the measured scorecard this pattern produces.
- [[stage-review]] — the stage where performance is assessed.
