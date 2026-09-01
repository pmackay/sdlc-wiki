---
type: capability
subtype: command
belongs_to: "[[beads]]"
implements: []
produces: []
applies: ["[[pattern-context-engineering]]"]
equivalent_to: []
sources: "gastownhall/beads — docs/workflows + docs/CLI_REFERENCE.md (MIT, 2026)"
raw: ["../../raw/beads/2026-08-31-beads.md"]
updated: 2026-08-31
---

# bd compact

`bd compact` · `bd admin compact` · `bd flatten` · `bd gc` — the forgetting machinery, and two genuinely different operations that share a name.

**Semantic compaction** (`bd admin compact`) is the interesting one: it *summarizes old closed issues* to save context window — the README calls it *"semantic 'memory decay'"*, and `bd restore` brings back the pre-compaction content of a compacted issue. A closed bead from four months ago still costs tokens whenever an agent lists or searches near it; compaction replaces the detail with a summary and keeps the graph intact.

**History compaction** (`bd compact`) is storage hygiene over Dolt: because every write auto-commits, a busy database accumulates commits fast, so this squashes those older than `--days` (default 30) into a single base commit, cherry-picks the recent ones back on top, and runs Dolt GC. `bd flatten` is the extreme version — squash *all* history into one commit — and `bd gc` runs the whole sweep: decay old issues, compact commits, GC.

Together they are the answer to the obvious objection to this whole layer: **a store that never forgets eventually costs more context than it saves.** Beads is the only tool in the wiki that treats that as a first-class problem, with three mechanisms — compaction here, the ephemeral phase in [[beads-mol]], and deletion in [[beads-delete]] — and one honest trade: `flatten` and `prune` destroy history that `bd history` and `bd diff` were the reason for keeping.

Maps to **no canonical SDLC stage**.

## See Also
- [[beads-prime]] — the consumer of the context budget this protects.
- [[beads-delete]] — deleting instead of summarizing.
- [[beads-backup]] — take one first; `flatten` is irreversible.
- [[pattern-context-engineering]] — the pattern it serves.
