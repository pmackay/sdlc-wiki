---
type: capability
subtype: command
belongs_to: "[[gstack]]"
implements: "[[stage-align]]"
delegates_to: []
produces: "[[artifact-product-brief]]"
applies: ["[[pattern-grilling]]", "[[pattern-source-grounding]]"]
equivalent_to: ["[[gsd-discuss-phase]]", "[[mp-grill-me]]", "[[addy-interview-me]]", "[[openspec-explore]]", "[[ce-brainstorm]]", "[[sp-brainstorming]]"]
sources: "gstack — Garry Tan (2026)"
raw: ["../../raw/gstack/2026-07-05-gstack-framework.md"]
updated: 2026-07-05
---

# /office-hours

`/office-hours` — "YC Office Hours." **Start here.** The align-stage entry point: it reframes your product idea *before* you write code, using **six forcing questions** that push back on your framing, challenge premises, and extract capabilities you didn't realize you were describing. The canonical example: a user asks for a "daily briefing app"; office-hours replies "what you actually described is a personal chief of staff AI," extracts five capabilities, challenges four premises, and generates three implementation approaches with effort estimates and a narrowest-wedge recommendation.

**Produces:** a reframed product/design doc ([[artifact-product-brief]]) that **every downstream gstack skill reads** — [[gstack-plan-ceo-review]] challenges its scope, [[gstack-plan-eng-review]] turns it into a test plan, and so on. This feed-forward is the backbone of the sprint.

It is gstack's member of the cross-framework **grilling / align** cluster — the interrogate-until- decisions-resolve entry point ([[pattern-grilling]]) — alongside [[gsd-discuss-phase]], [[mp-grill-me]], [[addy-interview-me]], [[openspec-explore]], and [[ce-brainstorm]]. It also enacts the *Search Before Building* ethos ([[pattern-source-grounding]]). Available as a native OpenClaw skill too (`gstack-openclaw-office-hours`).

## See Also
- [[gstack-plan-ceo-review]] — the usual next step; reads this doc and challenges scope.
- [[stage-align]] — the canonical stage this implements.
- [[gsd-discuss-phase]] · [[mp-grill-me]] · [[addy-interview-me]] — grilling-cluster counterparts.
