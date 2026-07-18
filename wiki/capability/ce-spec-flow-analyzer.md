---
type: capability
subtype: sub-agent
belongs_to: "[[compound-engineering]]"
implements: "[[stage-plan]]"
delegates_to: []
produces: []
applies: ["[[pattern-fresh-context-subagents]]", "[[pattern-plan-verification-loop]]"]
equivalent_to: []
sources: "Compound Engineering — EveryInc/compound-engineering-plugin (2026)"
raw: ["../../raw/compound-engineering/2026-07-04-compound-engineering-every.md", "../../raw/compound-engineering/2026-07-04-compound-engineering-plugin.md"]
updated: 2026-07-05
---

# ce-spec-flow-analyzer

Analyzes specifications, plans, and feature descriptions **from the end-user's perspective** to surface missing flows, ambiguous requirements, and unspecified edge cases **before implementation begins — when they are cheapest to fix**. It grounds in the codebase first (existing patterns, conventions for error handling/auth/validation) so its feedback is concrete rather than generic.

Dispatched by [[ce-plan]], it implements [[stage-plan]] and applies [[pattern-plan-verification-loop]]: it is the flow-completeness lens behind [[ce-doc-review]], the sub-agent analogue of GSD's [[gsd-plan-checker]] and Spec Kit's [[speckit-analyze]] gates — but user-flow-oriented rather than cross-artifact-consistency-oriented.

## See Also
- [[ce-plan]] — the dispatcher; [[ce-doc-review]] — the plan-review skill it feeds.
- [[gsd-plan-checker]] · [[speckit-analyze]] — plan-verification gate relatives.
- [[stage-plan]] — the canonical stage this supports.
