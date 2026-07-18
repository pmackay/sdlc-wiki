---
source_urls:
  - https://github.com/EveryInc/compound-engineering-plugin
  - https://raw.githubusercontent.com/EveryInc/compound-engineering-plugin/main/README.md
  - https://github.com/EveryInc/compound-engineering-plugin/tree/main/docs/skills
collected: 2026-07-04
published: Unknown
---

# EveryInc/compound-engineering-plugin

> Fetched rendition (WebFetch of README + docs/skills/README.md + repo tree via `gh api`,
> 2026-07-04). Skill/sub-agent rosters enumerated from the actual repo tree.

## Overview

An AI-assisted engineering workflow system that makes each unit of work easier than the last
by emphasizing **planning, review, and knowledge capture over execution alone**. Central
thesis: **"Each unit of engineering work should make subsequent units easier — not harder."**
Effort allocation: **"80% is in planning and review, 20% in execution."**

Repo stats (2026-07-04): ~22.6k stars, 1.7k forks, 187 releases. TypeScript (76.5%), Python
(18.5%), Shell (4.2%). MIT license.

## Install (Claude Code)

```
/plugin marketplace add EveryInc/compound-engineering-plugin
/plugin install compound-engineering
```

Also ships manifests for Cursor, Codex App/CLI, Kimi Code CLI, GitHub Copilot, Factory Droid,
Qwen Code, OpenCode, Pi, and Antigravity CLI (`agy`).

## The main loop (six steps)

1. **Brainstorm** — `/ce-brainstorm` — define what something should become through dialogue; outputs a requirements-only unified plan (`docs/brainstorms/`).
2. **Plan** — `/ce-plan` — bound execution with guardrails; enrich into implementation-ready plans with U-IDs and test scenarios; WHAT not HOW (`docs/plans/`).
3. **Work** — `/ce-work` — execute against guardrails; figure out HOW with code; ship through quality gates (in a git worktree).
4. **Simplify** — `/ce-simplify-code` — refine recently changed code for reuse, quality, efficiency while preserving behavior.
5. **Review** — `/ce-code-review` — structured multi-agent review with skill-local personas, confidence-gated findings, four modes.
6. **Compound** — `/ce-compound` — close the loop by capturing learnings into `docs/solutions/` so the next iteration starts smarter.

Each cycle sharpens the next: new brainstorms read prior compound notes as grounding; reviews
catch patterns, not just bugs. *"A good compound note means the next agent does not have to
learn the same lesson from scratch."*

## `/lfg` — autonomous full loop

Runs the complete pipeline hands-off after brainstorm: plans, executes, simplifies, reviews
with fixes, tests, commits, pushes, opens a PR, and watches CI until green. Returns when the
PR is ready.

## Full skill roster (29 top-level skills)

| Skill | One-liner |
|-------|-----------|
| `/ce-strategy` | Create/maintain `STRATEGY.md` — the upstream anchor read by ideate, brainstorm, and plan. |
| `/ce-ideate` | Discover strong, qualified directions with conceptual frames and adversarial filtering. |
| `/ce-pov` | Form a decisive verdict on external inputs with dual grounding and Adopt/Trial/Hold/Reject outcomes. |
| `/ce-explain` | Turn concepts, diffs, or recent work into dense visual explainers with optional verification. |
| `/ce-brainstorm` | Define what something should become through collaborative dialogue and requirements-only plans. |
| `/ce-plan` | Bound execution with guardrails; enrich plans with U-IDs and test scenarios; WHAT not HOW. |
| `/ce-doc-review` | Review requirements or plans using reviewer personas across coherence, feasibility, security lenses. |
| `/ce-work` | Execute against implementation-ready guardrails; figure out HOW with code; ship through quality gates. |
| `/ce-worktree` | Ensure work happens in an isolated git worktree with native harness detection + fallback. |
| `/ce-simplify-code` | Refine recently changed code for reuse, quality, efficiency while preserving behavior. |
| `/ce-code-review` | Structured code review with skill-local personas, confidence-gated findings, four modes. |
| `/ce-compound` | Close the loop by capturing learnings into `docs/solutions/` so the next iteration starts smarter. |
| `/ce-compound-refresh` | Maintain `docs/solutions/` over time with Keep/Update/Consolidate/Replace/Delete outcomes. |
| `/ce-debug` | Find root causes systematically through causal chains, predictions, and post-fix polish. |
| `/ce-optimize` | Metric-driven iterative optimization with three-tier evaluation and parallel experiments. |
| `/ce-polish` | Conversational UX polish — start dev server, open browser, iterate together; framework auto-detect. |
| `/ce-proof` | Publish, view, comment on, and edit markdown via the Proof collaborative editor. |
| `/ce-sweep` | Ingest Slack/GitHub items since cursors, acknowledge at source, analyze, verify fixes, reconcile plans. |
| `/ce-product-pulse` | Single-page time-windowed report on usage, performance, errors, followups for timeline tracking. |
| `/ce-promote` | Draft user-facing announcement copy for shipped features across X, changelog, LinkedIn, email. |
| `/ce-riffrec-feedback-analysis` | Turn raw Riffrec recordings into structured feedback with bug or extensive-analysis handoff. |
| `/ce-resolve-pr-feedback` | Evaluate, fix, and reply to PR review feedback in parallel including nitpicks. |
| `/ce-commit` | Create a single, well-crafted git commit with convention awareness and file-level splitting. |
| `/ce-commit-push-pr` | Go from working changes to open PR with adaptive descriptions and three workflow modes. |
| `/ce-dogfood` | Hands-off diff-scoped browser QA with autonomous small-breakage fixes and durable reporting. |
| `/ce-test-browser` | End-to-end browser tests on PR/branch-affected pages using agent-browser exclusively. |
| `/ce-test-xcode` | Build and test iOS apps on simulator using XcodeBuildMCP with screenshots and logs. |
| `/ce-setup` | Diagnose optional tool capabilities and bootstrap safe project-local configuration. |
| `/lfg` | Run the full hands-off engineering pipeline from planning through green PR with CI watch. |

## Sub-agents (26 distinct, referenced under skills/*/references/agents/)

- **Research / grounding:** repo-profiler, learnings-researcher, best-practices-researcher, framework-docs-researcher, web-researcher, external-evidence-researcher, slack-researcher, issue-intelligence-analyst, session-historian, git-history-analyzer, repo-research-analyst, precedent-activity-scout, project-grounding-scout, work-recap-scout, spec-flow-analyzer, media-analyzer.
- **Review / quality specialists:** security-sentinel, performance-oracle, data-integrity-guardian, data-migration-reviewer, deployment-verification-agent, pattern-recognition-specialist, pr-comment-resolver.
- **Design / planning:** architecture-strategist, agent-native-planning-strategist, figma-design-sync.

The `ce-code-review` skill additionally carries ~16 persona *lenses* (correctness, security,
performance, maintainability, reliability, testing, api-contract, data-migration, adversarial,
agent-native, deployment-verification, project-standards, previous-comments, learnings-researcher,
plus stack-specific Swift/iOS and frontend-races reviewers). `ce-doc-review` carries 7 doc
personas (coherence, feasibility, security-lens, product-lens, design-lens, scope-guardian,
adversarial-document).

## Knowledge compounding — the mechanism

`/ce-compound` writes solved problems into **`docs/solutions/`** as structured solution
documents (validated against a YAML frontmatter schema; see `skills/ce-compound/references/`).
A council of research sub-agents (session-historian, pattern-recognition-specialist,
security-sentinel, performance-oracle, best-practices-researcher, framework-docs-researcher,
data-integrity-guardian) mines the completed work for reusable lessons. Future `/ce-brainstorm`,
`/ce-plan`, and `/ce-code-review` runs read these notes as grounding (via `learnings-researcher`),
embedding prior patterns into planning and review. `/ce-compound-refresh` keeps the corpus
healthy over time (Keep/Update/Consolidate/Replace/Delete). *"The return mechanism — where
compounded learnings feed into future cycles — is the whole point."*
