---
source: "Factory.ai — Agent Readiness"
urls:
  - https://factory.ai/agent-readiness
  - https://factory.ai/product/agent-readiness
  - https://factory.ai/news/agent-readiness
  - https://docs.factory.ai/web/agent-readiness/overview
  - https://docs.factory.ai/docs/agent-readiness/readiness-report
  - https://docs.factory.ai/web/agent-readiness/dashboard
captured: 2026-08-07
capture_method: "WebFetch of the marketing, announcement, and docs pages; the public report gallery and dashboard render client-side and were not scrapeable"
license: proprietary (Factory.ai product)
---

# Factory.ai — Agent Readiness (capture 2026-08-07)

## Thesis

> "The agent is not broken. The environment is."

Teams deploying AI coding agents get uneven results because of **codebase** limitations rather than model deficiencies. Poor feedback loops, undocumented environment variables, and unclear build processes compound into problems that defeat any agent; well-structured codebases amplify agent effectiveness. Agent Readiness "measures whether repositories have the structure, validation, and operational signals that let autonomous agents work reliably."

This inverts the usual framing: instead of improving the agent or the prompt, improve the **repository** the agent works in.

## The five readiness levels

| Level | Name | What it means |
|-------|------|---------------|
| 1 | **Functional** | Code runs with basic tooling — README, linter, type checker, unit tests. "Basic tooling is in place." |
| 2 | **Documented** | Basic documentation and process automation in place. |
| 3 | **Standardized** | Clear processes enforced through automation across the organization; security and observability configured. |
| 4 | **Optimized** | Fast feedback loops with data-driven improvements; continuous measurement. |
| 5 | **Autonomous** | Self-improving systems with sophisticated orchestration. "Systems can improve themselves with agent support." |

**Progression rule:** a repo must pass **80% of the criteria at a level** (and all previous levels) before the next level unlocks. Levels stay locked until the previous one reaches 80%.

**Target:** Level 3 is stated as the minimum bar for production-grade autonomous operation — "most teams aim here first." At L3 agents can handle routine maintenance: bug fixes, tests, dependency upgrades.

## The technical pillars

The docs overview lists **nine**; the launch announcement lists **eight** (with "Code Quality" in place of "Task Discovery" and "Product & Experimentation", and "Security & Governance" merged). Both variants recorded verbatim:

**Docs overview (9 pillars):**

1. **Style & Validation** — linters, type checkers, formatters, pre-commit hooks
2. **Build System** — documented commands, pinned dependencies, VCS tools
3. **Testing** — unit and integration tests with local execution capability
4. **Documentation** — AGENTS.md, README, maintained guides
5. **Development Environment** — devcontainers, environment templates, local services
6. **Debugging & Observability** — structured logging, distributed tracing, metrics
7. **Security** — branch protection, secret scanning, CODEOWNERS
8. **Task Discovery** — issue templates, labeling systems, PR templates
9. **Product & Experimentation** — analytics instrumentation, experiment infrastructure

**Launch announcement (8 pillars):** Style & Validation · Build System · Testing · Documentation · Dev Environment · Code Quality · Observability · Security & Governance.

Each pillar is justified by the failure mode it removes. Examples given: linters/type checkers/formatters "catch obvious errors instantly, helping agents avoid wasting cycles on syntax errors, style inconsistencies, and type mismatches"; fast unit and integration tests "create tight feedback loops, allowing agents to learn whether their changes work correctly by running tests, seeing failures, and iterating."

Scale: "100+ signals" evaluated per repository.

## How the evaluation runs (`/readiness-report`)

Run from inside a git repository with an `origin` remote configured, via the `droid` CLI. Sequence:

1. **Language detection** — identifies supported languages (JavaScript/TypeScript, Python, Rust, Go, Java, Ruby) from config files and source.
2. **Sub-application discovery** — classifies the repo as a monorepo or single package; identifies independently deployable applications.
3. **Criteria evaluation** — assesses the repository against the readiness criteria.
4. **Report storage** — persists results for visualization in the Factory App.
5. **Summary output** — human-readable evaluation report.

**Scoring.** Criteria are **binary (pass/fail)**, evaluated at both repository and application scope. Scores are reported as a numerator/denominator: how many sub-applications pass each criterion out of the total evaluated.

**Difficulty axis.** Each criterion carries an independent difficulty rating — **Basic**, **Intermediate**, or **Advanced** — indicating *implementation effort*, orthogonal to which level the criterion belongs to.

**Determinism.** Factory addressed LLM non-determinism by **grounding each evaluation against the previous report**, reducing run-to-run variance from **7% to 0.6%**.

## Remediation (`/readiness-fix`)

Automatically addresses failing criteria:

- fetches the most recent stored report;
- starts an agent session to implement fixes — cited examples: pre-commit hooks, AGENTS.md files, CI configuration, documentation improvements;
- the user reviews changes before committing.

Natural-language instructions can be added to focus remediation on specific areas and exclude others. The dashboard also allows selecting failing criteria marked "Planned" and triggering automated fixes directly from the web UI.

## The dashboard (organization scope)

Three summary cards: **Organization Score** ("average readiness level across all measured repositories, rounded down"), **Repositories Tracked** (repos with reports vs. total enabled), **Last Updated**.

Org score is `floor(mean(repo levels))` — e.g. repos at levels 3, 2, 3 → `floor(8/3)` = Level 2.

Also provides: a time-series graph of organizational progress over 7d / 1m / 6m / 1y / all; a searchable paginated repositories table (current level, progress %, last evaluation date); and per-repository detail pages breaking down individual criteria with pass/fail indicators and **rationale explanations**.

A public gallery at `factory.ai/agent-readiness` publishes reports for well-known open-source repos (e.g. `factory.ai/agent-readiness/fastapi_fastapi`), showing levels in the 2–4 range and pass rates of roughly 53–74%.

## Access surfaces

- `/readiness-report` and `/readiness-fix` slash commands in the Droid CLI.
- Readiness Dashboard in the Factory web app.
- Readiness Reports API (`docs.factory.ai/docs/api-reference/readiness-reports`).

## Related third-party implementations (noted, not captured in depth)

- **kodustech/agent-readiness** (GitHub) — "the open-source alternative to Factory.ai's Agent Readiness." **7 pillars / 39 automated checks**: Style & Linting (6), Testing (6), Documentation (8), Dev Environment (5), CI/CD (6), Code Health (3), Security (5). Levels: 1 Foundational · 2 Guided · 3 Structured · 4 Optimized · 5 Autonomous, with the same **≥80% per level** advancement rule. Criteria live in `src/pillars/`, one file per pillar.
- **agent-ready.org** — "AI Agent Readiness Scanner."

## Notes on capture completeness

The full list of "100+ signals" is **not published**; the docs describe pillars, levels, scoring, and the run/fix flow but not the individual criteria. The public report gallery and dashboard render client-side and could not be scraped. `docs.factory.ai/web/agent-readiness/criteria` and `/web/agent-readiness/readiness-report` return 404; the report doc lives at `docs.factory.ai/docs/agent-readiness/readiness-report`.
