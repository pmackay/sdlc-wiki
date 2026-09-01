---
type: pattern
sources: "Open GSD docs (2026); GitHub/spec-kit (2026); bmad-code-org/BMAD-METHOD (2026); jayminwest/seeds (2026)"
updated: 2026-08-31
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

In Fowler's *harness engineering* terms this is an **inferential sensor** run at the earliest useful point — a feedback control on the *plan* before any code exists ([[topic-harness-engineering]]).

Seeds — the cluster's first gate that is not a model:

- [[seeds-plan-submit]] — an AJV schema generated from the plan template checks required sections, `min_length`, `min`, step-index range, and self-references before any child seed is spawned. Failure is pre-write and returns a patchable partial-state diff (`errors[].path/code/fix` plus the plan as submitted), so the agent revises rather than restarts — the framework's *"one-shot with resume"*.
- [[seeds-plan-validate]] — re-runs the gate against the current template definition, the mechanism behind its claim that a failure should be fixed in the planning *process* rather than in code review.

The trade against the five model-based gates above is sharp in both directions: this one cannot be argued out of its verdict, and it checks shape rather than quality — it notices a missing `risks` array, never a wrong approach.

## See Also
- [[pattern-spec-driven-development]] — the broader method this gates.
- [[topic-harness-engineering]] — the guides/sensors control system this is a sensor within.
- [[stage-plan]] — the stage where this applies.
