---
type: capability
subtype: skill
belongs_to: "[[matt-pocock-skills]]"
implements: []
delegates_to: []
produces: []
applies: []
equivalent_to: ["[[addy-using-agent-skills]]", "[[gstack-router]]", "[[sp-using-superpowers]]"]
sources: "Matt Pocock — Skills for Real Engineers v1.1 (2026)"
raw: ["../../raw/matt-pocock-skills/2026-07-09-skills-v1.1-update.md"]
updated: 2026-07-09
---

# ask-matt

`/ask-matt` — a user-invoked **router** over the skills in the repo: "you don't remember every skill,
so ask." It describes **flows** — paths through the skills — anchored on one **main flow**
(`idea → ship`): `/grill-with-docs` → (optional prototype detour bridged by `/handoff`) →
`/to-spec` → `/to-tickets` → `/implement` (per ticket, clearing context between each) →
`/code-review` — plus two **on-ramps** ([[mp-wayfinder]] for work too big for one session;
[[mp-diagnosing-bugs]] as the "something's broken" entry) and a **vocabulary layer** underneath
([[mp-domain-modeling]], [[mp-codebase-design]]).

Newly paged (was previously catalogued). A **meta / dispatcher** capability spanning the whole
lifecycle rather than one stage, so it carries no `implements:` edge. Its cross-framework
counterparts are Addy's [[addy-using-agent-skills]] and gstack's [[gstack-router]] — each the
"which skill fits?" front door for its pack.

## See Also
- [[matt-pocock-skills]] — the toolkit this routes; its main flow is `idea → grill → to-spec → to-tickets → implement → code-review`.
- [[addy-using-agent-skills]] · [[gstack-router]] — the cross-framework routing counterparts.
