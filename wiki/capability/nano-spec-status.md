---
type: capability
subtype: command
belongs_to: "[[nano-spec]]"
delegates_to: []
produces: []
applies: ["[[pattern-session-handoff]]"]
equivalent_to: []
sources: "Tao An — nano-spec (2025)"
raw: ["../../raw/nano-spec/2025-12-01-nano-spec.md"]
updated: 2026-07-13
---

# nano-spec status

`/nano-spec status <task-name>` — reads a task's `todo.md` and `log.md` from the [[artifact-nano-spec-pack|pack]] and reports a lightweight progress summary: completed tasks vs. total, current blockers (if any), and the date of the last log entry.

A pure **read/report** action — it produces no artifact and maps to **no canonical SDLC stage** (it is project-status tracking, not a lifecycle step, analogous to how [[gstack-landing-report]] or [[gstack-health]] are read-only status surfaces). It exists to make the pack's living state legible on demand, which is why it applies [[pattern-session-handoff]]: the summary is the "where are we?" snapshot used at review time or when handing the task to a teammate or a fresh agent.

## See Also
- [[nano-spec-create]] — creates the pack this reports on; [[nano-spec-update]] — mutates it.
- [[artifact-nano-spec-pack]] — the source it reads (`todo.md` + `log.md`).
- [[pattern-session-handoff]] — the pattern this serves (surfacing state across a boundary).
- [[nano-spec]] — the parent framework. </content>
