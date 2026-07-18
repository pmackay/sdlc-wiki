---
type: capability
subtype: sub-agent
belongs_to: "[[compound-engineering]]"
implements: "[[stage-align]]"
delegates_to: []
produces: []
applies: ["[[pattern-fresh-context-subagents]]", "[[pattern-knowledge-compounding]]", "[[pattern-context-engineering]]"]
equivalent_to: []
sources: "Compound Engineering — EveryInc/compound-engineering-plugin (2026)"
raw: ["../../raw/compound-engineering/2026-07-04-compound-engineering-every.md", "../../raw/compound-engineering/2026-07-04-compound-engineering-plugin.md"]
updated: 2026-07-05
---

# ce-learnings-researcher

A domain-agnostic **institutional-knowledge researcher** that finds and distills applicable
past learnings from the team's knowledge base *before* new work begins — bug learnings,
architecture patterns, design patterns, tooling decisions, conventions, and workflow
discoveries are all first-class. Its work helps callers avoid re-discovering what the team
already learned.

It is the **consuming side** of [[pattern-knowledge-compounding]]: it reads the
[[artifact-solution-doc|`docs/solutions/` corpus]] that [[ce-compound]] writes and re-injects
relevant lessons into new work. Dispatched by [[ce-ideate]], [[ce-code-review]], and other
front-of-loop skills, it is the concrete mechanism by which learnings captured in
[[stage-learn]] flow back into [[stage-align]] — the arrow that closes the compounding loop. No
cross-framework counterpart: it is unique to Compound Engineering's loop.

## See Also
- [[ce-compound]] — writes the corpus this agent reads back in ([[stage-learn]] → [[stage-align]]).
- [[ce-repo-profiler]] — the companion grounding scout (project profile vs past lessons).
- [[pattern-knowledge-compounding]] — the loop this agent completes.
- [[stage-align]] — where it grounds new work; [[stage-learn]] — the source of what it re-injects.
