---
type: capability
subtype: skill
belongs_to: "[[superpowers]]"
implements: "[[stage-review]]"
delegates_to: []
produces: ["[[artifact-review-report]]"]
applies: ["[[pattern-adversarial-review]]", "[[pattern-fresh-context-subagents]]"]
equivalent_to: ["[[addy-code-review]]", "[[ce-code-review]]", "[[gstack-review]]", "[[bmad-code-review]]", "[[mp-code-review]]"]
sources: "Superpowers v6.1.1 (2026)"
raw: ["../../raw/superpowers/2026-07-17-superpowers.md"]
updated: 2026-07-17
---

# requesting-code-review

Dispatch a **fresh-context code-reviewer subagent** to catch issues before they cascade ([[pattern-adversarial-review]], [[pattern-fresh-context-subagents]]). *"Review early, review often."* The reviewer gets precisely-crafted context (a description, the requirements/plan, and the BASE→HEAD SHAs) — **never the controller's session history** — so it judges the work product, not the author's thought process → [[artifact-review-report]].

Review is **mandatory** after each task in subagent-driven development, after a major feature, and before merge; optional but valuable when stuck or before refactoring. Findings are acted on by **severity**: fix Critical immediately, fix Important before proceeding, note Minor for later — and the skill explicitly permits **pushing back with technical reasoning** if the reviewer is wrong (the request side of [[sp-receiving-code-review]]). It ships the reviewer prompt template (`code-reviewer.md`) that [[sp-subagent-driven-development]] also uses for its final whole-branch review.

It joins the five-plus-framework **code-review cluster** — [[addy-code-review]] ↔ [[ce-code-review]] ↔ [[gstack-review]] ↔ [[bmad-code-review]] ↔ [[mp-code-review]] — all producing [[artifact-review-report]]; Superpowers' distinctive angle is treating review as a **dispatched fresh-context subagent gate wired into the execution loop** (between every task), not a standalone command.

## See Also
- [[sp-receiving-code-review]] — the reception side: how to respond to the findings this produces.
- [[sp-subagent-driven-development]] — reuses this skill's reviewer template for the final whole-branch review.
- [[addy-code-review]] · [[ce-code-review]] · [[gstack-review]] · [[bmad-code-review]] · [[mp-code-review]] — the code-review cluster.
- [[artifact-review-report]] — the output; [[pattern-adversarial-review]] · [[pattern-fresh-context-subagents]] — the techniques.
- [[stage-review]] — the canonical stage this implements.
