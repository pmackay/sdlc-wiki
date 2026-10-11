---
type: capability
subtype: skill
belongs_to: "[[matt-pocock-skills]]"
implements: "[[stage-align]]"
delegates_to: []
produces: ["[[artifact-issue]]"]
applies: ["[[pattern-scale-adaptive-planning]]", "[[pattern-fresh-context-subagents]]"]
equivalent_to: []
docs_url: "https://www.aihero.dev/skills-wayfinder"
sources: "Matt Pocock — Skills for Real Engineers v1.1 (2026); v1.2.0 (2026-08-05)"
raw: ["../../raw/matt-pocock-skills/2026-10-04-skills-v1.3.1-update.md", "../../raw/matt-pocock-skills/2026-07-09-skills-v1.1-update.md"]
updated: 2026-10-11
---

# wayfinder

`/wayfinder` — a user-invoked engineering skill for planning **a huge chunk of work — more than one agent session can hold** — as a **shared map of decision tickets** on the repo's issue tracker, resolved one at a time until the way to the **destination** is clear. A **decision ticket** is "a question whose resolution is a decision", not a slice of a build to execute; the repo's own `GLOSSARY.md` records the term.

Naming the destination is the first act; the map (a single `wayfinder:map` issue whose child issues are its tickets) is an *index*, not a store — it gists each closed decision and links to the ticket that holds it. **Plan, don't do**: tickets resolve *decisions*, not deliverables; the pull to just build is the signal you've reached the map's edge and should hand off.

## How it works

- Every ticket is classified **HITL** (human-in-the-loop: grilling, prototype) or **AFK** (agent-alone: research; `task` either), and blocking prefers the tracker's native dependency links so the frontier renders in the tracker UI.
- It sizes ceremony to work bigger than a single context ([[pattern-scale-adaptive-planning]]) and advances one fresh session at a time ([[pattern-fresh-context-subagents]]).
- **Research burns down in parallel.** Research is a real ticket type, because it is a shared blocker that downstream decisions hang on, but charting doesn't stop to read it. After creating the tickets, the charting session fires a [[mp-research]] subagent per research ticket and captures findings on a throwaway `research/<name>` branch with a context pointer. Research tickets are "the one exception to *one ticket per session*".

## Where it sits

A **situational on-ramp** (greenfield project or a feature too big for one session), *not* the default entry flow — the grill-led `idea → ship` chain stays the front door. [[mp-ask-matt]] flags it as the heaviest flow and calls out two mistakes. The first is over-reaching: a well-scoped feature belongs on [[mp-grill-with-docs]]. The second is losing the way at the handoff: when the map clears, merge at [[mp-to-spec]], which "collapses the map's linked decisions into a buildable plan", rather than looping straight into [[mp-implement]] (only right when the effort turned out genuinely small).

No cross-framework counterpart — the decision-map-for-oversized-work framing is unique to MP.

## See Also
- [[mp-to-tickets]] — the sibling for work that *does* fit a normal decomposition; wayfinder feeds into it once the fog clears.
- [[mp-grill-with-docs]] · [[mp-grill-me]] — the front-door grill skills that signpost *up* to wayfinder when an effort is too big to hold.
- [[bmad-sprint-planning]] — BMAD's large-work backlog mapping (a loose relative).
- [[stage-align]] — the canonical stage this implements (it resolves *decisions* about what to build, upstream of the spec; [[mp-to-spec]] then writes the spec in [[stage-specify]]).

## Version history

### v1.2.0 (2026-08-05)
- **Investigation tickets → decision tickets.** People kept reading a wayfinder ticket as an ordinary *implementation* ticket; the unit was renamed and recorded in the repo glossary, so it no longer conflicts with the "avoid: ticket" guidance.
- Research tickets are burned down by parallel [[mp-research]] subagents during charting, instead of being parked for a separately launched session.
- [[mp-ask-matt]] added the two routing warnings (over-reaching; merge at `/to-spec`, not `/implement`).

### Initial ingest (2026-07-09, v1.1)
- Graduated from `in-progress/` (was `decision-mapping`) into `engineering/`, as a map of "investigation tickets" resolving decisions upstream of the spec.
