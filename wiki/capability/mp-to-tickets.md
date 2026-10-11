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
sources: "Matt Pocock — Skills for Real Engineers v1.1 (2026); v1.2.0 (2026-08-05)"
raw: ["../../raw/matt-pocock-skills/2026-10-04-skills-v1.3.1-update.md", "../../raw/matt-pocock-skills/2026-07-09-skills-v1.1-update.md"]
updated: 2026-10-11
---

# to-tickets

`/to-tickets` — a user-invoked engineering skill that breaks a plan, spec, or the current conversation into a set of **tracer-bullet tickets** ([[artifact-issue]]), each declaring its **blocking edges** (the tickets that must finish first). One skill owns both decomposition and dependency-ordering. Each slice cuts a narrow but *complete* path through every layer and is sized to fit a single fresh context window ([[pattern-vertical-slice]]).

The tickets read two ways depending on the tracker `/setup-matt-pocock-skills` configured. On the **local-markdown tracker**, each ticket is its own file under `.scratch/<feature>/issues/<NN>-<slug>.md`, edges are written as text, and you work them blockers-first by hand; the spec beside them is `spec.md`. On a **real tracker**, edges become native blocking links, so any ticket whose blockers are done is on the frontier and several agents can run at once. Those blocking edges are what [[mp-implement-spec]] reads as a **task graph** to schedule parallel implementers off the ready frontier.

**Distinctive: wide-refactor handling.** A *wide refactor* (e.g. rename a column) whose blast radius breaks thousands of call sites can't land green as a vertical slice, so `to-tickets` sequences it as **expand → migrate-in-batches → contract** (add the new form beside the old, migrate call sites in blast-radius-sized batches each keeping CI green, then delete the old form) — the exception to vertical slicing no other framework here spells out.

MP's member of the cross-framework **decompose** cluster: it slices work into dependency-ordered, independently-shippable units, like [[addy-planning]], [[speckit-tasks]], and BMAD's [[bmad-create-epics-and-stories]]; [[speckit-taskstoissues]] is the export half Spec Kit splits into a second command. Fed by [[mp-to-spec]]; its tickets are then built by [[mp-implement]] or [[mp-implement-spec]].

## See Also
- [[seeds-plan-submit]] — the same decomposition run by a program: an AJV-validated plan whose steps spawn the tickets and whose `blocks` indices become real dependency edges, into a JSONL store in the repo rather than a hosted tracker.
- [[mp-to-spec]] — produces the spec this slices.
- [[mp-implement]] — builds the tickets this produces.
- [[mp-implement-spec]] — consumes the tickets as a task graph.
- [[mp-wayfinder]] — the sibling for work too big to decompose in one session (a map of decision tickets).
- [[addy-planning]] · [[speckit-tasks]] · [[bmad-create-epics-and-stories]] — decompose-cluster counterparts.
- [[stage-plan]] — the canonical stage this implements.

## Version history

### v1.3.0 (2026-10-04)
- Its blocking edges became the task graph [[mp-implement-spec]] schedules from.

### v1.2.0 (2026-08-05)
- Local-markdown tickets became one file per ticket under `.scratch/<feature>/issues/`, never a single combined `tickets.md`; the spec file became `spec.md`, not `PRD.md`.

### v1.1.0 (2026-07-08; ingested 2026-07-09)
- Renamed from `/to-issues` and merged with the former `/to-plan`, so one skill owns decomposition and dependency-ordering.

### Initial ingest (2026-06-28)
- Documented as `to-issues`: break plans/specs/PRDs into independently-grabbable vertical-slice issues.
