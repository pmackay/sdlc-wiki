---
type: capability
subtype: sub-agent
belongs_to: "[[compound-engineering]]"
implements: "[[stage-align]]"
delegates_to: []
produces: []
applies: ["[[pattern-fresh-context-subagents]]", "[[pattern-source-grounding]]"]
equivalent_to: []
sources: "Compound Engineering — EveryInc/compound-engineering-plugin (2026)"
raw: ["../../raw/compound-engineering/2026-07-04-compound-engineering-every.md", "../../raw/compound-engineering/2026-07-04-compound-engineering-plugin.md"]
updated: 2026-07-05
---

# ce-precedent-activity-scout

A **precedent-&-activity scout** for the verdict skill ([[ce-pov]]). It surfaces two things without forming an opinion: (1) **precedent** — has the team already evaluated, adopted, or *rejected* this? (closed issues, PR threads, a PR closed-without-merging = "tried X, backed it out", `docs/solutions/`, ADRs) — often the highest-value finding because it stops the caller re-litigating a settled question; and (2) **incumbent pain / exposure** — open issues and in-flight PRs bearing on the candidate or its incumbent.

It implements [[stage-align]] (evaluate-external-inputs flavor) as the **prior-decision** axis of [[ce-pov]]'s grounding trio. It reads the same [[artifact-solution-doc|`docs/solutions/`]] corpus as [[ce-learnings-researcher]], but to find *decisions* rather than *lessons*.

## See Also
- [[ce-pov]] — the dispatcher.
- [[ce-external-evidence-researcher]] · [[ce-project-grounding-scout]] — the other two verdict scouts.
- [[ce-issue-intelligence-analyst]] — also mines the tracker, but for theme-level ideation signal.
- [[stage-align]] — the canonical stage this supports.
