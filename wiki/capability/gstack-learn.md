---
type: capability
subtype: command
belongs_to: "[[gstack]]"
implements: "[[stage-learn]]"
delegates_to: []
produces: "[[artifact-solution-doc]]"
applies: ["[[pattern-knowledge-compounding]]", "[[pattern-context-engineering]]"]
equivalent_to: ["[[ce-compound]]", "[[ce-compound-refresh]]"]
sources: "gstack — Garry Tan (2026)"
raw: ["../../raw/gstack/2026-07-05-gstack-framework.md"]
updated: 2026-07-05
---

# /learn

`/learn` — **Memory**. Manage what gstack learned across sessions: review, search, prune, and export
project-specific **patterns, pitfalls, and preferences**. "Learnings compound across sessions so
gstack gets smarter on your codebase over time." Shares storage with the browser **domain skills**
([[gstack-skillify]]) and, when configured, the gbrain persistent memory
([[gstack-setup-gbrain]]).

gstack's **agent-grounding** flavor of [[stage-learn]] — the direct counterpart to Compound
Engineering's [[ce-compound]] / [[ce-compound-refresh]] (a maintained, machine-consumable learnings
corpus that future runs auto-read → [[artifact-solution-doc]], [[pattern-knowledge-compounding]]).
Its team-process sibling is [[gstack-retro]]. Together they make gstack the **third framework** to
evidence the learn stage.

## See Also
- [[gstack-retro]] — the team-retrospective flavor of learn in gstack.
- [[gstack-skillify]] · [[gstack-setup-gbrain]] — the domain-skill and persistent-memory stores it shares.
- [[ce-compound]] · [[ce-compound-refresh]] — the agent-grounding-corpus counterparts.
- [[stage-learn]] — the canonical stage this implements.
