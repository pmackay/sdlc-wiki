---
type: capability
subtype: command
belongs_to: "[[beads]]"
implements: []
produces: []
applies: []
equivalent_to: []
sources: "gastownhall/beads — docs/CLI_REFERENCE.md + docs/multi-agent + docs/architecture (MIT, 2026)"
raw: ["../../raw/beads/2026-08-31-beads.md"]
updated: 2026-08-31
---

# bd repo

`bd repo add|list|remove|sync` — multi-repository configuration, plus the two features built on it: **routing** and **cross-repo dependencies**. `bd migrate issues` moves beads between repositories; `bd ship` *"publishes a capability for cross-project dependencies"*.

**Routing** decides which repository a new bead lands in, from your role and the `routing.*` config keys (an explicit `--repo` always wins). The role split is the practically useful part, and it is aimed squarely at open-source work:

- **Contributors** (`bd init --contributor`) route planning issues to a separate repo, e.g. `~/.beads-planning` — *"keeps experimental work out of PRs."*
- **Maintainers** are auto-detected from SSH URLs or credentialed HTTPS.

That solves a problem the whole store layer creates: if the tracker lives *in* the repo, then an agent's speculative planning beads want to be committed to a repo the agent does not own. Beads' answer is to make the destination a routing decision rather than a fact about where you are standing. [[seeds]] has no equivalent, and `bd init --stealth` covers the same ground more bluntly — use beads locally without committing anything to the shared repo.

**Cross-repo dependencies** use an external reference: `bd dep add bd-42 external:other-repo:api-ready`. So a frontend bead can block on a backend capability, and `bd ship` is how the providing side declares that capability exists to be depended on.

Maps to **no canonical SDLC stage**.

## See Also
- [[beads-federation]] — the cross-organization case.
- [[beads-dep]] — the edges that go external.
- [[beads-init]] — `--contributor` and `--stealth`, the two routing postures.
- [[beads-config]] — where `routing.*` lives.
