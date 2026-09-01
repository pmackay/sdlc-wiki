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

# bd jira

`bd jira pull|push|sync|status` — the two-way bridge to Jira.

Beads' charter keeps every bridge on a short leash: *"Tracker integrations are adoption bridges, not a second product surface. They should map external tracker data into beads concepts and keep the dependency graph useful. They should not replicate tracker UIs, notification systems, credential vaults, webhook gateways, or cross-tracker automation."*

Jira is the bridge that most tests that boundary, because it is the tracker with the most concepts that have no beads equivalent — workflows and transitions, sprints and boards, custom fields, permission schemes, epics-as-issue-links. The charter's answer is `metadata`: per-integration data goes in the opaque per-issue bag first, and *"promote metadata to first-class schema only when the field has broad, durable meaning for beads itself."* So a Jira-only field survives the round trip without becoming part of beads' model.

The practical consequence is worth stating plainly: this bridge preserves *what beads needs* — identity, status, priority, assignment, and the dependency edges that make [[beads-ready]] work — and does not attempt to be a Jira client. An agent gets a usable graph; a human keeps their board.

Maps to **no canonical SDLC stage**.

## See Also
- [[beads-update]] — `--metadata`, where non-mapping fields land.
- [[beads-github]] · [[beads-gitlab]] · [[beads-linear]] · [[beads-ado]] · [[beads-notion]] — the sibling bridges.
