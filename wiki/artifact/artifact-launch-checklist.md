---
type: artifact
sources: "Addy Osmani — Agent Skills (2026)"
updated: 2026-07-04
---

# Artifact: Launch checklist + rollback plan

A pre-launch gate for a production deploy: the checklist of what must be true before shipping, the feature-flag state and staged-rollout plan, the monitoring/alerting that must be live, and an explicit **rollback procedure** for when it isn't. The concrete output of preparing to ship — and, when produced by `/ship`, the merge of the review, security, and test reports into a **go/no-go** decision.

## Produced by (backlinks)
- [[addy-shipping]] — pre-launch checklist, staged rollout, rollback, monitoring setup.

- [[ce-deployment-verification-agent]] — Compound Engineering computes the launch-readiness checklist at *plan* time (shift-left), via [[ce-plan]].

## See Also
- [[pattern-feature-flags]] — the rollout/rollback mechanism the checklist tracks.
- [[artifact-review-report]] · [[artifact-security-audit]] · [[artifact-perf-audit]] — the reports merged into the go/no-go.
- [[artifact-pull-request]] — GSD's ship-time artifact; [[stage-release]] is the shared stage.
