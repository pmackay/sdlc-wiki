---
type: pattern
sources: "EveryInc/compound-engineering-plugin — /lfg, /ce-dogfood (2026); gstack — Garry Tan (2026); mattpocock/sandcastle (2026); jayminwest/warren (2026); sipyourdrink-ltd/bernstein (2026); jayminwest/seeds (2026); gastownhall/beads (2026); disler/super-simple-software-factory (2026); github/gh-aw (2026); pstack v0.15.2 — Lauren Tan (2026); Tessl docs (2026); Builder.io — BuilderIO/skills (2026)"
raw: ["../../raw/gstack/2026-07-05-gstack-framework.md"]
updated: 2026-09-26
---

# Pattern: Autonomous loop (hands-off pipeline to a terminal success gate)

Chain a multi-step workflow **end-to-end without human checkpoints**, self-correcting on failure until a **terminal success condition** is met — then stop and hand back. The defining features are (a) no between-step approval, (b) a *machine-checkable* stopping gate (CI green, tests pass, QA clean) rather than "looks done", and (c) automatic retry/repair when a step fails.

Compound Engineering's [[lfg]] is the archetype: after a brainstorm it runs plan → work → simplify → review-with-fixes → test → commit → push → open PR → **watch CI until green**, returning only when the PR is merge-ready. [[ce-dogfood]] applies the same shape scoped to QA: hands-off browser testing that **fixes small breakages on its own** and reports what it repaired.

## Why it's distinctive

Most frameworks here are **human-checkpointed** by design — GSD, Addy, BMAD, Spec Kit stop between phases for a human to review. The autonomous loop is the opposite stance: trust the guardrails ([[pattern-worktree-isolation]], a bounded [[artifact-plan-md|plan]], a hard success gate) enough to remove the human from the inner loop. It trades interactive control for throughput, and depends on the *quality of the upstream planning* (the 80/20 front-load) to be safe. Nearest relatives: Addy's `/build auto` (runs an approved plan task-by-task without per-task approval) and BMAD's [[bmad-quick-dev]] `dev-auto` unattended path — both are narrower, single-stage autonomies; `lfg` is the whole lifecycle.

## Applied by (backlinks)

Compound Engineering:

- [[lfg]] — full plan-to-green-PR autonomous pipeline with CI watch.
- [[ce-dogfood]] — autonomous diff-scoped browser QA with self-repair.

gstack (scoped autonomies rather than a whole-lifecycle loop):

- [[gstack-qa]] — self-fixing find→fix→verify browser QA that leaves a regression test per fix.
- [[gstack-ios-fix]] — autonomous iOS bug fixer with regression-snapshot capture.
- [[gstack-canary]] — post-deploy monitoring loop watching for errors/regressions.

Seeds:

- [[seeds-ready]] — the queue the loop polls: open issues with no unresolved blockers, derived from the dependency graph so it is correct the moment a blocker closes. `--respect-schedule` reads warren's `queued` / `scheduledFor` keys so work can be parked without being lost. The process-layer half of a loop [[warren]] closes by having its agents self-claim from `.seeds/`.

Beads:

- [[beads-ready]] — the claimable frontier plus atomic `--claim`; the dispatch primitive an unattended loop turns on, derived from the graph so it is correct the instant a blocker closes.
- [[beads-gate]] — a parked step waits on a human, a timer, or a GitHub run as a *blocking bead*, so *"agents never need to poll or spin"*. An unattended loop can suspend indefinitely at zero cost — the alternative to [[lfg]] burning turns watching CI.

pstack — **autonomy and authority deliberately decoupled**:

- [[pstack-poteto-mode]] — five long-run playbooks: *Autonomous run* (drive one task to a predicate), *Orchestrate* (a standing multi-day program under one coordinator), *Autopilot-full* (independent PRs to merged, one owner each), *Autopilot-stack* (one linear stack for the operator to land), and *Multi-phase plan*. Session overrides — *"don't stop"*, *"going to bed"*, *"run until done"* — keep it going.
- [[pstack-principle-never-block-on-the-human]] — proceed on reversible work and let the human course-correct after the fact; **always pause** for irreversible writes (force-push to shared branches, deploys, data deletion, customer messages).
- [[pstack-benny-reproduce-and-fix]] — the most autonomous capability here and the least authorized: triggered by an external report with nobody watching, it reproduces through the real UI and still ends at a **bounded draft PR** after before-and-after proof, failing closed on incomplete configuration.
- [[pstack-show-me-your-work]] — the audit trail that makes an unattended run reviewable afterwards.

Tessl — unattended loops supplied from the [registry layer](../registry/index.md):

- [[tessl-schedule]] — runs a registry plugin against a repo on a cron, with pause, resume, run history, and manual trigger. The closest paged comparison is [[gh-aw]], which wraps the same idea in compiled authorization and budget ceilings this does not have.
- [[tessl-review-fix]] — a find-fix-re-verify loop whose target is a **capability**: rewrite the skill, re-score it, repeat until it clears a threshold or the iteration budget runs out.
- [[tessl-agent]] — autonomously monitors and improves the agentic setup.

builder-skills (a factory made of skills, scheduled by the host):

- [[builder-factory]] — creates one host automation per enabled workflow and reads each one back. The loop runs on whatever scheduler the harness provides.
- [[builder-factory-collect]] · [[builder-factory-lookback]] · [[builder-factory-watchdog]] — the scheduled intake, retrospective, and follow-through jobs. Every external action is separately gated ([[pattern-action-gating]]).
- [[builder-plow-ahead]] — the interactive version, an explicit autonomy contract with listed stop conditions and an auditable decision recap.
- [[builder-stay-within-limits]] — budget as a loop terminator; pause at 95% of the usage window and resume from a self-contained wake prompt.

## Enabled by (infrastructure)

The process-layer loops above are *skills that instruct an agent*; the [execution layer](../runtime/index.md) is where the loop becomes *runtime machinery* — the purpose-built home for "AFK" (away-from-keyboard) agents:

- [[sandcastle]] (library) — a bounded AFK `run()` with a **machine-checkable stop** (`completionSignal`), iteration cap (`maxIterations`), idle/completion timeouts, and `exec`-gated success checks (e.g. `npm test` before a review run). The `simple-loop` template is the archetype.
- [[warren]] (platform) — the entire product *is* the loop: dispatch → sandbox → validate → push → open PR → spin down, plus cron triggers and serial plan-runs that gate each child on the previous PR merging.
- [[sssf]] (library) — the **bounded, single-shot** end of the range: an ADW chain runs to a two-part terminal gate — every phase green **and** the script's own `run.finish(accepted=…)` criterion — with self-repair inside it. `adw_simple_sdlc` loops the builder against the suite's verbatim output (`MAX_FIX_LOOPS`), then against the reviewer's blocking findings (`MAX_REVISION_LOOPS`), re-runs the suite when a revision invalidated a green result, and commits only once both came back clean. No daemon, no cron, no CI watch: the loop is a Python `for` statement, which is the point (*"code owns sequencing, retries, and acceptance"*). The acceptance split is the transferable idea — *"a test phase that ran a red suite did its job perfectly"*, so phases passing and the run being acceptable are asked as separate questions.
- [[bernstein]] (platform) — a goal goes in and merged code comes out: an orchestrator **tick loop** over a task DAG, with adaptive timeouts sized from history, bounded retries that **escalate to a more capable model** on failure, a purpose-constraint circuit breaker, token/cost kill-switches, and **quiescence self-stop** (with heartbeat-renewed *hold* leases so an external HITL workflow can keep an idle-looking orchestrator alive).
- [[gh-aw]] (platform) — the **event-driven** end of the range: the loop's trigger is the repo's own event stream (an opened issue, a failed `workflow_run`, a deploy in error state, cron or fuzzy schedules like *"daily around 14:00"*), and its bounds are declared as frontmatter data rather than scripted — `max-turns`, per-run and daily AI-credit budgets, `cooldown`, `user-rate-limit`, and `stop-after: "+7d"` (a loop that disables its own trigger at a deadline). The announcement names the operating shape "continuous": triage, documentation, simplification, test improvement, quality hygiene, reporting.

## Persisted by (store)

- [[beads]] — [[beads-ready]] plus atomic `--claim` is the frontier an unattended loop polls, and [[beads-gate]] lets a step park on a human, a timer, or a GitHub run without spinning. The store makes the loop *resumable*: a crashed run leaves the graph intact and the next one picks up the frontier.
- [[seeds]] — the same frontier over JSONL; [[warren]]'s agents self-claim from `.seeds/` and its plan-run walks the children serially.

The division of labour with the infrastructure roster above is clean: a runtime supplies the loop, a store supplies the state that makes stopping and restarting it safe.

## See Also
- [[pattern-idempotent-operations]] — the precondition; an unattended run that is interrupted must be safe to re-enter.
- [[pattern-worktree-isolation]] — the safety substrate that makes unattended runs non-destructive.
- [[bmad-quick-dev]] — BMAD's unattended fast path (single-stage analogue).
- [[compound-engineering]] — the framework applying this pattern.
- [[sandcastle]] · [[warren]] · [[bernstein]] · [[gh-aw]] — the runtimes purpose-built to host AFK autonomous runs.
