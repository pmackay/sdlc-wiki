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
sources: "Matt Pocock — Skills for Real Engineers (2026); v1.3.0 (2026-10-04)"
raw: ["../../raw/matt-pocock-skills/2026-10-04-skills-v1.3.1-update.md", "../../raw/matt-pocock-skills/2026-06-28-skills-for-real-engineers.md"]
updated: 2026-10-11
---

# grill-with-docs

`/grill-with-docs` — a user-invoked engineering skill that runs a grilling session ([[pattern-grilling]]) **while building a domain model**, updating the project's `GLOSSARY.md` (was `CONTEXT.md` before v1.3.0) shared-language glossary ([[artifact-domain-model]]) and recording decisions as [[artifact-adr]] inline. It targets failure modes #1 (alignment) and #2 (verbosity): shared terminology lets the agent decode project jargon and stay terse.

> **v1.2.0–v1.3.0.** It runs [[mp-grilling]]'s round-by-round frontier. Its most-reported problem was that the named sub-skill didn't reliably load, and v1.3.0 targets it by invoking dependencies with an explicit "Call the Skill tool with `grilling`" instruction instead of bare `/grilling` prose. [[mp-ask-matt]] now splits it from [[mp-grill-me]] on one test: use grill-with-docs whenever you are in a working directory, because it "leaves a paper trail".

## See Also
- [[mp-grill-me]] — grilling without the docs side-effects.
- [[mp-domain-modeling]] — deepens the same domain model.
- [[stage-align]] — the canonical stage this implements.
