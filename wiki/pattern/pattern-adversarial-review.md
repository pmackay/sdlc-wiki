---
type: pattern
sources: "Addy Osmani — Agent Skills (2026); bmad-code-org/BMAD-METHOD (2026); obra/superpowers (2026)"
updated: 2026-07-17
---

# Pattern: Adversarial fresh-context review

Subject a non-trivial decision to a review that starts from a **clean context** and is prompted to *disprove* it, rather than confirm it. The loop is **CLAIM → EXTRACT → DOUBT → RECONCILE → STOP**: state the claim, extract the assumptions it rests on, actively try to break each one, reconcile the survivors, and stop once the decision either holds or is replaced. Optionally escalates to a different model for a second opinion when the user authorizes it.

Because the reviewer has no stake in the original reasoning (fresh context), it catches the confident-but-wrong outputs that self-review rationalizes away. Applied in-flight, while stakes are still cheap to correct.

## Applied by (backlinks)

Addy Osmani — Agent Skills:

- [[addy-doubt-driven-development]] — the canonical CLAIM→EXTRACT→DOUBT→RECONCILE→STOP loop.

BMAD:

- [[bmad-code-review]] — parallel review layers under a "the reviewer must find issues. No 'looks good' allowed" mandate; "zero findings triggers a halt."
- [[bmad-forge-idea]] — the same distrust aimed at a *concept*: pressure-test it "until it hardens, proves out, or dies cheaply."

A second framework promotes this from an Addy-only technique to a **two-framework** pattern. Addy runs an in-flight *doubt loop* over a decision; BMAD runs *hunter layers* over a diff (and over an idea). Both share the honest caveat that an AI told to find problems will manufacture them — so, in BMAD's words, "human filtering remains the essential final step."

Compound Engineering:

- [[ce-code-review]] — a dedicated adversarial persona + optional cross-model pass.
- [[ce-ideate]] — adversarial filtering of candidate directions before any survive.
- [[ce-security-sentinel]] — thinks like an attacker ("how could this be exploited?").

gstack:

- [[gstack-codex]] — Codex "adversarial challenge" mode actively tries to break the code (cross-model).
- [[gstack-review]] — finds the bugs that pass CI but break in production.

Superpowers:

- [[sp-requesting-code-review]] — dispatch a fresh-context reviewer specifically to *catch issues before they cascade* (never the controller's history).
- [[sp-subagent-driven-development]] — a two-stage task review (spec compliance ∥ code quality) after every task, with a rule against pre-judging findings ("do not flag X" is forbidden).

In Fowler's *harness engineering* terms this is the archetypal **inferential sensor** (LLM-as-judge) — a semantic feedback control for the judgments no deterministic linter can make; use it where a **computational sensor** can't reach. See [[topic-harness-engineering]].

## See Also
- [[pattern-parallel-persona-review]] — BMAD implements this by fanning several adversarial layers out in parallel.
- [[pattern-fresh-context-subagents]] — the clean-context mechanism this builds on.
- [[pattern-anti-rationalization]] — the passive, page-level form of the same distrust.
- [[topic-harness-engineering]] — guides vs sensors; computational vs inferential controls.
- [[stage-implement]], [[stage-review]] — where the doubt loops run.
