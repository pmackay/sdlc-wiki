---
type: capability
subtype: command
belongs_to: "[[beads]]"
implements: []
produces: []
applies: []
equivalent_to: []
sources: "gastownhall/beads — README + docs/core-concepts + docs/CLI_REFERENCE.md (MIT, 2026)"
raw: ["../../raw/beads/2026-08-31-beads.md"]
updated: 2026-08-31
---

# bd supersede

`bd supersede <old> <new>` — mark a bead as superseded by a newer one; with `bd duplicate` and `bd dep relate`, this is beads' **knowledge-graph link** surface: `relates-to`, `duplicates`, `supersedes`, `replies-to`.

These four carry meaning **without affecting schedulability** — a distinction beads draws deliberately and no other tool here draws at all. The result is that one database is simultaneously a work queue and a record of how the work relates: why this bead replaced that one, which two are the same question, which comment answers which ([[beads-comment]]'s `--thread` uses `replies-to`). A framework would write that history in a markdown document that rots; a store keeps it queryable next to the work.

`replies-to` is the load-bearing one for [[beads-mail]]: threaded messages are beads linked by reply edges, which is how beads gets agent-to-agent messaging without a message bus.

Maps to **no canonical SDLC stage**.

## See Also
- [[beads-dep]] — the gating edges these sit beside.
- [[beads-query]] — duplicate detection, which produces `duplicates` links.
- [[beads-mail]] — the threading built on `replies-to`.
