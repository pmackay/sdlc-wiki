---
type: capability
subtype: command
belongs_to: "[[beads]]"
implements: []
produces: []
applies: ["[[pattern-deterministic-gates]]"]
equivalent_to: []
sources: "gastownhall/beads — README + docs/core-concepts + docs/CLI_REFERENCE.md (MIT, 2026)"
raw: ["../../raw/beads/2026-08-31-beads.md"]
updated: 2026-08-31
---

# bd graph

`bd graph` — render the dependency graph, and `bd graph check` — verify its integrity. `bd dep tree` is the same data as an indented tree.

`graph check` is the [[pattern-deterministic-gates]] instance: a program-decided verdict over the store's structural invariants (cycles, dangling references, orphaned edges) with an exit code. It sits alongside [[beads-doctor]] as one of the four checks beads runs on itself — the others being [[beads-lint]] on issue content and [[beads-preflight]] on the working tree.

`bd recompute-blocked` is the repair to `graph check`'s diagnosis: it recomputes the `is_blocked` flag across the database, *"repairing stale flags after a pull"* — a real failure mode when a Dolt merge lands edges whose derived state was computed elsewhere. It is documented with [[beads-migrate]].

Maps to **no canonical SDLC stage**.

## See Also
- [[beads-dep]] — the edges being rendered and checked.
- [[beads-doctor]] — the broader health command.
- [[pattern-deterministic-gates]] — the pattern `graph check` applies.
