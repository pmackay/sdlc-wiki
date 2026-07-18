---
type: capability
subtype: command
belongs_to: "[[openspec]]"
implements: "[[stage-specify]]"
produces: ["[[artifact-proposal-md]]", "[[artifact-spec-delta]]", "[[artifact-design-md]]", "[[artifact-plan-md]]"]
applies: ["[[pattern-spec-driven-development]]", "[[pattern-living-specification]]"]
equivalent_to: ["[[addy-spec-driven-development]]", "[[mp-to-spec]]", "[[speckit-specify]]", "[[bmad-prd]]", "[[bm-prd-creator]]", "[[nano-spec-create]]"]
sources: "Fission-AI/OpenSpec docs — commands.md, concepts.md (2026)"
raw: ["../../raw/openspec/2026-07-04-openspec-framework.md"]
updated: 2026-07-09
---

# /opsx:propose

`/opsx:propose` — "Create a new change and generate planning artifacts in one step." It
scaffolds `openspec/changes/<name>/` and generates **all four planning artifacts at once**,
in dependency order:

1. [[artifact-proposal-md]] (`proposal.md`) — the why/what and in/out-of-scope boundaries.
2. [[artifact-spec-delta]] (`specs/<domain>/spec.md`) — ADDED/MODIFIED/REMOVED requirement deltas against the living spec, each with Given/When/Then scenarios.
3. [[artifact-design-md]] (`design.md`) — the technical approach and architecture decisions.
4. [[artifact-plan-md]] (`tasks.md`) — the hierarchically numbered implementation checklist.

Best for "straightforward changes with clear requirements." It is the heart of OpenSpec's
[[pattern-spec-driven-development]] and the entry to its [[pattern-living-specification]]
loop — the change it authors is a delta that [[openspec-sync]] will later fold into the
durable spec.

## Spans specify *and* plan

Because one command emits the spec deltas *and* the design + task breakdown, `propose`
straddles two canonical stages. Its `implements:` edge points at [[stage-specify]] — the spec
delta is the durable, framework-defining output — but its `design.md` + `tasks.md` also do
the [[stage-plan]] job (the *how* and the task decomposition). OpenSpec keeps these fluid
(one step) rather than gating them as separate phases.

In the **expanded profile** the same work is done incrementally: `/opsx:new` scaffolds the
folder, then `/opsx:continue` generates one artifact at a time (or `/opsx:ff` fast-forwards
through all of them) in the `proposal → specs → design → tasks` dependency order — see
[[openspec]].

## Cross-framework equivalents

`propose` is one entry in the **five-framework specify** cluster: OpenSpec's spec deltas ↔
Addy's [[addy-spec-driven-development]] (`SPEC.md`) ↔ Matt's [[mp-to-spec]] (PRD) ↔ Spec Kit's
[[speckit-specify]] (`spec.md`) ↔ BMAD's [[bmad-prd]] (facilitated `prd.md`). All five "write
the spec down before building," differing in house format — a versioned delta against a living
spec vs a root `SPEC.md` vs a PRD in the tracker vs a per-feature `spec.md` with
`[NEEDS CLARIFICATION]` markers vs a stakes-calibrated PRD. Like `propose`,
Spec Kit's flow also spans specify→plan, but splits them into separate commands
([[speckit-specify]] then [[speckit-plan]] / [[speckit-tasks]]) rather than one fluid step.

## See Also
- [[openspec-explore]] — the discovery that precedes proposing.
- [[openspec-apply]] — consumes the `tasks.md` this produces.
- [[addy-spec-driven-development]] · [[mp-to-spec]] · [[speckit-specify]] · [[bmad-prd]] — the specify-cluster counterparts.
- [[stage-specify]] — the canonical stage this implements (also touches [[stage-plan]]).
