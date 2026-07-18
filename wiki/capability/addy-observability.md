---
type: capability
subtype: skill
belongs_to: "[[addy-agent-skills]]"
implements: "[[stage-release]]"
delegates_to: []
produces: []
applies: []
equivalent_to: []
sources: "Addy Osmani — Agent Skills (2026)"
raw: ["../../raw/addy-agent-skills/2026-07-04-agent-skills.md"]
updated: 2026-07-04
---

# Observability & Instrumentation

Instruments code so production behavior is visible and diagnosable — telemetry written alongside the feature, the same way tests are, so the first user-reported bug is a query and not archaeology. Its distinctive discipline is question-first: before adding any signal, write the 2-4 questions an on-call engineer will ask, then map each signal to one. It picks the right signal per question — metrics say *that* something is wrong, traces say *where*, logs say *why*.

Concretely it prescribes structured logging with stable event names and mandatory correlation IDs (never secrets or PII), **RED** metrics on every endpoint and dependency with bounded label sets (cardinality is the failure mode), OpenTelemetry distributed tracing, and symptom-based alerting on what users feel rather than on causes like CPU. Observability is a new domain for this wiki; it feeds the launch-day monitoring that [[addy-shipping]] depends on.

## See Also
- [[addy-shipping]] — the launch skill whose monitoring this instrumentation feeds.
- [[stage-release]] — the canonical stage this implements.
