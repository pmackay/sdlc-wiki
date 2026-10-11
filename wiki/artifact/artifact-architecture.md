---
type: artifact
sources: "bmad-code-org/BMAD-METHOD — bmad-architecture (2026); pstack v0.15.2 — Lauren Tan (2026)"
raw: ["../../raw/bmad/2026-07-04-bmad-method-framework.md"]
updated: 2026-09-11
---

# Artifact: architecture

BMAD's Solutioning deliverable — `ARCHITECTURE-SPINE.md`, "a lean spine of invariants … projected into whatever format the work needs." What makes it distinctive among the wiki's design artifacts is its **invariants-only discipline**: the spine "fixes only the invariants … the design paradigm, the boundary and dependency rules, how state is mutated, who owns shared data." Everything structural — "stack, tree, full data shape" — is treated as "**seed**: true at cold-start, owned by the code once it exists."

That makes it a deliberately *thin, durable* system-architecture contract rather than a full up-front design — BMAD's [[pattern-scale-adaptive-planning|just-in-time]] answer to over-specification. It gates through [[bmad-check-implementation-readiness]] before any story is built.

## Produced by (backlinks)
- [[bmad-architecture]] — produces and updates the spine.

pstack:

- [[pstack-architect]] — a design package of types, function signatures, class shapes, and module boundaries with `not implemented` bodies and pseudocode, synthesized across four model perspectives and screened against a shipped design red-flag list. pstack's substitute for a written spec: *"the best spec is code."*

## See Also
- [[artifact-design-md]] — the *per-change* / lower-level design artifact (OpenSpec `design.md`, SpecKit `plan.md`+`data-model.md`+`contracts/`, BMAD UX `DESIGN.md`); the architecture spine is the higher-level system contract above it.
- [[pattern-scale-adaptive-planning]] — the technique behind the invariants/seed split.
- [[stage-plan]] — the stage this artifact supports.
