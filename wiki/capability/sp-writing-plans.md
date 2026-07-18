---
type: capability
subtype: skill
belongs_to: "[[superpowers]]"
implements: "[[stage-plan]]"
delegates_to: ["[[sp-subagent-driven-development]]", "[[sp-executing-plans]]"]
produces: ["[[artifact-plan-md]]"]
applies: ["[[pattern-vertical-slice]]", "[[pattern-test-driven-development]]"]
equivalent_to: ["[[gsd-plan-phase]]", "[[addy-planning]]", "[[speckit-tasks]]", "[[mp-to-tickets]]", "[[ce-plan]]", "[[bmad-create-epics-and-stories]]"]
sources: "Superpowers v6.1.1 (2026)"
raw: ["../../raw/superpowers/2026-07-17-superpowers.md"]
updated: 2026-07-17
---

# writing-plans

Turn an approved design into a **comprehensive implementation plan** written for *"an enthusiastic junior engineer with poor taste, no judgement, no project context, and an aversion to testing."* The plan is the single source of truth an executor (human or subagent) follows verbatim, so it must carry everything: which files to touch, complete code, interfaces, and exact verification commands.

Structure: a **File Structure** map (decomposition decisions locked here) → **task right-sizing** (a task is the smallest unit that carries its own test cycle and is worth a reviewer's gate, [[pattern-vertical-slice]]) → **bite-sized steps** of 2-5 minutes each, embodying the TDD loop ("write the failing test" / "run it to see it fail" / "minimal code" / "run to see it pass" / "commit", [[pattern-test-driven-development]]). Each task block names exact **Files** (create/modify/ test) and **Interfaces** (Consumes/Produces — exact signatures, since an executor sees only its own task).

> **The No-Placeholders law:** "TBD", "add appropriate error handling", "write tests for the above" (without the test code), "similar to Task N", or any reference to an undefined type are **plan failures**. A self-review pass checks spec coverage, scans for these red flags, and verifies type consistency across tasks. → [[artifact-plan-md]].

The **execution handoff** offers two paths: [[sp-subagent-driven-development]] (recommended) or [[sp-executing-plans]]. It joins the cross-framework decompose/plan cluster with [[gsd-plan-phase]], [[addy-planning]], [[speckit-tasks]], [[mp-to-tickets]], [[ce-plan]], and [[bmad-create-epics-and-stories]] — distinctive for baking the TDD micro-loop directly into every task's steps and forbidding placeholders outright.

## See Also
- [[sp-brainstorming]] — supplies the approved design this plan decomposes.
- [[sp-subagent-driven-development]] · [[sp-executing-plans]] — the two execution paths it hands off to.
- [[gsd-plan-phase]] · [[addy-planning]] · [[speckit-tasks]] · [[mp-to-tickets]] · [[ce-plan]] · [[bmad-create-epics-and-stories]] — the plan/decompose cluster.
- [[artifact-plan-md]] — the plan it produces.
- [[stage-plan]] — the canonical stage this implements.
