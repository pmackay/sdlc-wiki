---
type: capability
subtype: skill
belongs_to: "[[addy-agent-skills]]"
implements: "[[stage-specify]]"
delegates_to: []
produces: ["[[artifact-spec-md]]"]
applies: ["[[pattern-spec-driven-development]]"]
equivalent_to: ["[[mp-to-spec]]", "[[openspec-propose]]", "[[speckit-specify]]", "[[bmad-prd]]", "[[bm-prd-creator]]", "[[nano-spec-create]]"]
sources: "Addy Osmani — Agent Skills (2026)"
raw: ["../../raw/addy-agent-skills/2026-07-04-agent-skills.md"]
updated: 2026-07-09
---

# Spec-Driven Development

Write a structured spec (a [[artifact-spec-md]]) before any code — the shared source of truth defining what we're building, why, and how we'll know it's done. The spec covers six core areas: **objective, commands, project structure, code style, testing strategy, and boundaries** (an Always / Ask-first / Never triad). It sits at the head of a gated SPECIFY → PLAN → TASKS → IMPLEMENT workflow, each phase human-reviewed before advancing.

This is the **second framework — alongside Matt Pocock's [[mp-to-spec]] — to treat spec authoring as its own step** rather than folding it into planning. That convergence is the evidence that promoted [[stage-specify]] out of [[stage-plan]] in this wiki's ontology. It applies [[pattern-spec-driven-development]].

## See Also
- [[artifact-spec-md]] — the document this produces.
- [[mp-to-spec]] — the equivalent spec-authoring skill in Matt Pocock's pack.
- [[openspec-propose]] — OpenSpec's spec-first counterpart; writes a delta-based spec (+ design/tasks) before code.
- [[speckit-specify]] — Spec Kit's spec-first counterpart; the SPECIFY → PLAN → TASKS → IMPLEMENT phrasing here mirrors Spec Kit's workflow.
- [[bmad-prd]] — BMAD's spec-first counterpart; a facilitated PRD (the fifth framework in the specify cluster).
- [[stage-specify]] — the canonical stage this implements.
