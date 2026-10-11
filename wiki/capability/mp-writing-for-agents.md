---
type: capability
subtype: skill
belongs_to: "[[matt-pocock-skills]]"
implements: []
delegates_to: []
produces: ["[[artifact-skill-doc]]"]
applies: ["[[pattern-context-engineering]]"]
equivalent_to: ["[[sp-writing-skills]]"]
docs_url: "https://www.aihero.dev/skills-writing-for-agents"
sources: "Matt Pocock — Skills for Real Engineers v1.3.1 (2026-10-04)"
raw: ["../../raw/matt-pocock-skills/2026-10-04-skills-v1.3.1-update.md"]
updated: 2026-10-11
---

# writing-for-agents

`writing-for-agents` — a **model-invoked** productivity skill: "Writing documents for agents. Use when creating or editing skills, or modifying AGENTS.md or CLAUDE.md." It is the reference for writing *any* document an agent consumes: a skill, an `AGENTS.md` / `CLAUDE.md`, or a doc reached by a pointer. "The packaging differs; the writing does not."

Its definitions live in one `SKILL.md`, with skill-only mechanics (frontmatter, user- vs model-invoked, router skills) disclosed to a separate `SKILL-MECHANICS.md`. Being model-invoked, it fires whenever skills or steering files are edited, and [[mp-retro]] loads it before proposing any steering change.

## The vocabulary

The goal is **predictability**: "the agent takes the same *process* every run rather than producing the same output." The levers:

- **Context pointer**: a reference in context that names out-of-context material *and* the condition for reaching it (a skill description, an `AGENTS.md` line). "The pointer's *wording*, not its target, decides when the agent reaches the material." Front-load the leading word; one trigger per **branch**.
- **The two loads**: **context load** (always-loaded tokens and attention) vs **cognitive load** (the human as index: knowing which documents exist). The second is "the price of human agency; spend it where human judgement matters."
- **Information hierarchy**: in-file **steps** → in-file **reference** → **disclosed reference** behind a pointer. **Progressive disclosure** protects the top of that ladder; **co-location** keeps a concept's definition, rules and caveats together; **sprawl** is a document simply too long.
- **Completion criteria**: each step ends on one, graded by **clarity** (vague bounds invite *premature completion*) and **demand** (exhaustive bars drive *legwork*). Split by sequence only across a real context boundary.
- **Leading words**: compact pretrained concepts (*tight*, *red*, *tracer bullets*) that anchor behaviour in the fewest tokens, in the body and in the pointer. **Negation** is the failure mode beside it: prompt the positive.
- **Pruning**: **single source of truth**. The **environment** is a source of truth too, so a doc restating `package.json` or `--help` is a **cache** that earns its place only when the lookup is expensive. Hunt **relevance**, **sediment**, and **no-ops** ("delete the whole sentence").

## Where it sits

Off-stage, as a writing reference rather than a lifecycle step, but it is the standard [[stage-learn]] work is held to. Its nearest counterpart is Superpowers' [[sp-writing-skills]] (which treats skill authoring as TDD on process docs). Matt Pocock's version is broader in scope (all agent-facing docs) and puts its weight on pointer wording and load budgets rather than test-first authoring. It is the toolkit's most explicit statement of [[pattern-context-engineering]], and it reads as a guide-authoring manual for [[topic-harness-engineering]].

## See Also
- [[mp-retro]] — loads it before writing any environment change.
- [[mp-wait-what]] — a three-line skill built on its leading-word theory.
- [[sp-writing-skills]] · [[pstack-reflect]] — other frameworks' skill-authoring disciplines.
- [[artifact-skill-doc]] — what it governs the writing of.

## Version history
- **v1.2.2 (2026-08-05):** made model-invokable in Codex again (dropped `policy.allow_implicit_invocation: false`; updated Codex display metadata that still named `writing-great-skills`), and moved to the Model-invoked lists in the READMEs.
- **v1.2.0 (2026-08-05):** renamed from `writing-great-skills` (breaking, no alias) and restructured. The scope widened from skills to all agent-facing documents, the separate `GLOSSARY.md` was merged into `SKILL.md`, skill-only mechanics moved to `SKILL-MECHANICS.md`, it became model-invoked, and the pruning section gained **cache**.
- **Initial ingest (2026-06-28):** catalogued (not paged) as `writing-great-skills`, a reference for authoring skills well.
