---
type: capability
subtype: sub-agent
belongs_to: "[[compound-engineering]]"
implements: "[[stage-implement]]"
delegates_to: []
produces: []
applies: ["[[pattern-fresh-context-subagents]]"]
equivalent_to: []
sources: "Compound Engineering — EveryInc/compound-engineering-plugin (2026)"
raw: ["../../raw/compound-engineering/2026-07-04-compound-engineering-every.md", "../../raw/compound-engineering/2026-07-04-compound-engineering-plugin.md"]
updated: 2026-07-05
---

# ce-figma-design-sync

A **design-to-code synchronization specialist** that ensures pixel-perfect alignment between
Figma designs and their web implementations. It captures the Figma design via the Figma MCP
(colors, typography, spacing, layout, shadows, borders + a screenshot), captures the live
implementation via agent-browser, compares them systematically, and makes precise CSS/Tailwind
adjustments to close the gap.

Dispatched by [[ce-work]], it implements [[stage-implement]] as the UI-fidelity arm of
execution. It complements [[ce-polish]] (conversational UX iteration) — polish shapes the
experience, this agent enforces fidelity to a design source of truth — and relates to Addy's
[[addy-frontend-ui]] (production-quality UI craft).

## See Also
- [[ce-work]] — the dispatcher; [[ce-polish]] — the conversational UX-iteration sibling.
- [[addy-frontend-ui]] — production-quality UI craft relative.
- [[stage-implement]] — the canonical stage this supports.
