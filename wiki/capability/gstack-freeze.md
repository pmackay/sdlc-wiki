---
type: capability
subtype: command
belongs_to: "[[gstack]]"
implements: "[[stage-implement]]"
delegates_to: []
produces: []
applies: ["[[pattern-edit-guardrails]]"]
equivalent_to: []
sources: "gstack — Garry Tan (2026)"
raw: ["../../raw/gstack/2026-07-05-gstack-framework.md"]
updated: 2026-07-05
---

# /freeze

`/freeze` — **edit lock**. Restricts file edits to a single directory for the session — a **hard
block, not just a warning** — so the agent can't accidentally change code outside the current scope
while debugging or doing focused work. [[gstack-unfreeze]] clears the boundary;
[[gstack-investigate]] auto-freezes to the module under investigation.

The scope-lock half of gstack's [[pattern-edit-guardrails]] (the destructive-command-warning half
is [[gstack-careful]]; [[gstack-guard]] combines both). No cross-framework counterpart.

## See Also
- [[gstack-unfreeze]] — removes the freeze boundary.
- [[gstack-careful]] — the destructive-command guardrail.
- [[gstack-guard]] — careful + freeze together.
- [[gstack-investigate]] — auto-activates this to scope a debugging session.
- [[stage-implement]] — the stage these guardrails protect.
