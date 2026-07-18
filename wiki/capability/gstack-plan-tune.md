---
type: capability
subtype: command
belongs_to: "[[gstack]]"
implements: "[[stage-plan]]"
delegates_to: []
produces: []
applies: ["[[pattern-knowledge-compounding]]"]
equivalent_to: []
sources: "gstack — Garry Tan (2026)"
raw: ["../../raw/gstack/2026-07-05-gstack-framework.md"]
updated: 2026-07-05
---

# /plan-tune

`/plan-tune` — self-tuning **AskUserQuestion sensitivity** plus a developer **psychographic**
profile for the plan-review skills (v1: observational). It calibrates how often the plan reviews
stop to ask the user vs auto-decide, learning per-question and per-developer over time so the
review panel matches your taste and tolerance for interruption.

A plan-review *meta* capability: it does not review a plan itself but tunes the behaviour of
[[gstack-plan-ceo-review]] / [[gstack-plan-design-review]] / [[gstack-plan-eng-review]] /
[[gstack-plan-devex-review]] and [[gstack-autoplan]]. The learned sensitivity is a small instance
of [[pattern-knowledge-compounding]] (the tool gets better on you over time).

## See Also
- [[gstack-autoplan]] · [[gstack-plan-ceo-review]] — the skills this tunes.
- [[stage-plan]] — the canonical stage this supports.
