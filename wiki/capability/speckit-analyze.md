---
type: capability
subtype: command
belongs_to: "[[speckit]]"
implements: "[[stage-plan]]"
applies: "[[pattern-plan-verification-loop]]"
equivalent_to: ["[[gsd-plan-checker]]", "[[bmad-check-implementation-readiness]]", "[[ce-doc-review]]"]
sources: "GitHub/spec-kit README + spec-driven.md (2026)"
raw: ["../../raw/speckit/2026-07-04-speckit-framework.md"]
updated: 2026-07-04
---

# speckit-analyze

**`/speckit.analyze`** — "Cross-artifact consistency & coverage analysis." An optional gate
that validates the planning artifacts (spec, plan, tasks) against each other **and against
the [[artifact-constitution]]** before implementation begins: architectural compliance with
all nine constitutional articles, consistency checking for contradictions and gaps, and
documentation of justified exceptions. It ensures "every technical choice links back to a
specific requirement," and is framed as "continuous refinement as an ongoing process rather
than a one-time gate."

## A plan-gate, not a build-validation

`analyze` runs on the *artifacts* before code exists, so it belongs to [[stage-plan]] (a
gate on the plan) rather than [[stage-validate]] (which confirms a built system). It is Spec
Kit's node in the **plan-verification** cluster ([[pattern-plan-verification-loop]]):

- [[gsd-plan-checker]] — GSD's eight-dimension plan gate, up to three revisions.
- [[bmad-check-implementation-readiness]] — BMAD's PASS/CONCERNS/FAIL completeness gate over PRD + UX + architecture + epics.

This cluster promotes [[pattern-plan-verification-loop]] to a **three-framework** pattern. The
distinction: GSD's checker scores one plan on eight quality dimensions; Spec Kit's analyze
checks *consistency and coverage across multiple artifacts* and constitutional compliance; and
BMAD checks *completeness across the whole planning document set* before implementation.

## See Also
- [[speckit]] — the framework.
- [[speckit-plan]] / [[speckit-tasks]] — the artifacts this command audits.
- [[speckit-constitution]] — the principles it enforces.
- [[gsd-plan-checker]] · [[bmad-check-implementation-readiness]] — the plan-verification counterparts.
- [[stage-plan]] — the canonical stage.
