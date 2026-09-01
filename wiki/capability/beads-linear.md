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

# bd linear

`bd linear pull|push|sync|status|teams` — the two-way bridge to Linear, with `teams` listing the available teams (Linear's routing unit, the analogue of a GitHub repo or GitLab project).

Beads' charter keeps every bridge on a short leash: *"Tracker integrations are adoption bridges, not a second product surface. They should map external tracker data into beads concepts and keep the dependency graph useful. They should not replicate tracker UIs, notification systems, credential vaults, webhook gateways, or cross-tracker automation."*

Linear is the closest external tracker to beads' own model — typed issues, explicit relations, a project hierarchy — so the mapping loses least here. It is also the tracker most likely to be *already* driven by agents through its own API, which makes the bridge a genuine choice rather than a migration aid: either the agent talks to Linear directly, or it works against a local graph that syncs. The case for the second is everything on the [[beads]] page — offline operation, branchable work data, gates, ephemeral work, and a `bd ready` frontier that costs one local query instead of a network round trip per poll.

Maps to **no canonical SDLC stage**.

## See Also
- [[beads-ready]] — the local-frontier argument for syncing rather than calling out.
- [[beads-github]] · [[beads-gitlab]] · [[beads-jira]] · [[beads-ado]] · [[beads-notion]] — the sibling bridges.
