---
type: capability
subtype: sub-agent
belongs_to: "[[bmad]]"
implements: "[[stage-plan]]"
delegates_to: ["[[bmad-architecture]]", "[[bmad-check-implementation-readiness]]"]
produces: ["[[artifact-architecture]]"]
applies: ["[[pattern-persona-agents]]", "[[pattern-spec-driven-development]]"]
equivalent_to: []
sources: "bmad-code-org/BMAD-METHOD — bmad-agent-architect (2026)"
raw: ["../../raw/bmad/2026-07-04-bmad-method-framework.md"]
updated: 2026-07-04
---

# bmad-architect

**Winston** 🏗️ (`bmad-agent-architect`) — BMAD's **Solutioning persona**: "Convert the PRD and UX into technical architecture decisions that keep implementation on track." He "channels Martin Fowler's pragmatism and Werner Vogels's cloud-scale realism," favouring "boring technology for stability" ([[pattern-persona-agents]]).

Winston owns BMAD's *how*, dispatching [[bmad-architecture]] (CA) to produce the [[artifact-architecture|architecture spine]] and [[bmad-check-implementation-readiness]] (IR) to gate the plan before code. His spine deliberately fixes **only invariants**, deferring concrete structure to the code — BMAD's [[pattern-scale-adaptive-planning|just-in-time]] take on design.

## See Also
- [[bmad]] — the framework.
- [[bmad-pm]] — supplies the PRD + epics Winston designs around.
- [[mp-codebase-design]], [[addy-api-design]] — the cross-framework design cluster (deep modules / contracts).
- [[stage-plan]] — the canonical stage.
