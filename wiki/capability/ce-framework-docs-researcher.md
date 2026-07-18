---
type: capability
subtype: sub-agent
belongs_to: "[[compound-engineering]]"
implements: "[[stage-learn]]"
delegates_to: []
produces: ["[[artifact-solution-doc]]"]
applies: ["[[pattern-fresh-context-subagents]]", "[[pattern-source-grounding]]", "[[pattern-knowledge-compounding]]"]
equivalent_to: []
sources: "Compound Engineering — EveryInc/compound-engineering-plugin (2026)"
raw: ["../../raw/compound-engineering/2026-07-04-compound-engineering-every.md", "../../raw/compound-engineering/2026-07-04-compound-engineering-plugin.md"]
updated: 2026-07-05
---

# ce-framework-docs-researcher

A meticulous **Framework Documentation Researcher** that gathers and synthesizes technical documentation and best practices for the specific libraries/frameworks in play. On a durable-learning invocation it converts framework docs into **evidence for the learning**: authoritative references, version-specific caveats, corrected terminology, and links that help future readers understand *why* the solution works — prioritizing documentation that validates, narrows, or improves the captured lesson.

Dispatched by [[ce-compound]], it implements [[stage-learn]], feeding [[artifact-solution-doc]]. It is the framework-/version-specific complement to [[ce-best-practices-researcher]]'s broader best-practice synthesis.

## See Also
- [[ce-compound]] — the dispatcher; [[ce-best-practices-researcher]] — the broader best-practices sibling.
- [[pattern-source-grounding]] · [[pattern-knowledge-compounding]] — the techniques.
- [[stage-learn]] — the canonical stage this supports.
