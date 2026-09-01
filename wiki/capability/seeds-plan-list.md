---
type: capability
subtype: command
belongs_to: "[[seeds]]"
implements: []
produces: []
applies: []
equivalent_to: []
sources: "Jaymin West — jayminwest/seeds PLAN_SPEC.md + README.md (MIT, v0.5.15, 2026)"
raw: ["../../raw/seeds/2026-08-31-seeds.md"]
updated: 2026-08-31
---

# sd plan list

`sd plan list` — query the plan store by `--seed`, `--status` (`draft | approved | active | done`), `--outcome` (`success | partial | failure`), or `--template`, showing each plan's short name alongside its id.

The status values are derived rather than hand-set: `draft` on [[seeds-plan-prompt]], `approved` once [[seeds-plan-submit]] validates and spawns, `active` automatically as soon as any child seed goes `in_progress`, `done` when all children are closed. So `sd plan list --status active` answers "what is being built right now" from the issue graph, with nothing to keep in sync.

Filtering by `--outcome` is what makes [[seeds-plan-outcome]] worth recording at all: it is the only query surface over which templates and approaches actually worked, in a framework that deliberately ships no aggregation.

A pure **read** command; maps to **no canonical SDLC stage**.

## See Also
- [[seeds-plan-show]] — the single-plan detail view.
- [[seeds-plan-outcome]] — writes the field this filters on.
- [[seeds-stats]] — the issue-side aggregate.
