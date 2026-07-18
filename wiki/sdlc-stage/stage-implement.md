---
type: sdlc-stage
aka: { gsd: "Execute", matt-pocock-skills: "implement / TDD / prototype / merge-conflicts", addy-agent-skills: "Build (+ Verify: debugging)", openspec: "apply", speckit: "implement", bmad: "Implementation (dev-story / quick-dev)", compound-engineering: "work (+ worktree / debug / polish)", gstack: "Build (design-html / investigate) + guardrails + context", bm-skills: "design-system", superpowers: "subagent-driven / executing-plans (+ TDD / debugging / worktrees / parallel-agents)" }
sources: "Synthesized from GSD + Matt Pocock + Addy Osmani + OpenSpec + Spec Kit + BMAD + Compound Engineering + gstack + Superpowers (2026)"
updated: 2026-07-17
---

# Stage: Implement

Canonical lifecycle stage: **write the code that satisfies the plan** — including building it, testing it into existence, and fixing it. Framework-neutral name (was `stage-execute`, GSD's term) in standard SDLC vocabulary. Characteristically parallelized and context-isolated to avoid degradation at scale.

**Derived projection** — evidence is the capabilities that `implements: [[stage-implement]]`.

## Implemented by (backlinks)

GSD:

- [[gsd-execute-phase]] — wave-based parallel execution ([[pattern-wave-parallelism]]).
- [[gsd-executor]] — one atomic commit per task → [[artifact-atomic-commit]]; sole Edit-capable agent.
- [[gsd-debugger]] — evidence-tracking bug investigation ([[pattern-systematic-debugging]]).

Matt Pocock — Skills for Real Engineers:

- [[mp-implement]] — build the work from a spec/tickets, TDD at seams, then code-review → [[artifact-atomic-commit]] (v1.1; MP's first first-class execute skill).
- [[mp-tdd]] — test-first red → green loop (v1.1: refactor moved to [[mp-code-review]]) ([[pattern-test-driven-development]]).
- [[mp-prototype]] — throwaway prototypes ([[pattern-throwaway-prototype]]).
- [[mp-diagnosing-bugs]] — structured debugging loop ([[pattern-systematic-debugging]]).
- [[mp-resolving-merge-conflicts]] — resolve merge/rebase conflicts from each side's primary-source intent (v1.1; [[pattern-trunk-based-development]]).

Addy Osmani — Agent Skills (its whole Build phase, plus debugging which it files under Verify):

- [[addy-incremental-implementation]] — thin vertical slices → [[artifact-atomic-commit]] ([[pattern-vertical-slice]], [[pattern-feature-flags]]).
- [[addy-tdd]] — red-green-refactor; Prove-It for bugs ([[pattern-test-driven-development]]).
- [[addy-debugging]] — five-step triage: reproduce, localize, reduce, fix, guard ([[pattern-systematic-debugging]]).
- [[addy-api-design]] — contract-first interfaces ([[pattern-contract-first]], [[pattern-deep-modules]]).
- [[addy-frontend-ui]] — production-quality UI + WCAG 2.1 AA accessibility.
- [[addy-context-engineering]] — right context at the right time ([[pattern-context-engineering]]).
- [[addy-source-driven-development]] — cite official docs ([[pattern-source-grounding]]).
- [[addy-doubt-driven-development]] — in-flight adversarial review ([[pattern-adversarial-review]]).

OpenSpec:

- [[openspec-apply]] — walk the `tasks.md` checklist sequentially, resuming from checkpoints.

Spec Kit:

- [[speckit-implement]] — execute `tasks.md`, with TDD mandated by the constitution (tests fail before code) ([[pattern-test-driven-development]]).

BMAD:

- [[bmad-dev]] — the Implementation persona (Amelia); absorbed the classic SM + QA roles.
- [[bmad-dev-story]] — implement one fully-contexted story test-first in a fresh context → [[artifact-atomic-commit]] ([[pattern-test-driven-development]], [[pattern-context-engineering]], [[pattern-fresh-context-subagents]]).
- [[bmad-quick-dev]] — Quick-Flow fast path for small work ([[pattern-scale-adaptive-planning]]).

(The story it executes is prepared upstream by [[bmad-create-story]] in [[stage-plan]] — the plan→implement bridge.)

Compound Engineering:

- [[ce-work]] — execute the guardrailed plan (HOW) inside an isolated worktree, simulating real usage via MCP ([[pattern-worktree-isolation]], [[pattern-vertical-slice]]) → [[artifact-atomic-commit]].
- [[ce-worktree]] — the git-worktree isolation the work runs in ([[pattern-worktree-isolation]]).
- [[ce-debug]] — causal-chain + prediction-driven root-cause ([[pattern-systematic-debugging]]).
- [[ce-polish]] — conversational UX iteration against a live dev server.

gstack (build + debugging + the guardrails/session infrastructure that make autonomous building safe):

- [[gstack-design-shotgun]] — explore 4-6 AI mockup variants with taste memory → [[artifact-design-mockup]] ([[pattern-throwaway-prototype]]).
- [[gstack-design-html]] — turn an approved mockup into production Pretext-native HTML/CSS.
- [[gstack-investigate]] — Iron-Law root-cause debugging (no fix without investigation; auto-freeze) ([[pattern-systematic-debugging]]); debugging cluster with [[gsd-debugger]] / [[mp-diagnosing-bugs]] / [[addy-debugging]] / [[ce-debug]].
- [[gstack-scrape]] — browser data-extraction automation (compounds via [[gstack-skillify]]).
- [[gstack-careful]] · [[gstack-freeze]] · [[gstack-guard]] · [[gstack-unfreeze]] — safety guardrails / directory-scoped edit locks ([[pattern-edit-guardrails]]).
- [[gstack-context-save]] · [[gstack-context-restore]] — save/restore working context + WIP checkpoints ([[pattern-session-handoff]]).
- [[gstack-pair-agent]] — cross-vendor multi-agent collaboration through a shared browser (novel; no counterpart).

Builder Methods — BM Skills:

- [[bm-design-system]] — scaffold a React + Tailwind v4 design system into the codebase (runnable components + a live reference page + `AGENTS.md`/`CLAUDE.md` guardrails → [[artifact-design-md]]); counterpart to [[addy-frontend-ui]] ([[pattern-context-engineering]]).

Superpowers (the densest implement roster here — execution engines + the TDD/debug/isolation/parallelism disciplines that run inside them):

- [[sp-subagent-driven-development]] — fresh implementer subagent per task + two-stage task review + final whole-branch review → [[artifact-atomic-commit]] ([[pattern-fresh-context-subagents]], [[pattern-adversarial-review]]).
- [[sp-executing-plans]] — the parallel-session executor: batch execution with human checkpoints (subagent-free fallback) → [[artifact-atomic-commit]] ([[pattern-test-driven-development]]).
- [[sp-test-driven-development]] — RED-GREEN-REFACTOR; Iron Law "no production code without a failing test first" ([[pattern-test-driven-development]]).
- [[sp-systematic-debugging]] — four-phase root-cause process; Iron Law "no fixes without investigation"; question the architecture after 3 failed fixes ([[pattern-systematic-debugging]]).
- [[sp-using-git-worktrees]] — ensure an isolated workspace (native-tool-first, git fallback, clean-baseline check) ([[pattern-worktree-isolation]]).
- [[sp-dispatching-parallel-agents]] — one focused subagent per independent problem domain, dispatched concurrently ([[pattern-fresh-context-subagents]], [[pattern-wave-parallelism]]).

## Cross-framework equivalents
The capability-level clusters landing here now span all eight frameworks:

- **Debugging:** GSD's [[gsd-debugger]] ↔ Matt's [[mp-diagnosing-bugs]] ↔ Addy's [[addy-debugging]] ↔ Compound Engineering's [[ce-debug]] ↔ gstack's [[gstack-investigate]] ↔ Superpowers' [[sp-systematic-debugging]] (`equivalent_to`), all applying [[pattern-systematic-debugging]]. (Addy categorizes debugging under its *Verify* phase, but it is the same activity, so it clusters here; CE adds an explicit prediction-confirmation step; gstack and Superpowers share an **Iron-Law "no fix without investigation"** and a stop-after-3-fixes rule.)
- **Test-first:** Matt's [[mp-tdd]] ↔ Addy's [[addy-tdd]] ↔ GSD's [[gsd-plan-phase]] `--tdd` ↔ Spec Kit's [[speckit-implement]] (TDD "NON-NEGOTIABLE") ↔ BMAD's [[bmad-dev-story]] (Amelia is "disciplined in Kent Beck's TDD") ↔ Superpowers' [[sp-test-driven-development]], clustered at [[pattern-test-driven-development]] — Spec Kit mandates it via the [[artifact-constitution]]; Superpowers matches its non-negotiability through rhetoric (delete-and-restart any code written before its test).
- **Execute loop (now eight frameworks):** OpenSpec's [[openspec-apply]] ↔ Addy's [[addy-incremental-implementation]] ↔ GSD's [[gsd-execute-phase]] ↔ Spec Kit's [[speckit-implement]] ↔ BMAD's [[bmad-dev-story]] ↔ Compound Engineering's [[ce-work]] ↔ Matt Pocock's [[mp-implement]] ↔ **Superpowers' [[sp-executing-plans]] / [[sp-subagent-driven-development]]** — walk the plan/tickets unit-by-unit. They differ in mechanics: GSD parallelizes into [[pattern-wave-parallelism]] waves, Addy cuts thin [[pattern-vertical-slice]]s, OpenSpec runs a plain resumable sequential pass, Spec Kit drives test-first per the constitution, BMAD drives from a single fully-contexted [[artifact-story|story]] per fresh context, CE bounds execution with plan **guardrails** in [[pattern-worktree-isolation|worktree isolation]], MP drives [[mp-tdd]] at pre-agreed seams, and Superpowers offers **two modes** — continuous same-session [[pattern-fresh-context-subagents|fresh-subagent-per-task]] with a two-stage review ([[sp-subagent-driven-development]], clustering with [[gsd-execute-phase]] / [[bmad-dev-story]]) or checkpointed batch execution ([[sp-executing-plans]]).
- **Worktree isolation:** Compound Engineering's [[ce-worktree]] ↔ Superpowers' [[sp-using-git-worktrees]] — both make an isolated git worktree a first-class execution step ([[pattern-worktree-isolation]]).
- **Interface design:** Addy's [[addy-api-design]] ↔ Matt's [[mp-codebase-design]] — deep modules / stable contracts (Spec Kit authors its `contracts/` upstream in [[speckit-plan]]).

## See Also
- [[stage-plan]] — produces the plan executed here.
- [[stage-validate]] — confirms the result works; [[stage-review]] — confirms it's good.
