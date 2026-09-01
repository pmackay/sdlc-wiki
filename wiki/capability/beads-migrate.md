---
type: capability
subtype: command
belongs_to: "[[beads]]"
implements: []
produces: []
applies: []
equivalent_to: []
sources: "gastownhall/beads — docs/CLI_REFERENCE.md (MIT, 2026)"
raw: ["../../raw/beads/2026-08-31-beads.md"]
updated: 2026-08-31
---

# bd migrate

`bd migrate schema|hooks|sync|issues` — the migration surface, plus `bd rename` (rename a bead id), `bd rename-prefix` (rename the prefix across a whole database), and `bd recompute-blocked` (repair stale `is_blocked` flags after a pull).

**Schema migration is the tax on choosing a real database**, and beads pays it visibly. `bd migrate schema` applies pending migrations idempotently; a **schema-version guard** refuses to open a database that a newer binary has migrated ahead of the current one, with an actionable error rather than *"column X could not be found in any table in scope"*; and `BD_IGNORE_SCHEMA_SKEW=1` is the documented escape hatch. On a remote-backed database the upgrade choreography is explicit: *"exactly one designated clone runs `bd migrate` and `bd dolt push`; other clones install the new binary and run `bd bootstrap`."*

That paragraph has no counterpart in [[seeds]], and it is the strongest single argument for the JSONL side of the layer's [storage disagreement](../store/index.md#what-the-matrix-shows): plain files have no schema to migrate, no version to guard, and no designated-clone protocol. The counter-argument is on beads' side of the same page — schemas are what make `bd sql`, `bd query`, typed edges, and cell-level merge possible at all.

`bd migrate hooks` moves pre-existing git hooks to the marker-managed format (`--dry-run` previews; [[beads-doctor]] `--fix` is the apply path), `bd migrate sync` sets up the `sync.branch` workflow for multi-clone setups, and `bd migrate issues` moves beads between repositories ([[beads-repo]]).

Maps to **no canonical SDLC stage**.

## See Also
- [[beads-dolt]] — the engine whose schema this migrates.
- [[beads-upgrade]] — the binary-side half of the same problem.
- [[beads-backup]] — run first.
- [[seeds]] — the store with no schema to migrate.
