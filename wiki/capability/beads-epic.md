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

# bd epic

`bd epic status` — completion status for an epic and its children; `bd epic close-eligible` — close epics whose children are all complete. `bd children` lists one level, and `bd flatten` (documented with [[beads-compact]]) squashes structure away.

Beads expresses hierarchy twice over, which is unusual: as `parent-child` dependency edges, *and* in the identifier itself — `bd-a3f8` (epic) → `bd-a3f8.1` (task) → `bd-a3f8.1.1` (sub-task). The hierarchical ID means an agent can see the structure without a graph query, and the docs note the practical effect on the ready frontier: a blocked parent blocks its children, so an epic is a real gate rather than a label.

`close-eligible` is a small piece of automation with a specific target: epics that stay open forever because nobody noticed the last child closed. It is the epic-level twin of `bd orphans` ([[beads-list]]) — both find work that is done but not recorded as done.

Maps to **no canonical SDLC stage**.

## See Also
- [[beads-swarm]] — turns a validated epic into a parallel-dispatch molecule.
- [[beads-dep]] — the `parent-child` edge.
- [[beads-mol]] — the templated way to create a whole hierarchy at once.
