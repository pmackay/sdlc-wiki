---
type: capability
subtype: skill
belongs_to: "[[addy-agent-skills]]"
implements: "[[stage-release]]"
delegates_to: []
produces: []
applies: ["[[pattern-shift-left]]", "[[pattern-feature-flags]]", "[[pattern-trunk-based-development]]"]
equivalent_to: []
sources: "Addy Osmani — Agent Skills (2026)"
raw: ["../../raw/addy-agent-skills/2026-07-04-agent-skills.md"]
updated: 2026-07-04
---

# CI/CD & Automation

Automates the quality gates so no change reaches production without passing lint, type checks,
tests, build, and security audit — the enforcement mechanism for every other skill, applied
consistently on every change. Two principles anchor it: [[pattern-shift-left]] (catch problems
as early in the pipeline as possible, where they cost minutes not hours) and *Faster is Safer*
(smaller, more frequent releases reduce risk rather than increase it).

Its distinctive mechanism is the sequential quality-gate pipeline where no gate can be skipped —
if lint fails you fix lint, you don't disable the rule. Beyond the gates it covers preview and
staged deployments, [[pattern-feature-flags]] to decouple deployment from release, rollback
workflows, and a failure feedback loop that pipes CI errors straight back to the agent for a
fix. It leans on [[pattern-trunk-based-development]] as the branching model the pipeline guards.

## See Also
- [[pattern-shift-left]] — the early-detection principle it enforces.
- [[pattern-feature-flags]] — how it decouples deploy from release.
- [[stage-release]] — the canonical stage this implements.
