---
type: capability
subtype: skill
belongs_to: "[[addy-agent-skills]]"
implements: "[[stage-release]]"
delegates_to: ["[[addy-code-reviewer]]", "[[addy-security-auditor]]", "[[addy-test-engineer]]"]
produces: ["[[artifact-launch-checklist]]"]
applies: ["[[pattern-parallel-persona-review]]", "[[pattern-feature-flags]]"]
equivalent_to: ["[[gsd-ship]]", "[[openspec-archive]]", "[[ce-commit-push-pr]]", "[[gstack-ship]]", "[[sp-finishing-a-development-branch]]"]
sources: "Addy Osmani — Agent Skills (2026)"
raw: ["../../raw/addy-agent-skills/2026-07-04-agent-skills.md"]
updated: 2026-07-04
---

# Shipping & Launch

Ships with confidence: every launch reversible, observable, and incremental. It runs a
multi-section pre-launch [[artifact-launch-checklist]] (code quality, security, performance,
accessibility, infrastructure, documentation), then a feature-flag lifecycle and staged rollout
(deploy dark → team → 5% canary → 25/50/100%) governed by explicit advance/hold/roll-back
thresholds, backed by monitoring and a documented rollback plan. It applies
[[pattern-feature-flags]] to decouple deployment from release.

Its distinctive mechanism is fan-out orchestration: `/ship` spawns the three review personas —
[[addy-code-reviewer]], [[addy-security-auditor]], and [[addy-test-engineer]] — concurrently,
then merges their verdicts into a single go/no-go decision with a rollback plan
([[pattern-parallel-persona-review]]). This clusters it with GSD's ship command,
[[gsd-ship]], which orchestrates launch the same way.

## See Also
- [[gsd-ship]] — the GSD equivalent ship orchestrator.
- [[openspec-archive]] — OpenSpec's finalize step (spec-merge + archive, no deploy).
- [[addy-code-reviewer]] — review persona spawned in the fan-out.
- [[addy-security-auditor]] — security persona spawned in the fan-out.
- [[addy-test-engineer]] — test persona spawned in the fan-out.
- [[artifact-launch-checklist]] — the checklist it produces.
- [[stage-release]] — the canonical stage this implements.
