---
type: capability
subtype: command
belongs_to: "[[tessl]]"
implements: "[[stage-review]]"
delegates_to: []
produces: ["[[artifact-review-report]]"]
applies: ["[[pattern-deterministic-gates]]", "[[pattern-scale-adaptive-planning]]"]
equivalent_to: ["[[pstack-blast-radius]]"]
sources: "Tessl docs — CLI v0.108.0 (2026)"
raw: ["../../raw/tessl/2026-09-12-tessl-platform.md"]
updated: 2026-09-12
---

# tessl change risk

Assess the risk of the current diff and **exit non-zero when human review is required**: `tessl change risk`, with `tessl change risk init` writing starter configuration (including a "conservative starter" preset).

The exit-code behavior is what makes it interesting rather than advisory. This is a machine-readable answer to *does a person need to look at this?*, which is the routing decision that matters most once agents open more PRs than anyone can read. It converts reviewer attention from a constant into something allocated by measured blast radius — [[pattern-scale-adaptive-planning]] applied to the review budget rather than to planning ceremony.

Its nearest counterpart is [[pstack-blast-radius]], and the contrast is instructive. Both answer *how dangerous is this change?* — but pstack's is a **workflow a developer runs** that demands one safety fact be proven by executing code, and Tessl's is a **gate in CI** that emits a verdict and an exit code. Depth versus throughput, and the split follows the layer: a framework optimizes one engineer's rigor, a platform optimizes an organization's flow.

Tessl pairs it with [[tessl-change-verify]]: risk decides *whether* to look, verify decides *what fails*.

## See Also
- [[tessl-change-verify]] — the paired verifier pass over changed files.
- [[tessl-code-review]] — the full PR review this triages into.
- [[pstack-blast-radius]] — the framework-side counterpart, proof-driven rather than gate-driven.
- [[stage-review]] — the canonical stage this implements.
