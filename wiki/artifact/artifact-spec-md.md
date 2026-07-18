---
type: artifact
sources: "Addy Osmani — Agent Skills (2026); GitHub/spec-kit (2026); bmad-code-org/BMAD-METHOD (2026); Matt Pocock — Skills for Real Engineers v1.1 (2026)"
updated: 2026-07-09
---

# Artifact: SPEC.md / spec.md

A structured specification written **before any code** — the durable contract the rest of the lifecycle plans and builds against. Four frameworks produce a spec document in this slot, with different house formats:

- **Addy — `SPEC.md`** (project root): six core areas — objective & target users, commands, project structure, code style, testing strategy, and boundaries (always-do / ask-first / never-do).
- **Spec Kit — `specs/<feature>/spec.md`** (per feature): user stories + acceptance criteria, plus explicit **`[NEEDS CLARIFICATION]`** markers that flag ambiguities for [[speckit-clarify]] to resolve. Focuses on WHAT/WHY, deferring the HOW to [[speckit-plan]].
- **BMAD — `SPEC.md`** (the "SPEC kernel", from [[bmad-spec]]): a tight five-field machine contract — Problem, Capabilities, Constraints, Non-goals, Success signal — used as the lightweight [[pattern-scale-adaptive-planning|Quick-Flow]] alternative to a full PRD.
- **Matt Pocock — the spec from [[mp-to-spec]]** (v1.1): synthesized from the conversation (no interview), leads with a Problem Statement, sketches testing **seams**, and is published to the issue tracker with a `ready-for-agent` label. "Spec" is MP's single through-line term (was `to-prd`).

Upstream of planning it is a counterpart to GSD's [[artifact-context-md]] and to the fuller [[artifact-prd]] (BMAD) — same job (capture what & why durably), different house format. OpenSpec's [[artifact-spec-delta]] is the odd one out: a *delta* against a living spec rather than a whole rewritten document.

## Produced by (backlinks)
- [[addy-spec-driven-development]] — authors the six-area `SPEC.md`.
- [[speckit-specify]] — generates `spec.md` with user stories + `[NEEDS CLARIFICATION]` markers.
- [[bmad-spec]] — distills intent into the five-field SPEC kernel.
- [[gstack-spec]] — gstack's five-phase executable spec, gated by a Codex quality check before filing.
- [[mp-to-spec]] — synthesizes the conversation into a spec (formerly `to-prd`), seams-first, published to the tracker.

## See Also
- [[artifact-prd]] — the fuller product-requirements counterpart (MP / BMAD).
- [[artifact-spec-delta]] — OpenSpec's delta-against-living-spec counterpart.
- [[artifact-checklist]] — Spec Kit's quality gate on this spec.
- [[artifact-plan-md]] — what the spec is decomposed into next.
- [[stage-specify]] — the stage this artifact defines.
