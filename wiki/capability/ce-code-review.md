---
type: capability
subtype: skill
belongs_to: "[[compound-engineering]]"
implements: "[[stage-review]]"
delegates_to: ["[[ce-learnings-researcher]]"]
produces: ["[[artifact-review-report]]"]
applies: ["[[pattern-parallel-persona-review]]", "[[pattern-adversarial-review]]", "[[pattern-fresh-context-subagents]]", "[[pattern-knowledge-compounding]]"]
equivalent_to: ["[[addy-code-review]]", "[[bmad-code-review]]", "[[mp-code-review]]", "[[gstack-review]]", "[[sp-requesting-code-review]]"]
sources: "Compound Engineering — EveryInc/compound-engineering-plugin (2026)"
raw: ["../../raw/compound-engineering/2026-07-04-compound-engineering-every.md", "../../raw/compound-engineering/2026-07-04-compound-engineering-plugin.md"]
updated: 2026-07-09
---

# /ce-code-review

`/ce-code-review` — "Structured code review with skill-local personas, confidence-gated findings, four modes." Step 5 of the loop and the wiki's richest review fan-out: ~16 skill-local reviewer personas (correctness, security, performance, maintainability, reliability, testing, api-contract, data-migration, adversarial, agent-native, deployment-verification, project-standards, previous-comments, learnings-researcher, + Swift/iOS and frontend-races stack reviewers) run in fresh context ([[pattern-fresh-context-subagents]], [[pattern-parallel-persona-review]]), with an **adversarial** and optional **cross-model** pass ([[pattern-adversarial-review]]). Findings are **confidence-gated** — only those above a bar surface — and one persona (`learnings-researcher`) pulls the `docs/solutions/` compound corpus in, so past lessons sharpen this review ([[pattern-knowledge-compounding]] on the consuming side). → [[artifact-review-report]].

It implements [[stage-review]] (quality gate) and is the code-side sibling of [[ce-doc-review]].

## Cross-framework equivalents
Code-review cluster: `ce-code-review` ↔ [[addy-code-review]] ↔ [[bmad-code-review]] — multi-lens pre-merge quality review. (GSD's [[gsd-verifier]] is validate-side too but goal-backward/spec-conformance, so it sits in the [[openspec-verify]] cluster, not here.) `ce-code-review` most resembles [[bmad-code-review]] (adversarial parallel layers) and Addy's `/ship` persona fan-out, but adds **confidence gating**, **cross-model** review, and **compound-corpus grounding**.

## See Also
- [[addy-code-review]] · [[bmad-code-review]] · [[gsd-verifier]] — code-review-cluster counterparts.
- [[addy-code-reviewer]] — Addy's Staff-Engineer review persona (the single-persona analogue).
- [[ce-doc-review]] — the plan-side sibling; [[ce-simplify-code]] — runs just before this.
- [[stage-review]] — the canonical stage this implements.
