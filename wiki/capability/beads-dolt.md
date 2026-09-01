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

# bd dolt

`bd dolt remote|push|pull|start|stop|status|test|commit|show|set|killall|clean-databases` — the storage-engine surface, plus `bd sql` for raw queries and `bd ping` for connectivity.

**Sync is the load-bearing part.** `bd dolt push` / `pull` move commits against `refs/dolt/data` **on your existing git remote** — a separate ref namespace from normal git refs, so the work graph travels with the repository without touching branches or triggering protected-branch rules, and there is no server to provision. That is the single design choice that makes a versioned SQL database practical as a per-project tracker.

Two storage modes: **embedded** (default, Dolt in-process, `.beads/embeddeddolt/`, one file-locked writer) and **server** (`bd init --server`, an external `dolt sql-server`, `.beads/dolt/`, many concurrent writers). `start` / `stop` / `killall` / `clean-databases` exist for the second — and their existence *is* the cost side of the Dolt bet: orphan server processes and stale test databases are failure modes plain files do not have.

`bd sql` runs raw SQL against the database, documented as *"useful for debugging, maintenance, and working around bugs in higher-level commands"* — an escape hatch that only a real database can offer, and the flip side of [[seeds]]' argument that a binary store is opaque. A beads database can be queried in ways its CLI never anticipated.

Beads keeps this surface behind a boundary rather than in its bones: the charter forbids beads from becoming a storage engine, and a `depguard` rule mechanically denies `github.com/dolthub/` imports outside `internal/storage/`.

Maps to **no canonical SDLC stage**.

## See Also
- [[beads-vc]] — the version-control operations on top of this engine.
- [[beads-export]] — the JSONL interchange format, which is *not* the sync mechanism.
- [[beads-migrate]] — schema migrations, the other cost of a real database.
- [[seeds]] — the store that rejected this whole approach; the disagreement is on both pages.
