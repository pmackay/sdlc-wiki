---
type: sdlc-stage
aka: { bmad: "retrospective (learning close-out)", compound-engineering: "compound", gstack: "Reflect (retro + learn)", superpowers: "writing-skills (capability-compounding)", seeds: "plan outcome (storage-only)", pstack: "reflect / automate-me / teach", builder-skills: "factory-lookback / turn-into-app", matt-pocock-skills: "retro (environment retrospective)" }
sources: "Synthesized from BMAD + Compound Engineering + gstack + Superpowers + Seeds + Builder Skills + Matt Pocock (2026); spec-flavor cousin in OpenSpec"
updated: 2026-10-11
---

# Stage: Learn

Canonical lifecycle stage: **harvest the learnings from completed work — bugs, failed tests, reusable solutions, process lessons — and fold them into a durable, reusable form so future iterations start ahead.** The output is not the shipped software (that is [[stage-release]]) but *knowledge*: a solution corpus, a retrospective's action items, or an updated living spec. Its defining property is that its product is **consumed by the front of the next loop** — [[stage-align]], [[stage-plan]], and [[stage-review]] read it as grounding — closing the loop rather than ending it.

**Derived projection** — evidence is the capabilities that `implements: [[stage-learn]]`.

> **New stage (promoted 2026-07-04); now beyond doubt — three frameworks (2026-07-05).** Was folded into [[stage-release]] as its "learning close-out" flavor (BMAD-only, single-framework). Compound Engineering made learning capture a **first-class, named step of its own loop** (`/ce-compound` is *"the money step… the whole point"*), giving the activity a **second framework** and clearing the ≥2-framework bar the [conventions](../CONVENTIONS.md#stage-re-derivation-keep-stages-framework-neutral) require — exactly as [[stage-specify]] was split out of [[stage-plan]]. **gstack (2026-07-05) is the third framework**, and the first to populate *both* flavors at once: its *Reflect* sprint phase ships [[gstack-retro]] (team retrospective) **and** [[gstack-learn]] (an agent-grounding learnings corpus), plus [[gstack-skillify]] (compound a successful run into a permanent skill). Split cleanly out of release: *release* delivers the work; *learn* extracts the reusable knowledge. See [Why a distinct stage](#why-a-distinct-stage-not-a-flavor-of-release). **Superpowers (2026-07-17) is a fourth framework**, purely in the capability-compounding flavor: [[sp-writing-skills]] turns a proven technique into a permanent auto-triggering skill (↔ [[gstack-skillify]]).

## Why a distinct stage, not a flavor of release

[[stage-release]] finalizes and delivers a completed unit (ship-to-prod, or merge-the-spec). Learn does something categorically different: it treats the *just-completed work as a source of training data* and produces an artifact whose only purpose is to make **future** work better. The two are adjacent in time (both close the iteration) but opposite in direction — release points **outward** (to users / the trunk), learn points **backward-then-forward** (mine what happened → seed the next cycle). This is the loop-closing arrow that makes "compounding" possible; without it the lifecycle is a line, not a loop.

It is plausibly the **first genuinely new SDLC stage the agent era adds** — not a rename of a classic phase (align/plan/implement/validate/release all have pre-AI analogues) but an activity that only becomes first-class once learnings can be written in a **machine-consumable form the next agent reads automatically**. Traditional teams held retrospectives; few *institutionalized* the output as executable grounding. That is what changes here.

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

Seeds — a [store](../store/index.md) (and a stub, recorded because the gap is instructive):

- [[seeds-plan-outcome]] — record a plan's `success | partial | failure` result. Storage-only by design: *"aggregation and retros are out of scope and left to teams."* Nothing reads it but a `--outcome` filter on [[seeds-plan-list]]. The framework's own thesis argues for closing the loop — a failure should become a new section or validation rule in the plan template — but seeds records the datum and stops, delegating the compounding to mulch, which [[seeds-plan-prompt]] reads back in as prior art on the next plan. The lesson-to-template step no capability performs is the clearest missing link this stage has.

pstack (all three flavors — targeted skill edit, personal mode skill, and human explainer):

- [[pstack-reflect]] — three parallel review lenses over the transcript, synthesized into Accepted / Rejected / Backlog and routed to concrete edits on **existing** skills → [[artifact-skill-doc]]. Its structural-enforcement check *demotes* any accepted learning better served by a lint rule, script, or runtime check, which is a built-in brake on prose accretion.
- [[pstack-automate-me]] — mines the user's own transcripts into a personal `-mode` skill, updating in place across runs and preserving sections the user has not contradicted ([[pattern-knowledge-compounding]]).
- [[pstack-teach]] — explains a change or subsystem so a person understands it, built up diagram by diagram → [[artifact-explainer]] (the human-facing flavor; counterpart to [[ce-explain]]).

builder-skills:

- [[builder-factory-lookback]] — a bounded retrospective over production signal: recurrence after a claimed fix, sibling-path escapes, and one systemic correction at the shared boundary → [[artifact-retrospective]]. The first instance of a **third flavor** of this stage (see below).
- [[builder-turn-into-app]] — packages a proven thread or skill into a runnable app; the counterpart of [[gstack-skillify]] and [[pstack-automate-me]] with an app for people as the output rather than a skill for agents.

Matt Pocock — Skills for Real Engineers (environment-compounding flavor; added 2026-10-11):

- [[mp-retro]] — a retrospective on one coding session (current by default, or a past one found in the machine's session logs) that suggests changes to the agent's **environment**, not the code: navigation pointers, automated checks, coding standards, steering files, tool economy, information access. Candidates are presented in severity order. Its standards rule is the sharp one: a **mechanical** violation "gets a deterministic check, full stop" (linter rule, pre-commit hook, or CI job), and `CODING_STANDARDS.md` ([[artifact-standards]]) is kept for judgement calls. v1.3.0 routes it as the **last step of MP's main flow** and v1.3.1 as the follow-up to [[mp-diagnosing-bugs]]. It is MP's first capability on this stage, which the wiki had listed as a gap since 2026-06-28.

## Flavors of "learn" in the evidence

- **Agent-grounding corpus (Compound Engineering; gstack).** Machine-consumable learnings written where future *agents* auto-read them ([[artifact-solution-doc]]); the corpus itself is a maintained artifact ([[ce-compound-refresh]]) or a searchable cross-session store ([[gstack-learn]]
  + gbrain). This is the sharpest, most novel form. gstack and Superpowers extend it with **capability compounding** — [[gstack-skillify]] turns a successful run into a permanent skill, and Superpowers' [[sp-writing-skills]] authors new auto-triggering skills test-first → [[artifact-skill-doc]] (the library grows itself).
- **Team-process retrospective (BMAD; gstack).** A human-facing report extracting lessons and action items for future *sprints* → [[artifact-retrospective]] ([[bmad-retrospective]], [[gstack-retro]]). The traditional agile form, agent-facilitated.

- **Environment compounding (Matt Pocock; pstack in part).** The lesson is written into the agent's *harness*, the checks, standards, pointers and tooling the next session runs inside, rather than into a corpus it reads or a report people read ([[mp-retro]]). It is the stage's most explicitly **computational** flavor: mechanical findings become lint rules, hooks, or CI jobs. [[pstack-reflect]]'s structural-enforcement demotion is the same instinct applied to skill edits.

Same generic activity (harvest lessons → fold into a durable form that improves future iterations); different consumers (agents vs the human team). gstack is the first framework to ship **both** flavors.

**A third flavor, added 2026-09-26: production-signal learning ([[builder-skills]]).** [[builder-factory-lookback]] harvests lessons from neither an agent session nor a sprint. It learns from **the product's behaviour in the field**: a bounded history of user feedback, telemetry, runtime errors, recurring CI failures, and prior fixes marked shipped. It asks why the same class of problem keeps coming back. The output is a structural change at a shared boundary plus a regression check, and the lookback is only finished when *"the live recurrence stopped."* The consumer is the codebase itself rather than future agents or the team. It is recorded as a flavor rather than a split because the evidence is one framework ([[ce-product-pulse]] reports post-release signal but, filed under [[stage-release]], looks for no causes), well under the ≥2-framework bar.

## Cross-framework equivalents

The **learning-capture** cluster: Compound Engineering's [[ce-compound]] ↔ BMAD's [[bmad-retrospective]] — both close the iteration by harvesting what was learned so the next one starts ahead. They are *not* set as `equivalent_to` edges: the terminal acts differ (a maintained agent-readable corpus vs a one-off human retrospective), like the release cluster's deliberately-unclustered flavors.

> **Spec-flavored cousin in OpenSpec.** [[openspec-sync]] merges a completed change's [[artifact-spec-delta]] into the [[pattern-living-specification|living spec]] so future work builds on it — arguably *compounding knowledge at the spec level*. It is kept under [[stage-release]] because its primary act is **finalization** (retire the change), not lesson extraction; noted here as the third angle on "fold what you learned back in." If a framework ships a dedicated spec-learning step distinct from archival, revisit.

## See Also
- [[stage-release]] — the sibling close-out stage; learn was split out of it. Release delivers; learn compounds.
- [[stage-align]] · [[stage-plan]] · [[stage-review]] — the stages that *consume* this stage's output as grounding, closing the loop.
- [[pattern-knowledge-compounding]] — the technique behind the stage (each unit of work leaves reusable lessons for the next).
- [[compound-engineering]] · [[bmad]] · [[matt-pocock-skills]] — frameworks implementing this stage; [[seeds]] contributes a store-side stub.
- [[beads-remember]] · [[beads-audit]] — the [store layer](../store/index.md) does the *storing* half of compounding without a Learn capability: durable memories auto-primed into every session, and labelled interaction traces kept for fine-tuning. Neither harvests a lesson, which is why neither implements this stage.
- [[warren]] — the runtime whose `.mulch/` store is where the seeds half of this loop actually compounds.
