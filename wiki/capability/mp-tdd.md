---
type: capability
subtype: skill
belongs_to: "[[matt-pocock-skills]]"
implements: "[[stage-implement]]"
delegates_to: []
produces: []
applies: ["[[pattern-test-driven-development]]"]
equivalent_to: ["[[addy-tdd]]", "[[sp-test-driven-development]]"]
docs_url: "https://www.aihero.dev/skills-tdd"
sources: "Matt Pocock — Skills for Real Engineers v1.1 (2026)"
raw: ["../../raw/matt-pocock-skills/2026-07-09-skills-v1.1-update.md"]
updated: 2026-07-09
---

# tdd

A **model-invoked** engineering skill that drives a test-first loop for features and bugs (see [[pattern-test-driven-development]]). One of the feedback-loop answers to failure mode #3 ("the code doesn't work"): a failing test first gives the agent ground truth before it writes implementation.

> **Reshaped in v1.1 (2026-07-09) to reference-only, red → green.** The step-by-step workflow was dropped (the loop is anchored by leading words the model already holds) and **the refactor stage moved out to [[mp-code-review]]** — TDD is now red → green; refactoring belongs to review. The leading word for *where tests go* is **seam**: test only at pre-agreed seams, confirmed with the user before any test is written. Two anti-patterns are emphasised — implementation-coupled tests and **tautological tests** (assertions recomputed the way the code computes them, so they pass by construction). It is driven by [[mp-implement]] at those seams.

GSD offers the same discipline as a flag on its planner (`gsd-plan-phase --tdd`); the shared technique is clustered at [[pattern-test-driven-development]].

## See Also
- [[mp-implement]] — drives this loop at pre-agreed seams.
- [[mp-code-review]] — now owns the refactor stage TDD dropped.
- [[mp-diagnosing-bugs]] — the debugging counterpart feedback loop.
- [[gsd-plan-phase]] — GSD's `--tdd` mode.
- [[addy-tdd]] — Addy's TDD skill; same red-green discipline.
- [[stage-implement]] — the canonical stage this implements.
