---
type: pattern
sources: "Every — 'Compound Engineering' (2025-12-11); EveryInc/compound-engineering-plugin (2026); gstack — Garry Tan (2026); obra/superpowers (2026); jayminwest/warren (2026); Agent OS — Builder Methods (2026); sipyourdrink-ltd/bernstein (2026); jayminwest/seeds (2026); gastownhall/beads (2026); github/gh-aw (2026)"
updated: 2026-09-01
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

Seeds — compounding wired into the *planning prompt* rather than into a retro:

- [[seeds-plan-prompt]] — when mulch is on `PATH`, infers a domain and mines prior conventions, decisions, and failures into each section's `prior_art`, so a new plan's `risks` section arrives pre-populated with the failures earlier plans actually hit. Where [[ce-compound]] and [[gstack-learn]] build a corpus and trust a later session to read it, seeds injects the relevant subset at the one moment it changes the outcome. Soft coupling: mulch absent, planning still works.
- [[seeds-plan-submit]] — `--record-decision` (off by default) writes the chosen approach back out as a mulch decision linked to the plan, closing the loop in the other direction.

Beads — compounding as a store primitive rather than a skill's output:

- [[beads-remember]] — `bd remember "insight"` persists *"across sessions and account rotations"* and is injected into every session by [[beads-prime]]; the README tells agents to use it **instead of** writing `MEMORY.md` files. Where [[ce-compound]] and [[gstack-learn]] maintain a corpus and trust a later session to read it, beads pushes the whole set into context unconditionally at session start.
- [[beads-kv]] — the untyped sibling, for durable values rather than durable prose.
- [[beads-formula]] — a workflow that worked is captured as a reusable DAG template, and `bd mol distill` extracts one *from an epic that already happened* — the [[gstack-skillify]] move applied to a work graph instead of a skill.
- [[beads-federation]] — accumulated state shared peer-to-peer across repos and organizations, so compounding is not confined to one clone.
- [[beads-audit]] — records labelled prompt/response traces for *"dataset generation (SFT/RL fine-tuning)"*: compounding aimed at model weights rather than at context, which nothing else in this wiki attempts.

## Enabled by (infrastructure)

The most striking cross-layer finding in the wiki: an [execution-layer](../runtime/index.md) runtime bakes the harvest-externalize-reinject loop into the substrate, so compounding happens *without a process-layer skill asking for it*:

- [[warren]] (platform) — a project's `.mulch/` directory is **persistent agent memory across runs**: prior expertise is primed into context on spawn, the agent records new conventions/patterns/failure-modes with `ml record`, and reap merges them back (last-write-wins, just files in the repo, no database). This is the infrastructure realization of [[ce-compound]] / [[gstack-learn]] — machine-consumable memory every future run auto-reads. Its `.seeds/` issue queue and `canopy` versioned prompt library compound work-items and prompts the same way.
- [[bernstein]] (platform) — the same loop, more elaborately instrumented and with an explicit review gate on the reinject step. `core/knowledge/lessons.py` propagates lessons **tag-matched and confidence-decayed over time** into later spawns under a bounded context-injection budget; a per-task **knowledge diary** (`tried` / `worked` / `failed` / `rationale` / `tags`) is distilled from each closing transcript, and a periodic **synthesis** pass clusters diaries into themes — but lands `approved: false` until an operator runs `bernstein knowledge synthesize --apply`, because *"no role prompt is mutated by the synthesizer alone."* A `CrossTaskKB` publish/subscribe facade over SQLite lets one task hand a fact to another *"without writing files into a shared worktree path and hoping the next agent reads them."*
- [[gh-aw]] (platform) — two substrate memories for recurring workflows, split by durability: `cache-memory` (files in the GitHub Actions cache, 10GB per repo, ~7-day eviction, sanitized on restore) for session-scale state, and `repo-memory` (git branches, versioned, unlimited retention) for the long term. The distinctive twist is **integrity-scoped** compounding: cache keys include the content-trust level, so a run operating on `merged`-only data never inherits memory written by a run that read `unapproved` content — the first runtime here to treat accumulated memory itself as a prompt-injection surface.

## Persisted by (store)

- [[beads]] — [[beads-remember]] and [[beads-kv]] make durable insight a store primitive, auto-injected every session by [[beads-prime]], with the README instructing agents **not** to hand-maintain `MEMORY.md` files. [[beads-audit]] extends the idea to model weights, recording labelled interaction traces for fine-tuning.
- [[seeds]] — deliberately delegates: [[seeds-plan-prompt]] shells out to mulch for prior art rather than storing insight itself. Worth noting as the layer's internal contrast — one store owns memory, the other borrows it.

Also in this layer but unpaged: [[warren]]'s `.mulch/` (expertise records merged across runs) and canopy (a versioned prompt library), which is why the store node's `memory` subtype exists.

## See Also
- [[stage-learn]] — the canonical stage this pattern defines.
- [[topic-harness-engineering]] — this pattern is the *steering loop* that refines guides and sensors over time.
- [[pattern-living-specification]] — spec-level compounding (OpenSpec's [[openspec-sync]]); a narrower cousin.
- [[pattern-context-engineering]] — how the compounded knowledge is fed back in.
- [[compound-engineering]] — the framework built around this pattern.
- [[warren]] · [[bernstein]] — the runtimes that move knowledge compounding into the substrate (`.mulch/`; confidence-decayed lessons + HITL-gated diary synthesis).
