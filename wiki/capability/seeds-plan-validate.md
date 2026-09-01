---
type: capability
subtype: command
belongs_to: "[[seeds]]"
implements: "[[stage-plan]]"
produces: []
applies: ["[[pattern-plan-verification-loop]]", "[[pattern-deterministic-gates]]"]
equivalent_to: []
sources: "Jaymin West — jayminwest/seeds PLAN_SPEC.md + README.md (MIT, v0.5.15, 2026)"
raw: ["../../raw/seeds/2026-08-31-seeds.md"]
updated: 2026-08-31
---

# sd plan validate

`sd plan validate <pl-id>` — re-run the AJV validation of an existing plan against the **current** template definition, rather than the one in force when it was submitted.

It exists because templates are project config, not code. When a team edits `.seeds/config.yaml` to add a required section or tighten a `min` — which is precisely the framework's prescribed response to a failure (*"the fix belongs in the planning process — adding a new section, validation rule, or risk check that prevents the failure mode next time"*) — every plan already in flight is now measured against a rule it never saw. `sd plan validate` is how you find out which ones no longer conform.

That makes it the closing half of the planning thesis: the template is the place a lesson is encoded, and this command is the sweep that applies the new rule retroactively. Implements [[stage-plan]] as a gate over the plan artifact ([[pattern-plan-verification-loop]], [[pattern-deterministic-gates]]).

## See Also
- [[seeds-plan-submit]] — runs the same validation at write time.
- [[seeds-config]] — where the templates that define the rules are edited.
- [[seeds-plan-edit]] — the repair surface once validation reports a gap.
- [[stage-plan]] — the canonical stage this implements.
