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

# sd plan review

`sd plan review <pl-id> --by <name>` — record a reviewer's name against a plan. *"Informational; not a state transition."*

It is listed here for completeness and because of the gap it exposes. The framework's thesis is that **plans should be the artifact reviewed** — attention spent before implementation rather than after — and this is the entire mechanism supporting it: a free-text name field, plus a *"review suggested"* hint that [[seeds-plan-show]] prints when a plan is `approved` or `active` with no reviewer recorded. Nothing gates on it, nothing checks that a review happened, and the reviewer records no findings.

So it maps to **no canonical SDLC stage**: storing who is said to have looked at a plan does not perform [[stage-review]] in the sense the other frameworks' review capabilities do — [[gstack-plan-eng-review]] and [[ce-doc-review]] actually read the plan and return findings. The honest reading is that seeds asserts the review thesis and delegates the execution of it to whatever agent or human the team points at the plan; what seeds contributes is the *validation* gate ([[seeds-plan-submit]]), which is a different control entirely.

## See Also
- [[seeds-plan-show]] — prints the review-suggested hint.
- [[seeds-plan-submit]] — the framework's real, deterministic plan gate.
- [[gstack-plan-eng-review]] · [[ce-doc-review]] · [[gsd-plan-checker]] — plan reviews that produce findings.
- [[stage-review]] — the stage this deliberately does not implement.
