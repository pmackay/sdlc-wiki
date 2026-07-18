---
type: capability
subtype: skill
belongs_to: "[[matt-pocock-skills]]"
implements: []
delegates_to: []
produces: ["[[artifact-handoff-doc]]"]
applies: ["[[pattern-session-handoff]]"]
equivalent_to: []
sources: "Matt Pocock — Skills for Real Engineers (2026)"
raw: ["../../raw/matt-pocock-skills/2026-06-28-skills-for-real-engineers.md"]
updated: 2026-06-28
---

# handoff

`/handoff` — a user-invoked productivity skill that **compacts a conversation into a
handoff document** ([[artifact-handoff-doc]]) so a fresh agent (or session) can pick up
without losing context. Applies [[pattern-session-handoff]].

Cross-cutting: it serves any lifecycle stage rather than one, so it carries no `implements:`
edge. GSD addresses the same need structurally with `STATE.md` / `CONTEXT.md` persistence
and `pause-work` / `resume-work` — clustered at [[pattern-session-handoff]].

## See Also
- [[gsd]] — GSD's built-in session-handoff mechanism.
- [[pattern-session-handoff]] — the shared technique.
