---
type: capability
subtype: command
belongs_to: "[[speckit]]"
implements: "[[stage-plan]]"
produces: ["[[artifact-design-md]]", "[[artifact-research-md]]"]
applies: ["[[pattern-contract-first]]", "[[pattern-spec-driven-development]]"]
equivalent_to: ["[[gsd-plan-phase]]", "[[ce-plan]]"]
sources: "GitHub/spec-kit README + spec-driven.md (2026)"
raw: ["../../raw/speckit/2026-07-04-speckit-framework.md"]
updated: 2026-07-04
---

# speckit-plan

**`/speckit.plan`** — "Create technical implementation plans with your chosen tech stack." Generates the technical planning from the finalized spec: it analyzes requirements and acceptance criteria, validates alignment with the [[artifact-constitution]] through **phase gates**, converts business requirements into technical architecture, and derives technology choices with documented rationale.

It produces a cluster of "how" artifacts (rolled up here as [[artifact-design-md]] plus [[artifact-research-md]]):

- `plan.md` — high-level implementation strategy with a phase breakdown.
- `data-model.md` — entity definitions and schema design.
- `contracts/` — API specifications (REST endpoints, WebSocket events) — authored *before* implementation, which is why this command [[pattern-contract-first|applies contract-first design]].
- `research.md` — technology investigation and comparative analysis.
- `quickstart.md` — key validation scenarios for acceptance testing.

Constitutional enforcement is explicit: "Phase -1" gates enforce simplicity (≤3 projects), anti-abstraction (framework-direct usage), and integration-first testing.

## Cross-framework cluster (plan)

Clusters with [[gsd-plan-phase]] — both research, then produce a design/plan validated by a gate before execution. In Spec Kit the decomposition into a task list is split into a separate command, [[speckit-tasks]], and the gate into [[speckit-analyze]].

## See Also
- [[speckit]] — the framework.
- [[speckit-tasks]] — turns this plan into the executable task list.
- [[speckit-analyze]] — gates these artifacts for consistency before implementation.
- [[stage-plan]] — the canonical stage.
