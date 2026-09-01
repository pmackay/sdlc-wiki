---
type: capability
subtype: command
belongs_to: "[[beads]]"
implements: []
produces: []
applies: []
equivalent_to: ["[[seeds-close]]"]
sources: "gastownhall/beads — README + docs/core-concepts + docs/CLI_REFERENCE.md (MIT, 2026)"
raw: ["../../raw/beads/2026-08-31-beads.md"]
updated: 2026-08-31
---

# bd close

`bd close <id> [<id>…] --reason "…"` — close one or more beads, and `bd reopen` to walk one back. Closing is what moves the graph: every bead listing this one in a blocking edge becomes eligible for [[beads-ready]] the moment the write commits.

Because every write auto-commits to Dolt, a close is also a point in version history — `bd history <id>` and `bd diff` can show it later, and the events journal records **who** performed it (an `actor` column stamped inside the mutating transaction). Beads therefore does not need a separate audit trail for issue state: the database *is* one, versioned.

`bd epic close-eligible` is the bulk cousin, closing epics whose children have all completed ([[beads-epic]]); `bd orphans` catches the opposite failure — work committed with a bead id in the commit message but never closed ([[beads-list]]).

Maps to **no canonical SDLC stage**.

## See Also
- [[beads-ready]] — the frontier this command feeds by releasing blockers.
- [[beads-show]] — the audit trail a close becomes part of.
- [[beads-delete]] — for removing rather than completing.
