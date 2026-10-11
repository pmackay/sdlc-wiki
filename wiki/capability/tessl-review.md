---
type: capability
subtype: command
belongs_to: "[[tessl]]"
implements: []
delegates_to: []
produces: ["[[artifact-review-report]]", "[[artifact-standards]]"]
applies: ["[[pattern-deterministic-gates]]", "[[pattern-adversarial-review]]"]
equivalent_to: []
sources: "Tessl docs — CLI v0.108.0 (2026)"
raw: ["../../raw/tessl/2026-09-12-tessl-platform.md"]
updated: 2026-09-12
---

# tessl review

Score a skill against a rubric: `review run`, `review view`, `review list`, `review retry`. Three scored areas — **validation** (structure and format), **description** (how well the description triggers the skill at the right time), and **content** (how well the instructions guide the agent once loaded).

It is deliberately the *cheap* instrument of a pair, and [[tessl]] is careful about the distinction: **a review tells you whether a skill is well written; an [[tessl-eval|eval]] tells you whether it works.** A review is fast, structural, runs automatically on publish, and is explicitly compared to *"static analysis for code"*. Reach for it for quick structural feedback; reach for the eval when you need evidence of effect.

**The description score is the one with no code analogue.** In a skill, the description is not documentation — it is the trigger condition the agent matches a task against, so a badly written description means a correct skill that never loads. Scoring it separately from the content is a recognition that a capability has two independent failure modes: never firing, and firing badly.

Two mechanisms make it governance rather than advice. `review run --threshold` **fails the build** below a score, so substandard skills never merge ([[pattern-deterministic-gates]]); and the default rubric is **forkable**, so an organization encodes its own bar as a versioned artifact and applies it to every review → [[artifact-standards]]. *"When a team shares skills, quality stops being a personal matter. A weak skill that one person tolerates becomes everyone's problem once it is in the shared repository, shaping how every agent on the team behaves."*

## See Also
- [[tessl-eval]] — the expensive sibling that measures effect rather than form.
- [[tessl-review-security]] — the safety scan run alongside the quality score.
- [[tessl-review-fix]] — iterates a skill until it clears the threshold.
- [[artifact-review-report]] — the output.
