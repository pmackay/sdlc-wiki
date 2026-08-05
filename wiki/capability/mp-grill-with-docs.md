---
type: capability
subtype: skill
belongs_to: "[[matt-pocock-skills]]"
implements: "[[stage-align]]"
delegates_to: ["[[mp-grilling]]"]
produces: ["[[artifact-domain-model]]", "[[artifact-adr]]"]
applies: ["[[pattern-grilling]]"]
equivalent_to: []
docs_url: "https://www.aihero.dev/skills-grill-with-docs"
sources: "Matt Pocock — Skills for Real Engineers (2026)"
raw: ["../../raw/matt-pocock-skills/2026-06-28-skills-for-real-engineers.md"]
updated: 2026-06-28
---

# grill-with-docs

`/grill-with-docs` — a user-invoked engineering skill that runs a grilling session ([[pattern-grilling]]) **while building a domain model**, updating the project's `CONTEXT.md` shared-language glossary ([[artifact-domain-model]]) and recording decisions as [[artifact-adr]] inline. It targets failure modes #1 (alignment) and #2 (verbosity): shared terminology lets the agent decode project jargon and stay terse.

## See Also
- [[mp-grill-me]] — grilling without the docs side-effects.
- [[mp-domain-modeling]] — deepens the same domain model.
- [[stage-align]] — the canonical stage this implements.
