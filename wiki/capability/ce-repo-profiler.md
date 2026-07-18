---
type: capability
subtype: sub-agent
belongs_to: "[[compound-engineering]]"
implements: "[[stage-align]]"
delegates_to: []
produces: []
applies: ["[[pattern-fresh-context-subagents]]", "[[pattern-context-engineering]]"]
equivalent_to: []
sources: "Compound Engineering — EveryInc/compound-engineering-plugin (2026)"
raw: ["../../raw/compound-engineering/2026-07-04-compound-engineering-every.md", "../../raw/compound-engineering/2026-07-04-compound-engineering-plugin.md"]
updated: 2026-07-05
---

# ce-repo-profiler

A repo-profiling scout that derives the **question-agnostic project profile** — the stable
orientation (languages, manifests, lockfiles, license, root docs, top-level structure) that
every repo-grounding skill reuses. It is dispatched only on a **cache miss**; its output is
written to a shared profile cache and reused across skills and sessions at the same commit. It
derives *only* agnostic facts — anything question-specific is the caller's job, or the cached
artifact would be wrong to reuse.

It is the most widely shared sub-agent in Compound Engineering — nearly every skill
([[ce-brainstorm]], [[ce-ideate]], [[ce-code-review]], [[ce-compound]], [[ce-debug]],
[[ce-explain]]) dispatches it — so it is filed under [[stage-align]] as a front-of-loop
grounding primitive rather than owned by one stage. It embodies [[pattern-context-engineering]]:
compute the orientation once, cache it, feed it to everything.

## See Also
- [[ce-brainstorm]] — a primary dispatcher (shared across the whole loop via a profile cache).
- [[ce-learnings-researcher]] — the companion grounding scout that adds *past-lessons* context on top of the profile.
- [[pattern-context-engineering]] · [[pattern-fresh-context-subagents]] — the techniques.
- [[stage-align]] — the canonical stage this supports.
