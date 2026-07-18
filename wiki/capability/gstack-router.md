---
type: capability
subtype: command
belongs_to: "[[gstack]]"
implements: []
delegates_to: []
produces: []
applies: []
equivalent_to: ["[[addy-using-agent-skills]]", "[[mp-ask-matt]]", "[[sp-using-superpowers]]"]
sources: "gstack — Garry Tan (2026)"
raw: ["../../raw/gstack/2026-07-05-gstack-framework.md"]
updated: 2026-07-09
---

# gstack (router)

The root `gstack` **skill** — "Router for the gstack skill suite." It routes incoming work to the right specialist skill (triggers: "gstack", "which gstack skill", "route this with gstack") and, together with **proactive skill suggestions**, notices what stage you're in (brainstorming, reviewing, debugging, testing) and recommends the matching skill. Voice-friendly trigger phrases let you say what you want naturally instead of remembering slash-command names.

A **meta / dispatcher** capability spanning the whole lifecycle rather than one stage, so it carries no `implements:` edge. Its cross-framework counterpart is Addy Osmani's [[addy-using-agent-skills]] (the meta-skill that routes work to the right skill and defines shared operating rules). Paged as `gstack-router` to keep the framework basename [[gstack]] distinct.

## See Also
- [[gstack]] — the framework this routes for.
- [[addy-using-agent-skills]] — the cross-framework routing/meta-skill counterpart.
