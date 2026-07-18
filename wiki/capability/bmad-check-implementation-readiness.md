---
type: capability
subtype: skill
belongs_to: "[[bmad]]"
implements: "[[stage-plan]]"
delegates_to: []
produces: []
applies: ["[[pattern-plan-verification-loop]]"]
equivalent_to: ["[[gsd-plan-checker]]", "[[speckit-analyze]]", "[[ce-doc-review]]"]
sources: "bmad-code-org/BMAD-METHOD — bmad-check-implementation-readiness (2026)"
raw: ["../../raw/bmad/2026-07-04-bmad-method-framework.md"]
updated: 2026-07-04
---

# bmad-check-implementation-readiness

**`bmad-check-implementation-readiness`** — "Validate PRD, UX, Architecture and Epics specs are complete." BMAD's pre-build gate (owned by [[bmad-architect]] / [[bmad-pm]]), returning a **PASS / CONCERNS / FAIL** readiness verdict before any story is implemented ([[pattern-plan-verification-loop]]).

## Cross-framework cluster (plan verification)
This promotes the plan-verification gate to a **three-framework** pattern:

- [[gsd-plan-checker]] — GSD's eight-dimension plan gate, up to three revisions.
- [[speckit-analyze]] — SpecKit's cross-artifact consistency & coverage gate vs the constitution.

The three differ in scope: GSD scores a *single plan* on quality dimensions, SpecKit checks *consistency across artifacts* (spec ↔ plan ↔ tasks), and BMAD checks *cross-document completeness* across the whole planning set (PRD + UX + architecture + epics) before code.

## See Also
- [[bmad]] — the framework.
- [[pattern-plan-verification-loop]] — the technique, now three-framework.
- [[stage-plan]] — the canonical stage.
