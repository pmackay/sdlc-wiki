---
type: capability
subtype: command
belongs_to: "[[beads]]"
implements: []
produces: []
applies: []
equivalent_to: ["[[seeds-show]]"]
sources: "gastownhall/beads — README + docs/core-concepts + docs/CLI_REFERENCE.md (MIT, 2026)"
raw: ["../../raw/beads/2026-08-31-beads.md"]
updated: 2026-08-31
---

# bd show

`bd show <id>` — full bead detail plus its audit trail: fields, typed dependency edges, labels, comments, metadata, and the version history behind it. `--json` is the agent path, and the docs recommend narrowing it — `bd show <id> --json | jq '.[0] | {id,title,metadata,description,notes}'` — precisely so an agent reads the structured execution metadata before the prose.

Two relatives share the page: `bd children` lists the child beads of a parent (the hierarchy view, complementing [[beads-epic]]), and `bd history` shows the version history of one bead, which exists because every write is a Dolt commit — a per-issue changelog nobody had to build.

A pure **read** command; maps to **no canonical SDLC stage**.

## See Also
- [[beads-list]] · [[beads-query]] — the plural and filtered reads.
- [[beads-graph]] — the same relationships rendered as a graph.
- [[beads-vc]] — the database-wide version-control view `bd history` is a slice of.
