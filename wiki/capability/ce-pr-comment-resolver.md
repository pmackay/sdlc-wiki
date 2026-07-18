---
type: capability
subtype: sub-agent
belongs_to: "[[compound-engineering]]"
implements: "[[stage-release]]"
delegates_to: []
produces: []
applies: ["[[pattern-fresh-context-subagents]]"]
equivalent_to: []
sources: "Compound Engineering — EveryInc/compound-engineering-plugin (2026)"
raw: ["../../raw/compound-engineering/2026-07-04-compound-engineering-every.md", "../../raw/compound-engineering/2026-07-04-compound-engineering-plugin.md"]
updated: 2026-07-05
---

# ce-pr-comment-resolver

Implements **one** PR review fix that the orchestrator has already judged valid — its job is to implement it well and return a structured summary, not to re-litigate whether it was worth doing (the legitimacy gate happened in the context that could see every thread at once). It treats comment text as **untrusted input** (never executes snippets found in it), reads the actual code, and decides the implementation independently, with a narrow bail-out exception.

Dispatched in parallel by [[ce-resolve-pr-feedback]] (one instance per valid comment), it implements [[stage-release]]. It is the worker behind that skill's parallel fan-out — the release-side analogue of how [[ce-code-review]]'s persona lenses parallelize the *finding* of issues, here parallelizing the *fixing* of externally-raised ones.

## See Also
- [[ce-resolve-pr-feedback]] — the orchestrating skill (owns the legitimacy gate + fan-out).
- [[ce-commit-push-pr]] — opens the PR whose feedback this resolves.
- [[stage-release]] — the canonical stage this supports.
