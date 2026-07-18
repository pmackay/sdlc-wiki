---
type: capability
subtype: skill
belongs_to: "[[matt-pocock-skills]]"
implements: "[[stage-plan]]"
delegates_to: []
produces: ["[[artifact-issue]]"]
applies: ["[[pattern-scale-adaptive-planning]]", "[[pattern-fresh-context-subagents]]"]
equivalent_to: []
sources: "Matt Pocock — Skills for Real Engineers v1.1 (2026)"
raw: ["../../raw/matt-pocock-skills/2026-07-09-skills-v1.1-update.md"]
updated: 2026-07-09
---

# wayfinder

`/wayfinder` — a user-invoked engineering skill for planning **a huge chunk of work — more than one agent session can hold** — as a **shared map of investigation tickets** on the repo's issue tracker, resolved one at a time until the way to the **destination** is clear. Naming the destination is the first act; the map (a single `wayfinder:map` issue whose child issues are its tickets) is an *index*, not a store — it gists each closed decision and links to the ticket that holds it. **Plan, don't do**: tickets resolve *decisions*, not deliverables; the pull to just build is the signal you've reached the map's edge and should hand off (to [[mp-to-spec]] / [[mp-to-tickets]] / [[mp-implement]]).

**New in v1.1 (2026-07-09)** — graduated from `in-progress/` (was `decision-mapping`) into `engineering/`. Positioned as a **situational on-ramp** (greenfield project or a feature too big for one session), *not* the default entry flow — the grill-led `idea → ship` chain stays the front door. Every ticket is classified **HITL** (human-in-the-loop: grilling, prototype) or **AFK** (agent-alone: research; `task` either), and blocking prefers the tracker's native dependency links so the frontier renders in the tracker UI. It sizes ceremony to work bigger than a single context ([[pattern-scale-adaptive-planning]]) and advances one fresh session at a time ([[pattern-fresh-context-subagents]]). No cross-framework counterpart — the investigation-map-for- oversized-work framing is unique to MP.

## See Also
- [[mp-to-tickets]] — the sibling for work that *does* fit a normal decomposition; wayfinder feeds into it once the fog clears.
- [[mp-grill-with-docs]] · [[mp-grill-me]] — the front-door grill skills that signpost *up* to wayfinder when an effort is too big to hold.
- [[bmad-sprint-planning]] — BMAD's large-work backlog mapping (a loose relative).
- [[stage-plan]] — the canonical stage this implements.
