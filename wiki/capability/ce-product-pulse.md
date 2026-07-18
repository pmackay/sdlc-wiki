---
type: capability
subtype: skill
belongs_to: "[[compound-engineering]]"
implements: "[[stage-release]]"
delegates_to: []
produces: []
applies: ["[[pattern-measure-first]]"]
equivalent_to: []
sources: "Compound Engineering — EveryInc/compound-engineering-plugin (2026)"
raw: ["../../raw/compound-engineering/2026-07-04-compound-engineering-every.md", "../../raw/compound-engineering/2026-07-04-compound-engineering-plugin.md"]
updated: 2026-07-04
---

# /ce-product-pulse

`/ce-product-pulse` — "Generate single-page time-windowed report on usage, performance, errors, followups for timeline tracking." A post-release observability/analytics report: for a given time window it consolidates usage, performance, errors, and open follow-ups into a single-page snapshot for timeline tracking.

It implements [[stage-release]] on the **operate/monitor** side — keeping shipped work healthy and visible. It relates to Addy's [[addy-observability]] (which owns logging/metrics/alerting); `ce-product-pulse` is the *reporting* layer over that signal, and its output feeds [[ce-sweep]] and the next [[stage-align]] cycle. It touches the `stage-operate/maintain` watch-item parked on [[stage-release]].

## See Also
- [[addy-observability]] — the metrics/alerting layer this reports over.
- [[ce-sweep]] — consumes product signal to seed the next cycle; [[ce-promote]] — the launch it measures.
- [[stage-release]] — the canonical stage this implements (operate/monitor flavor).
