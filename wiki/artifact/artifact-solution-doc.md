---
type: artifact
sources: "EveryInc/compound-engineering-plugin — skills/ce-compound (2026)"
raw: ["../../raw/compound-engineering/2026-07-04-compound-engineering-plugin.md"]
updated: 2026-07-05
---

# Artifact: solution doc

Compound Engineering's **signature artifact** — a structured learning file under
`docs/solutions/`, written by [[ce-compound]] at the close of each iteration. It records a
problem that was solved and its reusable resolution: the symptom, the root cause, the fix, and
the generalizable lesson, validated against a YAML frontmatter schema
(`skills/ce-compound/references/schema.yaml`).

What makes it distinctive is **who reads it and when**: unlike a changelog (for humans, about
what shipped) or an [[artifact-adr]] (a one-time decision record), a solution doc is
**machine-consumable grounding** that future *agents* pull in automatically — [[ce-brainstorm]],
[[ce-plan]], and [[ce-code-review]] read the corpus (via a `learnings-researcher` persona) so a
past lesson shapes the next feature without a human re-teaching it. The corpus is a **maintained
collection**, not a write-only log: [[ce-compound-refresh]] applies Keep/Update/Consolidate/
Replace/Delete verdicts to keep it accurate and small.

It is the concrete embodiment of [[pattern-knowledge-compounding]] and the primary output of the
[[stage-learn]] stage. BMAD's [[bmad-retrospective]] produces the sibling *human-facing* form
(lessons + action items); Compound Engineering's is agent-facing.

## Produced by (backlinks)
- [[ce-compound]] — writes solution docs from mined completed work (orchestrates the council below).
- [[ce-compound-refresh]] — maintains the corpus over time.
- Council members whose analysis is distilled into the docs: [[ce-session-historian]], [[ce-pattern-recognition-specialist]], [[ce-best-practices-researcher]], [[ce-framework-docs-researcher]], [[ce-security-sentinel]], [[ce-performance-oracle]], [[ce-data-integrity-guardian]].
- [[gstack-learn]] — gstack's cross-session learnings corpus (the agent-grounding flavor of learn).

## See Also
- [[pattern-knowledge-compounding]] — the technique this artifact realizes.
- [[artifact-explainer]] — the human-facing learning artifact sibling ([[ce-explain]]).
- [[artifact-adr]] — a one-time decision record, versus this reusable, agent-consumed lesson.
- [[stage-learn]] — the stage this artifact is the output of.
