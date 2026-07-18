---
type: capability
subtype: command
belongs_to: "[[gstack]]"
implements: "[[stage-plan]]"
delegates_to: []
produces: []
applies: ["[[pattern-persona-agents]]", "[[pattern-parallel-persona-review]]"]
equivalent_to: ["[[ce-doc-review]]"]
sources: "gstack — Garry Tan (2026)"
raw: ["../../raw/gstack/2026-07-05-gstack-framework.md"]
updated: 2026-07-05
---

# /plan-devex-review

`/plan-devex-review` — the **Developer Experience Lead** persona in gstack's plan-review panel.
Interactive DX review: explores developer personas, benchmarks against competitors' **TTHW**
(time-to-hello-world), designs your "magical moment," and traces friction points step by step.
Three modes: **DX EXPANSION, DX POLISH, DX TRIAGE**; 20-45 forcing questions.

The plan-time half of a boomerang with the live [[gstack-devex-review]], which measures TTHW against
the real onboarding flow and compares back to these scores. One of the four `plan-*-review` persona
reviews ([[pattern-persona-agents]]) that [[gstack-autoplan]] chains; clusters with [[ce-doc-review]].

Use it when building **for developers** (API, CLI, SDK, docs); use [[gstack-plan-design-review]]
when building for end users.

## See Also
- [[gstack-devex-review]] — the live-audit boomerang that re-measures TTHW.
- [[gstack-plan-design-review]] — the end-user-facing sibling review.
- [[gstack-autoplan]] — runs this review as part of the panel.
- [[stage-plan]] — the canonical stage this implements.
