---
type: artifact
sources: "Fission-AI/OpenSpec — concepts.md (2026)"
raw: ["../../raw/openspec/2026-07-04-openspec-framework.md"]
updated: 2026-07-04
---

# Artifact: proposal.md

`openspec/changes/<name>/proposal.md` — the **why and what** of a change. It captures the
problem statement, the scope boundaries (what is in and out of scope), and the proposed
technical approach at a high level. It is the first artifact in a change's dependency chain
(`proposal → specs → design → tasks`) and the intent that the spec deltas, design, and tasks
then flesh out.

OpenSpec deliberately **splits apart** what other frameworks bundle into one spec document:
the *why/scope* lives here in `proposal.md`, the *behavioral requirements* live in the
[[artifact-spec-delta]], the *how* lives in [[artifact-design-md]], and the *task list* lives
in [[artifact-plan-md]] (`tasks.md`). So `proposal.md` is the rationale layer only —
narrower than a full [[artifact-prd]] or [[artifact-spec-md]], which fold requirements and
scope into a single file.

## Produced by (backlinks)
- [[openspec-propose]] — authors it as the first of the four planning artifacts.

## See Also
- [[artifact-spec-delta]] — the behavioral requirements this proposal frames.
- [[artifact-design-md]] · [[artifact-plan-md]] — the how and the task list that follow it.
- [[artifact-prd]] · [[artifact-spec-md]] — single-document spec counterparts from other frameworks.
- [[artifact-product-brief]] — BMAD's comparable pre-PRD why/what + scope scoping document.
- [[stage-specify]] — the stage that produces it.
