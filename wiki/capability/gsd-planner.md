---
type: capability
subtype: sub-agent
belongs_to: "[[gsd]]"
implements: "[[stage-plan]]"
delegates_to: []
produces: "[[artifact-plan-md]]"
applies: ["[[pattern-fresh-context-subagents]]", "[[pattern-spec-driven-development]]"]
equivalent_to: []
sources: "Open GSD docs — agents (2026)"
raw: ["../../raw/gsd/2026-06-27-gsd-core-framework.md"]
updated: 2026-06-27
---

# gsd-planner

Specialist sub-agent invoked by [[gsd-plan-phase]] that "creates atomic execution plans with task definitions and acceptance criteria." Runs on an Opus-tier model in a fresh context, reading planning artifacts only.

**Produces:** [[artifact-plan-md]] (`{phase}-PLAN.md`, executable task prompts), which then passes through [[gsd-plan-checker]] before execution.

## See Also
- [[gsd-phase-researcher]] — supplies research inputs.
- [[gsd-plan-checker]] — verifies the plan this produces.
