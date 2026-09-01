---
type: capability
subtype: command
belongs_to: "[[beads]]"
implements: []
produces: []
applies: []
equivalent_to: []
sources: "gastownhall/beads — docs/CLI_REFERENCE.md + engdocs/INTEGRATION_CHARTER.md (MIT, 2026)"
raw: ["../../raw/beads/2026-08-31-beads.md"]
updated: 2026-08-31
---

# bd notion

`bd notion init|connect|pull|push|sync|status` — the bridge to Notion, and the only one of the six with **two** setup paths: `bd notion init` *"creates a dedicated Beads database in Notion"*, while `connect` attaches to an existing database or data source.

Beads' charter keeps every bridge on a short leash: *"Tracker integrations are adoption bridges, not a second product surface. They should map external tracker data into beads concepts and keep the dependency graph useful. They should not replicate tracker UIs, notification systems, credential vaults, webhook gateways, or cross-tracker automation."*

Notion is the outlier in the set because it is not a tracker — it is a document tool people *use* as a tracker, with no fixed schema. Hence `init`: rather than mapping onto whatever columns someone happened to create, beads can lay down a database shaped like its own model. That is a bridge that ships a schema, which sits closer to the charter's fence than the other five, and is defensible only because the alternative is guessing at an arbitrary Notion table.

It is also the bridge that most reveals what the store layer is competing with. A Notion board full of tasks *is* a work store — durable, shared, and outliving any session — just one with no dependency graph, no readiness computation, no atomic claim, and no API an agent can poll cheaply. Adding those four is roughly the whole value proposition of this layer, and this command is how a team keeps the human-facing surface they like while an agent gets the graph it needs.

Maps to **no canonical SDLC stage**.

## See Also
- [[beads-ready]] — the computation a Notion board cannot perform.
- [[beads-github]] · [[beads-gitlab]] · [[beads-jira]] · [[beads-linear]] · [[beads-ado]] — the sibling bridges.
- [The store layer](../store/index.md) — what a document tool used as a tracker is missing.
