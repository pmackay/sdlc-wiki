---
type: capability
subtype: sub-agent
belongs_to: "[[compound-engineering]]"
implements: "[[stage-review]]"
delegates_to: []
produces: []
applies: ["[[pattern-fresh-context-subagents]]"]
equivalent_to: []
sources: "Compound Engineering — EveryInc/compound-engineering-plugin (2026)"
raw: ["../../raw/compound-engineering/2026-07-04-compound-engineering-every.md", "../../raw/compound-engineering/2026-07-04-compound-engineering-plugin.md"]
updated: 2026-07-05
---

# ce-data-integrity-guardian

A **Data Integrity Guardian** — expert in database design, migration safety, and data governance (ACID, GDPR/CCPA). It protects data integrity, ensures migration safety (reversibility, rollback, data-loss and NULL-handling checks), and maintains privacy compliance.

It implements [[stage-review]] (data-safety review). On the [[ce-compound]] council it converts data-integrity analysis into lesson validation (which invariant was at risk, why the fix preserves it, rollback/migration caveats) for [[artifact-solution-doc]]. It is the compound/validate-side data reviewer, complementing the plan-side [[ce-data-migration-reviewer]] and [[ce-deployment-verification-agent]].

## See Also
- [[ce-compound]] — the learning dispatcher; [[ce-data-migration-reviewer]] — the plan-side data sibling.
- [[ce-deployment-verification-agent]] — launch-readiness data checklists (plan-side).
- [[stage-review]] — the canonical stage this supports; [[stage-learn]] — its compound-council role.
