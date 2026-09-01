---
type: capability
subtype: skill
belongs_to: "[[matt-pocock-skills]]"
implements: "[[stage-plan]]"
delegates_to: []
produces: ["[[artifact-issue]]"]
applies: ["[[pattern-vertical-slice]]"]
equivalent_to: ["[[addy-planning]]", "[[speckit-tasks]]", "[[speckit-taskstoissues]]", "[[bmad-create-epics-and-stories]]", "[[sp-writing-plans]]", "[[seeds-plan-submit]]"]
docs_url: "https://www.aihero.dev/skills-to-tickets"
sources: "Matt Pocock — Skills for Real Engineers v1.1 (2026)"
raw: ["../../raw/matt-pocock-skills/2026-07-09-skills-v1.1-update.md"]
updated: 2026-08-31
---

# to-tickets

`/to-tickets` — a user-invoked engineering skill that breaks a plan, spec, or the current conversation into a set of **tracer-bullet tickets** ([[artifact-issue]]), each declaring its **blocking edges** (the tickets that must finish first). Each slice cuts a narrow but *complete* path through every layer and is sized to fit a single fresh context window ([[pattern-vertical-slice]]). The one artifact reads two ways depending on the tracker `/setup-matt-pocock-skills` configured: a **local `tickets.md`** writes edges as text and you work it top-to-bottom by hand, or a **real tracker** writes them as native blocking links so any ticket whose blockers are done is on the frontier and several agents can run at once.

> **Renamed from `/to-issues` and merged with the former `/to-plan` (v1.1, 2026-07-09).** One skill now owns both decomposition and dependency-ordering.

**Distinctive: wide-refactor handling.** A *wide refactor* (e.g. rename a column) whose blast radius breaks thousands of call sites can't land green as a vertical slice, so `to-tickets` sequences it as **expand → migrate-in-batches → contract** (add the new form beside the old, migrate call sites in blast-radius-sized batches each keeping CI green, then delete the old form) — the exception to vertical slicing no other framework here spells out.

MP's member of the cross-framework **decompose** cluster: it slices work into dependency-ordered, independently-shippable units, like [[addy-planning]], [[speckit-tasks]], and BMAD's [[bmad-create-epics-and-stories]]; [[speckit-taskstoissues]] is the export half Spec Kit splits into a second command. Fed by [[mp-to-spec]]; its tickets are then built by [[mp-implement]].

## See Also
- [[seeds-plan-submit]] — the same decomposition run by a program: an AJV-validated plan whose steps spawn the tickets and whose `blocks` indices become real dependency edges, into a JSONL store in the repo rather than a hosted tracker.
- [[mp-to-spec]] — produces the spec this slices.
- [[mp-implement]] — builds the tickets this produces.
- [[mp-wayfinder]] — the sibling for work too big to decompose in one session (investigation-ticket map).
- [[addy-planning]] · [[speckit-tasks]] · [[bmad-create-epics-and-stories]] — decompose-cluster counterparts.
- [[stage-plan]] — the canonical stage this implements.
