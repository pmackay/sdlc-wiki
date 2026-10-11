---
type: capability
subtype: skill
belongs_to: "[[matt-pocock-skills]]"
implements: "[[stage-align]]"
delegates_to: []
produces: []
applies: ["[[pattern-grilling]]"]
equivalent_to: []
docs_url: "https://www.aihero.dev/skills-grilling"
sources: "Matt Pocock — Skills for Real Engineers v1.1 (2026); v1.2.0 (2026-08-05)"
raw: ["../../raw/matt-pocock-skills/2026-10-04-skills-v1.3.1-update.md", "../../raw/matt-pocock-skills/2026-07-09-skills-v1.1-update.md"]
updated: 2026-10-11
---

# grilling

A **model-invoked** productivity skill: the reusable interview loop that underlies both [[mp-grill-me]] and [[mp-grill-with-docs]]. It is the canonical implementation of [[pattern-grilling]] — keep asking until decision branches resolve — factored out so other skills compose it rather than re-implement it.

> **Sharpened in v1.1 (2026-07-09) on two fronts.** (1) A **confirmation gate**: the agent won't enact the plan until the user confirms shared understanding has been reached. (2) **Facts vs. decisions**: *facts* get looked up (explore the codebase), *decisions* are put to the human and wait for an answer — so when another skill (e.g. [[mp-wayfinder]] or [[mp-triage]]) runs grilling inside a resolve-the-ticket frame, the agent can't race ahead and answer its own decisions (the HITL guarantee).

> **Reworked in v1.2.0 (2026-08-05): round-by-round, not one-question-at-a-time.** It now maps the decision tree and asks the whole **frontier** (every question whose prerequisites are already settled) in one numbered round, then recomputes the frontier from the answers and asks the next round. "Same 13 questions land in ~3 rounds instead of 13." Facts the environment can answer go to **background sub-agents**, so research never blocks a round; only questions downstream of a running exploration wait for it. The session ends when the frontier is empty. Each question has a fixed shape (`❓ **Q1** - **<title>**`, the body, then the recommendation on its own `➡️` line), and since v1.3.0 rounds are separated by `---`. The description was also generalised from "a plan" to "a plan, decision, or idea". [[mp-grill-me]], [[mp-grill-with-docs]] and [[mp-triage]] all run the frontier a round at a time; a global `CLAUDE.md` line still opts back into one-at-a-time. The **frontier** leading word recurs in [[mp-implement-spec]] (the ready tickets in a task graph).

## See Also
- [[mp-grill-me]], [[mp-grill-with-docs]] — the user-facing skills built on this loop.
- [[stage-align]] — the canonical stage this implements.
- [[mp-to-questionnaire]] — the inverse: grills the *send* when the answers live in someone else's head.
