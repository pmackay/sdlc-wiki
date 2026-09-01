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

# bd hooks

`bd hooks install|list|uninstall|run` — git hooks for beads integration, **embedded in the `bd` binary** so *"they work for all bd users, not just source repo users"*, installed as thin shims that call `bd hooks run`.

Two hooks, and the second is a fossil worth keeping:

- **pre-commit** — commits pending Dolt changes, so the work graph and the code land together in one human action.
- **post-merge** — runs chained hooks, plus *"a legacy JSONL import fallback **only when no Dolt remote is configured**"* — the vestige of the export-round-trip design that [[seeds]]' critique was aimed at, now gated off for anyone synced properly.

Hooks are the mechanism behind beads' commit convention: put the bead id in parentheses (`git commit -m "Fix auth validation bug (bd-abc)"`) and the store can cross-reference commits against open beads to find orphans ([[beads-list]], [[beads-doctor]]).

The shim-plus-marker design has its own migration story — `bd migrate hooks --dry-run` previews moving pre-existing hooks to the marker-managed format, and `bd doctor --fix` is the apply path ([[beads-migrate]]).

Maps to **no canonical SDLC stage**.

## See Also
- [[beads-setup]] — installs harness hooks; this installs git hooks.
- [[beads-doctor]] — detects and repairs hook drift.
- [[claude-code]] — the harness whose own hook system beads plugs `bd prime` into.
