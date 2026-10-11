---
type: capability
subtype: skill
belongs_to: "[[matt-pocock-skills]]"
implements: []
delegates_to: []
produces: []
applies: ["[[pattern-session-handoff]]"]
equivalent_to: ["[[addy-using-agent-skills]]", "[[gstack-router]]", "[[sp-using-superpowers]]"]
docs_url: "https://www.aihero.dev/skills-ask-matt"
sources: "Matt Pocock — Skills for Real Engineers v1.1 (2026); v1.3.1 (2026-10-04)"
raw: ["../../raw/matt-pocock-skills/2026-10-04-skills-v1.3.1-update.md", "../../raw/matt-pocock-skills/2026-07-09-skills-v1.1-update.md"]
updated: 2026-10-11
---

# ask-matt

`/ask-matt` — a user-invoked **router** over the skills in the repo: "you don't remember every skill, so ask." It describes **flows** (paths through the skills) anchored on one **main flow**, two **on-ramps**, a codebase-health lane, a **vocabulary layer** underneath, and a list of standalone skills.

## The main flow (v1.3.1)

1. [[mp-grill-with-docs]] sharpens the idea in a working directory. With no working directory, use [[mp-grill-me]].
2. *Branch:* if a question needs a runnable answer, detour through [[mp-prototype]], bridged out and back by [[mp-handoff]].
3. *Branch:* is this a multi-session build?
   - **Yes** → [[mp-to-spec]] → [[mp-to-tickets]], then either [[mp-implement]] per ticket (`/clear` between each) **or** [[mp-implement-spec]] for the whole spec at once (implementer subagents across the ready frontier, one integration branch).
   - **No** → [[mp-implement]] in the same context.
   - Either way the build drives [[mp-tdd]] and closes with [[mp-code-review]]. When the work goes up as a PR, [[mp-pr]] shapes the body.
4. [[mp-retro]] **closes the loop**: it suggests changes to the agent's *environment* (checks, standards, pointers, tooling) so the next build starts better.

**On-ramps:** [[mp-triage]] (raw incoming issues only; tickets from `/to-tickets` are already agent-ready, so "don't triage them"), [[mp-diagnosing-bugs]] (then `/retro` once the fix is in; v1.3.1), and [[mp-wayfinder]] (the "most cognitively demanding flow", reserved for an idea that won't fit one session). When wayfinder's map clears, "it hands off, it doesn't build": merge onto the main flow at [[mp-to-spec]], not straight into `/implement`.

**Standalone:** [[mp-grill-me]], [[mp-grilling]], [[mp-prototype]], [[mp-research]], [[mp-to-questionnaire]], [[mp-wizard]], [[mp-wait-what]], `teach`, [[mp-writing-for-agents]]. **Codebase health:** [[mp-improve-codebase-architecture]]. **Vocabulary underneath:** [[mp-domain-modeling]], [[mp-codebase-design]].

## Phase boundaries (v1.2.0)

A **phase** is a chunk of work inside a session (the grilling, the implementation, the QA). At the boundary between two phases there are five options, in order:

- **Continue**: the one to rule out first, "the only move that keeps the conversation as a primary source rather than a summary of one".
- **`/clear`**: when nothing here matters to what's next.
- **[[mp-handoff]]**: narrowed in v1.2.0. It is only for when something must *travel*: a new harness, a new directory, a colleague, or a side task forked mid-phase.
- **Subagent**: a tightly scoped task run AFK in its own window.
- **`/compact`**: the default, at the bottom of the tree rather than the first reach.

The reasoning is disclosed to `PHASE-BOUNDARIES.md` ([[pattern-session-handoff]]). Context hygiene keeps steps 1–3 in one unbroken window up to `/to-tickets`, within the **smart zone**, updated from ~120k to **~150k tokens** in v1.2.0.

## History

Newly paged in v1.1 (it was catalogued before). v1.2.0 added the phase-boundary tree, the wayfinder routing fixes, and routes for [[mp-grilling]], [[mp-to-questionnaire]], [[mp-wizard]] and [[mp-wait-what]]. v1.3.0 added [[mp-implement-spec]], [[mp-pr]], and [[mp-retro]] as the main flow's new tail, and dropped `resolving-merge-conflicts` ([[mp-resolving-merge-conflicts]], removed). v1.3.1 replaced the stale diagnosing-bugs → improve-codebase-architecture hand-off with `/retro`.

A **meta / dispatcher** capability spanning the whole lifecycle rather than one stage, so it carries no `implements:` edge. Its cross-framework counterparts are Addy's [[addy-using-agent-skills]], gstack's [[gstack-router]], and Superpowers' [[sp-using-superpowers]]: each is the "which skill fits?" front door for its pack.

## See Also
- [[matt-pocock-skills]] — the toolkit this routes.
- [[addy-using-agent-skills]] · [[gstack-router]] · [[sp-using-superpowers]] — the cross-framework routing counterparts.
