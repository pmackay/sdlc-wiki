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

A **model-invoked** engineering skill that actively builds and sharpens the project's domain model — challenging terms against the glossary, stress-testing with edge-case scenarios, and updating the `GLOSSARY.md` (was `CONTEXT.md` before v1.3.0) shared-language glossary ([[artifact-domain-model]]) and ADRs ([[artifact-adr]]) inline. Directly attacks failure mode #2 (verbosity): a precise shared vocabulary lets the agent say more with fewer words, name code consistently, and navigate the codebase faster ([[pattern-context-engineering]]).

> **v1.1 (2026-07-09): absorbed the deprecated `ubiquitous-language` skill.** MP retired the separate DDD-glossary skill (which wrote `UBIQUITOUS_LANGUAGE.md`); building/hardening the ubiquitous language is now part of domain-modeling itself.

> **v1.3.0 (2026-10-04): `CONTEXT.md` → `GLOSSARY.md`.** The domain-doc convention was renamed everywhere the skills read and write it (`CONTEXT-MAP.md` → `GLOSSARY-MAP.md` for multi-context repos). Existing files must be `git mv`'d, since the skills only look for the new names. The trigger was also broadened to "discussing codebase terminology, writing or editing a GLOSSARY.md, or recording or editing an ADR". The reused vocabulary now also feeds [[mp-wait-what]] and [[mp-pr]], which both write in the `GLOSSARY.md` language.

## See Also
- [[mp-grill-with-docs]] — bootstraps the domain model during a grilling session.
- [[mp-codebase-design]] — turns the model into module boundaries.
- [[stage-plan]] — the canonical stage this implements.
