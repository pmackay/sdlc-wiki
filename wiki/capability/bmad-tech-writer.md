---
type: capability
subtype: sub-agent
belongs_to: "[[bmad]]"
implements: "[[stage-align]]"
delegates_to: ["[[bmad-document-project]]"]
produces: []
applies: ["[[pattern-persona-agents]]", "[[pattern-context-engineering]]"]
equivalent_to: []
sources: "bmad-code-org/BMAD-METHOD — bmad-agent-tech-writer (2026)"
raw: ["../../raw/bmad/2026-07-04-bmad-method-framework.md"]
updated: 2026-07-04
---

# bmad-tech-writer

**Paige** 📚 (`bmad-agent-tech-writer`) — BMAD's **documentation persona**: "Capture and curate
project knowledge so humans and future LLM agents stay in sync." She "writes with Julia
Evans's accessibility and Edward Tufte's visual precision" ([[pattern-persona-agents]]).

Paige's remit is documentation *as context engineering* — the docs she produces are inputs to
the other agents ([[pattern-context-engineering]]). Her menu: [[bmad-document-project]] (DP,
brownfield scan), write-document (WD), mermaid-gen (MG), validate-doc (VD), explain-concept
(EC). The latter four are conversational doc utilities catalogued on [[bmad]].

## See Also
- [[bmad]] — the framework.
- [[bmad-document-project]] — her primary brownfield-documentation workflow.
- [[addy-documentation]] — Addy's dev-time documentation skill (ADRs + API docs); Paige works earlier, capturing project knowledge for AI context rather than authoring reference docs.
- [[stage-align]] — the canonical stage.
