---
type: sdlc-stage
aka: { gsd: "Discuss", matt-pocock-skills: "grilling / grill-me / triage", addy-agent-skills: "Define / interview-me", openspec: "explore", speckit: "clarify / constitution", bmad: "Analysis (brainstorm / forge-idea / research)", compound-engineering: "brainstorm / ideate / strategy", gstack: "Think (office-hours)", superpowers: "brainstorming" }
sources: "Synthesized from GSD + Matt Pocock + Addy Osmani + OpenSpec + Spec Kit + BMAD + Compound Engineering + gstack + Superpowers (2026)"
updated: 2026-07-17
---

# Stage: Align

Canonical lifecycle stage: **align on what to build and why before implementation** —
close the human↔agent gap, capture and lock decisions. Framework-neutral name (was
`stage-discuss`, GSD's term). GSD calls it "Discuss", Matt Pocock "grilling", Addy
"interview-me", OpenSpec "explore", Spec Kit "clarify". Sits at the front of the loop, ahead
of [[stage-specify]] and [[stage-plan]]. In the pre-spec arc (explore → shape → execute),
this is the *shape* step.

Alignment *flavors* now show up in the evidence: GSD, Matt, Addy, and Spec Kit align by
**interrogating the human** ([[pattern-grilling]]), whereas OpenSpec's [[openspec-explore]]
aligns by **investigating the codebase and comparing approaches** before committing — the
*explore* sub-step of the arc (the counterpart to Addy's [[addy-idea-refine]] ideation). Same
canonical stage; complementary techniques. Spec Kit's [[speckit-clarify]] grills *after* the
spec is drafted (resolving `[NEEDS CLARIFICATION]` markers) rather than before — a sequencing
variation, not a different stage. **BMAD (sixth framework) is the first to populate *all three*
flavors at once**: it grills via the facilitator stance ([[bmad-analyst]]), investigates via
[[bmad-document-project]], ideates via [[bmad-brainstorming]], and adds a pronounced
**adversarial pressure-testing** sub-flavor ([[bmad-forge-idea]], [[bmad-prfaq]]) that hardens
an idea before it is specified. A further flavor — **establishing governing principles**
([[speckit-constitution]]) — appears in only one framework and is parked below as a split
candidate.

This page is a **derived projection** — its evidence is the capabilities that
`implements: [[stage-align]]`.

## Implemented by (backlinks)

GSD:

- [[gsd-discuss-phase]] — adaptive questioning, codebase scouting, decision capture → [[artifact-context-md]].

Matt Pocock — Skills for Real Engineers:

- [[mp-grill-me]] — comprehensive interview until decisions resolve.
- [[mp-grilling]] — the reusable interview loop.
- [[mp-grill-with-docs]] — grilling that also writes a domain model + ADRs.
- [[mp-triage]] — move issues/PRs through a triage state machine → agent-ready briefs (intake flavor; v1.1); the intake counterpart to Compound Engineering's [[ce-sweep]].

Addy Osmani — Agent Skills:

- [[addy-interview-me]] — one-question-at-a-time interview to ~95% intent confidence.
- [[addy-idea-refine]] — divergent/convergent ideation (the *explore* sub-step).

OpenSpec:

- [[openspec-explore]] — investigate the codebase and compare approaches before committing.

Spec Kit:

- [[speckit-clarify]] — iterative dialogue that resolves the spec's `[NEEDS CLARIFICATION]` markers.
- [[speckit-constitution]] — establish immutable project governing principles (governance flavor; see split candidate).

BMAD:

- [[bmad-analyst]] — the Analysis persona (Mary); facilitator-stance elicitation over the align workflows.
- [[bmad-tech-writer]] — captures project knowledge for AI context.
- [[bmad-brainstorming]] — diverge-then-converge ideation (ideation flavor).
- [[bmad-forge-idea]] — adversarial pressure-testing of an idea until it hardens or dies cheaply.
- [[bmad-prfaq]] — Working-Backwards customer-first stress-test → [[artifact-product-brief]].
- [[bmad-research]] — market / domain / technical research → [[artifact-research-md]].
- [[bmad-product-brief]] — the pre-PRD scoping document → [[artifact-product-brief]].
- [[bmad-document-project]] — brownfield codebase investigation (codebase-investigation flavor).

Compound Engineering:

- [[ce-brainstorm]] — dialogue that defines requirements-only → [[artifact-brainstorm-md]] (grilling flavor).
- [[ce-ideate]] — conceptual-frame + adversarial-filter idea discovery (ideation flavor).
- [[ce-pov]] — decisive Adopt/Trial/Hold/Reject verdict on external inputs (evaluate-and-decide flavor).
- [[ce-strategy]] — maintain the `STRATEGY.md` upstream anchor → [[artifact-strategy-md]] (governance/strategy flavor; feeds the `stage-govern` candidate).
- [[ce-sweep]] — consolidate external feedback (Slack/GitHub) into inputs for the next cycle (feedback-intake flavor).

gstack (grilling flavor):

- [[gstack-office-hours]] — YC-Office-Hours reframing with six forcing questions; challenges premises and generates implementation alternatives → [[artifact-product-brief]] ([[pattern-grilling]], [[pattern-source-grounding]]). The design doc it writes feeds gstack's plan reviews.

Superpowers (grilling flavor):

- [[sp-brainstorming]] — Socratic one-question-at-a-time refinement; proposes 2-3 approaches; presents the design in sections for approval; HARD-GATE before any implementation → [[artifact-design-md]] ([[pattern-grilling]]). Its design doc folds straight into [[sp-writing-plans]] (Superpowers has no separate [[stage-specify]] capability, like GSD).

## Cross-framework equivalents
Nine frameworks now realize this stage. The **grilling / elicitation** cluster (interrogate
the human) spans GSD's [[gsd-discuss-phase]] ↔ Matt's [[mp-grill-me]] ↔ Addy's
[[addy-interview-me]] ↔ Spec Kit's [[speckit-clarify]] ↔ Compound Engineering's [[ce-brainstorm]]
↔ gstack's [[gstack-office-hours]] ↔ Superpowers' [[sp-brainstorming]], plus BMAD's facilitator personas, at [[pattern-grilling]]. The **codebase-investigation** flavor
clusters OpenSpec's [[openspec-explore]] ↔ Addy's [[addy-idea-refine]] ↔ BMAD's
[[bmad-document-project]]. The **ideation** flavor clusters [[addy-idea-refine]] ↔
[[bmad-brainstorming]] ↔ [[ce-ideate]]. Compound Engineering adds an **evaluate-external-inputs**
sub-flavor ([[ce-pov]], graded verdicts) with no counterpart elsewhere. Overwhelming evidence
this is a genuine canonical stage, not a framework quirk.

## Split candidates

### stage-govern (establish project-wide governing principles)
- **Distinction:** *govern* = set immutable, cross-cutting principles that later phases are
  mechanically gated against; distinct from aligning on *what to build* for a given change.
- **Evidence so far (one framework — below the ≥2 bar):**
  - Spec Kit **externalizes** principles into [[artifact-constitution]] via
    [[speckit-constitution]] and enforces them through [[speckit-analyze]] and [[speckit-plan]]'s
    "Phase -1" gates (see [[pattern-project-constitution]]).
  - GSD, Matt Pocock, and Addy embed principles *inside individual skills* (Addy's per-skill
    "Red Flags", MP's design heuristics) rather than a standing governing document.
  - OpenSpec has no project-wide charter.
  - BMAD (2026-07-04) does **not** advance it: its `project-context.md` (from
    `bmad-generate-project-context`) and `customize.toml` carry *dev-time rules/conventions* —
    context engineering, not an immutable numbered charter that gates every phase. Principles
    otherwise live inside the [[pattern-persona-agents|personas]].
  - Compound Engineering (2026-07-04) adds a **standing upstream anchor** ([[artifact-strategy-md|STRATEGY.md]]
    via [[ce-strategy]]) that ideate/brainstorm/plan defer to — structurally like a charter, but it
    frames *product direction* (what/why to build) and is *read as context*, not an immutable set
    of principles *mechanically gated* against every artifact. Related flavor, but not the same
    govern activity. Still one framework (Spec Kit) for gated immutable principles.
- **Decisive trigger:** a second framework that ships a dedicated set-the-project-principles
  capability → clears the bar → split into `stage-govern`.

## See Also
- [[stage-specify]] · [[stage-plan]] — the next stages.
- [[gsd]], [[openspec]], [[speckit]] — frameworks implementing this stage.
