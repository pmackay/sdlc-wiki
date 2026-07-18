---
type: capability
subtype: sub-agent
belongs_to: "[[compound-engineering]]"
implements: "[[stage-learn]]"
delegates_to: []
produces: ["[[artifact-solution-doc]]"]
applies: ["[[pattern-fresh-context-subagents]]", "[[pattern-knowledge-compounding]]"]
equivalent_to: []
sources: "Compound Engineering — EveryInc/compound-engineering-plugin (2026)"
raw: ["../../raw/compound-engineering/2026-07-04-compound-engineering-every.md", "../../raw/compound-engineering/2026-07-04-compound-engineering-plugin.md"]
updated: 2026-07-05
---

# ce-session-historian

Extracts **institutional knowledge from coding-agent session history**. Given pre-extracted
skeleton and error files from the caller's session-history flow, it synthesizes findings about a
specific problem — what was learned, tried, and decided in prior sessions across Claude Code,
Codex, Cursor, and Pi. Its scope is **synthesis only** (the caller handles discovery, filtering,
and per-session extraction).

Dispatched by [[ce-compound]], it implements [[stage-learn]]: mining the *record of how the work
happened* is the raw material of [[pattern-knowledge-compounding]], feeding
[[artifact-solution-doc]]. It is the past-sessions analogue of [[ce-work-recap-scout]] (which
gathers recent work for a human explainer) and shares the "distill prior context" spirit of MP's
[[mp-handoff]].

## See Also
- [[ce-compound]] — the dispatcher; [[ce-work-recap-scout]] — the recent-work-recap sibling.
- [[ce-learnings-researcher]] — reads the resulting corpus back into new work.
- [[stage-learn]] — the canonical stage this supports.
