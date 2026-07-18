---
type: capability
subtype: command
belongs_to: "[[gstack]]"
implements: "[[stage-implement]]"
delegates_to: ["[[gstack-careful]]", "[[gstack-freeze]]"]
produces: []
applies: ["[[pattern-edit-guardrails]]"]
equivalent_to: []
sources: "gstack — Garry Tan (2026)"
raw: ["../../raw/gstack/2026-07-05-gstack-framework.md"]
updated: 2026-07-05
---

# /guard

`/guard` — **full safety mode**: activates [[gstack-careful]] (destructive-command warnings) **and** [[gstack-freeze]] (directory-scoped edits) in one command. "Maximum safety for prod work."

The combined form of gstack's [[pattern-edit-guardrails]]; delegates to its two constituent guardrails. Clear the freeze half with [[gstack-unfreeze]].

## See Also
- [[gstack-careful]] · [[gstack-freeze]] — the two guardrails this combines.
- [[gstack-unfreeze]] — removes the freeze boundary.
- [[stage-implement]] — the stage these guardrails protect.
