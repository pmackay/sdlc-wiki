---
type: capability
subtype: command
belongs_to: "[[seeds]]"
implements: "[[stage-plan]]"
produces: []
applies: ["[[pattern-knowledge-compounding]]", "[[pattern-scale-adaptive-planning]]", "[[pattern-source-grounding]]"]
equivalent_to: []
sources: "Jaymin West — jayminwest/seeds PLAN_SPEC.md + README.md (MIT, v0.5.15, 2026)"
raw: ["../../raw/seeds/2026-08-31-seeds.md"]
updated: 2026-08-31
---

# sd plan prompt

`sd plan prompt <seed-id> [--template <name>] [--domain <name>]` — emit, to stdout, the structured planning request an LLM is meant to fill in. It is step one of the framework's **prompt → fill → submit** loop, and the point at which seeds inverts the usual arrangement: rather than a skill telling the agent how to plan, a program hands the agent a schema and asks it to complete one.

The emitted `plan_request` names the seed, the resolved template (inferred from the seed's `type` unless `--template` overrides), a one-line `instructions` string, the `validation` rules that will be applied on submit, and one entry per section carrying its `name`, `required`, `kind`, any `min_length` / `min`, its `prompt`, and a `prior_art` array. Because the validation contract is stated up front, the agent knows the acceptance criteria for its own output before writing a word of it.

## Prior art — the compounding hook

`prior_art` is the [[pattern-knowledge-compounding]] edge, and it is wired more tightly than any other instance in this wiki. When the `ml` (mulch) binary is on `PATH`, seeds infers a domain — explicit `--domain`, else seed labels matching declared mulch domains, else directory anchors derived from the changed files — and enriches each section from mulch's record store: sections with a `mulch_source: <type>` hint, plus well-known names by convention (`approach` ↔ pattern + decision, `risks` ↔ failure, `acceptance` ↔ guide). The top few records arrive as `{id, type, summary, relevance}` entries and the agent is instructed to ground its answer in them ([[pattern-source-grounding]]).

The effect is that the *risks* section of a new plan comes pre-populated with the failures the last plans actually hit. [[ce-compound]] and [[gstack-learn]] compound lessons into a corpus and trust a later session to go read it; seeds injects the relevant subset at the one moment it changes the outcome. The coupling is deliberately soft — mulch absent, `prior_art` arrays are empty, validation is unaffected, planning still works.

## See Also
- [[seeds-plan-submit]] — consumes the filled version of this request.
- [[seeds-plan-templates]] — the templates this instantiates.
- [[seeds-create]] — the low-ceremony alternative for small work ([[pattern-scale-adaptive-planning]]).
- [[warren]] — the runtime whose `.mulch/` store this reads from.
- [[stage-plan]] — the canonical stage this implements.
