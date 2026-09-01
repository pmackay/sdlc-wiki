---
type: capability
subtype: command
belongs_to: "[[beads]]"
implements: []
produces: []
applies: []
equivalent_to: ["[[seeds-upgrade]]", "[[gstack-upgrade]]"]
sources: "gastownhall/beads — docs/CLI_REFERENCE.md (MIT, 2026)"
raw: ["../../raw/beads/2026-08-31-beads.md"]
updated: 2026-08-31
---

# bd upgrade

`bd upgrade status|review|ack` — version management for the tool itself: has the binary changed, what changed since the version you last acknowledged, and mark the current one seen. `bd info --whats-new` prints the release notes.

`bd upgrade review` is the part with an idea in it. Rather than only checking for a newer version, it reports *changes since the version this workspace last acknowledged* — so an agent (or a human) returning to a project after a gap is told what moved underneath them, and `ack` records that they were told. For a tool an agent invokes dozens of times per session and whose behaviour is load-bearing, silent version drift is a real hazard, and beads makes noticing it a command rather than a habit.

The upgrade path is genuinely more involved than replacing a binary, which is why it gets this surface: *"sync remote-backed databases with your current `bd`, back up with `bd export --all`, upgrade the binary, then run `bd info --whats-new`, `bd hooks install`, and `bd version`"* — and if the upgrade crosses a schema migration, the designated-clone protocol in [[beads-migrate]] applies.

Maps to **no canonical SDLC stage**. Its counterparts elsewhere — [[seeds-upgrade]] and [[gstack-upgrade]] — are plain self-updaters; only beads has a stateful database to drag along.

## See Also
- [[beads-migrate]] — the schema half of an upgrade.
- [[beads-doctor]] — run after; it detects post-upgrade drift.
- [[seeds-upgrade]] · [[gstack-upgrade]] — the simpler counterparts.
