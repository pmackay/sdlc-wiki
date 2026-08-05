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
sources: "Matt Pocock — Skills for Real Engineers v1.1 (2026)"
raw: ["../../raw/matt-pocock-skills/2026-07-09-skills-v1.1-update.md"]
updated: 2026-07-09
---

# domain-modeling

A **model-invoked** engineering skill that actively builds and sharpens the project's domain model — challenging terms against the glossary, stress-testing with edge-case scenarios, and updating the `CONTEXT.md` shared-language glossary ([[artifact-domain-model]]) and ADRs ([[artifact-adr]]) inline. Directly attacks failure mode #2 (verbosity): a precise shared vocabulary lets the agent say more with fewer words, name code consistently, and navigate the codebase faster ([[pattern-context-engineering]]).

> **v1.1 (2026-07-09): absorbed the deprecated `ubiquitous-language` skill.** MP retired the separate DDD-glossary skill (which wrote `UBIQUITOUS_LANGUAGE.md`); building/hardening the ubiquitous language is now part of domain-modeling itself.

## See Also
- [[mp-grill-with-docs]] — bootstraps the domain model during a grilling session.
- [[mp-codebase-design]] — turns the model into module boundaries.
- [[stage-plan]] — the canonical stage this implements.
