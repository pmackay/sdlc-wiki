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

# bd export

`bd export` / `bd import` — JSONL out and in, for viewers, interchange, and migration between backends.

The documentation is unusually insistent about what this is *not*: `.beads/issues.jsonl` is *"a passive export for viewers and interchange — **it is not the database, not the sync protocol, and not a backup**."* Sync is [[beads-dolt]]; backup is [[beads-backup]]. The warning exists because the file looks exactly like a source of truth, and because an earlier design *did* round-trip through it — beads' post-merge git hook still carries *"a legacy JSONL import fallback, only when no Dolt remote is configured."*

That single sentence is also the crux of the layer's internal disagreement. [[seeds]]' case against beads cites a *"dual source of truth — binary DB + JSONL export, manually kept in sync"*; beads' answer is to demote the export to an artifact nobody is required to reconcile. Whether that resolves the objection or relocates it is a fair question, and one the wiki leaves open — but the JSONL file that seeds made *the* database is, in beads, deliberately the least authoritative thing in `.beads/`.

`bd export --all` is the documented pre-upgrade safety step, and `bd migrate issues` moves beads between repositories ([[beads-repo]]).

Maps to **no canonical SDLC stage**.

## See Also
- [[beads-dolt]] — the actual sync mechanism.
- [[beads-backup]] — the actual backup mechanism.
- [[seeds]] — where this same file format is the source of truth.
