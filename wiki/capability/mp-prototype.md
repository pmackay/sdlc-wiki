---
type: capability
subtype: skill
belongs_to: "[[matt-pocock-skills]]"
implements: "[[stage-implement]]"
delegates_to: []
produces: []
applies: ["[[pattern-throwaway-prototype]]"]
equivalent_to: []
docs_url: "https://www.aihero.dev/skills-prototype"
sources: "Matt Pocock — Skills for Real Engineers v1.1 (2026)"
raw: ["../../raw/matt-pocock-skills/2026-07-09-skills-v1.1-update.md"]
updated: 2026-07-09
---

# prototype

`/prototype` — a **model-invoked** (v1.1: was user-invoked) engineering skill that builds a **throwaway prototype** to answer a design question — a runnable terminal app for a state/logic sanity-check, or several radically different UI variations toggleable from one route (see [[pattern-throwaway-prototype]]). Build to learn, then discard; the value is the knowledge, not the code. Now model-invoked, so the agent (and other skills) can reach for it autonomously; in MP's main flow it is the prototype detour bridged into and out of by [[mp-handoff]] when a question needs a runnable answer.

## See Also
- [[mp-to-spec]] — turn validated learnings into a spec.
- [[stage-implement]] — the canonical stage this implements.
