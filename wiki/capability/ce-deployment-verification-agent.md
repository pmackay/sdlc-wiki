---
type: capability
subtype: sub-agent
belongs_to: "[[compound-engineering]]"
implements: "[[stage-plan]]"
delegates_to: []
produces: ["[[artifact-launch-checklist]]"]
applies: ["[[pattern-fresh-context-subagents]]"]
equivalent_to: []
sources: "Compound Engineering — EveryInc/compound-engineering-plugin (2026)"
raw: ["../../raw/compound-engineering/2026-07-04-compound-engineering-every.md", "../../raw/compound-engineering/2026-07-04-compound-engineering-plugin.md"]
updated: 2026-07-05
---

# ce-deployment-verification-agent

A **Deployment Verification Agent** that produces concrete, executable checklists for risky data deployments so engineers aren't guessing at launch time: identify data invariants, write read-only SQL verification queries, document destructive steps (backfills, batching), and define monitoring + rollback + stop/go criteria. On planning invocations it emits **launch-readiness requirements** to fold into the plan.

Dispatched by [[ce-plan]], it implements [[stage-plan]] and produces a [[artifact-launch-checklist]] (the same artifact Addy's [[addy-shipping]] emits at ship time) — Compound Engineering computes it *at plan time*, an instance of the 80/20 front-load ([[pattern-shift-left]]). It pairs with [[ce-data-migration-reviewer]].

## See Also
- [[ce-plan]] — the dispatcher.
- [[ce-data-migration-reviewer]] — the migration-correctness sibling.
- [[addy-shipping]] — produces the same launch-checklist artifact at ship time (vs plan time here).
- [[stage-plan]] — the canonical stage this supports.
