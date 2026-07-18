---
type: pattern
sources: "EveryInc/compound-engineering-plugin — /lfg, /ce-dogfood (2026); gstack — Garry Tan (2026)"
raw: ["../../raw/gstack/2026-07-05-gstack-framework.md"]
updated: 2026-07-05
---

# Pattern: Autonomous loop (hands-off pipeline to a terminal success gate)

Chain a multi-step workflow **end-to-end without human checkpoints**, self-correcting on failure
until a **terminal success condition** is met — then stop and hand back. The defining features
are (a) no between-step approval, (b) a *machine-checkable* stopping gate (CI green, tests pass,
QA clean) rather than "looks done", and (c) automatic retry/repair when a step fails.

Compound Engineering's [[lfg]] is the archetype: after a brainstorm it runs plan → work →
simplify → review-with-fixes → test → commit → push → open PR → **watch CI until green**,
returning only when the PR is merge-ready. [[ce-dogfood]] applies the same shape scoped to QA:
hands-off browser testing that **fixes small breakages on its own** and reports what it repaired.

## Why it's distinctive

Most frameworks here are **human-checkpointed** by design — GSD, Addy, BMAD, Spec Kit stop
between phases for a human to review. The autonomous loop is the opposite stance: trust the
guardrails ([[pattern-worktree-isolation]], a bounded [[artifact-plan-md|plan]], a hard success
gate) enough to remove the human from the inner loop. It trades interactive control for
throughput, and depends on the *quality of the upstream planning* (the 80/20 front-load) to be
safe. Nearest relatives: Addy's `/build auto` (runs an approved plan task-by-task without
per-task approval) and BMAD's [[bmad-quick-dev]] `dev-auto` unattended path — both are narrower,
single-stage autonomies; `lfg` is the whole lifecycle.

## Applied by (backlinks)

Compound Engineering:

- [[lfg]] — full plan-to-green-PR autonomous pipeline with CI watch.
- [[ce-dogfood]] — autonomous diff-scoped browser QA with self-repair.

gstack (scoped autonomies rather than a whole-lifecycle loop):

- [[gstack-qa]] — self-fixing find→fix→verify browser QA that leaves a regression test per fix.
- [[gstack-ios-fix]] — autonomous iOS bug fixer with regression-snapshot capture.
- [[gstack-canary]] — post-deploy monitoring loop watching for errors/regressions.

## See Also
- [[pattern-worktree-isolation]] — the safety substrate that makes unattended runs non-destructive.
- [[bmad-quick-dev]] — BMAD's unattended fast path (single-stage analogue).
- [[compound-engineering]] — the framework applying this pattern.
