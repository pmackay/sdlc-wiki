---
type: pattern
sources: "Addy Osmani — Agent Skills (2026); bmad-code-org/BMAD-METHOD (2026)"
updated: 2026-07-05
---

# Pattern: Parallel persona review (fan-out / merge)

Spawn several **specialist reviewer personas** concurrently — each a fresh-context subagent
with a single lens (code quality, security, test coverage, performance) — then **merge** their
independent reports into one decision. The personas share no state and impose no ordering,
which is exactly what makes parallel execution safe and useful. A firm rule keeps it acyclic:
**personas never invoke personas** (subagents can't spawn subagents), so the fan-out is one
level deep and the merge is done by the orchestrator.

## Applied by (backlinks)

Addy Osmani — Agent Skills:

- [[addy-shipping]] — `/ship` fans out [[addy-code-reviewer]], [[addy-security-auditor]], [[addy-test-engineer]] in parallel, then merges a go/no-go with a rollback plan.

BMAD:

- [[bmad-code-review]] — fans several single-lens layers (Blind Hunter, Edge Case Hunter, Acceptance Auditor) over one diff in parallel, then triages. BMAD's Party-Mode subagent mode is the same fan-out for open decisions rather than review.

A second framework promotes this from an Addy-only technique to a **two-framework** pattern.
Addy fans out *specialist role* personas at ship time (quality/security/tests); BMAD fans out
*adversarial hunter* layers over a single code change.

Compound Engineering:

- [[ce-code-review]] — ~16 skill-local reviewer personas fan out in fresh context, confidence-gated.
- [[ce-doc-review]] — 7 reviewer-persona lenses over requirements/plans before code.

gstack:

- [[gstack-autoplan]] — runs the CEO / design / eng / DX plan-review persona panel with smart review routing.
- [[gstack-plan-ceo-review]] · [[gstack-plan-eng-review]] · [[gstack-plan-design-review]] · [[gstack-plan-devex-review]] — the four plan-review personas.

## See Also
- [[pattern-persona-agents]] — the broader BMAD substrate: named personas across the whole lifecycle, of which this review fan-out is one use.
- [[pattern-adversarial-review]] — BMAD's review layers each carry the "must find issues" mandate.
- [[pattern-fresh-context-subagents]] — each persona is a clean-context reviewer.
- [[pattern-wave-parallelism]] — GSD's related "independent work runs concurrently" technique (on the execution side rather than the review side).
- [[stage-release]], [[stage-review]] — the stages these fan-outs gate.
