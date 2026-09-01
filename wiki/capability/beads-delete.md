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

# bd delete

`bd delete <id>` — delete beads and clean up the references pointing at them. Three bulk siblings share the page: `bd prune` (*"permanently delete closed non-ephemeral beads"* to reclaim space and shrink exports), `bd purge` (delete closed **ephemeral** beads — the wisp reaper), and `bd admin cleanup` (delete closed issues to reduce database size).

Deletion needs a whole family here for a reason unique to this layer: a store that several agents append to for months **grows without bound**, and every byte of it is in the context an agent might pull. Beads is the only tool in this wiki that treats forgetting as a feature rather than an omission — `--ephemeral` beads and wisps are *born* deletable ([[beads-mol]]), `bd purge` collects them, and semantic compaction summarizes the rest ([[beads-compact]]).

The distinction between the three is the ephemerality flag, and it is worth keeping straight: `prune` removes durable closed work (irreversible history loss), `purge` removes work that was never meant to persist (routine hygiene).

Maps to **no canonical SDLC stage**.

## See Also
- [[beads-compact]] — the alternative to deleting: summarize and keep.
- [[beads-mol]] — wisps, the ephemeral lifecycle `purge` serves.
- [[beads-backup]] — take one before pruning.
