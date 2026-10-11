---
type: capability
subtype: skill
belongs_to: "[[matt-pocock-skills]]"
implements: "[[stage-plan]]"
delegates_to: []
produces: ["[[artifact-domain-model]]", "[[artifact-adr]]"]
applies: ["[[pattern-context-engineering]]"]
equivalent_to: []
docs_url: "https://www.aihero.dev/skills-domain-modeling"
sources: "Matt Pocock — Skills for Real Engineers v1.1 (2026); v1.3.0 (2026-10-04)"
raw: ["../../raw/matt-pocock-skills/2026-10-04-skills-v1.3.1-update.md", "../../raw/matt-pocock-skills/2026-07-09-skills-v1.1-update.md"]
updated: 2026-10-11
---

# domain-modeling

A **model-invoked** engineering skill that actively builds and sharpens the project's domain model and ubiquitous language — challenging terms against the glossary, stress-testing with edge-case scenarios, and updating the `GLOSSARY.md` shared-language glossary ([[artifact-domain-model]]) and ADRs ([[artifact-adr]]) inline. A multi-context repo indexes several glossaries through `GLOSSARY-MAP.md`. It triggers on "discussing codebase terminology, writing or editing a GLOSSARY.md, or recording or editing an ADR".

Directly attacks failure mode #2 (verbosity): a precise shared vocabulary lets the agent say more with fewer words, name code consistently, and navigate the codebase faster ([[pattern-context-engineering]]). The same vocabulary feeds [[mp-wait-what]] and [[mp-pr]], which both write in the `GLOSSARY.md` language.

## See Also
- [[mp-grill-with-docs]] — bootstraps the domain model during a grilling session.
- [[mp-codebase-design]] — turns the model into module boundaries.
- [[stage-plan]] — the canonical stage this implements.

## Version history

### v1.3.0 (2026-10-04)
- The domain-doc convention was renamed from `CONTEXT.md` / `CONTEXT-MAP.md` to `GLOSSARY.md` / `GLOSSARY-MAP.md` everywhere the skills read and write it. Existing files must be `git mv`'d, since the skills only look for the new names.
- The trigger was broadened from "pin down domain terminology or a ubiquitous language / record an architectural decision" to discussing codebase terminology or editing a GLOSSARY.md or ADR directly.

### v1.2.0 (2026-08-05)
- The deprecated `ubiquitous-language` skill (which wrote `UBIQUITOUS_LANGUAGE.md`) was deleted from the repo; this skill is its replacement.

### v1.1.0 (2026-07-08; ingested 2026-07-09)
- Absorbed the deprecated `ubiquitous-language` DDD-glossary skill: building and hardening the ubiquitous language became part of domain-modeling itself.

### Initial ingest (2026-06-28)
- Paged as the skill that sharpens the `CONTEXT.md` domain model and ADRs.
