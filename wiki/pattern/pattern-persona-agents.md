---
type: pattern
sources: "bmad-code-org/BMAD-METHOD (2026); gstack — Garry Tan (2026)"
raw: ["../../raw/bmad/2026-07-04-bmad-method-framework.md", "../../raw/gstack/2026-07-05-gstack-framework.md"]
updated: 2026-07-05
---

# Pattern: Persona agents (named role experts)

Organize the lifecycle around a cast of **distinct named expert personas**, one per role, each with a persistent character — a name, an icon, named influences, and stated principles — that "shape decisions across all dispatched workflows." Rather than invoking a neutral "planning command," you talk to *Mary the analyst* or *Winston the architect*, and the persona colours how the work is done. This is [[bmad]]'s signature contribution: six named agents (Mary/Paige/John/Sally/Winston/Amelia) anchor its four phases. **[[gstack]] is the second framework** built the same way — its whole toolkit is a cast of role specialists (a CEO, an eng manager, a senior designer, a DX lead, a staff engineer, a QA lead, a chief security officer, an SRE, a release engineer) invoked as slash-commands.

The payoff beyond flavour is **multi-perspective tension**. BMAD's **Party Mode** summons several personas into one roundtable where "the personas hold different priorities. The Architect guards the design, the PM guards scope, the Dev guards what's actually buildable" — and can spawn "a separate agent for each persona every substantive round" so "no single mind colors them all." That makes persona-agents a substrate for honest tradeoff decisions, pre-mortems, and reviews.

## Applied by (backlinks)

BMAD:

- [[bmad-analyst]] · [[bmad-tech-writer]] · [[bmad-pm]] · [[bmad-ux-designer]] · [[bmad-architect]] · [[bmad-dev]] — the six named personas, each anchoring a phase.
- [[bmad-brainstorming]] — persona-facilitated ideation.
- [[bmad-retrospective]] — a Party-Mode roundtable close-out.

gstack (a role specialist per skill; the plan-review panel is the clearest cluster):

- [[gstack-plan-ceo-review]] · [[gstack-plan-eng-review]] · [[gstack-plan-design-review]] · [[gstack-plan-devex-review]] — the CEO / Eng Manager / Senior Designer / DX Lead personas ([[pattern-parallel-persona-review]] via [[gstack-autoplan]]).
- [[gstack-review]] (Staff Engineer) · [[gstack-qa]] (QA Lead) · [[gstack-cso]] (Chief Security Officer) · [[gstack-canary]] (SRE) · [[gstack-ship]] (Release Engineer) — role specialists across the rest of the sprint.

## See Also
- [[pattern-parallel-persona-review]] — Addy's related fan-out: several *reviewer* personas in parallel, then merge. Persona-agents is the broader idea (personas across the whole lifecycle, collaborating as well as reviewing); Party Mode's subagent mode is effectively a parallel-persona review.
- [[pattern-grilling]] — the personas facilitate the human rather than autogenerating.
- [[bmad]] — the framework built on this pattern.
