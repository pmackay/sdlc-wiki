---
type: capability
subtype: command
belongs_to: "[[beads]]"
implements: []
produces: []
applies: []
equivalent_to: ["[[seeds-label]]"]
sources: "gastownhall/beads — README + docs/core-concepts + docs/CLI_REFERENCE.md (MIT, 2026)"
raw: ["../../raw/beads/2026-08-31-beads.md"]
updated: 2026-08-31
---

# bd label

`bd label add|remove|list|list-all|propagate` (with `bd tag` as an alias for `add`) — labels, normalized and queryable, filterable on every read command.

**`bd label propagate`** is the one worth noting: it pushes a label from a parent bead to all its children. In a hierarchy that agents extend over weeks, a label applied to an epic after its children exist would otherwise be invisible to any query filtering on it — a small operation that only makes sense in a store with durable structure.

Labels also carry semantics elsewhere in the tool rather than being purely decorative: the `human` label is what [[beads-human]] queries, the `template` label marks a proto ([[beads-cook]]), and `bd set-state` maintains a state dimension as a label plus an event ([[beads-update]]).

Maps to **no canonical SDLC stage**.

## See Also
- [[beads-list]] — where labels are consumed as filters.
- [[beads-human]] — the label with special meaning.
- [[beads-cook]] — the `template` label on protos.
