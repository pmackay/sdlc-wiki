---
type: capability
subtype: sub-agent
belongs_to: "[[compound-engineering]]"
implements: "[[stage-learn]]"
delegates_to: []
produces: ["[[artifact-explainer]]"]
applies: ["[[pattern-fresh-context-subagents]]"]
equivalent_to: []
sources: "Compound Engineering — EveryInc/compound-engineering-plugin (2026)"
raw: ["../../raw/compound-engineering/2026-07-04-compound-engineering-every.md", "../../raw/compound-engineering/2026-07-04-compound-engineering-plugin.md"]
updated: 2026-07-05
---

# ce-work-recap-scout

A **work-recap scout** that gathers the evidence for a recap explainer: what actually happened in a repository over a given window — git activity, merged/open PRs — with pointers precise enough that the explainer can teach from them. It **extracts and quotes; it does not interpret, rank, or editorialize** (that is the explainer's job).

Dispatched by [[ce-explain]], it implements [[stage-learn]], feeding the human-facing [[artifact-explainer]]. It is the recent-work, human-facing counterpart to [[ce-session-historian]] (past agent sessions, feeding the machine-facing [[artifact-solution-doc]]) — together they mine "what happened" for the two flavors of [[stage-learn]].

## See Also
- [[ce-explain]] — the dispatcher; [[ce-session-historian]] — the past-sessions, agent-facing sibling.
- [[artifact-explainer]] — the output it feeds.
- [[stage-learn]] — the canonical stage this supports.
