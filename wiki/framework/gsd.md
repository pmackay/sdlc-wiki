---
type: framework
source_url: "https://github.com/open-gsd/gsd-core"
docs_url: "https://docs.opengsd.net/"
sources: "Open GSD docs (2026); open-gsd/gsd-core README (2026)"
raw: ["../../raw/gsd/2026-06-27-gsd-core-framework.md"]
updated: 2026-07-04
---

# GSD — Git. Ship. Done.

**GSD** is "a light-weight meta-prompting, context engineering, and spec-driven
development system for AI coding agents" (Claude Code, OpenCode, Gemini CLI, Codex,
Copilot, Cursor, Windsurf, and more). Install: `npx @opengsd/gsd-core@latest`.

It solves **context rot** — quality degradation as an agent fills its context window — by
routing heavy research and execution through fresh-context subagents (see
[[pattern-fresh-context-subagents]]) while keeping a lean main session. Its whole method
is spec-driven (see [[pattern-spec-driven-development]]).

GSD ships as a three-tool suite. This wiki documents **GSD Core**, the SDLC workflow
engine. (The others: **GSD Pi**, a standalone autonomous local coding agent with
worktree-isolated Git and multi-provider routing; **GSD Browser**, native CDP browser
automation with an MCP server.)

## The five-phase loop

Each milestone repeats this cycle, one phase per iteration. Each phase is a `command`
capability that `implements:` a canonical SDLC stage:

| Phase | Command | Stage |
|-------|---------|-------|
| Discuss | [[gsd-discuss-phase]] | [[stage-align]] |
| Plan    | [[gsd-plan-phase]]    | [[stage-plan]] |
| Execute | [[gsd-execute-phase]] | [[stage-implement]] |
| Verify  | [[gsd-verify-work]]   | [[stage-validate]] |
| Ship    | [[gsd-ship]]          | [[stage-release]] |

> **Conflict (source disagreement):** the docs homepage lists the pipeline as
> *Research → Plan → Execute → Verify → Ship*, but the GitHub README and every detailed
> doc page list *Discuss → Plan → Execute → Verify → Ship*. This wiki treats **Discuss**
> as canonical; "Research" on the homepage appears informal (research is a sub-step of
> Plan, run by [[gsd-phase-researcher]]). See [[stage-align]].

## Capabilities

### Commands (workflow)

The five phase commands, documented here:

- [[gsd-discuss-phase]] — Phase 1; lock decisions before planning.
- [[gsd-plan-phase]] — Phase 2; research, plan, verify.
- [[gsd-execute-phase]] — Phase 3; wave-based parallel execution.
- [[gsd-verify-work]] — Phase 4; conversational UAT with auto-diagnosis.
- [[gsd-ship]] — Phase 5; open PR, track merge, archive phase.

65+ slash commands total, grouped by namespace:

- **workflow** — the five phase commands above.
- **context** — `map-codebase`, `graphify`, `ingest-docs`, `extract-learnings`, `mempalace-capture` / `mempalace-recall`.
- **management** — `config`, `settings`, `update`, `workspace`, `workstreams`.
- **project** — `new-project`, `new-milestone`, `complete-milestone`, `phase`, `pause-work` / `resume-work`, `health`, `progress`.
- **quality** — `code-review`, `add-tests`, `secure-phase`, `ui-review`, `debug`, `audit-fix` / `audit-milestone` / `audit-uat`, `eval-review`.
- **autonomous** — `/gsd-autonomous`, `/gsd-manager`.
- **cross-AI review** — `/gsd-review`.

### Sub-agents (specialist agents)

34 specialist agents total. Each "receives a precisely scoped prompt and the subset of
planning artifacts it needs," running in parallel or sequentially to prevent context
degradation.

Documented here:

- [[gsd-phase-researcher]] — parallel domain research.
- [[gsd-planner]] — atomic plan authoring.
- [[gsd-plan-checker]] — eight-dimension plan gate.
- [[gsd-executor]] — code implementation, one commit per task.
- [[gsd-verifier]] — goal-backward verification.
- [[gsd-debugger]] — evidence-tracking bug investigation (equivalent to Matt Pocock's [[mp-diagnosing-bugs]]).

Not yet given dedicated pages:

- **Research** — gsd-project-researcher, gsd-domain-researcher, gsd-advisor-researcher, gsd-ai-researcher, gsd-research-synthesizer, gsd-roadmapper.
- **UI** — gsd-ui-researcher, gsd-ui-checker, gsd-ui-auditor.
- **Quality / audit** — gsd-code-reviewer, gsd-security-auditor, gsd-nyquist-auditor, gsd-eval-planner, gsd-eval-auditor, gsd-integration-checker.
- **Debug / fix** — gsd-debug-session-manager, gsd-code-fixer (gsd-debugger now has its own page).
- **Codebase & analysis** — gsd-codebase-mapper, gsd-assumptions-analyzer, gsd-pattern-mapper, gsd-framework-selector.
- **Docs** — gsd-doc-writer, gsd-doc-classifier, gsd-doc-synthesizer, gsd-doc-verifier.
- **Memory / profile** — gsd-mempalace-curator, gsd-intel-updater, gsd-user-profiler.

## Artifacts produced

All organized under a `.planning/` directory, with `STATE.md` / `CONTEXT.md` for
cross-session persistence:

- [[artifact-context-md]] — locked decisions + scope.
- [[artifact-plan-md]] — executable task prompts.
- [[artifact-research-md]] — parallel domain research output.
- [[artifact-uat-md]] — UAT results + diagnosed gaps.
- [[artifact-atomic-commit]] — one commit per completed task.
- [[artifact-pull-request]] — PR opened at ship time.

## Patterns applied

- [[pattern-spec-driven-development]] — drive agents from explicit specs.
- [[pattern-fresh-context-subagents]] — clean context per task to beat context rot.
- [[pattern-wave-parallelism]] — dependency-ordered parallel execution.
- [[pattern-plan-verification-loop]] — gate plans before execution.

## See Also
- [[compound-engineering]] — Every's compounding loop; [[gsd-execute-phase]] ↔ [[ce-work]] (execute), [[gsd-ship]] ↔ [[ce-commit-push-pr]] (finalize), [[gsd-debugger]] ↔ [[ce-debug]], [[gsd-plan-checker]] ↔ [[ce-doc-review]]; both use [[pattern-fresh-context-subagents]]. CE adds the seventh stage GSD lacks, [[stage-learn]].
- [[stage-align]], [[stage-specify]], [[stage-plan]], [[stage-implement]], [[stage-validate]], [[stage-release]] — the canonical lifecycle this framework implements.
- [[matt-pocock-skills]] — sibling framework; shares [[pattern-grilling]], [[pattern-vertical-slice]], [[pattern-test-driven-development]], [[pattern-systematic-debugging]], and [[pattern-session-handoff]].
- [[addy-agent-skills]] — lifecycle-complete framework; [[addy-shipping]] ↔ [[gsd-ship]], [[addy-incremental-implementation]] ↔ [[gsd-execute-phase]], [[addy-debugging]] ↔ [[gsd-debugger]], [[addy-planning]] ↔ [[gsd-plan-phase]], and it shares [[pattern-fresh-context-subagents]], [[pattern-vertical-slice]], [[pattern-test-driven-development]], and [[pattern-grilling]]. Its [[stage-release]] coverage far exceeds GSD's.
- [[openspec]] — sibling spec-driven framework; [[openspec-apply]] ↔ [[gsd-execute-phase]], [[openspec-verify]] ↔ [[gsd-verify-work]] / [[gsd-verifier]], [[openspec-archive]] ↔ [[gsd-ship]], [[openspec-explore]] ↔ [[gsd-discuss-phase]]. Both are [[pattern-spec-driven-development]]; OpenSpec keeps a permanent [[pattern-living-specification]] where GSD's specs are per-phase.
- [[bmad]] — closest sibling in breadth and context-engineering: both are full-lifecycle and subagent/persona-driven. [[bmad-dev-story]] ↔ [[gsd-execute-phase]], [[bmad-check-implementation-readiness]] ↔ [[gsd-plan-checker]], [[bmad-code-review]] ↔ [[gsd-verifier]]. GSD spreads execution across executor + verifier + debugger where BMAD folds it into one persona (Amelia); GSD ships to prod where BMAD core closes with a retrospective.
