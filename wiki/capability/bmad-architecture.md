---
type: capability
subtype: skill
belongs_to: "[[bmad]]"
implements: "[[stage-plan]]"
delegates_to: []
produces: ["[[artifact-architecture]]"]
applies: ["[[pattern-scale-adaptive-planning]]", "[[pattern-spec-driven-development]]"]
equivalent_to: []
sources: "bmad-code-org/BMAD-METHOD — bmad-architecture (2026)"
raw: ["../../raw/bmad/2026-07-04-bmad-method-framework.md"]
updated: 2026-07-04
---

# bmad-architecture

**`bmad-architecture`** — "Produce the architecture: a lean spine of invariants … projected
into whatever format the work needs." The Solutioning workflow owned by [[bmad-architect]],
producing [[artifact-architecture]] (`ARCHITECTURE-SPINE.md`).

Its distinctive stance is a **spine of invariants only** — "a consistency contract that fixes
only the invariants … the design paradigm, the boundary and dependency rules, how state is
mutated, who owns shared data." Everything structural (stack, tree, full data shape) is treated
as "seed: true at cold-start, owned by the code once it exists." That is BMAD's
[[pattern-scale-adaptive-planning|just-in-time]] answer to over-specified up-front design.

## See Also
- [[bmad]] — the framework.
- [[artifact-architecture]] — the spine document produced here.
- [[mp-codebase-design]], [[addy-api-design]], [[speckit-plan]] — the cross-framework design capabilities (see the design split candidate on [[stage-plan]]).
- [[bmad-check-implementation-readiness]] — gates this architecture (plus PRD/UX/epics) before code.
- [[stage-plan]] — the canonical stage.
