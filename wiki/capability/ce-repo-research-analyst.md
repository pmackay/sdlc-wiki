---
type: capability
subtype: sub-agent
belongs_to: "[[compound-engineering]]"
implements: "[[stage-review]]"
delegates_to: []
produces: []
applies: ["[[pattern-fresh-context-subagents]]", "[[pattern-measure-first]]"]
equivalent_to: []
sources: "Compound Engineering — EveryInc/compound-engineering-plugin (2026)"
raw: ["../../raw/compound-engineering/2026-07-04-compound-engineering-every.md", "../../raw/compound-engineering/2026-07-04-compound-engineering-plugin.md"]
updated: 2026-07-05
---

# ce-repo-research-analyst

A **repository research analyst** that systematically uncovers codebase patterns, guidelines,
and conventions. For optimization invocations (its home dispatcher [[ce-optimize]]) it converts
repo research into **optimization inputs**: likely hot paths, existing benchmark/profiling hooks,
metrics surfaces, expensive loops/queries, caching boundaries, test commands that measure
behavior, and constraints affecting safe experimentation — preferring concrete paths, commands,
and measurement opportunities over broad summaries. Supports a `Scope:` contract to run only
selected phases.

Dispatched by [[ce-optimize]], it implements [[stage-review]] ([[pattern-measure-first]]) — it
finds *where and how* to measure before optimization runs. It is the optimization-scoped,
measurement-oriented cousin of the question-agnostic [[ce-repo-profiler]].

## See Also
- [[ce-optimize]] — the dispatcher (metric-driven optimization).
- [[ce-repo-profiler]] — the question-agnostic profiling sibling.
- [[stage-review]] — the canonical stage this supports.
