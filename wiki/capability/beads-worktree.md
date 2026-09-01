---
type: capability
subtype: command
belongs_to: "[[beads]]"
implements: []
produces: []
applies: ["[[pattern-worktree-isolation]]"]
equivalent_to: ["[[sp-using-git-worktrees]]", "[[ce-worktree]]"]
sources: "gastownhall/beads — docs/CLI_REFERENCE.md (MIT, 2026)"
raw: ["../../raw/beads/2026-08-31-beads.md"]
updated: 2026-08-31
---

# bd worktree

`bd worktree create|list|info|remove` — *"manage git worktrees for parallel development"*, with safety checks on removal.

A tracker shipping worktree management looks like scope creep until you notice what makes it necessary. Beads' data lives in `.beads/` inside the repo; a git worktree is a second checkout of the same repository; so a naive worktree either shares the database (contention) or gets a stale copy (divergence). The docs' answer is that no special flags are needed — *"work directly with Dolt"* — and these commands exist to create the worktree with the store wired correctly and to refuse to remove one that still holds work.

That makes it the **store-side realization of [[pattern-worktree-isolation]]**, which is a fourth angle on a pattern that already had three. The process layer instructs an agent to work in a worktree ([[sp-using-git-worktrees]], [[ce-worktree]]); the runtime layer provisions isolation as substrate ([[warren]]'s `bwrap`, [[bernstein]]'s worktree-per-agent, [[sandcastle]]); and the store's contribution is making shared state *survive* the isolation — hash IDs that never collide, cell-level merge, and `bd recompute-blocked` to repair derived flags after the merge lands.

Isolation is only useful if the isolated agents can still see one queue. That is this layer's job.

Maps to **no canonical SDLC stage**.

## See Also
- [[beads-merge-slot]] — serializing the merges that isolated work produces.
- [[beads-vc]] — branching the work graph alongside the code branch.
- [[warren]] · [[bernstein]] · [[sandcastle]] — the runtime-side isolation.
- [[pattern-worktree-isolation]] — the shared pattern.
