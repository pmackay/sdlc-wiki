---
type: pattern
sources: "Every — 'Compound Engineering' (2025-12-11); EveryInc/compound-engineering-plugin (2026); gstack — Garry Tan (2026); obra/superpowers (2026); jayminwest/warren (2026); Agent OS — Builder Methods (2026)"
updated: 2026-08-05
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

Agent OS (standards-compounding flavor):

- [[agent-os-discover-standards]] — the Refine phase of Discover→Inject→Build→**Refine**: a project's improved [[artifact-standards|standards]] `sync-to-profile` back into a reusable base profile (with inheritance), so the *next project* starts from the compounded conventions. Compounding applied to **standards** rather than lessons — the [[topic-harness-engineering|steering loop]] baked into the convention layer. Narrower than [[ce-compound]] (harvests arbitrary lessons); it compounds only authored conventions.

## Enabled by (infrastructure)

The most striking cross-layer finding in the wiki: an [execution-layer](../runtime/index.md) runtime bakes the harvest-externalize-reinject loop into the substrate, so compounding happens *without a process-layer skill asking for it*:

- [[warren]] (platform) — a project's `.mulch/` directory is **persistent agent memory across runs**: prior expertise is primed into context on spawn, the agent records new conventions/patterns/failure-modes with `ml record`, and reap merges them back (last-write-wins, just files in the repo, no database). This is the infrastructure realization of [[ce-compound]] / [[gstack-learn]] — machine-consumable memory every future run auto-reads. Its `.seeds/` issue queue and `canopy` versioned prompt library compound work-items and prompts the same way.

## See Also
- [[stage-learn]] — the canonical stage this pattern defines.
- [[topic-harness-engineering]] — this pattern is the *steering loop* that refines guides and sensors over time.
- [[pattern-living-specification]] — spec-level compounding (OpenSpec's [[openspec-sync]]); a narrower cousin.
- [[pattern-context-engineering]] — how the compounded knowledge is fed back in.
- [[compound-engineering]] — the framework built around this pattern.
- [[warren]] — the runtime that moves knowledge compounding into the substrate (`.mulch/`).
