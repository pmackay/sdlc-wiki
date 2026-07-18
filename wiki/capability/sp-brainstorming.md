---
type: capability
subtype: skill
belongs_to: "[[superpowers]]"
implements: "[[stage-align]]"
delegates_to: ["[[sp-writing-plans]]"]
produces: ["[[artifact-design-md]]"]
applies: ["[[pattern-grilling]]"]
equivalent_to: ["[[gsd-discuss-phase]]", "[[mp-grill-me]]", "[[addy-interview-me]]", "[[ce-brainstorm]]", "[[gstack-office-hours]]"]
sources: "Superpowers v6.1.1 (2026)"
raw: ["../../raw/superpowers/2026-07-17-superpowers.md"]
updated: 2026-07-17
---

# brainstorming

The front of the pipeline: turn a rough idea into a validated design through **natural collaborative
dialogue** before writing any code ([[pattern-grilling]]). Explore project context → ask clarifying
questions **one at a time** (multiple-choice preferred) → propose **2-3 approaches** with trade-offs
and a recommendation → present the design **in sections**, getting approval after each → write the
design doc → self-review → user-review gate → hand off to [[sp-writing-plans]].

> **HARD-GATE:** *"Do NOT invoke any implementation skill, write any code, scaffold any project, or
> take any implementation action until you have presented a design and the user has approved it."*
> Explicitly rejects the "this is too simple to need a design" excuse — every project, even a config
> change, goes through the gate ([[pattern-anti-rationalization]]). The design can be short, but it
> must be presented and approved.

Distinctive details: an optional browser-based **visual companion** offered *just-in-time* (only when
a question is genuinely clearer shown than told, never upfront); a design-for-isolation principle
(decompose into small, single-purpose, independently-testable units); and a strict **terminal state**
— the *only* skill it may invoke next is [[sp-writing-plans]] (never a frontend/implementation skill).
It writes the validated design to `docs/superpowers/specs/YYYY-MM-DD-<topic>-design.md` and commits it
→ [[artifact-design-md]].

Superpowers has **no dedicated [[stage-specify]] capability**: the design doc this skill produces *is*
its spec, and it flows straight into planning — the same align→plan fold as [[gsd]].

## See Also
- [[sp-writing-plans]] — the mandated next step (the design's terminal handoff).
- [[gsd-discuss-phase]] · [[mp-grill-me]] · [[addy-interview-me]] · [[ce-brainstorm]] · [[gstack-office-hours]] — the align/grilling cluster across frameworks.
- [[pattern-grilling]] — the Socratic elicitation technique.
- [[artifact-design-md]] — the design doc it produces.
- [[stage-align]] — the canonical stage this implements.
