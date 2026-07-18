---
type: pattern
sources: "Every — 'Compound Engineering' (2025-12-11); EveryInc/compound-engineering-plugin (2026); gstack — Garry Tan (2026); obra/superpowers (2026)"
updated: 2026-07-17
---

# Pattern: Knowledge compounding (each unit of work makes the next easier)

Treat every completed unit of work as **training data for future work**: harvest its bugs, failed tests, and reusable solutions, write them into a **durable, reusable form**, and have future work **read that form as grounding**. The result is a lifecycle that *compounds* — each feature leaves the codebase and the agents a little smarter, so complexity grows *alongside* accumulated knowledge instead of decaying into debt. Compound Engineering's one-liner: **"each unit of engineering work should make subsequent units easier — not harder."**

Three coupled moves:

1. **Harvest at close.** At iteration end, mine what happened — not just *whether* it shipped (that is [[stage-release]]) but *what was learned*. Compound Engineering runs a research council of sub-agents over the completed work ([[ce-compound]]).
2. **Externalize into a durable, consumable form.** Write learnings where future work will find them: a machine-consumable corpus ([[artifact-solution-doc]] in `docs/solutions/`), a retrospective's action items, or a human-facing [[artifact-explainer]]. Keep it maintained, not write-only ([[ce-compound-refresh]]).
3. **Re-inject downstream.** The front of the next loop reads it: [[ce-brainstorm]], [[ce-plan]], and [[ce-code-review]] pull the corpus in (via a `learnings-researcher` persona) so *"the next agent does not have to learn the same lesson from scratch."*

## Why it's distinctive

This is the loop-closing arrow that no other pattern in the wiki supplies. [[pattern-session-handoff]] carries context across a *boundary* within one effort; [[pattern-context-engineering]] curates the right context *into* a task; [[pattern-living-specification]] compounds *spec* knowledge. Knowledge compounding is broader: it compounds **lessons** — the reusable how-and-why — in a form later iterations consume automatically. It is the technique behind the canonical [[stage-learn]] stage, and the reason a lifecycle can be a *loop* rather than a line. Its most novel form is **machine-consumable**: learnings written so the next *agent* reads them without a human in the loop, which is why [[stage-learn]] is plausibly the first genuinely new SDLC stage the agent era adds.

## Applied by (backlinks)

Compound Engineering:

- [[ce-compound]] — mines completed work → `docs/solutions/` ([[artifact-solution-doc]]); the reference realization.
- [[ce-compound-refresh]] — keeps the corpus healthy (Keep/Update/Consolidate/Replace/Delete).
- [[ce-explain]] — the human-facing flavor → [[artifact-explainer]].
- [[ce-brainstorm]] · [[ce-plan]] · [[ce-code-review]] — the *consuming* side: read the corpus as grounding.
- Council + bridge sub-agents — [[ce-session-historian]], [[ce-pattern-recognition-specialist]], [[ce-best-practices-researcher]], [[ce-framework-docs-researcher]] (harvest lessons); [[ce-learnings-researcher]] (re-inject them into new work).

BMAD:

- [[bmad-retrospective]] — the team-process flavor: harvest lessons + action items future sprints surface.

gstack (the **third framework**; both flavors plus a novel capability-compounding form):

- [[gstack-learn]] — cross-session learnings corpus (patterns/pitfalls/preferences) future sessions read; the agent-grounding flavor.
- [[gstack-retro]] — team-aware weekly retrospective; the team-process flavor.
- [[gstack-skillify]] — codify a successful run into a permanent browser-skill (the agent literally *gains a skill*).
- [[gstack-setup-gbrain]] · [[gstack-sync-gbrain]] — the persistent cross-machine memory substrate the learnings compound into.

Superpowers (capability-compounding flavor only):

- [[sp-writing-skills]] — codify a proven technique into a permanent, auto-triggering skill ([[artifact-skill-doc]]), authored test-first; the library grows itself. The direct counterpart to [[gstack-skillify]] — both make *the agent gain a capability* the compounded output, rather than a lesson it reads. Superpowers has no solution-corpus / retrospective flavor.

## See Also
- [[stage-learn]] — the canonical stage this pattern defines.
- [[pattern-living-specification]] — spec-level compounding (OpenSpec's [[openspec-sync]]); a narrower cousin.
- [[pattern-context-engineering]] — how the compounded knowledge is fed back in.
- [[compound-engineering]] — the framework built around this pattern.
