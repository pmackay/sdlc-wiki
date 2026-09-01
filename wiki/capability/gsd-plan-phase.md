---
type: capability
subtype: command
belongs_to: "[[gsd]]"
implements: "[[stage-plan]]"
delegates_to: ["[[gsd-phase-researcher]]", "[[gsd-planner]]", "[[gsd-plan-checker]]"]
produces: ["[[artifact-plan-md]]", "[[artifact-research-md]]"]
applies: ["[[pattern-spec-driven-development]]", "[[pattern-plan-verification-loop]]", "[[pattern-fresh-context-subagents]]", "[[pattern-vertical-slice]]", "[[pattern-test-driven-development]]"]
equivalent_to: ["[[addy-planning]]", "[[speckit-plan]]", "[[ce-plan]]", "[[sp-writing-plans]]", "[[seeds-plan-submit]]"]
sources: "Open GSD docs — workflow-commands (2026)"
raw: ["../../raw/gsd/2026-06-27-gsd-core-framework.md"]
updated: 2026-08-31
---

# /gsd-plan-phase

`/gsd-plan-phase N` — Phase 2, "the core planning step": research, plan, and verify a phase. Runs optional domain research via [[gsd-phase-researcher]] (four parallel instances: stack, features, architecture, pitfalls), produces an atomic plan via [[gsd-planner]], then enters a verification loop with [[gsd-plan-checker]] (eight dimensions, up to three revision cycles) until the plan is approved for execution — see [[pattern-plan-verification-loop]].

**Produces:** [[artifact-plan-md]] (`{phase}-PLAN.md`, executable task prompts) and [[artifact-research-md]] (`RESEARCH.md`, when research runs); `SKELETON.md` in MVP mode on Phase 1.

**Flags:** `--mvp` (vertical slices UI→API→DB — see [[pattern-vertical-slice]]), `--tdd` (test-first RED-GREEN cycles — see [[pattern-test-driven-development]]), `--gaps` (re-plan to close verified gaps). When `/gsd-ui-phase` runs first, also delegates to gsd-ui-researcher / gsd-ui-checker.

These two flags are where GSD and Matt Pocock's toolkit converge: `--mvp` ↔ [[mp-to-tickets]] (both cut [[pattern-vertical-slice]] work) and `--tdd` ↔ [[mp-tdd]] (both drive [[pattern-test-driven-development]]).

## See Also
- [[seeds-plan-submit]] — the decomposition cluster's deterministic member: its plan gate is a generated schema rather than a checker sub-agent like [[gsd-plan-checker]], so it cannot be argued with and cannot judge quality.
- [[gsd-discuss-phase]] — supplies the locked context this plans against.
- [[gsd-execute-phase]] — consumes the approved plan.
- [[addy-planning]] — Addy's planning skill; same spec-to-plan step.
- [[speckit-plan]] — Spec Kit's planning command; research + design gated against the constitution (its plan-gate is split into [[speckit-analyze]]).
- [[stage-plan]] — the canonical stage this implements.
