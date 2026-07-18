---
type: capability
subtype: skill
belongs_to: "[[compound-engineering]]"
implements: "[[stage-align]]"
delegates_to: ["[[ce-media-analyzer]]"]
produces: []
applies: ["[[pattern-context-engineering]]", "[[pattern-knowledge-compounding]]"]
equivalent_to: []
sources: "Compound Engineering — EveryInc/compound-engineering-plugin (2026)"
raw: ["../../raw/compound-engineering/2026-07-04-compound-engineering-every.md", "../../raw/compound-engineering/2026-07-04-compound-engineering-plugin.md"]
updated: 2026-07-04
---

# /ce-sweep

`/ce-sweep` — "Ingest Slack/GitHub items since cursors, acknowledge at source, analyze, verify fixes, reconcile plans." A lifecycle-tracking / feedback-consolidation skill: it pulls new items (Slack messages, GitHub issues/PRs) since the last cursor, acknowledges them at the source, analyzes and de-duplicates them, verifies whether reported issues are already fixed, and reconciles the findings back into existing plans.

It is a **feedback-intake** capability at the front of the loop — turning external signal into actionable inputs for the next [[ce-brainstorm]]/[[ce-plan]] cycle — so it implements [[stage-align]]. It has a foot in [[stage-learn]] too (consolidating what was learned from shipped work), but its primary act is *intake that seeds the next iteration*. No direct cross-framework counterpart; conceptually adjacent to [[ce-product-pulse]] (which reports post-release signal) and to the compound loop's grounding reads.

## See Also
- [[ce-product-pulse]] — post-release reporting sibling; `ce-sweep` turns signal into plan inputs.
- `ce-riffrec-feedback-analysis` — structures a specific feedback source (catalogued on [[compound-engineering]], not separately paged).
- [[stage-align]] — the canonical stage this implements.
