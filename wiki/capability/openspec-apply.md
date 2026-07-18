---
type: capability
subtype: command
belongs_to: "[[openspec]]"
implements: "[[stage-implement]]"
produces: ["[[artifact-plan-md]]"]
applies: ["[[pattern-spec-driven-development]]"]
equivalent_to: ["[[gsd-execute-phase]]", "[[addy-incremental-implementation]]", "[[speckit-implement]]", "[[bmad-dev-story]]", "[[ce-work]]", "[[mp-implement]]", "[[sp-executing-plans]]"]
sources: "Fission-AI/OpenSpec docs — commands.md (2026)"
raw: ["../../raw/openspec/2026-07-04-openspec-framework.md"]
updated: 2026-07-09
---

# /opsx:apply

`/opsx:apply` — "Implement tasks from the change." It works through the [[artifact-plan-md]] (`tasks.md`) checklist **sequentially**, writing the code for each item and marking it complete, and **resumes from checkpoints if interrupted** (the checked-off checklist is the progress ledger). The spec deltas and `design.md` authored by [[openspec-propose]] are the contract it builds against.

**Produces:** working code plus an updated `tasks.md` with items checked off. Unlike GSD it does not spawn fresh-context sub-agents or parallel waves — it is a single sequential loop over the checklist.

## Cross-framework equivalents

The **execute** cluster now spans five frameworks: OpenSpec's `apply` ↔ GSD's [[gsd-execute-phase]] ↔ Addy's [[addy-incremental-implementation]] ↔ Spec Kit's [[speckit-implement]] ↔ BMAD's [[bmad-dev-story]] (`equivalent_to`) — all walk an ordered unit of work, implementing each against the spec. They differ in mechanics: GSD parallelizes into [[pattern-wave-parallelism]] waves via fresh-context [[gsd-executor]]s, Addy cuts thin [[pattern-vertical-slice]]s with one commit each, Spec Kit mandates test-first (TDD non-negotiable), BMAD drives from a single fully-contexted story per fresh context, while OpenSpec runs a plain resumable sequential pass.

## See Also
- [[openspec-propose]] — supplies the tasks, spec deltas, and design this builds against.
- [[openspec-verify]] — checks that the implementation matches those artifacts.
- [[gsd-execute-phase]] · [[addy-incremental-implementation]] · [[speckit-implement]] · [[bmad-dev-story]] — execute-cluster counterparts.
- [[stage-implement]] — the canonical stage this implements.
