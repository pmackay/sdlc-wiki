---
type: artifact
sources: "Fission-AI/OpenSpec — concepts.md (2026); GitHub/spec-kit (2026); bmad-code-org/BMAD-METHOD (2026); Builder Methods — BM Skills (2026)"
raw: ["../../raw/openspec/2026-07-04-openspec-framework.md", "../../raw/speckit/2026-07-04-speckit-framework.md", "../../raw/bmad/2026-07-04-bmad-method-framework.md", "../../raw/bm-skills/2026-07-09-bm-skills.md"]
updated: 2026-07-09
---

# Artifact: design.md (technical "how")

The **how** of a change — technical approach, architecture decisions with rationale, data flow, and component interactions — kept separate from the behavioral spec. Two frameworks produce it:

- **OpenSpec — `openspec/changes/<name>/design.md`**: third artifact in the chain (`proposal → specs → design → tasks`), sitting between the behavioral [[artifact-spec-delta]] (what) and the [[artifact-plan-md]] (`tasks.md`, the checklist). OpenSpec's specs capture observable behavior only, so implementation choices are deliberately quarantined here.
- **Spec Kit — `plan.md` + `data-model.md` + `contracts/`**: emitted together by [[speckit-plan]]. `plan.md` is the strategy, `data-model.md` the entities/schema, and `contracts/` the API specs (the [[pattern-contract-first]] surface). Validated against the [[artifact-constitution]] via "Phase -1" gates.

- **BMAD — `DESIGN.md` + `EXPERIENCE.md`**: the two-spine UX design spec from [[bmad-ux]] (Sally) — `DESIGN.md` for visual identity, `EXPERIENCE.md` for behavioral logic / information architecture. The *design of the experience* rather than of the system internals.

It is a **per-change design record**: closely related to an [[artifact-adr]] (both capture decisions + rationale), but scoped to one change rather than a standing log, and the counterpart to the design work GSD folds into [[gsd-planner]] and Addy into [[addy-api-design]]. The higher-level *system* design contract is BMAD's [[artifact-architecture|architecture spine]].

## Produced by (backlinks)
- [[openspec-propose]] — authors it after the proposal and spec deltas.
- [[speckit-plan]] — emits `plan.md` + `data-model.md` + `contracts/` as the technical design.
- [[bmad-ux]] — emits `DESIGN.md` + `EXPERIENCE.md`, the UX design specification.
- [[gstack-design-consultation]] — builds the `DESIGN.md` design system from scratch (gstack).
- [[bm-design-system]] — scaffolds a React + Tailwind v4 design system as **runnable component code + a live reference page + agent guardrails** (Builder Methods; a code-scaffold form of the design system, not a doc).

## See Also
- [[artifact-architecture]] — BMAD's system-level architecture spine, above this lower-level design.
- [[artifact-spec-delta]] — the behavior this design realizes (OpenSpec).
- [[artifact-plan-md]] — the task checklist derived from this design.
- [[artifact-research-md]] — the investigation that feeds the design (Spec Kit `research.md`).
- [[artifact-adr]] — the standing architecture-decision-record counterpart.
- [[stage-plan]] — the stage this artifact's *how* belongs to.
