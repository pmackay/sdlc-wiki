---
type: capability
subtype: command
belongs_to: "[[gstack]]"
implements: "[[stage-implement]]"
delegates_to: []
produces: []
applies: []
equivalent_to: []
sources: "gstack — Garry Tan (2026)"
raw: ["../../raw/gstack/2026-07-05-gstack-framework.md"]
updated: 2026-07-05
---

# /scrape

`/scrape` — pull structured data from a web page via the persistent browser ([[gstack-browse]]).
The **first call prototypes** the extraction interactively; a **codified call runs in ~200ms**.
Once a scrape flow succeeds, [[gstack-skillify]] can codify it into a permanent, reusable
browser-skill on disk.

A browser-automation build utility rather than an SDLC-lifecycle step; filed under
[[stage-implement]] as an automation-building capability. Its compounding partner is
[[gstack-skillify]] (turn a successful run into a durable skill → [[pattern-knowledge-compounding]]).

## See Also
- [[gstack-skillify]] — codifies a successful scrape into a permanent browser-skill.
- [[gstack-browse]] — the browser daemon it runs against.
- [[stage-implement]] — the canonical stage this implements.
