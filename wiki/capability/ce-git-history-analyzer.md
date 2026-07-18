---
type: capability
subtype: sub-agent
belongs_to: "[[compound-engineering]]"
implements: "[[stage-plan]]"
delegates_to: []
produces: []
applies: ["[[pattern-fresh-context-subagents]]", "[[pattern-context-engineering]]"]
equivalent_to: []
sources: "Compound Engineering — EveryInc/compound-engineering-plugin (2026)"
raw: ["../../raw/compound-engineering/2026-07-04-compound-engineering-every.md", "../../raw/compound-engineering/2026-07-04-compound-engineering-plugin.md"]
updated: 2026-07-05
---

# ce-git-history-analyzer

A **Git History Analyzer** — archaeological analysis of a repository. It traces file evolution
(`git log --follow`), code origins (`git blame -w -C -C -C`), identifies major refactorings and
renames, and surfaces patterns in history that inform current decisions. It uses native
search/read tools for non-git exploration and shell only for git, one command per call.

Dispatched by [[ce-plan]] (history as planning context), it implements [[stage-plan]]
([[pattern-context-engineering]]). It complements [[ce-repo-profiler]] (static project profile)
with the *temporal* dimension — how the code got to where it is — and overlaps in spirit with the
essay's "agents research the codebase and commit history" during planning.

## See Also
- [[ce-plan]] — the dispatcher.
- [[ce-repo-profiler]] — the static-profile companion (structure vs history).
- [[stage-plan]] — the canonical stage this supports.
