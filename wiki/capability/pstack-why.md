---
type: capability
subtype: skill
belongs_to: "[[pstack]]"
implements: "[[stage-align]]"
delegates_to: []
produces: ["[[artifact-explainer]]"]
applies: ["[[pattern-source-grounding]]", "[[pattern-wave-parallelism]]", "[[pattern-evidence-before-claims]]", "[[pattern-fresh-context-subagents]]"]
equivalent_to: ["[[mp-research]]", "[[gsd-phase-researcher]]"]
sources: "pstack v0.15.2 — Lauren Tan (2026)"
raw: ["../../raw/pstack/2026-09-11-pstack-plugin.md"]
updated: 2026-09-11
---

# /why

Investigates the motivation and intent behind code: design rationale, tradeoffs, the motivating edge case, an external constraint, dead code, a regression, a postmortem, a data-backed threshold. Companion to [[pstack-how]] — *how* answers what the code does, *why* answers what forces led to its shape.

**This is the wiki's strongest instance of [[pattern-source-grounding]] pointed at organizational rather than public evidence.** Every other framework's research capability searches the codebase, the web, or a docs corpus. `/why` instead **discovers the available MCP servers at run time** and maps each to one of seven evidence categories, then spawns one investigator per category in parallel:

- source control history
- issue / ticket tracker
- long-form documents
- real-time team chat
- infrastructure observability
- error tracking
- product analytics warehouse

Reference playbooks ship per source (Linear, Notion, Slack, Sentry, Datadog, Databricks, incident postmortems, and code archaeology), so the skill degrades gracefully: an unavailable MCP is skipped and said so, and **a null result is itself a finding**. Before any investigator is spawned the skill builds a **code anchor** inline — file paths and line ranges, key symbols, the last commits via `git blame` and `git log --follow`, PR numbers extracted from merge subjects, and the PR bodies and reviews pulled through `gh` — and passes it to every investigator as seed context.

Its second distinctive contribution is an explicit **epistemics contract** (`references/epistemics.md`): a confidence framework and phrasing guide the synthesizer must follow, separating what is known from what is inferred. That contract is load-bearing enough that [[pstack-teach]] is forbidden from rewording it — *keep `why`'s confidence language intact, its hedges are findings, not style*.

## See Also
- [[pstack-how]] — the mechanism companion; the two are designed as a pair.
- [[pstack-recall]] — reuses this skill's per-source playbooks, re-pointed from "why was this built" to "what is the current state".
- [[pstack-blast-radius]] — borrows its citation rules and uses its step 2 to pull the PR and commits.
- [[mp-research]] · [[gsd-phase-researcher]] — the cross-framework research counterparts, both aimed at external or codebase sources rather than the organizational record.
- [[stage-align]] — the canonical stage this implements.
