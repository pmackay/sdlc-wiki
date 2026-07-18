---
type: capability
subtype: skill
belongs_to: "[[compound-engineering]]"
implements: "[[stage-plan]]"
delegates_to: ["[[ce-agent-native-planning-strategist]]", "[[ce-architecture-strategist]]", "[[ce-spec-flow-analyzer]]", "[[ce-git-history-analyzer]]", "[[ce-data-migration-reviewer]]", "[[ce-deployment-verification-agent]]"]
produces: ["[[artifact-plan-md]]"]
applies: ["[[pattern-context-engineering]]", "[[pattern-knowledge-compounding]]", "[[pattern-shift-left]]"]
equivalent_to: ["[[gsd-plan-phase]]", "[[addy-planning]]", "[[speckit-plan]]", "[[speckit-tasks]]", "[[sp-writing-plans]]"]
sources: "Compound Engineering — EveryInc/compound-engineering-plugin (2026)"
raw: ["../../raw/compound-engineering/2026-07-04-compound-engineering-every.md", "../../raw/compound-engineering/2026-07-04-compound-engineering-plugin.md"]
updated: 2026-07-04
---

# /ce-plan

`/ce-plan` — "Bound execution with guardrails, enrich plans with U-IDs and test scenarios, WHAT
not HOW." Step 2 of the loop and, per Every, the single biggest time sink (~40% of a developer's
time — the heart of the 80/20 front-load). It takes the requirements from [[ce-brainstorm]] and
enriches them into an **implementation-ready** plan (`docs/plans/`, [[artifact-plan-md]]):
uniquely-identified units (U-IDs), test scenarios, and **guardrails** that bound what
[[ce-work]] may do. Agents research the codebase + commit history + best practices and read the
compound corpus first, so the plan builds a shared mental model before any code exists.

It implements [[stage-plan]] and is the pivot of the WHAT→HOW split: `ce-plan` fixes the WHAT
(scope, guardrails, success criteria); [[ce-work]] figures out the HOW in code.

## Cross-framework equivalents
Plan cluster: `ce-plan` ↔ [[gsd-plan-phase]] ↔ [[addy-planning]] ↔ [[speckit-plan]] +
[[speckit-tasks]] — research, design, and decompose into verifiable, dependency-ordered units.
`ce-plan`'s signature is **guardrails + U-IDs + test scenarios** as the contract handed to
execution.

## See Also
- [[gsd-plan-phase]] · [[addy-planning]] · [[speckit-plan]] · [[speckit-tasks]] — plan-cluster counterparts.
- [[ce-doc-review]] — reviews this plan before execution ([[pattern-plan-verification-loop]]).
- [[ce-brainstorm]] — supplies the requirements; [[ce-work]] — consumes the plan.
- [[stage-plan]] — the canonical stage this implements.
