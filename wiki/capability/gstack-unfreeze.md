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

# /unfreeze

`/unfreeze` — clear the edit boundary set by [[gstack-freeze]] (or [[gstack-guard]]), allowing edits to all directories again. The release valve for gstack's [[pattern-edit-guardrails]].

## See Also
- [[gstack-freeze]] — the lock this clears.
- [[gstack-guard]] — the combined safety mode whose freeze half this releases.
- [[stage-implement]] — the stage these guardrails protect.
