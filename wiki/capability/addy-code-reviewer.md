---
type: capability
subtype: sub-agent
belongs_to: "[[addy-agent-skills]]"
implements: "[[stage-review]]"
delegates_to: []
produces: ["[[artifact-review-report]]"]
applies: ["[[pattern-fresh-context-subagents]]"]
equivalent_to: []
sources: "Addy Osmani — Agent Skills (2026)"
raw: ["../../raw/addy-agent-skills/2026-07-04-agent-skills.md"]
updated: 2026-07-05
---

# Code Reviewer (persona)

A Senior Staff Engineer persona that conducts thorough pre-merge review across five dimensions: correctness, readability, architecture, security, and performance. It reads the spec and tests first to understand intent, then categorizes every finding as Critical, Important, or Suggestion, and issues an APPROVE or REQUEST CHANGES verdict. The implicit bar is "would a staff engineer approve this?" — code with Critical issues is never approved, and every Critical or Important finding must carry a concrete fix recommendation.

It runs as a stateless review subagent with a fresh context and never invokes other personas: if a change warrants a deeper security or test pass, it surfaces that as a recommendation rather than delegating. It is invoked directly via [[addy-code-review]] for a single-perspective review, and participates in the [[addy-shipping]] `/ship` fan-out, where three review subagents (this one, the test engineer, and the security auditor) run in parallel.

## See Also
- [[addy-code-review]]
- [[addy-shipping]]
- [[gsd-verifier]]
- [[stage-review]]
