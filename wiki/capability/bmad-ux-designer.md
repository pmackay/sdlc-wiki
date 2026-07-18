---
type: capability
subtype: sub-agent
belongs_to: "[[bmad]]"
implements: "[[stage-specify]]"
delegates_to: ["[[bmad-ux]]"]
produces: ["[[artifact-design-md]]"]
applies: ["[[pattern-persona-agents]]"]
equivalent_to: []
sources: "bmad-code-org/BMAD-METHOD — bmad-agent-ux-designer (2026)"
raw: ["../../raw/bmad/2026-07-04-bmad-method-framework.md"]
updated: 2026-07-04
---

# bmad-ux-designer

**Sally** 🎨 (`bmad-agent-ux-designer`) — BMAD's **UX persona**: "Turn user needs and the PRD into UX design specifications that inform architecture and implementation." She is "grounded in Don Norman's human-centered design and Alan Cooper's persona discipline" ([[pattern-persona-agents]]).

Sally runs a single Planning workflow, [[bmad-ux]] (CU), which produces a two-spine design spec — `DESIGN.md` (visual identity) + `EXPERIENCE.md` (behavioral logic / information architecture) → [[artifact-design-md]] — that feeds both the architect and the developer.

## See Also
- [[bmad]] — the framework.
- [[bmad-pm]] — supplies the PRD Sally designs against.
- [[addy-frontend-ui]] — Addy's *build*-time UI skill; Sally works upstream, specifying UX before code exists.
- [[stage-specify]] — the canonical stage.
