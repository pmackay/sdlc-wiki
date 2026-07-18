---
type: capability
subtype: sub-agent
belongs_to: "[[bmad]]"
implements: "[[stage-implement]]"
delegates_to: ["[[bmad-create-story]]", "[[bmad-dev-story]]", "[[bmad-code-review]]", "[[bmad-sprint-planning]]", "[[bmad-retrospective]]", "[[bmad-quick-dev]]"]
produces: ["[[artifact-atomic-commit]]", "[[artifact-story]]", "[[artifact-review-report]]"]
applies: ["[[pattern-persona-agents]]", "[[pattern-test-driven-development]]", "[[pattern-fresh-context-subagents]]", "[[pattern-context-engineering]]"]
equivalent_to: []
sources: "bmad-code-org/BMAD-METHOD — bmad-agent-dev (2026)"
raw: ["../../raw/bmad/2026-07-04-bmad-method-framework.md"]
updated: 2026-07-04
---

# bmad-dev

**Amelia** 💻 (`bmad-agent-dev`) — BMAD's **Implementation persona**: "Implement approved stories with test-first discipline and ship working, verified code." She is "disciplined in Kent Beck's TDD and the Pragmatic Programmer's precision" and "speaks in file paths and AC IDs" ([[pattern-persona-agents]], [[pattern-test-driven-development]]).

In v6 Amelia **absorbed the classic Scrum Master and QA roles**, so she owns the entire implementation loop and dispatches the widest menu in the method:

- [[bmad-sprint-planning]] (SP) — generate the sprint backlog / status.
- [[bmad-create-story]] (CS) — write the context-filled [[artifact-story|story file]].
- [[bmad-dev-story]] (DS) — implement a story test-first.
- [[bmad-code-review]] (CR) — adversarial review in fresh context.
- [[bmad-quick-dev]] (QD) — the Quick-Flow fast path.
- [[bmad-retrospective]] (ER) — post-epic learning close-out.
- qa-generate-e2e-tests (QA) — E2E test generation (catalogued on [[bmad]]).

She runs each story in a **fresh context** and reviews in a different one ([[pattern-fresh-context-subagents]]), leaning on the story file's embedded context ([[pattern-context-engineering]]).

## See Also
- [[bmad]] — the framework.
- [[gsd-executor]], [[gsd-execute-phase]] — GSD's execution agents; Amelia is a single persona doing what GSD spreads across executor + verifier + debugger.
- [[stage-implement]] — the canonical stage.
