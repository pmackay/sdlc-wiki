---
type: capability
subtype: skill
belongs_to: "[[matt-pocock-skills]]"
implements: "[[stage-align]]"
delegates_to: []
produces: []
applies: ["[[pattern-grilling]]"]
equivalent_to: []
sources: "Matt Pocock — Skills for Real Engineers v1.1 (2026)"
raw: ["../../raw/matt-pocock-skills/2026-07-09-skills-v1.1-update.md"]
updated: 2026-07-09
---

# grilling

A **model-invoked** productivity skill: the reusable interview loop that underlies both
[[mp-grill-me]] and [[mp-grill-with-docs]]. It is the canonical implementation of
[[pattern-grilling]] — keep asking until decision branches resolve — factored out so other
skills compose it rather than re-implement it.

> **Sharpened in v1.1 (2026-07-09) on two fronts.** (1) A **confirmation gate**: the agent won't
> enact the plan until the user confirms shared understanding has been reached. (2) **Facts vs.
> decisions**: *facts* get looked up (explore the codebase), *decisions* are put to the human and
> wait for an answer — so when another skill (e.g. [[mp-wayfinder]] or [[mp-triage]]) runs grilling
> inside a resolve-the-ticket frame, the agent can't race ahead and answer its own decisions (the
> HITL guarantee).

## See Also
- [[mp-grill-me]], [[mp-grill-with-docs]] — the user-facing skills built on this loop.
- [[stage-align]] — the canonical stage this implements.
