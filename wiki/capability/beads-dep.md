---
type: capability
subtype: command
belongs_to: "[[beads]]"
implements: []
produces: []
applies: []
equivalent_to: ["[[seeds-dep]]"]
sources: "gastownhall/beads — README + docs/core-concepts + docs/CLI_REFERENCE.md (MIT, 2026)"
raw: ["../../raw/beads/2026-08-31-beads.md"]
updated: 2026-08-31
---

# bd dep

`bd dep add|remove|list|tree|relate|unrelate|cycles` (plus `bd link` as a shorthand) — the typed dependency edges that make beads a graph rather than a list. Edges are stored on both endpoints, so traversal is cheap either way, and `bd dep cycles` exists because a graph an agent edits will eventually contain one.

**The typing is the distinctive part** — beads has five edge kinds and only some of them gate work:

| Edge | Meaning | Gates ready work |
|---|---|---|
| `blocks` | hard ordering | **yes** |
| `parent-child` | epic / subtask structure | indirectly (a blocked parent blocks its children) |
| `discovered-from` | provenance: found while working on the parent | no |
| `related` | soft association | no |
| `conditional-blocks` · `waits-for` | workflow-step gating ([[beads-gate]]) | yes |

That distinction solves a real problem [[seeds-dep]] runs into with its single edge type, where its own docs have to warn that *"every unnecessary `sd dep add` hides the work from `sd ready`"*. In beads you can record that a bug was `discovered-from` a refactor, or that two beads are `related`, without removing anything from the frontier. Provenance and schedulability are separate concerns, separately expressed.

Cross-repo edges use an external reference: `bd dep add bd-42 external:other-repo:api-ready` ([[beads-repo]]).

Maps to **no canonical SDLC stage**: an edge records an ordering constraint; it does not perform the planning that decided it. (This is where beads and [[seeds]] part company — seeds files its dependency commands under [[stage-plan]] because sequencing is part of its planning methodology; beads' charter keeps the sequencing primitive and the planning policy apart.)

## See Also
- [[beads-ready]] — the query these edges gate.
- [[beads-graph]] — visualize and integrity-check them.
- [[beads-supersede]] — the non-gating knowledge links.
- [[beads-epic]] — the `parent-child` view.
