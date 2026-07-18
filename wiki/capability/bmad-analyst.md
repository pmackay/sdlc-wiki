---
type: capability
subtype: sub-agent
belongs_to: "[[bmad]]"
implements: "[[stage-align]]"
delegates_to: ["[[bmad-brainstorming]]", "[[bmad-research]]", "[[bmad-product-brief]]", "[[bmad-prfaq]]", "[[bmad-document-project]]"]
produces: ["[[artifact-product-brief]]", "[[artifact-research-md]]"]
applies: ["[[pattern-persona-agents]]", "[[pattern-grilling]]"]
equivalent_to: []
sources: "bmad-code-org/BMAD-METHOD — bmad-agent-analyst (2026)"
raw: ["../../raw/bmad/2026-07-04-bmad-method-framework.md"]
updated: 2026-07-04
---

# bmad-analyst

**Mary** 📊 (`bmad-agent-analyst`) — BMAD's **Analysis-phase persona**: "Help the user ideate, research and analyze before committing to a project." She "channels Michael Porter's strategic rigor and Barbara Minto's Pyramid Principle discipline" — the wiki's most explicitly character-driven align agent ([[pattern-persona-agents]]).

Mary is a menu of Analysis workflows rather than a single command; she dispatches:

- [[bmad-brainstorming]] (BP) — facilitated ideation.
- [[bmad-research]] (MR / DR / TR) — market, domain, and technical research.
- [[bmad-product-brief]] (CB) — the pre-PRD scoping brief.
- [[bmad-prfaq]] (WB) — the Working-Backwards PRFAQ challenge.
- [[bmad-document-project]] (DP) — brownfield documentation for AI context.

Like every BMAD planning persona she works as a **facilitator** — never generating content without user input ([[pattern-grilling]]).

## See Also
- [[bmad]] — the framework.
- [[bmad-pm]] — the Planning persona Mary hands off to (brief/research → PRD).
- [[stage-align]] — the canonical stage.
