---
type: capability
subtype: sub-agent
belongs_to: "[[bmad]]"
implements: "[[stage-specify]]"
delegates_to: ["[[bmad-prd]]", "[[bmad-create-epics-and-stories]]", "[[bmad-check-implementation-readiness]]", "[[bmad-correct-course]]"]
produces: ["[[artifact-prd]]"]
applies: ["[[pattern-persona-agents]]", "[[pattern-grilling]]", "[[pattern-spec-driven-development]]"]
equivalent_to: []
sources: "bmad-code-org/BMAD-METHOD — bmad-agent-pm (2026)"
raw: ["../../raw/bmad/2026-07-04-bmad-method-framework.md"]
updated: 2026-07-04
---

# bmad-pm

**John** 📋 (`bmad-agent-pm`) — BMAD's **Planning persona**: "Translate product vision into a
validated PRD, epics, and stories that development can execute." He "thinks like Marty Cagan
and Teresa Torres" and "writes with Bezos's six-pager discipline" ([[pattern-persona-agents]]).

John owns the spec-authoring spine of the method, dispatching:

- [[bmad-prd]] (PRD) — create / update / validate the requirements document.
- [[bmad-create-epics-and-stories]] (CE) — decompose requirements into epics and stories.
- [[bmad-check-implementation-readiness]] (IR) — the pre-build readiness gate.
- [[bmad-correct-course]] (CC) — mid-sprint change management.

He is a **facilitator** — coaching the human to decisions, "NEVER generat[ing] content without
user input" ([[pattern-grilling]]) — and his PRD drives everything downstream ([[pattern-spec-driven-development]]).

## See Also
- [[bmad]] — the framework.
- [[bmad-analyst]] — supplies the brief/research John turns into a PRD.
- [[bmad-architect]] — consumes the PRD to produce the architecture.
- [[stage-specify]] — the canonical stage.
