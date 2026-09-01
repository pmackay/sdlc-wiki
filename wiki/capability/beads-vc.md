---
type: capability
subtype: command
belongs_to: "[[beads]]"
implements: []
produces: []
applies: []
equivalent_to: []
sources: "gastownhall/beads — docs/CLI_REFERENCE.md + docs/multi-agent + docs/architecture (MIT, 2026)"
raw: ["../../raw/beads/2026-08-31-beads.md"]
updated: 2026-08-31
---

# bd vc

`bd vc commit|merge|status` plus `bd branch` and `bd diff` — version control **over the work data itself**, not over the code.

This is what a versioned database buys and it has no counterpart anywhere else in the wiki. You can branch the issue graph, merge it, diff two commits or branches, and read the history of a single bead ([[beads-show]]). Every write auto-commits (one Dolt commit per write command), so the history exists whether or not anyone curates it, and `bd vc status` reports the current branch and uncommitted changes exactly as git would.

Conflicts are *"rare with hash IDs"* — because ids are content-derived, two branches that each added work merge additively — and where cells do collide, Dolt resolves with **cell-level three-way merge** rather than line-level. Compare [[seeds]]' answer to the same problem: `merge=union` on append-only JSONL plus dedup-on-read, which is dramatically simpler and cannot merge two edits to the same field.

The genuinely novel affordance is branching the tracker *with* the code: a feature branch can carry its own beads, and merging the branch merges the work graph. No hosted tracker can do that, and it is the clearest illustration of why beads calls itself *distributed*.

Maps to **no canonical SDLC stage**.

## See Also
- [[beads-dolt]] — the engine underneath, and the sync that moves these commits.
- [[beads-compact]] — pruning the history this produces.
- [[beads-show]] — per-bead history, a slice of this.
