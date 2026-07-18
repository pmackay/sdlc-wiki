---
type: pattern
sources: "Open GSD docs (2026); GitHub/spec-kit (2026); bmad-code-org/BMAD-METHOD (2026)"
updated: 2026-07-05
---

# Pattern: Plan verification loop

Before any execution, run the generated plan through an automated checker across multiple quality dimensions, revising until it passes — a gate that prevents flawed plans from reaching code. In GSD, [[gsd-plan-checker]] verifies plans across **eight dimensions** with up to **three revision cycles** inside [[gsd-plan-phase]].

## Applied by (backlinks)

GSD:

- [[gsd-plan-phase]] — hosts the verification loop before execution.
- [[gsd-plan-checker]] — verifies across eight dimensions, up to three revisions.

Spec Kit:

- [[speckit-analyze]] — cross-artifact consistency & coverage gate, checked against the [[artifact-constitution]], before implementation.

BMAD:

- [[bmad-check-implementation-readiness]] — cross-document completeness gate over the whole planning set (PRD + UX + architecture + epics), returning PASS / CONCERNS / FAIL before any story is built.

A third framework promotes this to a **three-framework** pattern. The gates differ in what they check: GSD scores a *single plan* on eight quality dimensions, Spec Kit checks *consistency and coverage across multiple artifacts* (spec ↔ plan ↔ tasks) plus constitutional compliance, and BMAD checks *completeness across the full planning document set* before implementation.

Compound Engineering:

- [[ce-doc-review]] — gates the requirements/plan with a reviewer-persona fan-out before execution.
- [[ce-spec-flow-analyzer]] — surfaces missing flows / ambiguous requirements / edge cases before implementation.

gstack:

- [[gstack-plan-eng-review]] — locks architecture / edge-cases / tests, gating the plan before execution.

## See Also
- [[pattern-spec-driven-development]] — the broader method this gates.
- [[stage-plan]] — the stage where this applies.
