---
type: capability
subtype: command
belongs_to: "[[nano-spec]]"
delegates_to: []
produces: ["[[artifact-nano-spec-pack]]", "[[artifact-adr]]"]
applies: ["[[pattern-session-handoff]]"]
equivalent_to: []
sources: "Tao An — nano-spec (2025)"
raw: ["../../raw/nano-spec/2025-12-01-nano-spec.md"]
updated: 2026-07-13
---

# nano-spec update

`/nano-spec update <task-name> "<what to change>"` — reads the existing [[artifact-nano-spec-pack|pack]], applies a requested change (mark a todo done, record a decision in `doc.md`, revise scope, etc.), and appends a dated entry to `log.md`. This is the mechanism that keeps the pack a **living document through the build** rather than a write-once spec — the counterpart to [[nano-spec-create]]'s one-shot generation.

It maps to **no single canonical stage**: it is cross-cutting doc-maintenance that runs alongside [[stage-implement]] and [[stage-review]] as work proceeds. By continuously folding decisions (ADR-style records in `doc.md` → [[artifact-adr]]) and progress (`log.md`) back into the pack, it applies [[pattern-session-handoff]] — the up-to-date pack is what makes the "read all 4 files and explain the project" handoff work.

nano-spec's `log.md` journey trail is *within-task* progress logging, not cross-iteration [[pattern-knowledge-compounding]]: it captures learnings for handoff and retrospective, but nano-spec provides no mechanism to harvest them into durable grounding for *future* tasks (contrast [[ce-compound]] / [[gstack-learn]]). It therefore stops short of [[stage-learn]].

## See Also
- [[nano-spec-create]] — the initial generation this maintains; [[nano-spec-status]] — reads the result.
- [[artifact-nano-spec-pack]] — what it mutates; [[artifact-adr]] — the decision records it appends to `doc.md`.
- [[pattern-session-handoff]] — keeping the pack current for cross-boundary resumption.
- [[nano-spec]] — the parent framework. </content>
