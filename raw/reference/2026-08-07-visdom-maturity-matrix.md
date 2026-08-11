---
source: "VirtusLab — Visdom AI-Native SDLC Maturity Matrix"
urls:
  - https://visdom-maturity-matrix.virtuslab.com/
  - https://visdom-maturity-matrix.virtuslab.com/matrix
  - https://visdom-maturity-matrix.virtuslab.com/workshop
  - https://visdom-maturity-matrix.virtuslab.com/matrix/development
  - https://visdom-maturity-matrix.virtuslab.com/matrix/delivery
  - https://visdom-maturity-matrix.virtuslab.com/matrix/organization
  - https://visdom-maturity-matrix.virtuslab.com/matrix/infrastructure
  - https://virtuslab.com/blog/ai/ai-works-great-at-level-four
captured: 2026-08-07
capture_method: "WebFetch of the four perspective pages + the thesis blog post; sitemap.xml enumerated for the practice-guide slugs. The /workshop and /matrix landing pages render client-side and were not directly scrapeable."
license: proprietary (VirtusLab consulting asset; publicly readable)
---

# VirtusLab — Visdom AI-Native SDLC Maturity Matrix (capture 2026-08-07)

## Thesis

The industry lacks a **common vocabulary** for AI-adoption maturity — the same position DevOps was in around 2013–2014. Organizations all perceive themselves as "average" while operating at vastly different capability levels, so they make poor investment decisions and misalign expectations. The matrix exists to make honest self-assessment and cross-company comparison possible.

The headline claim (VirtusLab blog, *"AI Works Great — But Only at Maturity Level Four"*): **most companies sit at L1–L2 and conclude AI doesn't work; AI works great at L4.** The gap is not model quality but the infrastructure around the model.

Provenance claimed: the April 2026 version accumulated "sixty practices, four perspectives, and five levels" after "dozens of engagements from startups to regulated enterprises" — "based on patterns that actually worked or failed in existing companies, not theory."

## Structure

**4 perspectives × 4 capabilities each = 16 capabilities**, every capability scored across **5 levels**. Each level states **Must** criteria (typically 2–3) and **Should** criteria (typically 2).

| Perspective | Capabilities |
|---|---|
| **Development** — how developers work with AI day-to-day | coding-agent-usage · context-engineering · code-review-quality · testing-strategy |
| **Delivery Management** — how generated code reaches production | ci-cd-pipeline · merge-deploy · metrics · governance-compliance |
| **Organization** — governance, accountability, roles, compliance | ai-adoption-model · knowledge-management · team-structure-roles · tech-debt-modernization |
| **Infrastructure** — the technical foundations agents run on | agent-runtime-sandboxing · mcp-tool-integration · build-system · observability-feedback-loop |

### The five levels

- **L1 Ad-hoc** — "Copilot autocomplete, sidebar chat, the agent only sees the open file. Zero instruction files, zero MCP, README last updated eighteen months ago." Manual review, sub-40% coverage, flaky tests ignored. AI fundamentally cannot work well here.
- **L2 Guided** — instruction files and agentic tools adopted by ~half the team; basic agent-assisted review and unit-test generation; flaky tests isolated. Governance still outdated, agent context still fragmented. Transformation is announced more than achieved.
- **L3 Systematic** — CLI agents as the primary interface; structured context via MCP (architecture, ownership, SLAs); conventions written as agent-parseable rules; test reliability >90%; searchable audit trails. **Break-even — real ROI begins here.**
- **L4 Optimized** — unattended one-shot agents; multi-channel invocation (Slack, CLI, web, PagerDuty); 3–5 parallel sessions per developer; automated green/yellow/red evaluation with auto-merge; background continuous modernization; mutation testing. **"Green means merge — no human needed."** The realistic ceiling for most organizations.
- **L5 Autonomous** — multi-agent orchestration with planner-worker hierarchies; 100+ parallel agents, 1,000+ commits/week without manual dispatch; persistent agent identity and memory; production telemetry auto-updates agent context; self-healing test suites; human review limited to architectural decisions. "Today, a handful of companies do it" — mostly Bay Area, extraordinary budgets.

## The full criteria matrix

### Perspective: Development

**Coding Agent Usage**
- *L1* — Must: ≥1 AI coding assistant (Copilot, Cursor, Claude Code) installed and active for ≥1 developer; AI autocomplete or chat used ≥1×/week by the team. Should: AI chat available in the IDE sidebar; team has experimented on non-critical tasks.
- *L2* — Must: ≥1 agentic IDE (Cursor, Windsurf, Claude Code) used by 50%+ of the team; `CLAUDE.md` / `.cursorrules` or equivalent instruction file in **100% of active repositories**; agents operate in agentic/YOLO mode (multi-step edits without per-step approval). Should: developers use ≥2 AI tools in parallel; instruction files reviewed quarterly.
- *L3* — Must: CLI agents (Claude Code, Codex) are the **primary** coding interface for 50%+ of feature work; per-team or per-repo rules files maintained under code review; coding conventions written as **explicit, agent-parseable rules**. Should: agent usage tracked per developer and repo; instruction files follow a standardized template.
- *L4* — Must: unattended agents (Stripe "Minions" model, Cursor Automations) execute tasks without a developer present; agents invocable from ≥2 channels (Slack, CLI, web, PagerDuty); each developer runs **3–5 parallel agent sessions**. Should: agent task-completion rate without human intervention >60%; invocation produces a PR within a defined SLA.
- *L5* — Must: multi-agent orchestration (planner-worker hierarchy) in production; fleet sustains **100+ concurrent agents**; fleet produces **1,000+ commits/week** without manual dispatch. Should: planner agents decompose epics autonomously; fleet self-recovers from 90%+ of error cases without human escalation.

**Context Engineering**
- *L1* — Must: the agent can read the file(s) being worked on; developers can supply project context when needed. Should: a README exists (may be incomplete); context pasted manually into chat.
- *L2* — Must: `CLAUDE.md` or equivalent with project description, tech stack, top conventions; a written coding-conventions document referenced from the instruction files; instruction files **committed to the repo** (not local-only). Should: `CLAUDE.md` includes explicit prohibitions; instruction files reviewed in the standard PR process.
- *L3* — Must: **MCP servers provide structured context** (architecture, ownership, SLAs); context organized across ≥3 of the 5 levels — System, Code, Org, Historical, Operational; **token-budget management** implemented. Should: context sources versioned and tested; a budgeting policy defines priority order.
- *L4* — Must: the organization **pushes** context to agents automatically (BYOC — Bring Your Own Context); a knowledge graph (Graph Buddy, CodeTale, or equivalent) integrated with the agent context pipeline; ticket-to-spec automation generates acceptance tests from requirements without manual writing. Should: context push triggers on repository events; knowledge graph covers 80%+ of active repos.
- *L5* — Must: agents maintain **persistent identity and memory across sessions** (Beads / Git-backed); production telemetry feeds back into agent context automatically; agents detect stale documentation and update it unprompted. Should: agent memory persists architectural decisions; self-healing context updates validated by tests.

**Code Review & Quality**
- *L1* — Must: all code human-reviewed before merge; basic CI checks run. Should: review turnaround tracked; team aware that "AI-generated code has 1.7× more issues and 2.74× more security vulnerabilities."
- *L2* — Must: an AI-assisted review tool (CodeRabbit, Qodo, or equivalent) active on all repos; linter rules configured and run in CI on every PR; **PRs clearly indicate whether code is AI-generated or AI-assisted**. Should: AI review suggestions triaged; linter config committed and versioned.
- *L3* — Must: an AI review agent runs as **first-pass reviewer on every PR** before human review; **lint rules enforce architectural standards**; ≥3 architectural guardrail rules created from past bugs or incidents. Should: findings categorized by severity; new lint rules proposed automatically.
- *L4* — Must: automated **Green/Yellow/Red classification** on every PR; Green PRs **auto-merge without human review**; auto-approve rate target of 60%+ Green tracked and reported. Should: Yellow PRs reviewed within 1 hour; classification accuracy validated monthly.
- *L5* — Must: the agent fleet **self-reviews** (error-fix-converge loop) before submitting for merge; human review limited to Red (architectural decisions only); continuous auto-refactoring runs in the background. Should: self-review catches 90%+ of what a human reviewer would find; auto-refactor PRs tracked separately.

**Testing Strategy**
- *L1* — Must: an automated test suite exists and runs; the team writes and maintains its own tests. Should: team aware of flaky-test impact ("16% of dev time," Google data); AI-generated tests reviewed for circular testing.
- *L2* — Must: agents generate unit tests, **humans write acceptance tests**; a flaky-test quarantine process is active; humans define expected results for important paths. Should: flaky count tracked weekly; quarantined tests have a resolution SLA.
- *L3* — Must: expected results **derived from requirements/specs**; acceptance tests auto-generated from ticket requirements; incremental test selection runs only tests affected by changed code paths. Should: oracle reliability reviewed per service; generation includes edge cases.
- *L4* — Must: **a failing test reliably indicates a real defect**; agents iterate tests to green in an isolated **sandbox CI** without blocking the team queue; **mutation testing** validates that tests catch real defects. Should: sandbox iteration count tracked; mutation kill rate >80%.
- *L5* — Must: **self-healing test suite** (agent detects broken tests, diagnoses root cause, fixes); production logs automatically generate regression tests for observed failures; agents detect edge cases, write tests, fix bugs, and ship. Should: self-healing updates validated by mutation testing; production-to-test pipeline latency <1 hour.

### Perspective: Delivery Management

**CI/CD Pipeline**
- *L1* — a CI pipeline runs on pull requests; CI results reported after the pipeline completes.
- *L2* — CI completes in **<10 min** (median); build caching implemented (dependency + artifact cache); dedicated CI runners per team (no single shared queue).
- *L3* — CI **<5 min**; remote caching (Bazel remote cache, EngFlow, Gradle Enterprise); incremental builds run only changed modules/fragments.
- *L4* — CI **<2 min**; ephemeral sandbox environments spin up in **<10 s**; agent sandbox CI supports **50+ iteration attempts in 5 minutes** without blocking the team CI queue.
- *L5* — **sub-minute** feedback for standard changes; CI **auto-scales runner capacity based on agent load**; production feedback loop auto-adjusts the CI test suite.

**Merge & Deploy**
- *L1* — PRs reviewed before merge; the team ships PRs regularly.
- *L2* — merge queue implemented (GitHub merge queue, Mergify, equivalent); auto-rebase enabled for PRs targeting main; CD pipeline includes ≥1 gate (tests, security scan, approval).
- *L3* — policy-based merge rules enforced (OPA, branch protection); deterministic merge ordering with conflict detection; PRs require **max 2 CI rounds** before merge (Stripe benchmark).
- *L4* — Green-classified PRs **auto-merge and auto-deploy**; throughput **>50 PRs/day**; canary or progressive deployment automated.
- *L5* — **1,000+ merges/week**; full autonomous pipeline (agent produces PR → CI passes → merge → deploy → observe, no human in the loop); **rollback is agent-driven** (agent detects regression, reverts, opens a fix PR).

**Metrics**
- *L1* — delivery tracked with at least basic metrics; standard delivery metrics in place (AI-specific ones come later).
- *L2* — **DORA** tracked consistently with a dashboard; AI tool license count vs. active usage rate measured; PR throughput per developer tracked.
- *L3* — **ITS (Iterations-to-Success)** tracked, target **1–3**; **CPI (Cost-per-Iteration)** tracked, target **<$0.50**; CI feedback latency tracked (push → result).
- *L4* — **test-oracle reliability** measured on a dashboard; **auto-approve rate** tracked, target **>60%**; merge-queue wait time tracked, target **<10 min**.
- *L5* — **cost-per-feature** tracked (not cost-per-PR), aggregating agent + CI + review costs per delivered feature; **business-value throughput** is the primary metric (features/week, not PRs/week).

**Governance & Compliance**
- *L1* — the team knows which AI tools are in use; AI-generated code follows the normal review/merge process.
- *L2* — an **official AI tool policy** exists and is communicated; basic audit tracking (which developers use which tools); **EU AI Act** awareness briefing conducted.
- *L3* — **minimum viable audit trail per AI-assisted change**: model identifier, timestamp, context description, human approver; **policy-as-code** enforces compliance in CI (OPA); compliance gates run on every PR to in-scope repos.
- *L4* — **full provenance per change**: model version, prompt context, agent session ID, iteration count; automated compliance checks on every merge; **AI-generated code distinguishable from human-written code in version control**.
- *L5* — **continuous compliance** (agent monitors regulatory changes — EU AI Act, SOC2 — and proposes policy updates); **self-documenting audit trail** (agent decisions include reasoning, not just outcomes); enterprise-grade **RBAC per agent** (Stripe Toolshed model: each agent scoped).

### Perspective: Organization

**AI Adoption Model**
- *L1* — Must: AI tools adopted (licenses acquired); adoption tracked informally. Should: some developers experimenting; no outright ban.
- *L2* — Must: 2–3 pilot teams with explicit goals; an internal champion identified **with allocated time**; pilot metrics defined and tracked. Should: results shared broadly; champion has leadership access.
- *L3* — Must: a **platform team owns AI tooling**; the Internal Developer Platform includes an AI layer; standardized agent setup per team. Should: onboarding <30 minutes; platform tracks adoption breadth.
- *L4* — Must: **80%+ daily AI tool usage**; agent-fleet management recognized as a function; the developer role shifted to **supervision**. Should: "span of control" metric tracked; industry benchmarking conducted.
- *L5* — Must: centralized agent orchestration exists; developer as **"human-at-the-wheel"**; the organization optimized for agent throughput. Should: orchestration handles scheduling/allocation/recovery; agent utilization measured.

**Knowledge Management**
- *L1* — Must: the team has working system knowledge; onboarding includes a README or equivalent. Should: tribal knowledge recognized as a risk; informal sharing exists.
- *L2* — Must: a documentation refresh is active with measurable progress; **ADRs written for significant decisions**; a written onboarding path exists. Should: ADRs indexed/searchable; onboarding validated by a new hire.
- *L3* — Must: **documentation treated as engineering infrastructure**; lint rules enforce doc conventions; an operational knowledge graph exists. Should: freshness tracked (90-day flag); graph integrated with agent context.
- *L4* — Must: MCP servers **auto-feed** agents; unclear tickets auto-expanded to specs; agents auto-update docs on code changes. Should: "Context Fabric" covers 80%+ of repos; doc PRs merged within 24 h.
- *L5* — Must: the knowledge base is **self-evolving**; agents detect/update/validate stale context autonomously; organizational memory is **Git-backed and agent-readable**. Should: freshness score >95%; updates validated against the codebase.

**Team Structure & Roles**
- *L1* — Must: standard roles (dev, QA, PM); seniors review and fix AI-generated code. Should: team open to experimentation; informal champion present.
- *L2* — Must: an **AI champion per team** with allocated time; a **context engineer** role (initial); developer training on agent interaction conducted. Should: champion shares learnings regularly; training documented for new hires.
- *L3* — Must: a Platform Engineer responsible for AI tooling; **Context Engineer as a full dedicated role**; the team primarily *evaluates* AI code. Should: role definitions updated for AI; hiring criteria include tool proficiency.
- *L4* — Must: the developer formally defined as **"manager of an agent fleet"**; **span of control measured**; performance evaluation includes supervision effectiveness. Should: span targets per role; supervision training in onboarding.
- *L5* — Must: an **Agentic Engineer** role combining orchestration + supervision + architecture; the **PEV loop** is the standard workflow; **non-coders contribute via agents**. Should: a career ladder exists; non-coder contribution rate tracked.

**Tech Debt & Modernization**
- *L1* — Must: the team is aware of main debt areas; legacy systems kept stable. Should: debt enumerated; a migration backlog exists.
- *L2* — Must: debt categorized and prioritized; manual migration attempted or in progress; **OpenRewrite** evaluated or adopted. Should: debt reduction allocated in sprints; attempts documented with lessons.
- *L3* — Must: **agents work on debt reduction in the background**; library bumps/upgrades automated; OpenRewrite + agent systematic refactoring. Should: agent PRs follow standard review; dependency freshness tracked.
- *L4* — Must: **previously uneconomical projects now modernized by agents at low cost**; cross-repo migrations operative; major-version migrations agent-driven. Should: cost-per-migration tracked and decreasing; migrations meet defined SLAs.
- *L5* — Must: tech debt at a **near-zero steady state**; the agent fleet maintains/upgrades/patches 24/7; **CVE remediation fully autonomous**. Should: critical CVE fix deployed <24 h; debt score stable/improving for 6+ months.

### Perspective: Infrastructure

**Agent Runtime & Sandboxing**
- *L1* — agents execute in the developer's **local environment** with filesystem and shell access; access control is coarse-grained (all or none).
- *L2* — dedicated development environments separate from the primary workspace; basic sandboxing via Docker or equivalent; credentials scoped per project rather than org-wide.
- *L3* — isolated agent environments (**devbox model**) prevent cross-project access; **pre-warmed containers** with the codebase at HEAD and dependencies; network isolation prevents production access.
- *L4* — **ephemeral devboxes spin up in <10 s**, pre-loaded with codebase, dependencies, and MCP tools; **kernel-level policy enforcement** restricts agent actions via syscall filtering.
- *L5* — dedicated compute infrastructure for the agent fleet, separate from workstations; **auto-scaling** with load and business hours; each agent in a fully isolated environment or managed resource pool.

**MCP & Tool Integration**
- *L1* — agents use built-in tools only and rely on general/built-in knowledge; integrations performed manually by copy-paste.
- *L2* — **1–3 basic MCP servers** configured (Git, Jira, documentation); manual per-developer setup with a documented process; basic tool authorization.
- *L3* — a **centralized MCP platform** manages server provisioning and lifecycle; **domain-specific servers** (Architecture, Ownership, SLA MCPs); **RBAC** controls agent access to specific MCP tools.
- *L4* — **Toolshed model: "400+ tools behind one MCP"** (Stripe); **agent discovery** — agents query available tools at runtime; MCP governance covers lifecycle, versioning, audit logging.
- *L5* — MCP as a **bidirectional nervous system** with contextual flow; full production loop *Production → MCP → Agent → Code → Deploy*; **Agent-to-Agent Protocol** combined with MCP for multi-agent coordination.

**Build System**
- *L1* — a build system with default configuration; full rebuild on each change; CI on a shared queue.
- *L2* — build caching (dependency + compilation); parallel build steps (concurrent test/lint); dedicated CI resources per team.
- *L3* — an **advanced build system** (Bazel, Buck2, Pants); **remote execution** distributes build steps across machines; incremental builds run only changed targets.
- *L4* — any change gets build feedback in **<2 min**; **agent-specific build profiles** optimize for fast iteration feedback; the build system pre-caches likely subsequent builds.
- *L5* — the build is a **near-instantaneous commodity** for agents; the codebase is structured into self-contained modules eliminating bottlenecks; disk I/O optimized for concurrent agent workloads.

**Observability & Feedback Loop**
- *L1* — basic application logging; alerting fires on errors; production feedback not connected to development priorities.
- *L2* — **structured logging** (JSON, consistent fields); basic **OpenTelemetry** instrumentation; post-deploy monitoring checks after each deployment.
- *L3* — a full observability stack (OpenTelemetry + Grafana/Datadog); production metrics in accessible dashboards; **incident data available as agent context**.
- *L4* — production anomalies **auto-create tickets that trigger agent investigation**; self-healing for known patterns; infrastructure recommends code changes based on production data.
- *L5* — the **full production-to-agent loop** runs without human intervention — anomaly detection, investigation, fix, test, deploy; novel anomalies escalated to humans **with full investigation context**.

## The practice-guide layer

Beyond the matrix, the site publishes a **practice guide per cell-criterion** at `/guides/<perspective>/<slug>`. The sitemap enumerates **240 guides — exactly 60 per perspective** (the "sixty practices" figure in VirtusLab's own copy appears to count **per perspective**, i.e. 4 capabilities × 5 levels × ~3 criteria).

Each guide page follows a fixed template: **What It Is** (and how it differs from the lower-level approach) · **Why It Matters** (4–5 bullets of business value) · **Getting Started** (5–6 numbered implementation steps) · **Common Pitfalls** (5+ failure modes) · **Persona Examples** (3–4 named roles with a scenario and recommended actions) · **Links**. Metadata: maturity level, capability area, perspective.

The guide slugs are the criteria restated as memorable phrases — including the L1 anti-patterns. Development perspective, all 60:

```
3-5-parallel-agents-per-developer
5-level-context-system-code-org-historical-operational
acceptance-tests-from-tickets-autonomous-requirements
agent-aware-coding-conventions-explicit-implicit
agent-detects-edge-case-writes-test-fixes-bug-ships
agent-fleet-self-reviews-cursor-model-error-fix-converge
agent-generated-unit-tests-human-acceptance-tests
agent-in-ide-with-yolo-mode
agent-instruction-files-in-repo-60k-repos-on-github
agent-iterates-tests-to-green-in-sandbox-doesn-t-block-team-
ai-assisted-review-suggestions
ai-review-agent-as-first-pass
ai-tests-circularly-test-what-code-does-not-what-it-should-d
architecture-guardrails-bug-codify-lint-rule
autonomous-requirements-ticket-spec-acceptance-tests-auto
basic-linter-rules
byoc-org-pushes-context-to-the-agent
chat-in-sidebar-ad-hoc-questions
claude-md-cursorrules-in-repo
claude-md-with-basic-project-info
cli-agents-claude-code-codex-as-primary
context-budgeting-token-economy
continuous-auto-refactoring-in-background
copilot-autocomplete
copilot-claude-code-in-parallel
diff-awareness-reviewer-knows-it-s-ai-code
flaky-test-quarantine
flaky-tests-16-of-dev-time-google-data
green-auto-merge-fully-algorithmic
green-yellow-red-auto-evaluation
human-review-only-for-red-architectural
hundreds-of-agents-on-codebase-1000-commits-h
incremental-test-selection-only-changed-paths
knowledge-graph-graph-buddy-codetale
lint-as-architecture-standards-enforced-rules
manual-review-of-100-code
mcp-servers-architecture-ownership-sla
multi-agent-orchestration-gas-town-custom
mutation-testing-agent-validation
no-distinction-between-ai-vs-human-code
no-integration-with-codebase-context
one-shot-unattended-agents-stripe-minions-model
persistent-agent-identity-memory-beads-git
planner-worker-hierarchy
policy-based-auto-approval-60-green-target
production-logs-auto-generated-regression-tests
production-telemetry-context-auto-update
readme-outdated-for-6-months
review-bottleneck-2h-waiting-for-feedback
rules-files-per-team-per-repo
self-healing-context-agent-detects-stale-docs-updates
self-healing-test-suite
slack-cli-web-invocation-pr
test-oracle-stabilization
tests-written-manually-coverage-40
tors-90-test-oracle-reliability-score
tors-95
tribal-knowledge-in-people-s-heads
written-coding-conventions
zero-context-agent-sees-only-the-open-file
```

The delivery / organization / infrastructure slug sets (60 each) follow the same pattern and are re-derivable from `https://visdom-maturity-matrix.virtuslab.com/sitemap.xml`. Representative delivery examples: `ci-2-minutes`, `green-auto-merge-auto-deploy`, `rollback-is-agent-driven`, `its-iterations-to-success-target-1-3`, `cpi-cost-per-iteration-target-0-50`, `max-2-ci-rounds-per-pr-stripe-benchmark`, `enterprise-grade-rbac-per-agent-stripe-toolshed-model-400-mc`, `policy-as-code`, `minimum-viable-audit-trail-model-timestamp-context-approver`, `zero-audit-trail`, `shadow-ai-devs-with-private-subscriptions`, `how-much-did-we-save-silence`.

## Other site surfaces

`/workshop` (+ `/workshop/focus`) — a facilitated self-assessment flow, the intended delivery vehicle: a team scores itself per capability and picks focus areas. `/matrix` — the browsable grid. `/radar` — an "AI Radar." `/offer` and `/ai-sdlc-advisory` — VirtusLab's consulting engagement. `/changelog` and `/blog` (monthly, 2026-04 → 2026-08) — the matrix is versioned and actively revised.

## Notes on capture completeness

The four perspective pages yielded the complete 16-capability × 5-level criteria set above (Must/Should where the source distinguishes them; the Delivery page states criteria without the Must/Should split). The `/workshop` and `/matrix` landing pages are client-rendered and returned only navigation chrome; the individual practice-guide bodies (240 pages) were not captured — only their slugs and template structure.
