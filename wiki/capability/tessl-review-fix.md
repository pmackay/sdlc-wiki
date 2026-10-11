---
type: capability
subtype: command
belongs_to: "[[tessl]]"
implements: []
delegates_to: []
produces: ["[[artifact-skill-doc]]"]
applies: ["[[pattern-autonomous-loop]]", "[[pattern-deterministic-gates]]"]
equivalent_to: []
sources: "Tessl docs — CLI v0.108.0 (2026)"
raw: ["../../raw/tessl/2026-09-12-tessl-platform.md"]
updated: 2026-09-12
---

# tessl review fix

Improve a skill until it clears a score: `tessl review fix --threshold 90 --max-iterations 5`. A find-fix-re-verify loop ([[pattern-autonomous-loop]]) whose target is **a capability rather than a product** — the agent rewrites the instructions, re-scores them, and repeats until the rubric is satisfied or the iteration budget runs out.

Small, and worth a page for what it implies. Once a capability has a machine-readable quality score, improving it becomes an optimization problem an agent can run unattended — the same shape as [[gstack-qa]]'s self-fixing QA loop or [[ce-dogfood]], pointed at the skill corpus. The bounded iteration count and the required confirmation prompt (waived with a flag) are the guardrails on a loop that is, after all, rewriting the instructions every future agent will follow.

The obvious caution is that it optimizes for **the rubric**, not for effect. [[tessl]]'s own framing keeps the two apart: a review checks form, an eval checks whether behavior changed. A skill hill-climbed to 95 on structure that [[tessl-eval]] shows changes nothing is a real outcome, and the framework-side instinct against exactly this failure is [[pstack-principle-test-behavior-not-implementation]].

## See Also
- [[tessl-review]] — supplies the score this climbs.
- [[tessl-eval]] — the check that the climb was worth anything.
- [[pattern-autonomous-loop]] — the technique, aimed at a capability.
