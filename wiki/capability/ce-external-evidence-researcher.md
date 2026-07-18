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

# ce-external-evidence-researcher

An **external-evidence researcher for the verdict skill** ([[ce-pov]]). It gathers *verified*
external evidence about an external input so the caller can judge it — it **gathers and verifies,
the caller decides**, never recommending. It discounts stale claims (pricing/maturity/capability
older than ~12 months without confirmation) and, if neither web-search nor fetch is reachable,
reports "external research unavailable" and stops (the caller turns that into a "Hold") rather
than fabricating evidence.

It is one of [[ce-pov]]'s three grounding scouts — the **external** axis — alongside
[[ce-project-grounding-scout]] (this codebase) and [[ce-precedent-activity-scout]] (prior
decisions). It implements [[stage-align]] (evaluate-external-inputs flavor). It is the
verdict-oriented, evidence-weighted sibling of [[ce-web-researcher]] (which serves ideation).

## See Also
- [[ce-pov]] — the dispatcher (dual-grounded Adopt/Trial/Hold/Reject verdicts).
- [[ce-project-grounding-scout]] · [[ce-precedent-activity-scout]] — the other two verdict scouts.
- [[ce-web-researcher]] — the ideation-oriented external-research sibling.
- [[stage-align]] — the canonical stage this supports.
