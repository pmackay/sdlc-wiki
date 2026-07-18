---
type: pattern
sources: "Addy Osmani — Agent Skills (2026)"
updated: 2026-07-05
---

# Pattern: Source grounding (cite official docs)

Ground every framework/library decision in **official documentation**: look it up, cite the
source, and explicitly flag anything that could not be verified as unverified. Counters the
model's tendency to emit plausible-but-outdated API patterns from training data. The output
carries its provenance, so a reviewer can check the citation rather than trust the assertion.

## Applied by (backlinks)

Addy Osmani — Agent Skills:

- [[addy-source-driven-development]] — verify, cite, flag the unverified.

Compound Engineering:

- [[ce-ideate]] — grounds candidate directions in repo + web evidence.
- [[ce-pov]] — dual-grounded (repo + web) graded verdicts on external inputs.
- Research sub-agents — [[ce-web-researcher]], [[ce-external-evidence-researcher]], [[ce-slack-researcher]], [[ce-best-practices-researcher]], [[ce-framework-docs-researcher]] gather cited evidence.

gstack:

- [[gstack-office-hours]] · [[gstack-design-consultation]] · [[gstack-document-generate]] — research the landscape/codebase first (gstack's "Search Before Building" ethos).

## See Also
- [[pattern-adversarial-review]] — the complementary "distrust the output" technique.
- [[stage-implement]] — where source-grounded code is written.
