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

`/grill-with-docs` — a user-invoked engineering skill that runs a grilling session ([[pattern-grilling]]) **while building a domain model**, updating the project's `GLOSSARY.md` shared-language glossary ([[artifact-domain-model]]) and recording decisions as [[artifact-adr]] inline. It targets failure modes #1 (alignment) and #2 (verbosity): shared terminology lets the agent decode project jargon and stay terse.

It runs [[mp-grilling]]'s round-by-round frontier, loading it with an explicit "Call the Skill tool with `grilling`" instruction. [[mp-ask-matt]] makes it the default entry to the main flow whenever you are in a working directory, because it "leaves a paper trail"; [[mp-grill-me]] is the stateless version for when there is no repo under you.

## See Also
- [[mp-grill-me]] — grilling without the docs side-effects.
- [[mp-domain-modeling]] — deepens the same domain model.
- [[stage-align]] — the canonical stage this implements.

## Version history

### v1.3.0 (2026-10-04)
- The glossary file was renamed from `CONTEXT.md` to `GLOSSARY.md`.
- Dependencies are invoked with an explicit "Call the Skill tool with `grilling`" instruction instead of bare `/grilling` prose, targeting its most-reported problem: the named sub-skill didn't reliably load.

### v1.2.0 (2026-08-05)
- Runs grilling round by round over the question frontier. [[mp-ask-matt]] split it from [[mp-grill-me]] on whether you are in a working directory.

### Initial ingest (2026-06-28)
- Paged as grilling that builds a `CONTEXT.md` domain model and ADRs.
