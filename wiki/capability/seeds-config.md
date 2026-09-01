---
type: capability
subtype: command
belongs_to: "[[seeds]]"
implements: []
produces: []
applies: ["[[pattern-contract-first]]"]
equivalent_to: []
sources: "Jaymin West — jayminwest/seeds README + AGENTS.md + SPEC.md (MIT, v0.5.15, 2026)"
raw: ["../../raw/seeds/2026-08-31-seeds.md"]
updated: 2026-08-31
---

# sd config

`sd config schema` · `sd config show [--path <dot.path>]` · `sd config set <path> <value>` · `sd config unset <path>` — the typed surface over `.seeds/config.yaml`, which holds `project`, `version`, `max_plan_depth`, and the nested `plan_templates` editor.

`sd config schema` is the interesting one: seeds **publishes a JSON Schema for its own config file** so an external UI — warren's per-tool config editor is the named consumer — can render a form automatically and write back through the per-knob commands, with no bespoke integration on either side. That is [[pattern-contract-first]] applied to a config file: the schema is the interface, the CLI and the UI are both clients of it.

Writes are validated before they land. `<value>` is YAML-parsed, the whole post-write file is validated as a unit under the `config.yaml` advisory lock, and `additionalProperties: false` at the root means an unknown key is a rejection rather than a silent no-op — a deliberately stricter posture than the deliberately-unvalidated `Issue.extensions` bag at the issue level.

Because plan templates live here, this command is also the mechanism behind the framework's core claim that *"the fix belongs in the planning process"*: adding a required section or a stricter `min` to a template is one `sd config set`, and it gates every subsequent [[seeds-plan-submit]].

Maps to **no canonical SDLC stage** — project configuration.

## See Also
- [[seeds-plan-templates]] · [[seeds-plan-validate]] — what config changes affect, and how to re-check existing plans against them.
- [[warren]] — the control plane that renders this schema as a form.
- [[pattern-contract-first]] — the pattern the published schema applies.
