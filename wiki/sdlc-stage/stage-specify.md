---
type: sdlc-stage
aka: { matt-pocock-skills: "to-spec", addy-agent-skills: "spec-driven-development / SPEC.md", openspec: "propose / spec deltas", speckit: "specify / spec.md", bmad: "Planning (PRD / UX / SPEC kernel)", gstack: "spec", bm-skills: "PRD Creator", nano-spec: "create / 4-doc pack" }
sources: "Synthesized from Matt Pocock + Addy Osmani + OpenSpec + Spec Kit + BMAD + gstack + BM Skills + nano-spec (2026)"
updated: 2026-07-13
---

# Stage: Specify

Canonical lifecycle stage: **capture what to build and why in a durable specification** — a PRD / SPEC.md / spec-delta / requirements artifact — distinct from the *interactive* act of resolving decisions ([[stage-align]]) and from decomposing the *how* into executable units ([[stage-plan]]). The spec is the written contract the rest of the lifecycle plans and builds against.

**Promoted on the 2026-07-04 ingest; reinforced the same day by OpenSpec and Spec Kit.** Previously parked as a split candidate on [[stage-plan]] (one vote: Matt Pocock), it cleared the ≥2-framework bar when Addy Osmani's `/spec` phase became the second framework to treat spec authoring as its own step. **OpenSpec was the third** ([[openspec-propose]]), and **Spec Kit is the fourth** ([[speckit-specify]]) and **BMAD the fifth** ([[bmad-prd]]) — putting this stage beyond doubt. BMAD reinforces it structurally: its dedicated **Planning phase** (PRD + UX) sits between an Analysis phase ([[stage-align]]) and a Solutioning phase ([[stage-plan]]), treating spec authoring as an explicit, separate phase (see [Stage re-derivation](../CONVENTIONS.md#stage-re-derivation-keep-stages-framework-neutral)).

**Derived projection** — evidence is the capabilities that `implements: [[stage-specify]]`.

## Implemented by (backlinks)

Matt Pocock — Skills for Real Engineers:

- [[mp-to-spec]] — synthesize the conversation into a **spec** → [[artifact-spec-md]] (v1.1: renamed from `to-prd`; "spec" is now the through-line term, though it still opens "you may know this as a PRD"). Sketches testing seams before writing.

Addy Osmani — Agent Skills:

- [[addy-spec-driven-development]] — write a six-area SPEC.md before any code → [[artifact-spec-md]].

OpenSpec:

- [[openspec-propose]] — author the change as a [[artifact-spec-delta]] (+ proposal/design/tasks) before code.

Spec Kit:

- [[speckit-specify]] — define WHAT/WHY as `spec.md` (user stories + `[NEEDS CLARIFICATION]` markers) → [[artifact-spec-md]].
- [[speckit-checklist]] — generate a quality checklist that gates the spec's completeness/clarity/consistency → [[artifact-checklist]].

BMAD:

- [[bmad-pm]] — the Planning persona (John) that owns the PRD.
- [[bmad-prd]] — the facilitated create/update/validate PRD → [[artifact-prd]].
- [[bmad-ux-designer]] · [[bmad-ux]] — UX design specification (`DESIGN.md` + `EXPERIENCE.md`) → [[artifact-design-md]].
- [[bmad-spec]] — the five-field SPEC kernel → [[artifact-spec-md]] (Quick-Flow lightweight spec).

gstack (the sixth framework):

- [[gstack-spec]] — turn vague intent into a five-phase executable spec (with mandatory code-reading), gated by a **Codex quality check** before it files a deduped GitHub issue → [[artifact-spec-md]], [[artifact-issue]]. `--execute` spawns a fresh-worktree agent; [[gstack-ship]] closes the issue on merge.

Builder Methods — BM Skills:

- [[bm-prd-creator]] — a structured interview for **non-technical builders** → a visual HTML (or markdown) PRD → [[artifact-prd]] + milestone prompt files ([[artifact-plan-md]]); strict *what-not-how* boundary ([[pattern-grilling]], [[pattern-scale-adaptive-planning]]).

nano-spec (the eighth framework):

- [[nano-spec-create]] — generate a minimal **4-document pack** ([[artifact-nano-spec-pack]]: README/todo/doc/log) from a one-line description; the specify cluster's minimalist, tool-agnostic entry, positioned as the deliberate middle of a no-spec → nano → full-spec ceremony spectrum ([[pattern-scale-adaptive-planning]]).

GSD **folds this in**: [[gsd-plan-phase]] produces [[artifact-plan-md]] directly and captures intent upstream in [[artifact-context-md]], with no separate spec artifact.

## Cross-framework equivalents
Eight frameworks now converge on **write the spec down before building**: Addy's [[addy-spec-driven-development]] ↔ Matt's [[mp-to-spec]] ↔ OpenSpec's [[openspec-propose]] ↔ Spec Kit's [[speckit-specify]] ↔ BMAD's [[bmad-prd]] ↔ gstack's [[gstack-spec]] ↔ Builder Methods' [[bm-prd-creator]] ↔ nano-spec's [[nano-spec-create]] (`equivalent_to`), clustered at [[pattern-spec-driven-development]]. BM's is the outlier by *audience*: a non-technical-builder interview producing a **visual HTML PRD** + milestone prompts, where the rest assume a developer reader. nano-spec is the outlier by *weight*: a fixed **4-file pack** ([[artifact-nano-spec-pack]]) that deliberately minimizes ceremony — the smallest useful spec, tool-agnostic across ten agents — the opposite pole from Spec Kit's / gstack's gated maximalism and OpenSpec's permanent delta-maintained spec. gstack adds a **cross-model quality gate** ([[gstack-codex]] blocks specs below 7/10) — a QA step on the spec analogous to Spec Kit's [[speckit-checklist]] but enforced by a second model rather than a checklist artifact. They differ in artifact house-format — a root `SPEC.md`, a PRD in the issue tracker, an ADDED/MODIFIED/REMOVED [[artifact-spec-delta]] against a living spec, or a per-feature `spec.md` — but do the same job. OpenSpec is distinctive in that its spec is **permanent and delta-maintained** ([[pattern-living-specification]]) rather than a per-change document. Spec Kit adds a distinctive **spec-quality gate**, [[speckit-checklist]] ("unit tests for your English"), producing an [[artifact-checklist]] — a QA step on the requirements that no other framework here materialises as an artifact.

## See Also
- [[stage-align]] — the interactive elicitation / exploration that precedes writing the spec.
- [[stage-plan]] — decomposes the approved spec into tasks ([[openspec-propose]] folds this in).
- [[artifact-spec-md]] · [[artifact-prd]] · [[artifact-spec-delta]] · [[artifact-proposal-md]] · [[artifact-checklist]] · [[artifact-nano-spec-pack]] — the artifacts this stage produces.
