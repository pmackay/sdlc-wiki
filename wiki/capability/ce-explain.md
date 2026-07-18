---
type: capability
subtype: skill
belongs_to: "[[compound-engineering]]"
implements: "[[stage-learn]]"
delegates_to: ["[[ce-work-recap-scout]]"]
produces: ["[[artifact-explainer]]"]
applies: ["[[pattern-knowledge-compounding]]"]
equivalent_to: []
sources: "Compound Engineering — EveryInc/compound-engineering-plugin (2026)"
raw: ["../../raw/compound-engineering/2026-07-04-compound-engineering-every.md", "../../raw/compound-engineering/2026-07-04-compound-engineering-plugin.md"]
updated: 2026-07-04
---

# /ce-explain

`/ce-explain` — "Turn concepts, diffs, or recent work into dense visual explainers with optional verification." Produces a dense, visual **explainer** ([[artifact-explainer]]) of a concept, a diff, or recent work, optionally verifying its claims against the code.

It implements [[stage-learn]] as the **human-facing** cousin of [[ce-compound]]: where compound writes machine-consumable learnings for future *agents*, explain writes human-consumable learnings for the *developer* (and teammates). Both harvest completed work into durable knowledge that improves the next iteration — the two directions of [[pattern-knowledge-compounding]] (agent grounding vs personal/team understanding). No cross-framework counterpart is paged; MP's [[mp-handoff]] is the nearest relative (compact knowledge for a future reader), but handoff targets session continuity, not learning.

## See Also
- [[ce-compound]] — the agent-facing learning sibling; [[mp-handoff]] — the compact-for-a-future-reader relative.
- [[artifact-explainer]] — the output; [[pattern-knowledge-compounding]] — the technique.
- [[stage-learn]] — the canonical stage this implements.
