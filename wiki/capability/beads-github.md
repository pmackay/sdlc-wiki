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

# bd github

`bd github pull|push|sync|status|repos` — the two-way bridge to GitHub Issues. `repos` lists what you can reach, `pull` brings specific items in, `push` sends specific beads out, `sync` reconciles, `status` reports the state of the mapping.

Beads' charter keeps every bridge on a short leash: *"Tracker integrations are adoption bridges, not a second product surface. They should map external tracker data into beads concepts and keep the dependency graph useful. They should not replicate tracker UIs, notification systems, credential vaults, webhook gateways, or cross-tracker automation."*

Of the six bridges this is the one with the most other machinery around it, because beads already lives in a git repo. [[beads-gate]]'s `gh:run` and `gh:pr` types poll GitHub Actions and pull requests through `gh` to close a gate; [[beads-list]]'s `bd orphans` reads commit messages; [[beads-preflight]] checks PR readiness. So GitHub shows up in beads three separate ways — as a tracker to mirror (here), as an event source to wait on, and as the host of the repository the store lives inside.

The bridge answers the obvious objection to putting the tracker in the repo: a team's issues are already somewhere, and agents need the dependency graph regardless. Rather than asking anyone to migrate, beads mirrors — the graph gets built from work that continues to live where humans look at it. Compare [[speckit-taskstoissues]], which exports one-way from a task list, and [[gstack-spec]], which files a deduped GitHub issue as part of a lifecycle step; those are process-layer capabilities that *use* GitHub, while this is a store keeping two stores in step.

Maps to **no canonical SDLC stage**.

## See Also
- [[beads-gate]] — `gh:run` / `gh:pr` gates, the other GitHub touchpoint.
- [[beads-gitlab]] · [[beads-jira]] · [[beads-linear]] · [[beads-ado]] · [[beads-notion]] — the sibling bridges.
- [[artifact-issue]] — the shared concept the mapping preserves.
