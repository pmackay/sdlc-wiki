---
type: capability
subtype: command
belongs_to: "[[seeds]]"
implements: []
produces: []
applies: []
equivalent_to: []
sources: "Jaymin West — jayminwest/seeds PLAN_SPEC.md + README.md (MIT, v0.5.15, 2026)"
raw: ["../../raw/seeds/2026-08-31-seeds.md"]
updated: 2026-08-31
---

# sd plan templates

`sd plan templates` — list the plan templates available in this project: the three built-ins (`feature`, `bug`, `refactor`) plus anything declared under `plan_templates:` in `.seeds/config.yaml`, which overrides a built-in of the same name.

A template is a named set of **sections**, each with a `kind` (`text`, `list`, `steps`, or a nested object spec), a `required` flag, optional validation (`min_length`, `min`, `item`), an optional `mulch_source` hint, and the natural-language `prompt` the agent will see. Listing them is how an agent (or a UI) discovers what shapes of plan this project accepts before calling [[seeds-plan-prompt]].

`feature` is the default for seed types `task`, `feature`, and `epic`; `bug` for `bug`; `refactor` has no matching type and is opt-in via `--template refactor` only.

A pure **read** command; maps to **no canonical SDLC stage**.

## See Also
- [[seeds-plan-prompt]] — instantiates one of these templates against a seed.
- [[seeds-config]] — where custom templates are declared and edited.
- [[seeds-plan-validate]] — re-checks an existing plan after a template changes.
