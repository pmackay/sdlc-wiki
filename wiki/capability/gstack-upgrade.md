---
type: capability
subtype: command
belongs_to: "[[gstack]]"
implements: []
delegates_to: []
produces: []
applies: []
equivalent_to: []
sources: "gstack — Garry Tan (2026)"
raw: ["../../raw/gstack/2026-07-05-gstack-framework.md"]
updated: 2026-07-05
---

# /gstack-upgrade

`/gstack-upgrade` — the **Self-Updater**. Upgrades gstack to the latest version: detects a global vs
vendored install, syncs both, and shows what changed. (Team mode auto-updates silently once/hour, so
this is the manual path.)

**Meta-tooling** — it maintains gstack itself, not the user's software, so it carries no
`implements:` edge and belongs to no lifecycle stage. Catalogued for completeness.

## See Also
- [[gstack-router]] — the suite this keeps current.
