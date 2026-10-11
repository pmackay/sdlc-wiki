---
type: capability
subtype: command
belongs_to: "[[pstack]]"
implements: []
delegates_to: []
produces: ["[[artifact-standards]]"]
applies: ["[[pattern-idempotent-operations]]", "[[pattern-cross-model-review]]", "[[pattern-model-tiering]]"]
equivalent_to: ["[[gstack-upgrade]]"]
sources: "pstack v0.15.2 — Lauren Tan (2026); Builder.io — BuilderIO/skills (2026)"
raw: ["../../raw/pstack/2026-09-11-pstack-plugin.md"]
updated: 2026-09-26
---

# /setup-pstack

Configures **which model runs each role**, and writes the result as an always-applied rule at `~/.cursor/rules/pstack-models.mdc`. One of the two steps in the framework's entire getting-started instruction, and the only skill in the plugin without `disable-model-invocation: true`.

It exists because pstack's workflow skills are **multi-model by construction**. [[pstack-interrogate]] runs one reviewer per model, [[pstack-arena]] and [[pstack-architect]] run one candidate per runner and prefer a cross-judge from a different model family, [[pstack-how]] splits exploration onto a fast model and synthesis onto a reasoning model, [[pstack-reflect]] assigns a model per review lens, and [[pstack-swarm]] has a default worker model. The default panel out of the box splits work by model strength: precisely-specified code, prose, and judgment to the strongest reasoning model, fast mechanical code to the fastest. Every one of those choices is a per-role line here, and **a role with no line keeps its skill default**, so the rule overrides only what the user changes.

Five steps: **detect** the model slugs that can actually be passed to a subagent in this session (the dependable source, preferred over any docs), **load** the current rule if one exists, **map and confirm** every role with `AskQuestion` rather than free text, **validate** that every real slug written is in the detected set, and **write** the rule.

Two details are worth recording. **Panel roles take a list, and the list length sets the subagent count** — arena runners, architect runners, and interrogate reviewers each spawn one subagent per entry, so configuration changes fan-out width, not just model identity. And two aliases are always valid even though they are not detected slugs: `inherit-parent` and `auto` both mean *run this role on the parent chat model*, which is how a user on Cursor's Auto setting stays on Auto. **The whole file is overwritten on every run so re-runs stay idempotent** — [[pstack-principle-make-operations-idempotent]] applied to the framework's own configuration.

The rule is also what makes [[pstack-interrogate]]'s unresolvable-slug fallback coherent: when a model slug goes stale, the review proceeds on the closest equivalent and a separate PR updates this file.

## See Also
- [[pstack-principle-make-operations-idempotent]] — the principle the overwrite-whole-file rule applies.
- [[pstack-interrogate]] · [[pstack-arena]] · [[pstack-architect]] · [[pstack-reflect]] · [[pstack-swarm]] — the panel and per-role consumers.
- [[gstack-upgrade]] — the cross-framework self-configuration counterpart.
