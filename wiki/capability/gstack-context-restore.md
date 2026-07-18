---
type: capability
subtype: command
belongs_to: "[[gstack]]"
implements: "[[stage-implement]]"
delegates_to: []
produces: []
applies: ["[[pattern-session-handoff]]"]
equivalent_to: ["[[mp-handoff]]"]
sources: "gstack — Garry Tan (2026)"
raw: ["../../raw/gstack/2026-07-05-gstack-framework.md"]
updated: 2026-07-05
---

# /context-restore

`/context-restore` — resume from a context saved earlier by [[gstack-context-save]], **even across Conductor workspaces**. Reads the saved decisions/remaining-work and the `WIP:` checkpoint commits (their `[gstack-context]` bodies) to reconstruct session state after a crash or a context switch.

The consuming half of gstack's [[pattern-session-handoff]] loop; enables the 10-15-parallel-sprint workflow to survive interruptions. Clusters with Matt Pocock's [[mp-handoff]].

## See Also
- [[gstack-context-save]] — writes the context this restores.
- [[mp-handoff]] — the session-handoff counterpart.
- [[stage-implement]] — the stage this supports (work continuity).
