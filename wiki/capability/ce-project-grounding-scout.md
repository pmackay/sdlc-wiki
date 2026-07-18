---
type: capability
subtype: sub-agent
belongs_to: "[[compound-engineering]]"
implements: "[[stage-align]]"
delegates_to: []
produces: []
applies: ["[[pattern-fresh-context-subagents]]", "[[pattern-context-engineering]]"]
equivalent_to: []
sources: "Compound Engineering — EveryInc/compound-engineering-plugin (2026)"
raw: ["../../raw/compound-engineering/2026-07-04-compound-engineering-every.md", "../../raw/compound-engineering/2026-07-04-compound-engineering-plugin.md"]
updated: 2026-07-05
---

# ce-project-grounding-scout

A **project-grounding scout** for the verdict skill ([[ce-pov]]). It finds the concrete project
evidence that lets the caller judge an external input against *this* codebase — a "project
floor" in one of two shapes: **replacing an incumbent** (named incumbent + at least one concrete
touchpoint — a call site, module, or config a change would touch), or **net-new adoption** (the
project does not yet do this job). It gathers; the caller decides.

It implements [[stage-align]] (evaluate-external-inputs flavor) as the **this-codebase** axis of
[[ce-pov]]'s grounding trio, complementing [[ce-external-evidence-researcher]] (external) and
[[ce-precedent-activity-scout]] (prior decisions). It is the [[ce-pov]]-scoped cousin of
[[ce-repo-profiler]] — question-*specific* project grounding versus the profiler's
question-agnostic profile.

## See Also
- [[ce-pov]] — the dispatcher.
- [[ce-external-evidence-researcher]] · [[ce-precedent-activity-scout]] — the other two verdict scouts.
- [[ce-repo-profiler]] — the question-agnostic project-profile sibling.
- [[stage-align]] — the canonical stage this supports.
