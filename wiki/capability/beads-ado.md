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

# bd ado

`bd ado pull|push|sync|status|projects` — the two-way bridge to Azure DevOps work items, with `projects` listing accessible projects.

Beads' charter keeps every bridge on a short leash: *"Tracker integrations are adoption bridges, not a second product surface. They should map external tracker data into beads concepts and keep the dependency graph useful. They should not replicate tracker UIs, notification systems, credential vaults, webhook gateways, or cross-tracker automation."*

Its presence is mostly an adoption signal: Azure DevOps is enterprise ground, and a tool whose pitch is *"persistent memory for coding agents"* reaching there suggests the layer is being adopted inside organizations that will not move their tracker for any agent. That is the charter's thesis about bridges made concrete — the store has to meet the work where it already is.

Maps to **no canonical SDLC stage**.

## See Also
- [[beads-github]] · [[beads-gitlab]] · [[beads-jira]] · [[beads-linear]] · [[beads-notion]] — the sibling bridges.
- [[beads-repo]] — multi-repo routing, the other feature aimed at larger organizations.
