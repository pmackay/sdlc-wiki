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

# ce-slack-researcher

An **organizational-knowledge researcher** that surfaces decisions, constraints, discussions, and undocumented org knowledge from Slack that is relevant to the task — context not found in the codebase, docs, or issue tracker. Its output is a concise digest of findings (not raw message dumps): what the org has discussed and which decisions/constraints apply.

Dispatched by [[ce-brainstorm]] (and other align skills) to turn Slack context into requirements inputs, so it implements [[stage-align]]. It complements the codebase-facing [[ce-repo-profiler]] and the external-facing [[ce-web-researcher]] — the three cover the *organizational*, *project*, and *external* grounding axes respectively.

## See Also
- [[ce-brainstorm]] · [[ce-ideate]] — dispatchers that fold org context into requirements/ideas.
- [[ce-web-researcher]] · [[ce-repo-profiler]] — the external and project grounding siblings.
- [[stage-align]] — the canonical stage this supports.
