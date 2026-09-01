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

# sd stats

`sd stats` — project-level counts across the store: totals by status, type, and priority, with `--json` and the shared `--format` set for machine consumption.

A read-only status surface, the counterpart of [[gstack-landing-report]] or [[nano-spec-status]] elsewhere in the wiki: it makes the queue's shape legible on demand (how much is open, how much is blocked, where the P0s are) without advancing anything. Maps to **no canonical SDLC stage**.

## See Also
- [[seeds-block]] — `sd blocked`, the detail view behind the blocked count.
- [[seeds-list]] — the itemized view.
- [[seeds-doctor]] — the health counterpart: integrity rather than volume.
