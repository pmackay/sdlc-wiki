---
type: capability
subtype: skill
belongs_to: "[[bmad]]"
implements: "[[stage-align]]"
delegates_to: []
produces: ["[[artifact-research-md]]"]
applies: ["[[pattern-persona-agents]]"]
equivalent_to: []
sources: "bmad-code-org/BMAD-METHOD — bmad-market/domain/technical-research (2026)"
raw: ["../../raw/bmad/2026-07-04-bmad-method-framework.md"]
updated: 2026-07-04
---

# bmad-research

BMAD's Analysis-phase research capability — three sibling skills dispatched by [[bmad-analyst]], one page here since they share a workflow shape and all emit [[artifact-research-md]]:

- `bmad-market-research` (MR) — competition, customers, market sizing.
- `bmad-domain-research` (DR) — industry / domain deep dive.
- `bmad-technical-research` (TR) — technology and architecture feasibility.

Research grounds the align stage in evidence before a brief or PRD is written; its output "is input" to the [[bmad-product-brief]] and [[bmad-prd]] workflows.

## See Also
- [[bmad]] — the framework.
- [[gsd-phase-researcher]] — GSD's research agent, which runs *inside planning* (parallel domain research → [[artifact-research-md]]) rather than up front in align.
- [[addy-source-driven-development]] — grounding decisions in cited sources.
- [[stage-align]] — the canonical stage.
