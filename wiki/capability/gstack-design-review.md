---
type: capability
subtype: command
belongs_to: "[[gstack]]"
implements: "[[stage-review]]"
delegates_to: []
produces: ["[[artifact-review-report]]", "[[artifact-atomic-commit]]"]
applies: ["[[pattern-persona-agents]]"]
equivalent_to: []
sources: "gstack — Garry Tan (2026)"
raw: ["../../raw/gstack/2026-07-05-gstack-framework.md"]
updated: 2026-07-05
---

# /design-review

`/design-review` — the **Designer Who Codes**. A live-site visual audit (visual inconsistency, spacing issues, hierarchy problems, AI-slop patterns, slow interactions) — the same rubric as [[gstack-plan-design-review]] — that then **fixes what it finds**, with atomic commits and before/after screenshots.

The live-audit boomerang of [[gstack-plan-design-review]]: the plan-time review scores the design 0-10, this one re-audits the shipped implementation and closes the gap. Sits in gstack's **Review** phase ([[stage-review]]); produces both a report and the fixing commits. Its iOS sibling is [[gstack-ios-design-review]].

## See Also
- [[gstack-plan-design-review]] — the plan-time review this boomerangs from.
- [[gstack-ios-design-review]] — the iOS/HIG sibling.
- [[stage-review]] — the canonical stage this implements (Review side).
