---
type: capability
subtype: command
belongs_to: "[[gstack]]"
implements: "[[stage-review]]"
delegates_to: []
produces: []
applies: ["[[pattern-deterministic-gates]]"]
equivalent_to: []
sources: "gstack — Garry Tan (2026)"
raw: ["../../raw/gstack/2026-07-05-gstack-framework.md"]
updated: 2026-08-31
---

# /health

`/health` — a **code-quality dashboard**. Aggregates the type checker, linter, tests, and dead-code detection into one at-a-glance view of the codebase's health.

A read-only quality-signal capability in the **Review** side of [[stage-review]] — the standing scoreboard that complements the deeper, action-oriented reviews ([[gstack-review]], [[gstack-cso]], [[gstack-benchmark]]). No cross-framework counterpart is paged; it is a lighter, always-on health readout rather than a review that fixes.

## See Also
- [[gstack-review]] · [[gstack-cso]] · [[gstack-benchmark]] — the deeper validators it summarizes alongside.
- [[pattern-deterministic-gates]] — the technique: a verdict computed by a program, not judged by a model.
- [[stage-review]] — the canonical stage this implements.
