---
type: capability
subtype: skill
belongs_to: "[[builder-skills]]"
implements: "[[stage-plan]]"
delegates_to: []
produces: ["[[artifact-plan-md]]"]
applies: ["[[pattern-candidate-grafting]]", "[[pattern-cross-model-review]]", "[[pattern-evidence-before-claims]]"]
equivalent_to: []
sources: "Builder.io — BuilderIO/skills, MIT (2026)"
raw: ["../../raw/builder-skills/2026-09-26-builder-skills.md"]
updated: 2026-09-26
---
# /plan-arbiter

Turn competing plans from several agents (*"such as Codex and Claude Code"*) into **one executable direction**. It aims to *"produce a clear handoff instead of a blended mush."*

Five steps: collect the source plans (resolving the original artifacts where possible, *"so you can see prompt changes and assumptions that may be missing from a final summary"*); normalize each into comparable claims (objective, assumptions, touched surfaces, sequence, validation, rollback, cost, executor fit); cross-review them against each other and the real codebase; decide; and hand off. *"Do not reward verbosity."*

There are three outcomes: **Adopt**, **Hybrid**, and **Revise first**. The tie-break order is correctness and fit, then grounding in real files, then a simpler first cut, then a better validation and rollback story, then lower execution cost. It deliberately separates **plan quality from executor choice**: *"A cheaper/faster executor can be the right choice for implementation even when another model produced the best critique."* The decision memo has sections for Decision, Why, Execution Plan, **Borrowed From Other Plans**, **Rejected**, Verification, and **Executor Recommendation**.

The *Borrowed From Other Plans* section makes this a planning-stage instance of [[pattern-candidate-grafting]]: keep the pieces of the losing plans worth keeping instead of discarding them. It differs from [[pstack-arena]], which generates its own candidates. The arbiter judges candidates that independent agents produced. Read-only unless execution was asked for.

## See Also
- [[pstack-arena]] — generate N candidates and graft the losers; the arbiter judges candidates it did not generate.
- [[builder-agent-watchdog]] — the same stance, applied to finished work.
- [[stage-plan]] — the canonical stage this implements.
