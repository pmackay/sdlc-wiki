---
type: capability
subtype: command
belongs_to: "[[seeds]]"
implements: []
produces: []
applies: []
equivalent_to: []
sources: "Jaymin West — jayminwest/seeds README + AGENTS.md + SPEC.md (MIT, v0.5.15, 2026)"
raw: ["../../raw/seeds/2026-08-31-seeds.md"]
updated: 2026-08-31
---

# sd migrate-from-beads

`sd migrate-from-beads` — import `.beads/issues.jsonl` into `.seeds/`, the one-way door out of the tool seeds was written to replace.

The migration is cheap precisely because of the design argument behind seeds. Beads' problems were storage-shaped — a 2.8MB binary `beads.db` that cannot diff or merge, 286 export-state tracking files keeping a JSONL export in sync with it, lock contention between agents, and a dual source of truth — while its *data model* was fine, and seeds deliberately kept the `{project}-{4hex}` id format *"for familiarity, eases migration"*. So the importer reads the export beads was already producing and drops the machinery around it.

Maps to **no canonical SDLC stage** — data migration.

## See Also
- [[seeds-init]] — run first; this populates what it creates.
- [[seeds]] — the parent framework, whose *Why* section is the argument this command acts on.
