---
type: capability
subtype: skill
belongs_to: "[[compound-engineering]]"
implements: "[[stage-plan]]"
delegates_to: []
produces: ["[[artifact-review-report]]"]
applies: ["[[pattern-plan-verification-loop]]", "[[pattern-parallel-persona-review]]", "[[pattern-adversarial-review]]", "[[pattern-fresh-context-subagents]]"]
equivalent_to: ["[[gsd-plan-checker]]", "[[speckit-analyze]]", "[[bmad-check-implementation-readiness]]"]
sources: "Compound Engineering — EveryInc/compound-engineering-plugin (2026)"
raw: ["../../raw/compound-engineering/2026-07-04-compound-engineering-every.md", "../../raw/compound-engineering/2026-07-04-compound-engineering-plugin.md"]
updated: 2026-07-04
---

# /ce-doc-review

`/ce-doc-review` — "Review requirements or plans using reviewer personas across coherence,
feasibility, and security lenses." The plan-side analogue of [[ce-code-review]]: **before** any
code, it fans out fresh-context reviewer personas (coherence, feasibility, security-lens,
product-lens, design-lens, scope-guardian, adversarial-document) over the
[[artifact-brainstorm-md|requirements]] / [[artifact-plan-md|plan]] and reports
confidence-gated findings → [[artifact-review-report]].

This is [[pattern-plan-verification-loop]] realized with **parallel personas** rather than a
single checker — gating the plan before it is executed, which is the essence of the 80/20
front-load ([[pattern-shift-left]] applied to planning). It implements [[stage-plan]] (it
verifies plan artifacts), distinguishing it from [[ce-code-review]] which gates *code* in
[[stage-review]].

## Cross-framework equivalents
Plan-verification cluster: `ce-doc-review` ↔ [[gsd-plan-checker]] ↔ [[speckit-analyze]] ↔
[[bmad-check-implementation-readiness]] — each gates planning artifacts before implementation.
`ce-doc-review` is distinctive in using a **persona fan-out** ([[pattern-parallel-persona-review]])
where the others use a single multi-dimension checker.

## See Also
- [[gsd-plan-checker]] · [[speckit-analyze]] · [[bmad-check-implementation-readiness]] — plan-verification counterparts.
- [[ce-code-review]] — the code-side sibling (same persona machinery, [[stage-review]]).
- [[ce-plan]] — produces what this reviews.
- [[stage-plan]] — the canonical stage this implements.
