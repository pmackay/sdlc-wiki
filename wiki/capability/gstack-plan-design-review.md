---
type: capability
subtype: command
belongs_to: "[[gstack]]"
implements: "[[stage-plan]]"
delegates_to: []
produces: []
applies: ["[[pattern-persona-agents]]", "[[pattern-parallel-persona-review]]"]
equivalent_to: ["[[ce-doc-review]]"]
sources: "gstack — Garry Tan (2026)"
raw: ["../../raw/gstack/2026-07-05-gstack-framework.md"]
updated: 2026-07-05
---

# /plan-design-review

`/plan-design-review` — the **Senior Designer** persona in gstack's plan-review panel. Rates each design dimension **0-10**, explains what a 10 looks like, then edits the plan to get there. Includes **AI-slop detection**. Interactive — one AskUserQuestion per design choice.

The plan-time (before-code) half of a boomerang: its live-audit counterpart after shipping is [[gstack-design-review]], which re-scores the implementation against these plan scores. One of the four `plan-*-review` persona reviews ([[pattern-persona-agents]], [[pattern-parallel-persona-review]]) that [[gstack-autoplan]] chains; clusters with [[ce-doc-review]] as a persona-lens plan review.

Use it when building **for end users** (UI, web, mobile); use [[gstack-plan-devex-review]] when building for developers.

## See Also
- [[gstack-design-review]] — the live-audit boomerang that re-scores the shipped implementation.
- [[gstack-plan-devex-review]] — the developer-facing sibling review.
- [[gstack-autoplan]] — runs this review as part of the panel.
- [[stage-plan]] — the canonical stage this implements.
