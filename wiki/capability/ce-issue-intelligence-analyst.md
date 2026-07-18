---
type: capability
subtype: sub-agent
belongs_to: "[[compound-engineering]]"
implements: "[[stage-align]]"
delegates_to: []
produces: []
applies: ["[[pattern-fresh-context-subagents]]"]
equivalent_to: []
sources: "Compound Engineering — EveryInc/compound-engineering-plugin (2026)"
raw: ["../../raw/compound-engineering/2026-07-04-compound-engineering-every.md", "../../raw/compound-engineering/2026-07-04-compound-engineering-plugin.md"]
updated: 2026-07-05
---

# ce-issue-intelligence-analyst

An **issue-intelligence analyst** that extracts strategic signal from noisy issue trackers. Its output is **themes, not tickets**: 25 duplicate bugs about the same failure mode is one signal about systemic reliability, not 25 problems. A leader reading its report should immediately understand which areas need investment and why.

Dispatched by [[ce-ideate]] (turning tracker signal into qualified directions), so it implements [[stage-align]]. It is the tracker-facing counterpart to [[ce-slack-researcher]] (chat) and [[ce-web-researcher]] (external) — together they feed grounded ideation. Related to [[ce-sweep]], which also ingests GitHub items but for per-item reconciliation rather than theme-level intelligence.

## See Also
- [[ce-ideate]] — the dispatcher (theme intelligence → ideas).
- [[ce-sweep]] — per-item feedback intake (vs this agent's theme-level roll-up).
- [[ce-precedent-activity-scout]] — also mines issues/PRs, but for prior-decision precedent under [[ce-pov]].
- [[stage-align]] — the canonical stage this supports.
