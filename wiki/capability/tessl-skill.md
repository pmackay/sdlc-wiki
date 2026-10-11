---
type: capability
subtype: command
belongs_to: "[[tessl]]"
implements: []
delegates_to: []
produces: ["[[artifact-skill-doc]]"]
applies: ["[[pattern-knowledge-compounding]]"]
equivalent_to: ["[[sp-writing-skills]]", "[[gstack-skillify]]", "[[pstack-automate-me]]"]
sources: "Tessl docs — CLI v0.108.0 (2026)"
raw: ["../../raw/tessl/2026-09-12-tessl-platform.md"]
updated: 2026-09-12
---

# tessl skill

Scaffold, import, lint, publish, and unpublish a single skill: `skill new`, `skill import`, `skill lint`, `skill publish`, `skill unpublish`.

Where the wiki's framework-side skill-authoring capabilities ([[sp-writing-skills]], [[gstack-skillify]], [[pstack-automate-me]]) are concerned with *capturing* a technique, this one is concerned with **making it shippable**: lint it against a schema, score it, and put it somewhere other people's agents will load it from. Same artifact, different half of its life.

`tessl skill import` is the load-bearing one and reveals the layer's model. A standalone skill cannot be evaluated — evals attach to a bundle — so importing a loose `SKILL.md` into a plugin is the prerequisite for measuring it at all. *"If you have a standalone skill, import it into a plugin first."* Distribution and measurement are coupled by construction: the thing you can version is the thing you can prove.

Publishing is scoped — to a workspace by default, publicly with a flag — and triggers a review automatically, so a published skill always carries a score.

## See Also
- [[tessl-plugin]] — the bundle a skill must join to be evaluated or shipped as a unit.
- [[tessl-review]] — runs automatically on publish.
- [[sp-writing-skills]] · [[gstack-skillify]] · [[pstack-automate-me]] — the framework-side authoring counterparts.
- [[artifact-skill-doc]] — the artifact.
