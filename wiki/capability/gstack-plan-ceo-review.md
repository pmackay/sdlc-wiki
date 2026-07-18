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

# /plan-ceo-review

`/plan-ceo-review` — the **CEO / founder** persona in gstack's plan-review panel. Rethinks the problem and "finds the 10-star product hiding inside the request," then edits the plan toward it. Four scope modes: **Expansion, Selective Expansion, Hold Scope, Reduction**. Runs in plan mode, one taste decision at a time.

One of the four `plan-*-review` persona reviews ([[pattern-persona-agents]]) that [[gstack-autoplan]] chains. It is the scope/product lens; its plan-review sibling capabilities are [[gstack-plan-eng-review]] (architecture), [[gstack-plan-design-review]] (design), and [[gstack-plan-devex-review]] (developer experience). As a persona fan-out over the plan *before* code, the cluster's cross-framework counterpart is Compound Engineering's [[ce-doc-review]]; BMAD's [[bmad-check-implementation-readiness]] is the readiness-gate cousin.

## See Also
- [[gstack-autoplan]] — runs this review (plus design/eng/DX) automatically.
- [[gstack-office-hours]] — writes the doc this review reads.
- [[ce-doc-review]] — the persona-lens plan-review counterpart.
- [[stage-plan]] — the canonical stage this implements.
