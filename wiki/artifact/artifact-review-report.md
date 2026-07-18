---
type: artifact
sources: "Addy Osmani — Agent Skills (2026); bmad-code-org/BMAD-METHOD (2026); Matt Pocock — Skills for Real Engineers v1.1 (2026)"
updated: 2026-07-09
---

# Artifact: Code review report

A structured review of a change across **five axes** — correctness, readability, architecture, security, performance — with findings pinned to `file:line`, categorized by severity (Critical / Important / Suggestion, or Nit / Optional / FYI), and paired with fix recommendations. The go/no-go signal a change needs before it merges.

## Produced by (backlinks)
- [[addy-code-review]] — the `/review` skill workflow.
- [[addy-code-reviewer]] — the Staff-Engineer persona that emits the standard template (also in the `/ship` fan-out).
- [[bmad-code-review]] — adversarial parallel review layers (Blind Hunter / Edge Case Hunter / Acceptance Auditor) with structured triage.

- [[ce-code-review]] — Compound Engineering's ~16-persona confidence-gated review (adversarial + cross-model).
- [[ce-doc-review]] — Compound Engineering's plan/requirements-side persona review.
- [[gstack-review]] — gstack's Staff-Engineer pre-landing PR review (auto-fixes the obvious ones).
- [[gstack-codex]] — cross-model second-opinion review (OpenAI Codex).
- [[gstack-design-review]] · [[gstack-devex-review]] · [[gstack-ios-design-review]] — live design / developer-experience / iOS-HIG audit reports.
- [[mp-code-review]] — Matt Pocock's two-axis review: Standards (+ Fowler smell baseline) ∥ Spec, run as parallel sub-agents.

## See Also
- [[artifact-security-audit]] · [[artifact-perf-audit]] — the security and performance reports that join it in the `/ship` merge.
- [[stage-review]] — the stage this artifact gates.
