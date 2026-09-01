---
type: capability
subtype: command
belongs_to: "[[beads]]"
implements: []
produces: []
applies: []
equivalent_to: ["[[seeds-search]]"]
sources: "gastownhall/beads — README + docs/core-concepts + docs/CLI_REFERENCE.md (MIT, 2026)"
raw: ["../../raw/beads/2026-08-31-beads.md"]
updated: 2026-08-31
---

# bd query

`bd query` — *"query issues using a simple query language that supports compound filters, boolean operators, and date-relative expressions"*, the escape hatch when [[beads-list]]'s flags stop composing. `bd search <text>` is the plain text search beside it.

Three duplicate-detection commands share the page because they are one idea: `bd find-duplicates` finds *semantically similar* beads *"using text analysis or AI"*, `bd duplicates` finds and optionally merges them, and `bd duplicate <a> <b>` marks one as a duplicate of another — which is a knowledge-graph link, not a deletion ([[beads-supersede]]).

Duplicate detection earns its place in a store rather than a framework: a work graph that several agents append to over months accumulates near-identical beads, and nothing upstream prevents it. This is the tracker maintaining its own signal-to-noise.

`bd sql` — raw SQL against the underlying database, *"useful for debugging, maintenance, and working around bugs in higher-level commands"* — is the unrestricted version of this surface, and is documented with [[beads-dolt]].

Maps to **no canonical SDLC stage**.

## See Also
- [[beads-list]] — the flag-based read.
- [[beads-supersede]] — where a confirmed duplicate link lands.
- [[beads-dolt]] — the raw SQL surface underneath.
