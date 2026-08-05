---
type: capability
subtype: skill
belongs_to: "[[matt-pocock-skills]]"
implements: "[[stage-align]]"
delegates_to: ["[[mp-grilling]]"]
produces: []
applies: ["[[pattern-grilling]]"]
equivalent_to: ["[[addy-interview-me]]", "[[gsd-discuss-phase]]", "[[speckit-clarify]]", "[[ce-brainstorm]]", "[[gstack-office-hours]]", "[[sp-brainstorming]]"]
docs_url: "https://www.aihero.dev/skills-grill-me"
sources: "Matt Pocock — Skills for Real Engineers (2026)"
raw: ["../../raw/matt-pocock-skills/2026-06-28-skills-for-real-engineers.md"]
updated: 2026-07-04
---

# grill-me

`/grill-me` — a user-invoked productivity skill that conducts a **comprehensive interview** about a plan or design, asking detailed questions until every decision branch is resolved. It targets failure mode #1 ("the agent didn't do what I want") by closing the user↔agent communication gap *before* work begins. Runs on the shared [[pattern-grilling]] loop ([[mp-grilling]]).

## See Also
- [[mp-grill-with-docs]] — grilling that also writes a domain model + ADRs.
- [[gsd-discuss-phase]] — GSD's counterpart elicitation step (adaptive questioning).
- [[addy-interview-me]] — Addy's interview skill; same pre-work elicitation interview.
- [[speckit-clarify]] — Spec Kit's grilling step; resolves the spec's `[NEEDS CLARIFICATION]` markers.
- [[stage-align]] — the canonical stage this implements.
