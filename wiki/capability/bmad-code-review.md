---
type: capability
subtype: skill
belongs_to: "[[bmad]]"
implements: "[[stage-review]]"
delegates_to: []
produces: ["[[artifact-review-report]]"]
applies: ["[[pattern-adversarial-review]]", "[[pattern-parallel-persona-review]]", "[[pattern-fresh-context-subagents]]"]
equivalent_to: ["[[addy-code-review]]", "[[ce-code-review]]", "[[mp-code-review]]", "[[gstack-review]]", "[[sp-requesting-code-review]]"]
sources: "bmad-code-org/BMAD-METHOD — bmad-code-review (2026)"
raw: ["../../raw/bmad/2026-07-04-bmad-method-framework.md"]
updated: 2026-07-09
---

# bmad-code-review

**`bmad-code-review`** — "Review code changes adversarially using parallel review layers (Blind
Hunter, Edge Case Hunter, Acceptance Auditor) with structured triage." Owned by [[bmad-dev]]
and run in "fresh context, ideally different LLM" than the one that wrote the code
([[pattern-fresh-context-subagents]]) → [[artifact-review-report]].

It combines two patterns: it fans several single-lens reviewer layers out in parallel
([[pattern-parallel-persona-review]]), each under the [[pattern-adversarial-review|adversarial]]
mandate that "the reviewer must find issues. No 'looks good' allowed" — with the honest caveat
that "because the AI is instructed to find problems, it will find problems … Human filtering
remains the essential final step."

## Cross-framework cluster (code review)
- [[addy-code-review]] — Addy's five-axis review with severity labels + change sizing.

Both produce a [[artifact-review-report]]; BMAD's distinction is the multi-layer adversarial
fan-out over a single diff, versus Addy's structured single-pass rubric.

## See Also
- [[bmad]] — the framework.
- [[addy-code-reviewer]], [[gsd-verifier]] — related quality/verification agents.
- The **Test Architect (TEA)** module (Murat) adds enterprise quality gates BMM core lacks — see [[bmad]].
- [[stage-review]] — the canonical stage.
