---
source_urls:
  - https://github.com/addyosmani/agent-skills
  - https://raw.githubusercontent.com/addyosmani/agent-skills/main/README.md
  - https://raw.githubusercontent.com/addyosmani/agent-skills/main/docs/comparison.md
collected: 2026-07-04
published: Unknown
author: Addy Osmani
---

# Agent Skills (addyosmani/agent-skills)

## What it is
**Production-grade engineering skills for AI coding agents**, by **Addy Osmani**. Skills
encode the workflows, quality gates, and best practices senior engineers use, packaged so
agents follow them consistently across every phase of development. MIT-licensed. Distributed
as a Claude Code plugin (marketplace `addy-agent-skills`) and usable across Cursor, Gemini
CLI, Antigravity, OpenCode, Windsurf, Copilot, Kiro, and Codex.

Explicit design thesis: AI agents default to the shortest path — skipping specs, tests,
security reviews. Agent Skills gives them structured, opinionated, process-driven workflows
that enforce senior-engineering discipline. Bakes in concepts from *Software Engineering at
Google* and Google's engineering-practices guide (Hyrum's Law, the Beyoncé Rule, the test
pyramid, change sizing, review-speed norms, Chesterton's Fence, trunk-based development,
Shift Left, code-as-liability).

Install (Claude Code): `/plugin marketplace add addyosmani/agent-skills` then
`/plugin install agent-skills@addy-agent-skills`.

## Lifecycle diagram (from README)
```
  DEFINE          PLAN           BUILD          VERIFY         REVIEW          SHIP
 ┌──────┐      ┌──────┐      ┌──────┐      ┌──────┐      ┌──────┐      ┌──────┐
 │ Idea │ ───▶ │ Spec │ ───▶ │ Code │ ───▶ │ Test │ ───▶ │  QA  │ ───▶ │  Go  │
 │Refine│      │  PRD │      │ Impl │      │Debug │      │ Gate │      │ Live │
 └──────┘      └──────┘      └──────┘      └──────┘      └──────┘      └──────┘
  /spec          /plan          /build        /test         /review       /ship
```

## Commands (8 slash commands, mapped 1:1 to lifecycle phases)
Each command activates the right skill(s) automatically. In Claude Code they live in
`.claude/commands/` (also mirrored to `.gemini/commands/` and `commands/` for other tools).

| Doing | Command | Key principle | Invokes |
|-------|---------|---------------|---------|
| Define what to build | `/spec` | Spec before code | spec-driven-development |
| Plan how to build it | `/plan` | Small, atomic tasks | planning-and-task-breakdown |
| Build incrementally | `/build` (`/build auto`) | One slice at a time | incremental-implementation + test-driven-development |
| Prove it works | `/test` | Tests are proof | test-driven-development (+ browser-testing-with-devtools) |
| Review before merge | `/review` | Improve code health | code-review-and-quality (+ security, performance) |
| Audit web performance | `/webperf` | Measure before you optimize | web-performance-auditor persona |
| Simplify the code | `/code-simplify` | Clarity over cleverness | code-simplification |
| Ship to production | `/ship` | Faster is safer | shipping-and-launch; parallel fan-out to personas |

- `/build auto` generates the plan then implements every task in a single approved pass —
  removes the human stepping *between* tasks, not the verification (each task still
  test-driven and committed individually; pauses on failures/risky steps).
- `/ship` is a **fan-out orchestrator**: spawns `code-reviewer`, `security-auditor`, and
  `test-engineer` subagents concurrently (single turn), then merges into one go/no-go
  decision with a rollback plan. Personas don't invoke personas (subagents can't spawn
  subagents).

## The 24 skills (23 lifecycle + 1 meta)
Each skill has a consistent anatomy: Overview → When to Use → Process → Common
Rationalizations (excuses + rebuttals) → Red Flags → Verification (evidence requirements).
Progressive disclosure: SKILL.md is the entry point; references load only when needed.

### Meta
- **using-agent-skills** — maps incoming work to the right skill workflow; defines shared
  operating rules. The meta-skill router. Use at session start / when deciding which skill applies.

### Define — clarify what to build
- **interview-me** — one-question-at-a-time interview extracting what the user actually
  wants (not what they think they should want), until ~95% confidence. Triggers on
  underspecified asks or "interview me" / "grill me" / "are we sure?" / "stress-test my thinking".
- **idea-refine** — structured divergent/convergent thinking turning vague ideas into
  concrete proposals; stress-tests assumptions. Triggers on "ideate" / "refine this idea".
- **spec-driven-development** — write a PRD/SPEC.md covering objectives, commands, structure,
  code style, testing, and boundaries **before any code**. Six core areas: objective,
  commands, project structure, code style, testing strategy, boundaries. Saves SPEC.md.

### Plan — break it down
- **planning-and-task-breakdown** — decompose specs into small, verifiable tasks with
  acceptance criteria and dependency ordering; slice vertically; add checkpoints between
  phases; human review. Saves tasks/plan.md + tasks/todo.md.

### Build — write the code
- **incremental-implementation** — thin vertical slices: implement, test, verify, commit.
  Feature flags, safe defaults, rollback-friendly changes. For any change touching >1 file.
- **test-driven-development** — Red-Green-Refactor; test pyramid (80/15/5); test sizes;
  DAMP over DRY; Beyoncé Rule; browser testing. For implementing logic, fixing bugs (Prove-It
  pattern: write failing test that reproduces the bug first), changing behavior.
- **context-engineering** — feed agents the right information at the right time: rules files,
  context packing, MCP integrations. Use at session start, task switches, or when quality drops.
- **source-driven-development** — ground every framework decision in official documentation:
  verify, cite sources, flag what's unverified. For authoritative, source-cited code.
- **doubt-driven-development** — adversarial fresh-context review of every non-trivial
  in-flight decision: CLAIM → EXTRACT → DOUBT → RECONCILE → STOP, with optional
  user-authorized cross-model escalation. For high stakes (production, security,
  irreversible), unfamiliar code, or when verifying now is cheaper than debugging later.
- **frontend-ui-engineering** — component architecture, design systems, state management,
  responsive design, WCAG 2.1 AA accessibility. For user-facing interfaces that must look
  production-quality, not AI-generated.
- **api-and-interface-design** — contract-first design, Hyrum's Law, One-Version Rule, error
  semantics, boundary validation. For APIs, module boundaries, public interfaces.

### Verify — prove it works
- **browser-testing-with-devtools** — Chrome DevTools MCP for live runtime data: DOM
  inspection, console logs, network traces, performance profiling. Requires chrome-devtools
  MCP server. For anything running in a browser.
- **debugging-and-error-recovery** — five-step triage: reproduce, localize, reduce, fix,
  guard. Stop-the-line rule; safe fallbacks. For failing tests/builds or unexpected behavior.

### Review — quality gates before merge
- **code-review-and-quality** — five-axis review (correctness, readability, architecture,
  security, performance); change sizing (~100 lines); severity labels (Nit/Optional/FYI);
  review-speed norms; splitting strategies. Before merging any change.
- **code-simplification** — Chesterton's Fence, Rule of 500, reduce complexity while
  preserving exact behavior. When code works but is harder to read/maintain than it should be.
- **security-and-hardening** — OWASP Top 10 prevention, auth patterns, secrets management,
  dependency auditing, three-tier boundary system. For untrusted input, auth, data storage,
  external integrations.
- **performance-optimization** — measure-first: Core Web Vitals targets, profiling workflows,
  bundle analysis, anti-pattern detection. When perf requirements exist or regressions suspected.

### Ship — deploy with confidence
- **git-workflow-and-versioning** — trunk-based development, atomic commits, change sizing
  (~100 lines), commit-as-save-point, semantic versioning, tagging, changelogs. For any code change.
- **ci-cd-and-automation** — Shift Left, Faster is Safer, feature flags, quality-gate
  pipelines, failure feedback loops. For build/deploy pipelines.
- **deprecation-and-migration** — code-as-liability mindset, compulsory vs advisory
  deprecation, migration patterns, zombie-code removal. For removing/migrating/sunsetting.
- **documentation-and-adrs** — Architecture Decision Records, API docs, inline documentation
  standards — document the *why*. For architectural decisions, API changes, shipping features.
- **observability-and-instrumentation** — structured logging, RED metrics, OpenTelemetry
  tracing, symptom-based alerting — instrument as you build. For telemetry / production code.
- **shipping-and-launch** — pre-launch checklists, feature-flag lifecycle, staged rollouts,
  rollback procedures, monitoring setup. When preparing to deploy to production.

## Agent personas (4 specialist subagents)
| Agent | Role | Perspective |
|-------|------|-------------|
| code-reviewer | Senior Staff Engineer | Five-axis review with "would a staff engineer approve this?" standard |
| test-engineer | QA Specialist | Test strategy, coverage analysis, the Prove-It pattern; tests at the right level (unit/integration/E2E) |
| security-auditor | Security Engineer | Vulnerability detection, threat modeling, OWASP assessment; practical exploitable issues |
| web-performance-auditor | Web Performance Engineer | Core Web Vitals audit; Quick mode (source scan, "potential impact") vs Deep mode (Lighthouse/PSI/CrUX/trace data); metric-honesty rule; run via `/webperf` |

See `docs/agents.md` for the decision matrix and orchestration rules; `references/orchestration-patterns.md` for endorsed multi-persona patterns and the "personas don't invoke personas" rule.

## Reference checklists (pulled in by skills when needed)
- **definition-of-done.md** — project-wide standing bar every change clears (vs per-task acceptance criteria).
- **testing-patterns.md** — test structure, naming, mocking, React/API/E2E examples, anti-patterns.
- **security-checklist.md** — pre-commit checks, auth, input validation, headers, CORS, OWASP Top 10.
- **performance-checklist.md** — Core Web Vitals targets, frontend/backend checklists, measurement commands.
- **accessibility-checklist.md** — keyboard nav, screen readers, visual design, ARIA, testing tools.
- **observability-checklist.md** — on-call questions, structured logging, RED/USE metrics, tracing, symptom-based alerting, pre-launch gate.
- **orchestration-patterns.md** — endorsed multi-persona orchestration patterns, anti-patterns, "personas don't invoke personas".

## Key design choices
- **Process, not prose.** Skills are workflows with steps, checkpoints, exit criteria — not reference docs.
- **Anti-rationalization.** Every skill has a table of excuses agents use to skip steps (e.g. "I'll add tests later") with counter-arguments.
- **Verification is non-negotiable.** Every skill ends with evidence requirements (tests passing, build output, runtime data). "Seems right" is never sufficient.
- **Progressive disclosure.** SKILL.md is the entry point; supporting references load only when needed.

## How it compares (from docs/comparison.md)
Positions itself against **Superpowers** (obra/Jesse Vincent) and **Matt Pocock's skills**:
- **agent-skills** — organizes the *whole product lifecycle* (Define→Plan→Build→Verify→Review→Ship) with review personas + anti-rationalization guards; human checkpoint at each phase; broadest tool reach. Best for driving a feature through every phase with a checkpoint at each.
- **Superpowers** — autonomous, reasoning-heavy runs with subagents + git-worktree isolation; two-stage review; strict TDD (deletes prematurely written code); skills-that-write-skills. Best for handing off long autonomous/exploratory stretches.
- **Matt Pocock's skills** — a sharp, personal Claude Code toolkit distilled from one expert's daily workflow (grill-me, strict TDD, git guardrails). Best for a pragmatic daily loop.

Cited head-to-head (Om Mishra, Sonnet 4.6, same repo/prompt): agent-skills moved to code faster (~8m vs ~12m) and ran more validation passes (7 vs 5, catching a compatibility issue outside the feature); Superpowers invested more upfront architectural reasoning. Trade-off framed as *broad disciplined validation vs. heavy upfront reasoning*. Guidance: pick one framework as the active router; cherry-pick individual skills from others à la carte; don't run two meta-skill routers simultaneously (they fight over command names like `/tdd`).

## Repo structure
```
agent-skills/
├── skills/         # 24 skills (23 lifecycle + 1 meta), each a SKILL.md (+ references)
├── agents/         # 4 specialist personas
├── references/     # 7 supplementary checklists
├── hooks/          # session lifecycle hooks (session-start, sdd-cache, simplify-ignore)
├── .claude/commands/  # 8 slash commands (Claude Code)
├── .gemini/commands/  # 8 slash commands (Gemini CLI)
├── commands/          # 8 slash commands (Antigravity CLI)
├── plugin.json     # Antigravity plugin manifest
└── docs/           # setup guides per tool + comparison.md + agents.md + skill-anatomy.md
```
</content>
</invoke>
