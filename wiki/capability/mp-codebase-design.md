---
type: capability
subtype: skill
belongs_to: "[[matt-pocock-skills]]"
implements: "[[stage-plan]]"
delegates_to: []
produces: []
applies: ["[[pattern-deep-modules]]"]
equivalent_to: ["[[addy-api-design]]"]
docs_url: "https://www.aihero.dev/skills-codebase-design"
sources: "Matt Pocock — Skills for Real Engineers (2026)"
raw: ["../../raw/matt-pocock-skills/2026-06-28-skills-for-real-engineers.md"]
updated: 2026-07-04
---

# codebase-design

A **model-invoked** engineering skill that establishes discipline for **designing deep modules** — rich functionality behind small interfaces, placed at clean seams (see [[pattern-deep-modules]], Ousterhout). One of the "daily design investment" answers to failure mode #4 (ball of mud): deliberate interface design prevents architectural entropy.

## See Also
- [[mp-domain-modeling]] — supplies the concepts modules are organized around.
- [[mp-improve-codebase-architecture]] — finds where existing modules violate this.
- [[addy-api-design]] — Addy's API-design skill; same small-interface / deep-module discipline.
- [[stage-plan]] — the canonical stage this implements.
