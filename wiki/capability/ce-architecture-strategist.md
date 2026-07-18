---
type: capability
subtype: sub-agent
belongs_to: "[[compound-engineering]]"
implements: "[[stage-plan]]"
delegates_to: []
produces: []
applies: ["[[pattern-fresh-context-subagents]]", "[[pattern-deep-modules]]"]
equivalent_to: []
sources: "Compound Engineering — EveryInc/compound-engineering-plugin (2026)"
raw: ["../../raw/compound-engineering/2026-07-04-compound-engineering-every.md", "../../raw/compound-engineering/2026-07-04-compound-engineering-plugin.md"]
updated: 2026-07-05
---

# ce-architecture-strategist

A **System Architecture Expert** that ensures changes align with established architectural patterns and maintain system integrity. It maps the current architecture (docs, READMEs, code patterns, component relationships, service boundaries), evaluates how a proposed change fits, and flags anti-patterns / improvement opportunities against scalable-maintainable-software principles.

Dispatched by [[ce-plan]], it implements [[stage-plan]] (design-alignment). It is the reviewer counterpart to BMAD's [[bmad-architect]] (the persona who *authors* the architecture spine) and relates to Matt Pocock's [[mp-improve-codebase-architecture]] — a design/architecture lens, applied at plan time here rather than as a validate-stage audit.

## See Also
- [[ce-plan]] — the dispatcher.
- [[bmad-architect]] — BMAD's architecture *author* (this agent *reviews* alignment).
- [[mp-improve-codebase-architecture]] — MP's architecture-audit relative (validate-side).
- [[stage-plan]] — the canonical stage this supports.
