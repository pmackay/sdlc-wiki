---
type: capability
subtype: sub-agent
belongs_to: "[[gsd]]"
implements: "[[stage-plan]]"
delegates_to: []
produces: []
applies: ["[[pattern-plan-verification-loop]]"]
equivalent_to: ["[[speckit-analyze]]", "[[bmad-check-implementation-readiness]]", "[[ce-doc-review]]"]
sources: "Open GSD docs — agents (2026)"
raw: ["../../raw/gsd/2026-06-27-gsd-core-framework.md"]
updated: 2026-07-04
---

# gsd-plan-checker

Specialist sub-agent invoked by [[gsd-plan-phase]] that "verifies plans across eight dimensions before execution is permitted." Runs sequentially after [[gsd-planner]], driving up to three revision cycles — the [[pattern-plan-verification-loop]] — until the plan is approved. It is the gate between planning and execution.

Its cross-framework counterparts are Spec Kit's [[speckit-analyze]] and BMAD's [[bmad-check-implementation-readiness]] — together promoting [[pattern-plan-verification-loop]] to a **three-framework** pattern. The gates check different things: this checker scores a single plan on eight quality dimensions, `analyze` checks consistency and coverage *across* spec ↔ plan ↔ tasks plus constitutional compliance, and BMAD's readiness check verifies *completeness across the whole planning set* (PRD + UX + architecture + epics), returning PASS / CONCERNS / FAIL.

## See Also
- [[gsd-planner]] — produces the plan this checks.
- [[gsd-execute-phase]] — runs only after approval.
- [[speckit-analyze]] — Spec Kit's cross-artifact plan-verification gate.
- [[bmad-check-implementation-readiness]] — BMAD's cross-document readiness gate.
