---
type: capability
subtype: skill
belongs_to: "[[bmad]]"
implements: "[[stage-plan]]"
delegates_to: []
produces: []
applies: []
equivalent_to: []
sources: "bmad-code-org/BMAD-METHOD — bmad-correct-course (2026)"
raw: ["../../raw/bmad/2026-07-04-bmad-method-framework.md"]
updated: 2026-07-04
---

# bmad-correct-course

**`bmad-correct-course`** — "Manage significant changes during sprint execution." Owned by
[[bmad-pm]] (John), it is BMAD's mid-flight re-planning valve: when a discovery or scope change
lands during implementation, it re-routes the plan — updating epics/stories rather than letting
the sprint drift. It `implements: [[stage-plan]]` because the underlying activity is
re-planning, even though it fires inside the implementation phase.

## See Also
- [[bmad]] — the framework.
- [[speckit-converge]] — SpecKit's related adaptive step: assess the codebase vs the spec and append the gap as new tasks. Both re-plan against reality mid-stream, but converge re-derives from spec drift while correct-course responds to a deliberate scope change.
- [[stage-plan]] — the canonical stage.
