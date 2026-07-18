---
type: capability
subtype: skill
belongs_to: "[[addy-agent-skills]]"
implements: "[[stage-implement]]"
delegates_to: []
produces: ["[[artifact-atomic-commit]]"]
applies: ["[[pattern-vertical-slice]]", "[[pattern-feature-flags]]"]
equivalent_to: ["[[gsd-execute-phase]]", "[[openspec-apply]]", "[[speckit-implement]]", "[[bmad-dev-story]]", "[[ce-work]]", "[[mp-implement]]", "[[sp-executing-plans]]"]
sources: "Addy Osmani — Agent Skills (2026)"
raw: ["../../raw/addy-agent-skills/2026-07-04-agent-skills.md"]
updated: 2026-07-09
---

# Incremental Implementation

Build in thin vertical slices instead of one big pass: for each slice **implement → test → verify → commit**, then carry forward. Every increment leaves the system compilable and testable, changes one logical thing (yielding an [[artifact-atomic-commit]]), and stays rollback-friendly. Incomplete work hides behind [[pattern-feature-flags]] with safe, conservative defaults so small increments can merge without exposing unfinished features.

It is the execution discipline for any change touching more than one file, applies [[pattern-vertical-slice]], and leans on simplicity-first and scope discipline as core rules. It implements [[stage-implement]].

## See Also
- [[addy-tdd]] — the test half of each slice's verify step.
- [[gsd-execute-phase]] — the GSD equivalent execution phase.
- [[openspec-apply]] — OpenSpec's equivalent; walks the `tasks.md` checklist sequentially.
- [[speckit-implement]] — Spec Kit's equivalent; executes `tasks.md` with mandatory TDD.
- [[bmad-dev-story]] — BMAD's equivalent; implements one fully-contexted story at a time.
- [[stage-implement]] — the canonical stage this implements.
