---
type: capability
subtype: command
belongs_to: "[[seeds]]"
implements: "[[stage-learn]]"
produces: []
applies: []
equivalent_to: []
sources: "Jaymin West — jayminwest/seeds PLAN_SPEC.md + README.md (MIT, v0.5.15, 2026)"
raw: ["../../raw/seeds/2026-08-31-seeds.md"]
updated: 2026-08-31
---

# sd plan outcome

`sd plan outcome <pl-id> --result <success|partial|failure> [--note <text>]` — record how a plan actually turned out.

It is the framework's **only** Learn-stage capability, and it is deliberately minimal: *"Outcomes are storage-only — aggregation and retros are out of scope and left to teams."* Nothing reads the field except [[seeds-plan-list]]'s `--outcome` filter. There is no rollup, no per-template success rate, no feedback into the templates themselves.

That gap is worth naming, because the framework's own thesis argues for closing it. `PLAN_SPEC.md` holds that when an implementation fails the fix belongs in the *planning process* — a new section, validation rule, or risk check. `outcome` is where the evidence for such a change would come from: three `failure` results against the same template is exactly the signal that the template is missing a section. Seeds records the datum and stops. The compounding half is left to mulch, which [[seeds-plan-prompt]] reads back in as prior art on the next plan — so the loop does close in the os-eco ecosystem, just not inside seeds.

Compare [[bmad-retrospective]] and [[ce-compound]], which run a whole facilitated pass to extract lessons; this is a single enum write.

## See Also
- [[seeds-plan-prompt]] — where prior failures re-enter the process, via mulch.
- [[seeds-plan-list]] — the only consumer of the recorded outcome.
- [[ce-compound]] · [[gstack-learn]] — the substantive Learn capabilities this is a stub beside.
- [[stage-learn]] — the canonical stage this implements.
