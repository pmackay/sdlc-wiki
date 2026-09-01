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

# bd backup

`bd backup init|sync|status|remove|restore` (plus top-level `bd restore` for un-compacting a single bead) — a configured Dolt backup destination, pushed to on demand, with status reporting and a restore path.

Backup is a distinct command family from sync ([[beads-dolt]]) and from export ([[beads-export]]) because the three answer different questions — where the data lives for other machines, what it looks like for other tools, and what happens when it is gone. The docs route several irreversible operations through here first: `bd backup` is the documented step before mode migration, and before `bd flatten` or `bd prune` destroy history ([[beads-compact]], [[beads-delete]]).

Its presence is part of what makes the [store layer](../store/index.md) a real operational concern rather than a filing convention: once the work graph is the thing that survives sessions, losing it is worse than losing a session, and *"back up with `bd export --all`, upgrade the binary, then `bd info --whats-new`"* is a real runbook a tracker needs and a markdown TODO list does not.

Maps to **no canonical SDLC stage**.

## See Also
- [[beads-dolt]] — sync, which is not backup.
- [[beads-compact]] · [[beads-delete]] — the destructive operations to back up before.
- [[beads-migrate]] — the upgrade path this protects.
