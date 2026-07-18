---
type: capability
subtype: skill
belongs_to: "[[compound-engineering]]"
implements: "[[stage-align]]"
delegates_to: ["[[ce-repo-profiler]]", "[[ce-slack-researcher]]"]
produces: ["[[artifact-brainstorm-md]]"]
applies: ["[[pattern-grilling]]", "[[pattern-context-engineering]]", "[[pattern-knowledge-compounding]]"]
equivalent_to: ["[[addy-interview-me]]", "[[mp-grill-me]]", "[[gsd-discuss-phase]]", "[[speckit-clarify]]", "[[gstack-office-hours]]", "[[sp-brainstorming]]"]
sources: "Compound Engineering — EveryInc/compound-engineering-plugin (2026)"
raw: ["../../raw/compound-engineering/2026-07-04-compound-engineering-every.md", "../../raw/compound-engineering/2026-07-04-compound-engineering-plugin.md"]
updated: 2026-07-04
---

# /ce-brainstorm

`/ce-brainstorm` — "Define what something should become through collaborative dialogue and requirements-only unified plans." Step 1 of the Compound Engineering loop: a Q&A dialogue that converges on **what** to build (deliberately **requirements-only** — no HOW) and writes a unified plan to `docs/brainstorms/` → [[artifact-brainstorm-md]]. It reads the [[artifact-strategy-md|strategy]] and the `docs/solutions/` compound corpus first, so prior learnings shape the conversation ([[pattern-knowledge-compounding]] on the consuming side).

It is the front of the loop and sits in the **grilling / elicitation** cluster of [[stage-align]]. The requirements-only discipline is what lets [[ce-plan]] later own the WHAT→HOW enrichment cleanly.

## Cross-framework equivalents
Grilling/align cluster: `ce-brainstorm` ↔ [[addy-interview-me]] ↔ [[mp-grill-me]] ↔ [[gsd-discuss-phase]] ↔ [[speckit-clarify]] — all interrogate to resolve intent before building ([[pattern-grilling]]). `ce-brainstorm`'s output is a requirements plan (like [[gsd-discuss-phase]]'s CONTEXT.md), distinguishing it from pure ideation ([[ce-ideate]]).

## See Also
- [[addy-interview-me]] · [[mp-grill-me]] · [[gsd-discuss-phase]] · [[speckit-clarify]] — grilling-cluster counterparts.
- [[ce-ideate]] — the ideation sibling (generate directions); [[ce-plan]] — consumes the brainstorm.
- [[stage-align]] — the canonical stage this implements.
