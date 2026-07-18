---
type: framework
source_url: "https://github.com/EveryInc/compound-engineering-plugin"
docs_url: "https://every.to/chain-of-thought/compound-engineering-how-every-codes-with-agents"
sources: "Dan Shipper & Kieran Klaassen — 'Compound Engineering: How Every Codes with Agents', Every/Chain-of-Thought (2025-12-11); EveryInc/compound-engineering-plugin (2026)"
raw: ["../../raw/compound-engineering/2026-07-04-compound-engineering-every.md", "../../raw/compound-engineering/2026-07-04-compound-engineering-plugin.md"]
updated: 2026-07-05
---

# Compound Engineering

**Compound Engineering** is Every's methodology (and open-source Claude Code plugin) for coding when **AI agents write ~100% of the code**. Its one-line thesis: **"each unit of engineering work should make subsequent units easier — not harder."** Where traditional development accumulates technical debt, Compound Engineering accumulates *knowledge* — every bug, failed test, and problem-solving insight is captured and fed back so future agents avoid the mistake. The distinctive move is a **learning loop**: complexity grows *alongside* accumulated AI knowledge, so velocity accelerates over time rather than decaying. Authors Dan Shipper & Kieran Klaassen report single developers at Every now run **five products** — *"the work of five developers a few years ago."* MIT-licensed; portable across Claude Code, Cursor, Codex, Copilot, Factory Droid, Kimi, Qwen, OpenCode, Pi, and Antigravity.

- **Install (Claude Code):** `/plugin marketplace add EveryInc/compound-engineering-plugin` then `/plugin install compound-engineering`.
- **Effort allocation:** **~80% planning and review, ~20% work and compounding** — front-load thinking, and the execution + capture are cheap. (`ce-plan` alone is ~40% of a developer's time.)

## Distinctive contribution: the seventh stage

Compound Engineering is the framework that promotes a **new canonical SDLC stage** in this wiki: [[stage-learn]]. Its `/ce-compound` step — *"the money step… the whole point"* — captures reusable learnings into a `docs/solutions/` corpus that future `ce-brainstorm`/`ce-plan`/ `ce-code-review` runs read as grounding. That gave learning-capture a **second framework** (alongside BMAD's [[bmad-retrospective]]), clearing the bar to split it out of [[stage-release]]. See [[pattern-knowledge-compounding]] and [[stage-learn]]. Arguably the first genuinely *new* stage the agent era adds — the loop-closing arrow, not a rename of a classic phase.

Where [[gsd]] is an end-to-end workflow *engine* and [[bmad]] is a *persona*-oriented pipeline, Compound Engineering is a **loop that feeds itself**: it is the only framework here whose lifecycle is explicitly circular, with a dedicated step whose product is consumed by the front of the next iteration.

## The six-step loop (+ autonomous mode)

| Step | Command | What it does | Canonical stage |
|------|---------|--------------|-----------------|
| **Brainstorm** | `/ce-brainstorm` ([[ce-brainstorm]]) | Define what something should become through dialogue → requirements-only plan (`docs/brainstorms/`) | [[stage-align]] |
| **Plan** | `/ce-plan` ([[ce-plan]]) | Bound execution with guardrails; U-IDs + test scenarios; WHAT not HOW (`docs/plans/`) | [[stage-plan]] |
| **Work** | `/ce-work` ([[ce-work]]) | Execute against guardrails; figure out HOW with code, in an isolated worktree | [[stage-implement]] |
| **Simplify** | `/ce-simplify-code` ([[ce-simplify-code]]) | Refine fresh code for reuse/quality/efficiency, preserving behavior | [[stage-review]] |
| **Review** | `/ce-code-review` ([[ce-code-review]]) | Multi-agent persona review, confidence-gated, four modes | [[stage-review]] |
| **Compound** | `/ce-compound` ([[ce-compound]]) | Capture learnings → `docs/solutions/`; next iteration starts smarter | [[stage-learn]] |
| **(all, hands-off)** | `/lfg` ([[lfg]]) | Autonomous full pipeline: plan → work → simplify → review+fix → test → commit → push → PR → CI-green | [[stage-plan]]…[[stage-release]] |

## Distinctive mechanisms

- **Knowledge compounding as a first-class step** — [[ce-compound]] + [[ce-compound-refresh]] maintain `docs/solutions/` ([[artifact-solution-doc]]); a research council of sub-agents mines completed work, and `learnings-researcher` re-injects it downstream. This is [[pattern-knowledge-compounding]], the framework's signature.
- **80/20 front-loading** — planning and review dominate; `/ce-work` is the cheap middle. Guardrails written in [[ce-plan]] bound what `/ce-work` may do (WHAT-not-HOW split).
- **Autonomous full loop** — [[lfg]] chains every step hands-off and self-corrects until CI is green ([[pattern-autonomous-loop]]).
- **Worktree isolation** — [[ce-worktree]] / [[ce-work]] run each unit in a dedicated git worktree so parallel and experimental work never corrupts the mainline ([[pattern-worktree-isolation]]).
- **Persona-based, confidence-gated review** — [[ce-code-review]] and [[ce-doc-review]] fan out skill-local reviewer personas ([[pattern-parallel-persona-review]]) with adversarial and cross-model passes ([[pattern-adversarial-review]]), reporting only findings above a confidence bar.
- **Everything is grounded** — ideation, briefs, and verdicts cite dual evidence (repo + web) and read the compound corpus first ([[pattern-source-grounding]], [[pattern-context-engineering]]).

## Capabilities

### Skills — Align / discovery
- [[ce-strategy]] — create/maintain `STRATEGY.md`, the upstream anchor read by ideate/brainstorm/plan.
- [[ce-ideate]] — discover strong, qualified directions with conceptual frames + adversarial filtering.
- [[ce-pov]] — decisive Adopt/Trial/Hold/Reject verdict on external inputs, dual-grounded.
- [[ce-brainstorm]] — define what to build through dialogue → requirements-only unified plan.
- [[ce-sweep]] — ingest Slack/GitHub items since cursors, acknowledge, analyze, reconcile plans (feedback intake).

### Skills — Plan
- [[ce-plan]] — enrich requirements into implementation-ready guardrails (U-IDs, test scenarios).
- [[ce-doc-review]] — review requirements/plans with persona lenses *before* any code.

### Skills — Implement
- [[ce-work]] — execute the plan; figure out HOW with code; ship through quality gates.
- [[ce-worktree]] — ensure work happens in an isolated git worktree.
- [[ce-debug]] — systematic root-cause via causal chains, predictions, post-fix polish.
- [[ce-polish]] — conversational UX polish with a live dev server + browser.

### Skills — Review (quality gate; CE loop steps 4–5)
- [[ce-simplify-code]] — reduce complexity in fresh code while preserving behavior.
- [[ce-code-review]] — multi-persona, confidence-gated code review, four modes.
- [[ce-optimize]] — metric-driven iterative optimization with parallel experiments.

### Skills — Validate (functional testing)
- [[ce-test-browser]] — end-to-end browser tests on PR/branch-affected pages.
- [[ce-test-xcode]] — build/test iOS apps on simulator via XcodeBuildMCP.
- [[ce-dogfood]] — hands-off diff-scoped browser QA with autonomous small-breakage fixes.

### Skills — Release
- [[ce-commit]] — one well-crafted atomic commit with convention awareness.
- [[ce-commit-push-pr]] — working changes → open PR, three workflow modes.
- [[ce-resolve-pr-feedback]] — evaluate/fix/reply to PR review feedback in parallel.
- [[ce-promote]] — draft user-facing launch announcements across channels.
- [[ce-product-pulse]] — time-windowed post-release usage/perf/error report.

### Skills — Learn (the compounding step)
- [[ce-compound]] — capture reusable learnings into `docs/solutions/` (the money step).
- [[ce-compound-refresh]] — maintain the solution corpus over time.
- [[ce-explain]] — dense visual explainers of concepts/diffs/recent work (personal learning).

### Orchestrator
- [[lfg]] — the full hands-off pipeline from planning through green PR.

### Sub-agents (26, each paged)

Compound Engineering skills delegate to a large **shared** cast of sub-agents (each skill's `references/agents/`; many, e.g. [[ce-repo-profiler]] and [[ce-learnings-researcher]], are dispatched by several skills). Each is paged as a `subtype: sub-agent` capability, filed under the stage of its intrinsic activity (grouped below by function).

**Research / grounding:**

- [[ce-repo-profiler]] — question-agnostic cached project profile ([[stage-align]]).
- [[ce-learnings-researcher]] — re-injects the `docs/solutions/` corpus into new work ([[stage-align]]).
- [[ce-slack-researcher]] — org-knowledge digest from Slack ([[stage-align]]).
- [[ce-web-researcher]] — external grounding digest for ideation ([[stage-align]]).
- [[ce-issue-intelligence-analyst]] — theme-level issue-tracker intelligence ([[stage-align]]).
- [[ce-external-evidence-researcher]] — verified external evidence for verdicts ([[stage-align]]).
- [[ce-precedent-activity-scout]] — prior-decision precedent + incumbent pain ([[stage-align]]).
- [[ce-project-grounding-scout]] — this-codebase floor for verdicts ([[stage-align]]).
- [[ce-media-analyzer]] — feedback media → bug-shaped finding ([[stage-align]]).
- [[ce-git-history-analyzer]] — repo archaeology for planning ([[stage-plan]]).
- [[ce-session-historian]] — mine past agent sessions for lessons ([[stage-learn]]).
- [[ce-best-practices-researcher]] — authoritative best-practice synthesis ([[stage-learn]]).
- [[ce-framework-docs-researcher]] — framework/version docs for lessons ([[stage-learn]]).
- [[ce-work-recap-scout]] — gather recent-work evidence for explainers ([[stage-learn]]).
- [[ce-repo-research-analyst]] — optimization-input repo research ([[stage-review]]).

**Review / quality specialists:**

- [[ce-security-sentinel]] — attacker-minded security audit ([[stage-review]]; counterpart to [[addy-security-auditor]]).
- [[ce-performance-oracle]] — bottleneck analysis ([[stage-review]]; counterpart to [[addy-web-performance-auditor]]).
- [[ce-pattern-recognition-specialist]] — design/anti-pattern + recurring-problem analysis ([[stage-review]]).
- [[ce-data-integrity-guardian]] — data-safety / migration-integrity review ([[stage-review]]).
- [[ce-data-migration-reviewer]] — migration correctness + rollback, plan-time ([[stage-plan]]).
- [[ce-deployment-verification-agent]] — launch-readiness checklists, plan-time ([[stage-plan]]).
- [[ce-pr-comment-resolver]] — implements one validated PR-review fix ([[stage-release]]).

**Design / planning:**

- [[ce-architecture-strategist]] — architecture-alignment review ([[stage-plan]]).
- [[ce-agent-native-planning-strategist]] — decide agents-as-users, feed plan inputs ([[stage-plan]]).
- [[ce-spec-flow-analyzer]] — surface missing flows/edge-cases pre-implementation ([[stage-plan]]).
- [[ce-figma-design-sync]] — pixel-perfect Figma↔code sync ([[stage-implement]]).

The [[ce-session-historian]] + [[ce-pattern-recognition-specialist]] + [[ce-security-sentinel]] + [[ce-performance-oracle]] + [[ce-best-practices-researcher]] + [[ce-framework-docs-researcher]] + [[ce-data-integrity-guardian]] **council** is what powers [[ce-compound]]'s mining of completed work into [[artifact-solution-doc|solution docs]].

### Review persona lenses (bundled within review skills)
- `ce-code-review` carries ~16 persona lenses (correctness, security, performance, maintainability, reliability, testing, api-contract, data-migration, adversarial, agent-native, deployment-verification, project-standards, previous-comments, learnings-researcher, + Swift/iOS and frontend-races stack reviewers).
- `ce-doc-review` carries 7 (coherence, feasibility, security-lens, product-lens, design-lens, scope-guardian, adversarial-document).

### Infrastructure / product-specific (catalogued, not paged)
- `/ce-setup` — diagnose optional tool capabilities and bootstrap project-local config (infra bootstrap, like GSD/Addy setup skills — not a lifecycle stage).
- `/ce-proof` — publish/view/comment/edit markdown via Every's **Proof** collaborative editor (product integration).
- `/ce-riffrec-feedback-analysis` — structure raw **Riffrec** recordings into feedback (Every-product integration; feeds [[ce-sweep]]/[[stage-align]]).

## Artifacts produced
- [[artifact-brainstorm-md]] — `docs/brainstorms/` requirements-only unified plan ([[ce-brainstorm]]).
- [[artifact-strategy-md]] — `STRATEGY.md`, the upstream strategic anchor ([[ce-strategy]]).
- [[artifact-plan-md]] — `docs/plans/` implementation-ready guardrail plan ([[ce-plan]]).
- [[artifact-review-report]] — persona review findings ([[ce-code-review]], [[ce-doc-review]]).
- [[artifact-atomic-commit]] — one atomic commit per unit ([[ce-commit]]).
- [[artifact-pull-request]] — the opened PR ([[ce-commit-push-pr]], [[lfg]]).
- [[artifact-solution-doc]] — **signature** — `docs/solutions/` reusable learning ([[ce-compound]], [[ce-compound-refresh]]).
- [[artifact-explainer]] — dense visual explainer of a concept/diff ([[ce-explain]]).

## Patterns applied
- [[pattern-knowledge-compounding]] — **signature** — each unit of work leaves reusable, machine-consumable lessons future agents auto-consume ([[ce-compound]], [[ce-compound-refresh]]).
- [[pattern-autonomous-loop]] — chain the full pipeline hands-off with self-correction to a terminal success gate ([[lfg]]).
- [[pattern-worktree-isolation]] — isolate each unit of work in a dedicated git worktree ([[ce-worktree]], [[ce-work]]).
- [[pattern-parallel-persona-review]] — concurrent reviewer-persona fan-out ([[ce-code-review]], [[ce-doc-review]]).
- [[pattern-adversarial-review]] — adversarial + cross-model review passes ([[ce-code-review]]).
- [[pattern-plan-verification-loop]] — gate the plan/requirements before execution ([[ce-doc-review]]).
- [[pattern-fresh-context-subagents]] — stateless persona/scout sub-agents per task.
- [[pattern-context-engineering]] — read the compound corpus + repo profile as grounding.
- [[pattern-source-grounding]] — dual-grounded ideas/verdicts ([[ce-ideate]], [[ce-pov]]).
- [[pattern-measure-first]] — metric-driven optimization ([[ce-optimize]]).
- [[pattern-systematic-debugging]] — causal-chain root-cause ([[ce-debug]]).
- [[pattern-trunk-based-development]] — atomic commits, PR flow ([[ce-commit]], [[ce-commit-push-pr]]).

## See Also
- [[bmad]] — the other framework implementing [[stage-learn]]; its [[bmad-retrospective]] is the team-process flavor of Compound Engineering's agent-grounding [[ce-compound]].
- [[gsd]] — end-to-end workflow engine; shares the plan→execute→verify→ship spine and [[pattern-fresh-context-subagents]]; [[ce-commit-push-pr]] ↔ [[gsd-ship]].
- [[addy-agent-skills]] — the other lifecycle-broad pack; shares [[pattern-parallel-persona-review]] (its `/ship` fan-out ↔ CE's review personas), [[ce-simplify-code]] ↔ [[addy-code-simplification]], [[ce-debug]] ↔ [[addy-debugging]], the browser-testing and performance skills.
- [[openspec]] — its [[pattern-living-specification]] sync is a *spec-level* cousin of compounding (noted on [[stage-learn]]).
- [[stage-align]] · [[stage-plan]] · [[stage-implement]] · [[stage-review]] · [[stage-validate]] · [[stage-release]] · [[stage-learn]] — the canonical stages this framework's capabilities feed (it promotes [[stage-learn]], and its Simplify+Review loop steps land in the [[stage-review]] stage split out 2026-07-05).
