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

# bd gitlab

`bd gitlab pull|push|sync|status|projects` — the two-way bridge to GitLab issues, shaped identically to [[beads-github]] with `projects` in place of `repos` (GitLab's own noun for the container).

Beads' charter keeps every bridge on a short leash: *"Tracker integrations are adoption bridges, not a second product surface. They should map external tracker data into beads concepts and keep the dependency graph useful. They should not replicate tracker UIs, notification systems, credential vaults, webhook gateways, or cross-tracker automation."*

The uniformity across all six bridges is the point rather than an accident: each one is `pull` / `push` / `sync` / `status` plus a discovery command, which means the mapping — external item to bead, with dependencies preserved — is the same code path with different adapters. That is what *"map external tracker data into beads concepts"* buys, and it is why the charter forbids per-tracker feature growth: the moment one bridge grows a GitLab-specific notion the others cannot express, the shared model is gone.

Maps to **no canonical SDLC stage**.

## See Also
- [[beads-github]] — the sibling bridge with the richest surrounding machinery.
- [[beads-jira]] · [[beads-linear]] · [[beads-ado]] · [[beads-notion]] — the other bridges.
