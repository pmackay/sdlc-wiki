---
type: artifact
sources: "Addy Osmani — Agent Skills (2026); bmad-code-org/BMAD-METHOD (2026); Matt Pocock — Skills for Real Engineers v1.1 (2026); pstack v0.15.2 — Lauren Tan (2026); Tessl docs (2026); Builder.io — BuilderIO/skills (2026)"
updated: 2026-09-26
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

pstack:

- [[pstack-interrogate]] — a synthesized verdict from one reviewer per model against a shared rubric; explicitly **does not auto-apply changes**.
- [[pstack-blast-radius]] — a what-it-breaks writeup whose central section is *the one fact it is safe because of*, graded on a five-rung evidence ladder and marked **unproven** below rung 4.
- [[pstack-comment-sicko]] — touched files, deletion count, `MUST KILL` flags one line each, and skips.
- [[pstack-no-comments]] — the action report: deletions, restorations, reruns, fixes, encoding offers, and unenforced constraints left open.

Tessl — review reports at three different subjects, which is the layer's tell:

- [[tessl-review]] — scores a **skill** across validation, description, and content; runs automatically on publish and the score travels with the registry entry.
- [[tessl-review-security]] — severity-graded supply-chain findings on a skill or plugin ([[pattern-supply-chain-scanning]]).
- [[tessl-code-review]] — an agentic **pull-request** review with versioned, pinnable lenses.
- [[tessl-change-risk]] · [[tessl-change-verify]] — a risk verdict and per-file judge findings over a **diff**, both with CI exit codes.
- [[tessl-inventory]] — org-wide **Findings**, ranked by severity, across every repo scanned.

builder-skills:

- [[builder-factory-review-prs]] — per-PR findings with file, line, impact, and a concrete fix, kept separate from approval and merge decisions. A PR with no findings is recorded as such, with no comment invented.
- [[builder-agent-watchdog]] — the gap report: Status / Requested / Observed / Gaps / **Independent findings** / Fixes made / Remaining risk, classifying each issue as gap, bug, verification miss, scope drift, or no issue.

## See Also
- [[artifact-security-audit]] · [[artifact-perf-audit]] — the security and performance reports that join it in the `/ship` merge.
- [[stage-review]] — the stage this artifact gates.
