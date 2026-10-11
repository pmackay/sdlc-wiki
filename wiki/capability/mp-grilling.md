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

A **model-invoked** productivity skill: "Grill the user relentlessly about a plan, decision, or idea." It is the reusable interview loop that underlies both [[mp-grill-me]] and [[mp-grill-with-docs]], and the canonical implementation of [[pattern-grilling]] — keep asking until decision branches resolve — factored out so other skills compose it rather than re-implement it.

## How it works

- **Round by round over the frontier.** It maps the decision tree and asks the whole **frontier** (every question whose prerequisites are already settled) in one numbered round, then recomputes the frontier from the answers and asks the next round. "Same 13 questions land in ~3 rounds instead of 13." The session ends when the frontier is empty. A global `CLAUDE.md` line opts back into one-question-at-a-time.
- **Facts vs. decisions.** *Facts* the environment can answer are looked up, dispatched to **background sub-agents** so research never blocks a round; only questions downstream of a running exploration wait for it. *Decisions* are put to the human and wait for an answer, so when another skill (e.g. [[mp-wayfinder]] or [[mp-triage]]) runs grilling inside a resolve-the-ticket frame, the agent can't race ahead and answer its own decisions (the HITL guarantee).
- **Confirmation gate.** The agent won't act on it until the user confirms shared understanding has been reached.
- **Fixed question shape.** Each question is `❓ **Q1** - **<title>**`, then the body (prose or multiple choices), then the recommendation on its own `➡️` line; questions in a round are separated by `---`. A round reads as a scannable numbered list you can answer by number.

[[mp-grill-me]], [[mp-grill-with-docs]] and [[mp-triage]] all run the frontier a round at a time. The **frontier** leading word recurs in [[mp-implement-spec]] (the ready tickets in a task graph).

## See Also
- [[mp-grill-me]], [[mp-grill-with-docs]] — the user-facing skills built on this loop.
- [[mp-to-questionnaire]] — the inverse: grills the *send* when the answers live in someone else's head.
- [[stage-align]] — the canonical stage this implements.

## Version history

### v1.3.0 (2026-10-04)
- Questions in a round are separated by a horizontal rule (`---`); em-dashes removed from the skill text.

### v1.2.0 (2026-08-05)
- Reworked from one-question-at-a-time to **round-by-round over the frontier**, with facts dispatched to background sub-agents and a fixed `❓` / `➡️` question shape.
- Reworded for general use: "this plan" → "this", "exploring the codebase" → "exploring the environment"; the description now covers "a plan, decision, or idea" rather than only a plan.

### v1.1.0 (2026-07-08; ingested 2026-07-09)
- Added the **confirmation gate** and the **facts vs. decisions** split (the HITL guarantee).

### Initial ingest (2026-06-28)
- Paged as the reusable interview loop behind the grill skills, asking one question at a time.
