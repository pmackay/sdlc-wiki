---
type: pattern
sources: "Matt Pocock — Skills for Real Engineers (2026); Open GSD docs (2026); Addy Osmani — Agent Skills (2026); bmad-code-org/BMAD-METHOD (2026); obra/superpowers (2026); jayminwest/seeds (2026); gastownhall/beads (2026); pstack v0.15.2 — Lauren Tan (2026)"
updated: 2026-09-11
---

# Pattern: Vertical slice

Decompose work into units that each cut top-to-bottom through the stack (UI → API → DB) so every unit is independently buildable, shippable, and demoable — rather than horizontal layers that only deliver value once all are complete.

## Applied by (backlinks)

Matt Pocock — Skills for Real Engineers:

- [[mp-to-tickets]] — produces "independently-grabbable" vertical-slice issues.

GSD:

- [[gsd-plan-phase]] — `--mvp` mode plans vertical slices (UI→API→DB).

Addy Osmani — Agent Skills:

- [[addy-planning]] — breaks work into independently shippable slices.
- [[addy-incremental-implementation]] — builds one slice at a time, top-to-bottom.

BMAD:

- [[bmad-create-epics-and-stories]] — decomposes requirements into epics of independently shippable stories.
- [[bmad-create-story]] — each [[artifact-story|story]] is one self-contained, shippable slice, built one at a time.

Compound Engineering:

- [[ce-work]] — executes the guardrailed plan slice-by-slice through quality gates.

Superpowers:

- [[sp-writing-plans]] — each task is the smallest unit that carries its own test cycle and is worth a reviewer's gate — an independently testable slice.

Seeds:

- [[seeds-plan-submit]] — the `steps` section's own instruction is the rule: *"Decompose into ordered, independent implementation steps"*, each becoming exactly one child seed.
- [[seeds-dep]] — wires the ordering between those slices, with an explicit warning against over-wiring, since every unnecessary edge hides work from [[seeds-ready]].

Beads:

- [[beads-mol]] — a poured molecule is a set of independently-claimable, dependency-ordered beads, one per formula step; the slicing is inherited from the template rather than reasoned out per task.

pstack:

- [[pstack-principle-sequence-verifiable-units]] — break work into small units that each end in a verifiable state, check each before the next, and **order delivery so the sequence proves itself to a reviewer**. That third clause treats sequencing as a review affordance rather than only an execution tactic, and it governs how commits and PRs are stacked as well as how work is decomposed.
- [[pstack-figure-it-out]] — decompose into atomic, independently-landable units, sequenced riskiest-unknown-first, each run as an experiment with a verdict before the next begins.

## See Also
- [[artifact-issue]] — how Matt's skills materialize a slice.
- [[stage-plan]] — the stage where this applies.
