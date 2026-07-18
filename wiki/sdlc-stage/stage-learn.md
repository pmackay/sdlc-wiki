---
type: sdlc-stage
aka: { bmad: "retrospective (learning close-out)", compound-engineering: "compound", gstack: "Reflect (retro + learn)", superpowers: "writing-skills (capability-compounding)" }
sources: "Synthesized from BMAD + Compound Engineering + gstack + Superpowers (2026); spec-flavor cousin in OpenSpec"
updated: 2026-07-17
---

# Stage: Learn

Canonical lifecycle stage: **harvest the learnings from completed work — bugs, failed tests,
reusable solutions, process lessons — and fold them into a durable, reusable form so future
iterations start ahead.** The output is not the shipped software (that is [[stage-release]])
but *knowledge*: a solution corpus, a retrospective's action items, or an updated living spec.
Its defining property is that its product is **consumed by the front of the next loop** —
[[stage-align]], [[stage-plan]], and [[stage-review]] read it as
grounding — closing the loop rather than ending it.

**Derived projection** — evidence is the capabilities that `implements: [[stage-learn]]`.

> **New stage (promoted 2026-07-04); now beyond doubt — three frameworks (2026-07-05).** Was
> folded into [[stage-release]] as its "learning close-out" flavor (BMAD-only, single-framework).
> Compound Engineering made learning capture a **first-class, named step of its own loop**
> (`/ce-compound` is *"the money step… the whole point"*), giving the activity a **second
> framework** and clearing the ≥2-framework bar the [conventions](../CONVENTIONS.md#stage-re-derivation-keep-stages-framework-neutral)
> require — exactly as [[stage-specify]] was split out of [[stage-plan]]. **gstack (2026-07-05) is
> the third framework**, and the first to populate *both* flavors at once: its *Reflect* sprint
> phase ships [[gstack-retro]] (team retrospective) **and** [[gstack-learn]] (an agent-grounding
> learnings corpus), plus [[gstack-skillify]] (compound a successful run into a permanent skill).
> Split cleanly out of release: *release* delivers the work; *learn* extracts the reusable
> knowledge. See [Why a distinct stage](#why-a-distinct-stage-not-a-flavor-of-release).
> **Superpowers (2026-07-17) is a fourth framework**, purely in the capability-compounding flavor:
> [[sp-writing-skills]] turns a proven technique into a permanent auto-triggering skill (↔ [[gstack-skillify]]).

## Why a distinct stage, not a flavor of release

[[stage-release]] finalizes and delivers a completed unit (ship-to-prod, or merge-the-spec).
Learn does something categorically different: it treats the *just-completed work as a source
of training data* and produces an artifact whose only purpose is to make **future** work
better. The two are adjacent in time (both close the iteration) but opposite in direction —
release points **outward** (to users / the trunk), learn points **backward-then-forward** (mine
what happened → seed the next cycle). This is the loop-closing arrow that makes "compounding"
possible; without it the lifecycle is a line, not a loop.

It is plausibly the **first genuinely new SDLC stage the agent era adds** — not a rename of a
classic phase (align/plan/implement/validate/release all have pre-AI analogues) but an activity
that only becomes first-class once learnings can be written in a **machine-consumable form the
next agent reads automatically**. Traditional teams held retrospectives; few *institutionalized*
the output as executable grounding. That is what changes here.

## Implemented by (backlinks)

Compound Engineering:

- [[ce-compound]] — mine completed work with a research council and write reusable learnings to `docs/solutions/` → [[artifact-solution-doc]] ([[pattern-knowledge-compounding]]).
- [[ce-compound-refresh]] — keep the `docs/solutions/` corpus healthy over time (Keep/Update/Consolidate/Replace/Delete) → [[artifact-solution-doc]].
- [[ce-explain]] — turn concepts, diffs, or recent work into dense visual explainers → [[artifact-explainer]] (a human-facing learning artifact; the personal-knowledge cousin of compounding).

BMAD:

- [[bmad-retrospective]] — post-epic Party-Mode review to extract lessons and action items future sprints surface ([[pattern-persona-agents]]). BMAD's learning close-out; moved here from [[stage-release]] on 2026-07-04.

gstack (both flavors — the third framework):

- [[gstack-learn]] — manage the cross-session learnings corpus (patterns/pitfalls/preferences) future sessions read → [[artifact-solution-doc]] (agent-grounding flavor; [[pattern-knowledge-compounding]]).
- [[gstack-retro]] — team-aware weekly retrospective (per-person breakdowns, streaks) → [[artifact-retrospective]] (team-process flavor).
- [[gstack-skillify]] — codify a successful run into a permanent browser-skill; the agent *gains a capability* (a novel capability-compounding form).
- [[gstack-setup-gbrain]] · [[gstack-sync-gbrain]] — the persistent cross-machine memory substrate the learnings compound into (enabling).

Superpowers (capability-compounding flavor):

- [[sp-writing-skills]] — codify a proven technique into a permanent, auto-triggering skill ([[artifact-skill-doc]]) via **TDD-for-documentation** (baseline a subagent failing → write the skill → watch it comply); the library grows itself ([[pattern-knowledge-compounding]]). The direct counterpart to [[gstack-skillify]] — both make *the agent gain a capability* the learn output, rather than a lesson it reads.

## Two flavors of "learn" in the evidence

- **Agent-grounding corpus (Compound Engineering; gstack).** Machine-consumable learnings written
  where future *agents* auto-read them ([[artifact-solution-doc]]); the corpus itself is a
  maintained artifact ([[ce-compound-refresh]]) or a searchable cross-session store ([[gstack-learn]]
  + gbrain). This is the sharpest, most novel form. gstack and Superpowers extend it with **capability
  compounding** — [[gstack-skillify]] turns a successful run into a permanent skill, and Superpowers'
  [[sp-writing-skills]] authors new auto-triggering skills test-first → [[artifact-skill-doc]] (the
  library grows itself).
- **Team-process retrospective (BMAD; gstack).** A human-facing report extracting lessons and
  action items for future *sprints* → [[artifact-retrospective]] ([[bmad-retrospective]],
  [[gstack-retro]]). The traditional agile form, agent-facilitated.

Same generic activity (harvest lessons → fold into a durable form that improves future
iterations); different consumers (agents vs the human team). gstack is the first framework to
ship **both** flavors.

## Cross-framework equivalents

The **learning-capture** cluster: Compound Engineering's [[ce-compound]] ↔ BMAD's
[[bmad-retrospective]] — both close the iteration by harvesting what was learned so the next
one starts ahead. They are *not* set as `equivalent_to` edges: the terminal acts differ (a
maintained agent-readable corpus vs a one-off human retrospective), like the release cluster's
deliberately-unclustered flavors.

> **Spec-flavored cousin in OpenSpec.** [[openspec-sync]] merges a completed change's
> [[artifact-spec-delta]] into the [[pattern-living-specification|living spec]] so future work
> builds on it — arguably *compounding knowledge at the spec level*. It is kept under
> [[stage-release]] because its primary act is **finalization** (retire the change), not lesson
> extraction; noted here as the third angle on "fold what you learned back in." If a framework
> ships a dedicated spec-learning step distinct from archival, revisit.

## See Also
- [[stage-release]] — the sibling close-out stage; learn was split out of it. Release delivers; learn compounds.
- [[stage-align]] · [[stage-plan]] · [[stage-review]] — the stages that *consume* this stage's output as grounding, closing the loop.
- [[pattern-knowledge-compounding]] — the technique behind the stage (each unit of work leaves reusable lessons for the next).
- [[compound-engineering]] · [[bmad]] — the frameworks implementing this stage.
