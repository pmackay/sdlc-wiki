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

# /context-save

`/context-save` — save working context: git state, decisions made, and remaining work. With **continuous checkpoint mode** (`gstack-config set checkpoint_mode continuous`), skills also auto-commit as you go with a `WIP:` prefix and a structured `[gstack-context]` body (decisions, remaining work, failed approaches) — surviving crashes and context switches. Local by default; push is opt-in.

gstack's member of the **session-handoff** cluster ([[pattern-session-handoff]]) — compact context across a session/agent boundary — alongside Matt Pocock's [[mp-handoff]]. Its restore counterpart is [[gstack-context-restore]]. gstack becomes the **third framework** (with GSD + MP) evidencing the pattern.

## See Also
- [[gstack-context-restore]] — reconstructs session state from the saved context / WIP commits.
- [[mp-handoff]] — Matt Pocock's handoff-document counterpart.
- [[pattern-session-handoff]] — the technique.
- [[stage-implement]] — the stage this supports (work continuity).
