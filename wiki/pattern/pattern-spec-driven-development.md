---
type: pattern
sources: "Open GSD docs (2026); Fission-AI/OpenSpec (2026); GitHub/spec-kit (2026); bmad-code-org/BMAD-METHOD (2026); tao-hpu/nano-spec (2025); Agent OS — Builder Methods (2026)"
updated: 2026-08-05
---

# Pattern: Spec-driven development

Drive AI coding agents from explicit, versioned specifications rather than freeform prompting: capture decisions, write a plan/spec, execute against it, verify against it. GSD's whole five-phase loop is an instance — it pairs spec-driven development with meta-prompting and context engineering. [[openspec]] is the wiki's purest instance: its name *is* the practice (spec-driven development), and its four principles — fluid, iterative, easy, brownfield-first — are the clearest statement of the ethos. [[speckit]] is the wiki's **reference implementation** of the idea: GitHub's toolkit whose entire premise is "specifications don't serve code — code serves specifications."

Frameworks differ on **how durable the spec is**. GSD, Matt Pocock, and Addy write a *per-change* spec/PRD/plan that is executed then left behind — as does nano-spec, whose per-task 4-file pack is the most ephemeral instance. OpenSpec sits at the opposite pole: a **permanent, self-updating spec** with each change expressed as a delta against it — the [[pattern-living-specification]] specialization.

## Applied by (backlinks)

GSD:

- [[gsd-discuss-phase]] — captures decisions into the spec.
- [[gsd-plan-phase]] — turns the spec into an executable plan.
- [[gsd-verify-work]] — validates the build against the spec.
- [[gsd-ship]] — closes the iteration against the spec.
- [[gsd-planner]] — authors the plan from artifacts only.

Addy Osmani — Agent Skills:

- [[addy-spec-driven-development]] — drives the agent from an explicit, versioned spec.

OpenSpec:

- [[openspec-propose]] — authors the spec (as deltas) before code.
- [[openspec-apply]] — implements against the spec deltas + design.
- [[openspec-verify]] — validates the build against the spec artifacts.
- [[openspec-sync]] · [[openspec-archive]] — fold the delta back into the living spec.

Spec Kit:

- [[speckit-specify]] — defines the spec (WHAT/WHY) before code.
- [[speckit-plan]] — turns the spec into a technical plan validated against the constitution.

BMAD:

- [[bmad-prd]] — authors the durable PRD that drives the build.
- [[bmad-architecture]] — turns the PRD into the architecture spine.
- [[bmad-spec]] — the lightweight `SPEC.md` kernel on the Quick-Flow path.

gstack:

- [[gstack-spec]] — turns vague intent into a precise, executable five-phase spec with a Codex quality gate.

Builder Methods — BM Skills:

- [[bm-prd-creator]] — a non-technical-builder interview producing the PRD the build runs against.

nano-spec:

- [[nano-spec-create]] — the minimalist instance: a fixed 4-file pack ([[artifact-nano-spec-pack]]) as the smallest useful spec, then drive the agent from it.

Agent OS:

- [[agent-os-shape-spec]] — *shapes* (rather than generates) a spec in the harness's Plan Mode into a persistent, standards-bound pack; v3 delegates spec authoring to the model and keeps only the structuring + durability.

## See Also
- [[pattern-living-specification]] — OpenSpec's specialization: a permanent, delta-maintained spec.
- [[pattern-project-constitution]] — Spec Kit's specialization: principles externalized into a governing document.
- [[pattern-fresh-context-subagents]], [[pattern-plan-verification-loop]]
- [[gsd]], [[openspec]], [[speckit]] — frameworks built on this pattern.
