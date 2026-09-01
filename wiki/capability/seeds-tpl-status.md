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

# sd tpl status

`sd tpl status <id>` — convoy completion status for a poured template: total steps, completed, in progress, blocked, and the issue ids in step order.

A read-only progress surface over work that [[seeds-tpl-pour]] created, and the counterpart of [[seeds-plan-show]] on the convoy side. Because a convoy is only a shared tag over serially-blocked issues, the status is derived from the issues themselves — there is no convoy record to fall out of sync.

Maps to **no canonical SDLC stage**.

## See Also
- [[seeds-tpl-pour]] — creates the convoy this reports on.
- [[seeds-stats]] — the project-wide aggregate.
- [[nano-spec-status]] — the same read-only progress role in another framework.
