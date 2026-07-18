---
type: capability
subtype: command
belongs_to: "[[gstack]]"
implements: "[[stage-plan]]"
delegates_to: ["[[gstack-plan-ceo-review]]", "[[gstack-plan-design-review]]", "[[gstack-plan-eng-review]]", "[[gstack-plan-devex-review]]"]
produces: []
applies: ["[[pattern-parallel-persona-review]]", "[[pattern-scale-adaptive-planning]]"]
equivalent_to: []
sources: "gstack — Garry Tan (2026)"
raw: ["../../raw/gstack/2026-07-05-gstack-framework.md"]
updated: 2026-07-05
---

# /autoplan

`/autoplan` — the **auto-review pipeline**. One command runs the full plan-review panel — **CEO → design → eng → DX** — sequentially, reading each full review skill from disk and applying **auto-decisions via six decision principles**, so only genuine *taste* decisions surface for the user's approval. Auto-detects which reviews apply to the change (smart review routing: "CEO skips infra, design skips backend").

The orchestrator over gstack's four persona plan reviews ([[pattern-parallel-persona-review]]), sized to the work ([[pattern-scale-adaptive-planning]]). It is the practical single entry to the Plan stage; its delegates are [[gstack-plan-ceo-review]], [[gstack-plan-design-review]], [[gstack-plan-eng-review]], and [[gstack-plan-devex-review]].

## See Also
- [[gstack-plan-ceo-review]] · [[gstack-plan-design-review]] · [[gstack-plan-eng-review]] · [[gstack-plan-devex-review]] — the reviews it chains.
- [[gstack-office-hours]] — the align step that precedes it.
- [[lfg]] — Compound Engineering's autonomous full-pipeline analogue (broader scope).
- [[stage-plan]] — the canonical stage this implements.
