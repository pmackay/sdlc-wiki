---
type: capability
subtype: skill
belongs_to: "[[pstack]]"
implements: []
delegates_to: []
produces: []
applies: []
equivalent_to: []
sources: "pstack v0.15.2 — Lauren Tan (2026)"
raw: ["../../raw/pstack/2026-09-11-pstack-plugin.md"]
updated: 2026-09-11
---

# principle-migrate-callers-then-delete-legacy-apis

**Architecture principle.** Migrate callers and delete the old API in the same wave instead of preserving compatibility layers.

Applies when introducing a new internal API while old callers still exist. The delivery-shaped half of [[pstack-principle-outcome-oriented-execution]]: the migration is one wave, not a deprecation window.

## See Also
- [[pstack-poteto-mode]] — indexes this principle inline and reads the index at task start.
- [[pstack]] — the twenty-three-principle set this belongs to.
