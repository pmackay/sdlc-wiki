---
source_urls:
  - https://docs.opengsd.net/
  - https://github.com/open-gsd/gsd-core
  - https://docs.opengsd.net/llms.txt
  - https://docs.opengsd.net/core/commands/workflow-commands.md
  - https://docs.opengsd.net/core/concepts/agents.md
  - https://github.com/open-gsd/gsd-core/tree/main/commands/gsd
  - https://github.com/open-gsd/gsd-core/tree/main/agents
collected: 2026-06-27
published: Unknown
---

# GSD (Git. Ship. Done.) — Core Framework

## What it is
GSD = **Git. Ship. Done.** "A light-weight meta-prompting, context engineering, and
spec-driven development system for Claude Code, OpenCode, Gemini CLI, Kimi CLI, Kilo,
Codex, Copilot, Cursor, Windsurf, and more."

Open GSD is "a suite of AI-powered developer tools designed to make working with AI
coding agents fast, structured, and reliable." Three tools:
- **GSD Core** — spec-driven workflow engine (Claude Code, Cursor, Gemini CLI, …). [SDLC framework]
- **GSD Pi** — standalone autonomous local coding agent: TUI, web UI, worktree-isolated Git, multi-provider model routing.
- **GSD Browser** — native CDP browser automation with MCP server mode, versioned element refs, human-in-the-loop viewer.

## Core problem solved
GSD solves **context rot** — quality degradation as an AI fills its context window — by
routing heavy research and execution through **fresh-context subagents** while keeping a
lean main session. Install: `npx @opengsd/gsd-core@latest`.

## The Five-Phase Loop
Each milestone repeats this cycle, one phase per iteration:
1. **Discuss** — Capture implementation decisions before planning.
2. **Plan** — Research, decompose work; verify it fits a fresh context window.
3. **Execute** — Run plans in parallel waves; each executor gets clean 200k-token context.
4. **Verify** — Walk through built code; diagnose and fix before declaring done.
5. **Ship** — Create the PR, archive the phase, proceed to next phase.

CONFLICT: the docs homepage (docs.opengsd.net) lists the pipeline as
"Research → Plan → Execute → Verify → Ship". Every detailed source — the GitHub README,
core/concepts/workflow.md, and core/commands/workflow-commands.md — lists
"Discuss → Plan → Execute → Verify → Ship". Treat **Discuss** as the canonical first
phase; "Research" on the homepage appears to be informal (research is a sub-step of Plan).

## Workflow commands (the five phases)
- `/gsd-discuss-phase N` — "Gather phase context through adaptive questioning before planning." Loads project history, scouts the codebase for reusable components, identifies unresolved decisions, guides deep-dives. Produces `{phase_num}-CONTEXT.md` (locked decisions + scope). Flags: `--all`, `--batch`, `--power`. Sub-agents: gsd-assumptions-analyzer (assumptions mode).
- `/gsd-plan-phase N` — "Research, plan, and verify a phase — the core planning step." Optional domain research, planning logic, then a verification loop with a plan-checker until approval. Produces `{phase_num}-PLAN.md` (executable task prompts), `RESEARCH.md` (when research runs), `SKELETON.md` (MVP mode on Phase 1). Flags: `--mvp` (vertical slices UI→API→DB), `--tdd` (RED-GREEN), `--gaps`. Sub-agents: gsd-planner, gsd-plan-checker, gsd-phase-researcher, gsd-ui-researcher/gsd-ui-checker (when /gsd-ui-phase runs first).
- `/gsd-execute-phase N` — "Execute all plans in a phase with wave-based parallelization." Discovers task dependencies, groups into parallel waves, spawns subagents per wave, collects results. Flags: `--wave N`, `--interactive`. Sub-agents: gsd-executor (per wave), gsd-verifier (post-execution).
- `/gsd-verify-work N` — "Validate built features through conversational UAT with auto-diagnosis." Runs UAT, tracks results, diagnoses root causes, produces fix plans, queues for re-execution. Produces `{phase_num}-UAT.md` + auto fix plans.
- `/gsd-ship N` — "Create a pull request and prepare the phase for merge." Pushes phase branch, creates PR with auto-generated summary, triggers optional review, tracks merge. Produces a pull request. Flags: `--draft`.

## Command namespaces (65+ slash commands)
- Workflow: discuss/plan/execute/verify/ship phase pipeline.
- Context: mapping, knowledge graphs, learning extraction, doc ingestion (map-codebase, graphify, ingest-docs, extract-learnings, mempalace-capture/recall).
- Management: configuration, skill surfaces, updates, workspaces, workstreams (config, settings, update, workspace, workstreams).
- Project: milestones, phase management, session handoffs, health checks (new-project, new-milestone, complete-milestone, phase, pause-work, resume-work, health, progress).
- Quality: code review, testing, security, UI audits, debugging (code-review, add-tests, secure-phase, ui-review, debug, audit-fix, audit-milestone, audit-uat, eval-review).
- Autonomous: /gsd-autonomous, /gsd-manager for hands-free execution.
- Cross-AI review: /gsd-review for peer feedback before coding.

Full command file list (commands/gsd/): add-tests, ai-integration-phase, audit-fix,
audit-milestone, audit-uat, autonomous, capture, cleanup, code-review, complete-milestone,
config, debug, discuss-phase, docs-update, eval-review, execute-phase, explore,
extract-learnings, fast, forensics, graphify, health, help, import, inbox, ingest-docs,
manager, map-codebase, mempalace-capture, mempalace-recall, milestone-summary, mvp-phase,
new-milestone, new-project, ns-context, ns-ideate, ns-manage, ns-project, ns-review,
ns-workflow, pause-work, phase, plan-phase, plan-review-convergence, pr-branch,
profile-user, progress, quick, resume-work, review-backlog, review, secure-phase, settings,
ship, sketch, spec-phase, spike, stats, surface, thread, ui-phase, ui-review,
ultraplan-phase, undo, update, validate-phase, verify-work, workspace, workstreams.

## Specialist sub-agents (agents/)
"Each subagent receives a precisely scoped prompt and the subset of planning artifacts it
needs," working in parallel or sequentially, preventing context degradation.

Key agents (name — role — phase/command — isolation):
- gsd-phase-researcher — domain research for a phase; four parallel instances (stack, features, architecture, pitfalls) — /gsd-plan-phase — fresh context, ≤200K tokens.
- gsd-project-researcher — researches domain ecosystem before roadmap; four parallel instances — /gsd-new-project.
- gsd-domain-researcher — business domain + eval context for AI-integration phases — fresh context, web access.
- gsd-ui-researcher — UI design contracts, detects design-system state — /gsd-ui-phase.
- gsd-planner — atomic execution plans with task defs + acceptance criteria — /gsd-plan-phase — Opus-tier, fresh context, reads artifacts only.
- gsd-roadmapper — v1 roadmap with requirement mapping + success criteria — /gsd-new-project.
- gsd-plan-checker — verifies plans across eight dimensions before execution; up to three revision cycles — /gsd-plan-phase.
- gsd-research-synthesizer — consolidates four parallel researcher outputs — /gsd-new-project.
- gsd-executor — implements plans with one atomic git commit per completed task; fresh context window; only agent with Edit tool access — /gsd-execute-phase.
- gsd-verifier — performs a "goal-backward analysis," confirms built code satisfies requirements — /gsd-execute-phase.
- gsd-code-reviewer — bugs, security, quality; read-only — /gsd-code-review.
- gsd-security-auditor — verifies declared threat mitigations present; read-only — /gsd-secure-phase.
- gsd-nyquist-auditor — fills test-coverage gaps from a Nyquist validation pass; generates test files only.
- gsd-codebase-mapper — explores codebase, writes seven structured analysis docs; four parallel instances — /gsd-map-codebase.
- gsd-debugger — investigates bugs with persistent session state (hypotheses + evidence); state persists to .planning/debug/ — /gsd-debug.
- gsd-assumptions-analyzer — codebase assumptions with confidence + consequence mapping — /gsd-discuss-phase (assumptions mode).

Full agent list (agents/): gsd-advisor-researcher, gsd-ai-researcher,
gsd-assumptions-analyzer, gsd-code-fixer, gsd-code-reviewer, gsd-codebase-mapper,
gsd-debug-session-manager, gsd-debugger, gsd-doc-classifier, gsd-doc-synthesizer,
gsd-doc-verifier, gsd-doc-writer, gsd-domain-researcher, gsd-eval-auditor, gsd-eval-planner,
gsd-executor, gsd-framework-selector, gsd-integration-checker, gsd-intel-updater,
gsd-mempalace-curator, gsd-nyquist-auditor, gsd-pattern-mapper, gsd-phase-researcher,
gsd-plan-checker, gsd-planner, gsd-project-researcher, gsd-research-synthesizer,
gsd-roadmapper, gsd-security-auditor, gsd-ui-auditor, gsd-ui-checker, gsd-ui-researcher,
gsd-user-profiler, gsd-verifier.

## Artifacts & files
- `.planning/` directory — per-phase planning artifacts.
- `{phase}-CONTEXT.md` — locked decisions and scope (Discuss).
- `{phase}-PLAN.md` — executable task prompts (Plan); plus `RESEARCH.md`, `SKELETON.md`.
- `{phase}-UAT.md` — UAT results and diagnosed gaps (Verify).
- Atomic git commit — one per completed task (gsd-executor).
- Pull request — created at Ship.
- `STATE.md` — structured persistence across sessions; `CONTEXT.md` — session memory.
- `.planning/config.json` — settings.

## Concepts / patterns
- Spec-driven development; meta-prompting; context engineering.
- Context management: prevents context rot, monitors context usage in real time.
- Fresh-context subagents: each executor gets a clean ~200k-token context.
- Wave-based parallelization: tasks grouped by dependency into parallel execution waves.
- Plan verification loop: plan-checker verifies across eight dimensions, up to three revision cycles, before execution is permitted.
- Goal-backward analysis: verifier works backward from the goal to confirm requirements met.
- Git branching strategies: none, phase, or milestone.
- Model profiles: assign model tiers to agents (e.g. Opus-tier planner).

## Supported runtimes
Claude Code, OpenCode, Gemini CLI, Kimi CLI, Kilo, Codex, Copilot, Cursor, Windsurf.
