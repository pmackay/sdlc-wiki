---
type: capability
subtype: skill
belongs_to: "[[bmad]]"
implements: "[[stage-align]]"
delegates_to: []
produces: []
applies: ["[[pattern-context-engineering]]"]
equivalent_to: ["[[openspec-explore]]"]
sources: "bmad-code-org/BMAD-METHOD — bmad-document-project (2026)"
raw: ["../../raw/bmad/2026-07-04-bmad-method-framework.md"]
updated: 2026-07-04
---

# bmad-document-project

**`bmad-document-project`** — "Document brownfield projects for AI context." Dispatched by [[bmad-tech-writer]] (and [[bmad-analyst]], menu `DP`), it scans an existing codebase — full scan or targeted deep-dive — and produces an index, overview, source-tree map, and per-area deep-dives so agents can work an unfamiliar codebase with full context ([[pattern-context-engineering]]).

## Cross-framework cluster (codebase investigation)
- [[openspec-explore]] — OpenSpec's brownfield entry point: investigate the codebase before committing. Both realize the **codebase-investigation flavor** of [[stage-align]] (distinct from the human-interrogation / grilling flavor).

## See Also
- [[bmad]] — the framework.
- [[bmad-tech-writer]] — the persona that owns this workflow.
- [[stage-align]] — the canonical stage.
