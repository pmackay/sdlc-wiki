---
type: capability
subtype: command
belongs_to: "[[gstack]]"
implements: "[[stage-learn]]"
delegates_to: []
produces: []
applies: ["[[pattern-knowledge-compounding]]"]
equivalent_to: ["[[sp-writing-skills]]"]
sources: "gstack — Garry Tan (2026)"
raw: ["../../raw/gstack/2026-07-05-gstack-framework.md"]
updated: 2026-07-05
---

# /skillify

`/skillify` — codify the most recent successful [[gstack-scrape]] flow into a **permanent browser-skill on disk**. The per-site domain-skill mechanism: a saved note (e.g. "LinkedIn's Apply button lives in an iframe") is quarantined, becomes **active after 3 successful uses**, and can be promoted cross-project. Storage lives alongside [[gstack-learn]]'s per-project learnings.

A learn-stage capability: it turns a one-off successful run into **reusable, compounding capability** ([[pattern-knowledge-compounding]]) — the browser-automation analogue of writing a solution doc. The agent literally gains a new skill each time.

## See Also
- [[gstack-scrape]] — the flow this codifies.
- [[gstack-learn]] — the learnings store it shares.
- [[stage-learn]] — the canonical stage this implements.
