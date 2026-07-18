---
type: capability
subtype: command
belongs_to: "[[gstack]]"
implements: "[[stage-release]]"
delegates_to: []
produces: []
applies: []
equivalent_to: []
sources: "gstack — Garry Tan (2026)"
raw: ["../../raw/gstack/2026-07-05-gstack-framework.md"]
updated: 2026-07-05
---

# /landing-report

`/landing-report` — a **read-only dashboard** for the workspace-aware [[gstack-ship]] queue. Shows
where each parallel sprint stands in the ship pipeline — the "Review Readiness Dashboard" that tells
you where you stand before you ship, essential when running 10-15 sprints at once.

A reporting capability for [[stage-release]]; the read-only status view over the ship queue, the
release-stage analogue of the [[gstack-health]] quality dashboard.

## See Also
- [[gstack-ship]] — the queue this reports on.
- [[gstack-health]] — the quality-side dashboard sibling.
- [[stage-release]] — the canonical stage this supports.
