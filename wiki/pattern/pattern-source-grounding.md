---
type: pattern
sources: "Addy Osmani — Agent Skills (2026); jayminwest/seeds (2026); pstack v0.15.2 — Lauren Tan (2026); Builder.io — BuilderIO/skills (2026)"
updated: 2026-09-26
---

# Pattern: Source grounding (cite official docs)

Ground every framework/library decision in **official documentation**: look it up, cite the source, and explicitly flag anything that could not be verified as unverified. Counters the model's tendency to emit plausible-but-outdated API patterns from training data. The output carries its provenance, so a reviewer can check the citation rather than trust the assertion.

## Applied by (backlinks)

Addy Osmani — Agent Skills:

- [[addy-source-driven-development]] — verify, cite, flag the unverified.

Compound Engineering:

- [[ce-ideate]] — grounds candidate directions in repo + web evidence.
- [[ce-pov]] — dual-grounded (repo + web) graded verdicts on external inputs.
- Research sub-agents — [[ce-web-researcher]], [[ce-external-evidence-researcher]], [[ce-slack-researcher]], [[ce-best-practices-researcher]], [[ce-framework-docs-researcher]] gather cited evidence.

gstack:

- [[gstack-office-hours]] · [[gstack-design-consultation]] · [[gstack-document-generate]] — research the landscape/codebase first (gstack's "Search Before Building" ethos).

Seeds:

- [[seeds-plan-prompt]] — emits `prior_art` records (`{id, type, summary, relevance}`) mined from mulch alongside each plan section and instructs the model to ground its answer in them; the grounding corpus is the project's own accumulated conventions, decisions, and failures rather than external documentation.

pstack — **pointed at the organizational record rather than the public one**, which is new here:

- [[pstack-why]] — discovers available MCP servers at run time and fans one investigator across each of seven evidence categories: source control, issue tracker, long-form docs, real-time chat, infrastructure observability, error tracking, and the product analytics warehouse. Ships per-source playbooks (Linear, Notion, Slack, Sentry, Datadog, Databricks, postmortems, code archaeology), skips an unavailable MCP and says so, and treats **a null result as a finding**. Seeds every investigator with a code anchor built inline from `git blame`, `git log --follow`, and `gh pr view`.
- [[pstack-recall]] — reuses that machinery with the question re-pointed from *why was this built* to *what is the current state, what has been tried and did not hold, and what are users still reporting*.

builder-skills:

- [[builder-read-the-damn-docs]] — **signature**. An explicit trigger list (latest/current/official, new or upgraded packages, fast-moving APIs, auth/billing/migrations, deprecation errors, and *"you catch yourself about to write 'usually', 'probably', 'I think'"*), `npm view <pkg> version` before adding a dependency, and a stated fallback when docs cannot be reached.
- [[builder-visual-plan]] — *"Research before you draft"*, naming real files and symbols and leading with reuse.

## See Also
- [[pattern-adversarial-review]] — the complementary "distrust the output" technique.
- [[stage-implement]] — where source-grounded code is written.
