---
type: capability
subtype: sub-agent
belongs_to: "[[gsd]]"
implements: "[[stage-plan]]"
delegates_to: []
produces: "[[artifact-research-md]]"
applies: ["[[pattern-fresh-context-subagents]]"]
equivalent_to: ["[[mp-research]]"]
sources: "Open GSD docs — agents (2026)"
raw: ["../../raw/gsd/2026-06-27-gsd-core-framework.md"]
updated: 2026-07-09
---

# gsd-phase-researcher

Specialist sub-agent invoked by [[gsd-plan-phase]] for domain research before planning.
Runs as **four parallel instances**, each covering one axis — stack, features,
architecture, pitfalls — in a fresh context window of up to ~200K tokens
([[pattern-fresh-context-subagents]]).

**Produces:** [[artifact-research-md]] (`RESEARCH.md`).

## See Also
- [[gsd-planner]] — consumes the research to build the plan.
- [[gsd-plan-phase]] — orchestrates this sub-agent.
