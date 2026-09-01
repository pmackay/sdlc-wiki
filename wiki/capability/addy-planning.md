---
type: capability
subtype: skill
belongs_to: "[[addy-agent-skills]]"
implements: "[[stage-plan]]"
delegates_to: []
produces: ["[[artifact-plan-md]]"]
applies: ["[[pattern-vertical-slice]]"]
equivalent_to: ["[[mp-to-tickets]]", "[[gsd-plan-phase]]", "[[speckit-tasks]]", "[[bmad-create-epics-and-stories]]", "[[ce-plan]]", "[[sp-writing-plans]]", "[[seeds-plan-submit]]"]
sources: "Addy Osmani — Agent Skills (2026)"
raw: ["../../raw/addy-agent-skills/2026-07-04-agent-skills.md"]
updated: 2026-08-31
---

# Planning & Task Breakdown

Decompose a spec into small, verifiable tasks. The mechanism is read-only "plan mode" first, then map the **dependency graph** and build foundations bottom-up, **slice vertically** so each task delivers a working end-to-end path (per [[pattern-vertical-slice]]), and size every task so no unit touches more than ~5 files. Each task carries explicit acceptance criteria and a verification step; checkpoints fall between phases and a human reviews before implementation.

Output is saved to `tasks/plan.md` (the [[artifact-plan-md]]) and `tasks/todo.md`. It implements [[stage-plan]] and is the canonical source the spec skill defers to for slicing mechanics.

## See Also
- [[seeds-plan-submit]] — the same dependency-ordered decomposition, produced by validating a filled template rather than by instructing an agent.
- [[mp-to-tickets]] — the Matt Pocock equivalent breakdown skill.
- [[gsd-plan-phase]] — the GSD equivalent planning phase.
- [[speckit-tasks]] — Spec Kit's decomposition into a `[P]`-parallelizable, test-first task list.
- [[bmad-create-epics-and-stories]] — BMAD's decomposition into epics of context-rich stories.
- [[stage-plan]] — the canonical stage this implements.
