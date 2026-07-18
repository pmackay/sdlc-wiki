---
type: capability
subtype: sub-agent
belongs_to: "[[compound-engineering]]"
implements: "[[stage-plan]]"
delegates_to: []
produces: []
applies: ["[[pattern-fresh-context-subagents]]"]
equivalent_to: []
sources: "Compound Engineering — EveryInc/compound-engineering-plugin (2026)"
raw: ["../../raw/compound-engineering/2026-07-04-compound-engineering-every.md", "../../raw/compound-engineering/2026-07-04-compound-engineering-plugin.md"]
updated: 2026-07-05
---

# ce-data-migration-reviewer

A **data-migration & schema-change reviewer** that evaluates migration work in three layers:
schema drift / artifact risk, migration correctness (swapped mappings, missing backfills,
deploy-window breaks, data loss), and verification & rollback (concrete SQL + a credible
rollback path). It thinks in terms of the deploy window — old code on new schema, new code on old
data, partial failures — and never trusts fixtures.

Dispatched by [[ce-plan]], it implements [[stage-plan]]: on planning invocations it converts
migration analysis into plan **requirements** (expand/contract sequencing, backfill/batching,
dual-write, deploy-window risks). It pairs with [[ce-deployment-verification-agent]] (launch
checklists) and [[ce-data-integrity-guardian]] (the validate/learn-side data reviewer).

## See Also
- [[ce-plan]] — the dispatcher.
- [[ce-deployment-verification-agent]] — the launch-readiness sibling.
- [[ce-data-integrity-guardian]] — the data-safety reviewer on the compound council.
- [[stage-plan]] — the canonical stage this supports.
