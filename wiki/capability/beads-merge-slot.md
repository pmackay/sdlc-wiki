---
type: capability
subtype: command
belongs_to: "[[beads]]"
implements: []
produces: []
applies: ["[[pattern-trunk-based-development]]"]
equivalent_to: []
sources: "gastownhall/beads — docs/workflows + docs/CLI_REFERENCE.md (MIT, 2026)"
raw: ["../../raw/beads/2026-08-31-beads.md"]
updated: 2026-08-31
---

# bd merge-slot

`bd merge-slot create|acquire|check|release` — *"manage merge-slot gates for serialized conflict resolution"*: a mutual-exclusion lock, expressed as a bead.

Parallel agents can work in isolated worktrees all day, but they cannot all merge to trunk at once without fighting over the same conflicts. The merge slot is a single bead that one worker **acquires**, holds while it lands its change, and **releases**; everyone else's merge step is blocked until then. `bd merge-slot check` reports availability without taking it.

It is the same move as [[beads-gate]] — coordination as a graph property rather than as a running service — applied to exclusion rather than to waiting, and it has the same payoff: no lock server, no lease timeouts to tune, and the lock's state is as durable, auditable, and syncable as everything else in the store. It also has the same failure mode: a worker that dies holding the slot leaves it held, and nothing but [[beads-doctor]] or a human will notice.

Together with hash IDs (no renumbering on merge) and Dolt's cell-level merge, this is beads' answer to the multi-writer problem at the *code* level rather than the *database* level — the tracker is fine with concurrent writes; it is trunk that needs serializing.

Maps to **no canonical SDLC stage**.

## See Also
- [[beads-gate]] — the same primitive for waiting rather than excluding.
- [[beads-worktree]] — the isolation the slot serializes at the end of.
- [[beads-swarm]] — the parallel dispatch that creates the contention.
- [[pattern-trunk-based-development]] — the practice this protects.
