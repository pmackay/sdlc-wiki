---
type: capability
subtype: sub-agent
belongs_to: "[[compound-engineering]]"
implements: "[[stage-align]]"
delegates_to: []
produces: []
applies: ["[[pattern-fresh-context-subagents]]", "[[pattern-source-grounding]]"]
equivalent_to: []
sources: "Compound Engineering — EveryInc/compound-engineering-plugin (2026)"
raw: ["../../raw/compound-engineering/2026-07-04-compound-engineering-every.md", "../../raw/compound-engineering/2026-07-04-compound-engineering-plugin.md"]
updated: 2026-07-05
---

# ce-web-researcher

An **external web researcher** that turns open-ended queries into a focused, structured external grounding digest — prior art, adjacent solutions, market signals, and cross-domain analogies the calling agent cannot get from the local codebase or org memory. Output is a compact synthesis, not raw results: what the outside world already knows and where the strongest leverage points are.

Dispatched by [[ce-ideate]] to convert external research into idea-generation inputs, so it implements [[stage-align]] ([[pattern-source-grounding]]). It is the external-axis grounding scout, alongside [[ce-slack-researcher]] (org) and [[ce-repo-profiler]] (project); the verdict-skill [[ce-pov]] uses the more evidence-weighted [[ce-external-evidence-researcher]] for the same axis.

## See Also
- [[ce-ideate]] — the primary dispatcher (grounded idea discovery).
- [[ce-external-evidence-researcher]] — the verdict-oriented external-research sibling ([[ce-pov]]).
- [[ce-slack-researcher]] · [[ce-repo-profiler]] — the org and project grounding siblings.
- [[stage-align]] — the canonical stage this supports.
