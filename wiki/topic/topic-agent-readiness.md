---
type: topic
sources: "Factory.ai — Agent Readiness (2026); VirtusLab — Visdom AI-Native SDLC Maturity Matrix (2026); wiki synthesis"
raw: ["../../raw/reference/2026-08-07-factory-agent-readiness.md", "../../raw/reference/2026-08-07-visdom-maturity-matrix.md"]
updated: 2026-08-07
---

# Topic: Agent readiness — scoring the repository (and the org) the agent has to work in

> **This page is a curated overlay, not an ontology node.** It gathers pages from across the wiki around one theme and links *out* to them; it stores no edges and changes no synthesis. See [CONVENTIONS §The topic layer](../CONVENTIONS.md#the-topic-layer-curated-overlays).

**The question this topic answers:** given a repository and a team, *what has to be true before an agent can work well here* — and how do you measure the gap and close it? Two public rubrics now answer this with scored, leveled checklists: **Factory's Agent Readiness** (repository-scoped, mechanically evaluated) and **VirtusLab's Visdom AI-Native SDLC Maturity Matrix** (organization-scoped, workshop-facilitated). This page frames what they are, threads their criteria through the wiki pages that already implement them, and records what they expose that the wiki lacks.

## The inversion — why this is a different axis

Every other namespace in this wiki answers **"what does the agent do"**: a [[gsd|framework]] ships capabilities that perform [[stage-implement|stages]], applying [[pattern-test-driven-development|patterns]] on a [[claude-code|harness]] inside a [[sandcastle|runtime]]. The process layer acts *on* a codebase; the codebase itself has never been a node.

Readiness rubrics run the arrow backwards. They score **the substrate the agent acts on** — the repo's linters, tests, docs, CI latency, sandboxes, audit trails — and treat agent performance as a *dependent variable* of it. Factory states the thesis flatly:

> "The agent is not broken. The environment is."

That is a genuinely different claim from anything else here. GSD's answer to a failing agent is a better process; Superpowers' is a stricter skill; Agent OS's is a better guide layer. The readiness answer is: **your repo scores Level 2, and no process will save you until it scores 3.**

## It closes the gap [[topic-harness-engineering]] flagged

[[topic-harness-engineering]] ends by naming two Fowler concepts with **no home in the wiki**: *harnessability* ("how amenable a codebase is to harness controls, given its structure") and *ambient affordances* ("structural properties of the environment itself that make it legible, navigable, and tractable to agents").

These two rubrics are exactly that gap, operationalized and scored. Where Fowler names harnessability as a property, Factory and Visdom turn it into 100+ binary signals and a 16-capability grid. Read the two topics as a pair:

- [[topic-harness-engineering]] — the **controls you build** around the model (guides, sensors, the steering loop).
- **This page** — the **substrate those controls need**, and how far along it you actually are.

A cheap way to hold the relationship: a guide tells the agent the convention; a sensor catches the violation; **readiness is whether a sensor is even possible here.** You cannot have a computational control without a test suite, a lint config, and a CI job that finishes before the agent gives up.

## The two rubrics compared

| | **Factory — Agent Readiness** | **Visdom — AI-Native SDLC Maturity Matrix** |
|---|---|---|
| Author | Factory.ai (vendor, ships [[factory-droid]]) | VirtusLab (consultancy) |
| Scope | **one repository** (+ org roll-up) | **the whole organization** — dev, delivery, org design, infra |
| Structure | 8–9 **pillars** × 5 levels, "100+ signals" | 4 **perspectives** × 4 capabilities × 5 levels, 240 practice guides |
| Criteria | **binary pass/fail**, machine-evaluated, per sub-application | **Must / Should** prose criteria, human-assessed |
| Delivery | `/readiness-report` in the Droid CLI + web dashboard + API | a facilitated **workshop** + browsable matrix + per-practice guides |
| Remediation | `/readiness-fix` — an agent session that implements the fixes | consulting engagement; each practice has a "Getting Started" guide |
| Advancement | ≥80% of criteria at a level unlocks the next | levels are descriptive; L3 is break-even, L4 the realistic ceiling |
| Covers people? | no — repo artifacts only | **yes** — roles, champions, career ladder, EU AI Act compliance |
| Determinism | grounded against the previous report; variance 7% → 0.6% | n/a (human judgment) |

They are complements, not competitors. Factory answers *"is this repo ready?"* and can answer it every night in CI. Visdom answers *"is this company ready?"* and needs a room and a facilitator. Factory's nine pillars map almost entirely into Visdom's Development + Infrastructure perspectives; Visdom's Organization perspective has no Factory counterpart at all.

## The shared spine: five levels, ad-hoc → autonomous

Both land independently on the same ladder, and it is worth naming because it is now the field's default vocabulary:

| | Factory | Visdom |
|---|---|---|
| 1 | Functional — basic tooling exists | Ad-hoc — agent sees only the open file |
| 2 | Documented — docs + process automation | Guided — instruction files, half the team on agentic tools |
| 3 | Standardized — enforced through automation | Systematic — MCP context, lint-as-architecture. **Break-even** |
| 4 | Optimized — fast feedback, measured | Optimized — unattended agents, auto-merge. **"Green means merge"** |
| 5 | Autonomous — self-improving systems | Autonomous — 100+ agents, 1,000+ commits/week |

Both put the **payoff at L3–L4, not L1–L2** — Visdom's headline is that most companies sit at L1–L2, conclude AI doesn't work, and are measuring the environment rather than the model. Factory names L3 as the minimum bar for production-grade autonomy (agents handling bug fixes, tests, dependency upgrades unattended).

The interesting structural claim is that **the ladder is gated, not additive**. Factory enforces it mechanically (80% of a level unlocks the next); Visdom enforces it rhetorically (L4 practices are wasted on an L2 substrate). Buying more agent seats at L2 buys nothing.

## Where the criteria already live in this wiki

The rubrics' criteria are not new demands — most are things the wiki already documents as capabilities, patterns, or artifacts. The value of the mapping is showing *which pillar each page serves*, and where nothing exists.

**Style & Validation / Code Review & Quality**
- [[gstack-health]] — the standing type/lint/tests/dead-code dashboard; the closest thing here to a readiness score already.
- [[pattern-edit-guardrails]] — hooks and permission modes; Visdom's "lint-as-architecture" and "architecture guardrails: bug → codify lint rule" are the same move, promoting an incident into a computational control.
- [[addy-code-review]] · [[ce-code-review]] · [[gstack-review]] · [[bmad-code-review]] — the review cluster. Visdom L3 requires an AI reviewer as **first-pass on every PR**; L4 requires Green/Yellow/Red auto-classification with **auto-merge on Green**. No framework here goes that far — the wiki's reviews all report to a human.

**Testing**
- [[pattern-test-driven-development]] ([[mp-tdd]], [[addy-tdd]], [[speckit-implement]]) — L1–L2 territory in both rubrics.
- [[stage-validate]] and the browser-QA sensors ([[gstack-qa]], [[ce-dogfood]], [[addy-browser-testing]]) — Visdom's L2 "agents generate unit tests, humans write acceptance tests."
- **Not covered anywhere in the wiki:** mutation testing, test-oracle reliability (TORS), flaky-test quarantine, incremental test selection. Visdom makes these L3–L4 *musts*. See the gaps section.

**Documentation & Context**
- [[pattern-context-engineering]] — the flagship. Visdom's Context Engineering capability is this pattern turned into a five-level ladder (L2 `CLAUDE.md` committed to the repo → L3 MCP servers for architecture/ownership/SLAs + token budgeting → L4 org *pushes* context (BYOC) + knowledge graph → L5 persistent agent memory).
- [[artifact-standards]] and the [[agent-os]] guide-layer commands ([[agent-os-inject-standards]], [[agent-os-index-standards]], [[agent-os-discover-standards]]) — the purest instance of Visdom L3's "coding conventions written as explicit, agent-parseable rules."
- [[artifact-constitution]] / [[pattern-project-constitution]] ([[speckit-constitution]]) — the gated form of the same.
- [[artifact-adr]] — a named Visdom L2 Knowledge-Management *must*.
- [[artifact-diataxis-docs]] ([[gstack-document-release]], [[gstack-document-generate]]) — doc coverage as a maintained artifact.

**Build System, CI/CD & Dev Environment**
- [[addy-ci-cd]] — quality-gate pipelines, [[pattern-shift-left]], [[pattern-feature-flags]].
- [[addy-git-workflow]] / [[pattern-trunk-based-development]] — Visdom's Merge & Deploy L2–L3 (merge queue, auto-rebase, policy-based merge rules).
- [[gstack-land-and-deploy]] · [[gstack-setup-deploy]] — the wiki's only genuine deploy step; Visdom L4's canary/progressive deployment is [[gstack-canary]].
- **CI *latency* is a hard criterion in Visdom** (<10 / <5 / <2 / sub-minute minutes by level) and appears nowhere in this wiki as a first-class concern.

**Agent Runtime & Sandboxing**
- This is the [[sandcastle|runtime]] layer, and it is the one place the wiki is *ahead* of the rubrics' vocabulary. Visdom's Infrastructure L3–L5 ladder (devbox isolation → ephemeral <10 s sandboxes with kernel-level syscall policy → dedicated auto-scaling fleet compute) is a maturity scale over exactly what [[sandcastle]] and [[warren]] provide, and what [[pattern-worktree-isolation]] and [[pattern-autonomous-loop]] describe.
- [[ce-worktree]] is the process-side floor of that ladder; [[pattern-wave-parallelism]] is Visdom's "3–5 parallel agent sessions per developer" (L4).

**Observability & Security**
- [[addy-observability]] — structured logging, RED metrics, OpenTelemetry; Visdom L2–L3 almost verbatim.
- [[ce-product-pulse]] · [[gstack-canary]] — post-release monitoring; the *start* of Visdom's L4 production→agent loop.
- [[addy-security]] · [[gstack-cso]] · [[ce-security-sentinel]] · [[addy-security-auditor]] — OWASP/STRIDE review. Factory's Security pillar is blunter and more structural: branch protection, secret scanning, CODEOWNERS.

**Tech Debt & Knowledge (the steering loop)**
- [[pattern-knowledge-compounding]] ([[ce-compound]], [[gstack-learn]], [[ce-compound-refresh]], [[artifact-solution-doc]]) and [[stage-learn]] — Visdom's Knowledge Management L4–L5 ("agents auto-update docs on code changes," "self-evolving knowledge base," "organizational memory Git-backed and agent-readable") is the same loop, scored.
- [[addy-deprecation]] · [[addy-code-simplification]] / [[ce-simplify-code]] — the debt side; Visdom L3 wants agents doing debt reduction **in the background**, which no framework here schedules.

## What the rubrics expose that the wiki has no page for

These are the honest gaps — criteria treated as load-bearing by both rubrics with no counterpart in any of the twelve frameworks documented here. Several are candidate future pattern pages:

1. **Test-suite trustworthiness as a measured property** — mutation testing, test-oracle reliability (TORS, target >90–95%), flaky-test quarantine with an SLA, incremental test selection. Visdom's L4 *must* is stated as "a failing test reliably indicates a real defect." The wiki has [[pattern-test-driven-development]] but nothing about whether the resulting suite can be trusted — which is precisely what an autonomous agent depends on.
2. **Feedback latency as a first-class budget** — CI under 2 minutes, sandbox CI absorbing 50+ agent iterations in 5 minutes without blocking the team queue. Every framework here assumes verification is free.
3. **Agent-economics metrics** — ITS (iterations-to-success, target 1–3), CPI (cost-per-iteration, target <$0.50), auto-approve rate, cost-per-feature. The wiki has [[pattern-measure-first]] for *code* performance and nothing for *agent* performance.
4. **Provenance and audit of AI-generated code** — model version, prompt context, session ID, iteration count per change; AI-vs-human code distinguishable in VCS; EU AI Act readiness. Nothing here records who (or what) wrote a change, though [[artifact-atomic-commit]] and [[artifact-pull-request]] are where it would live.
5. **Auto-merge on classification** — Visdom L4's "Green means merge, no human needed." Every review capability in this wiki reports to a human; none of them close the loop.
6. **Org design** — the Context Engineer role, the developer as "manager of an agent fleet," span-of-control as a tracked metric. Out of scope for a tooling wiki, but it is half of why Visdom's L4 organizations get results.

## What the wiki has that the rubrics don't

Worth stating so the mapping isn't read as one-directional. Both rubrics are almost entirely about **substrate and delivery**; neither has anything to say about the *front* of the lifecycle. There is no readiness criterion for [[stage-align]], [[stage-specify]], or [[stage-plan]] — no grilling, no spec quality, no plan verification, no [[pattern-scale-adaptive-planning]]. Visdom's closest touch is "ticket-to-spec automation" as an L4 context criterion.

That is a real blind spot: a repo can score Level 4 on every mechanical signal and still have agents building the wrong thing fluently. The wiki's [[stage-specify]] cluster (nine frameworks) is the counterweight, and the two bodies of knowledge are close to disjoint.

## Why this is an overlay and not a new namespace

The tempting move is to mint a `readiness`/`maturity-model` node type. Resist it, for now, on the wiki's own stated discipline (see [CONVENTIONS §The execution layer](../CONVENTIONS.md#the-execution-layer-runtimes) on parking premature abstraction):

- A rubric **performs no SDLC stage and ships no capability** — it is not a [[gsd|framework]]. It is an assessment instrument *about* the substrate.
- The instances are few and structurally similar; a comparison table on one page is still cheaper than a namespace with two members.
- Every criterion that matters already has a home in `pattern` / `artifact` / `capability`. The rubrics contribute *organization and scoring*, not new nodes.

**Graduation trigger — revisit if any of these fire:**

1. A **third and fourth substantively different rubric** arrives (evidence is already accumulating: [kodustech/agent-readiness](https://github.com/kodustech/agent-readiness), the open-source Factory alternative — 7 pillars, 39 automated checks, same 5 levels and 80% rule — plus agent-ready.org). Near-clones of the same ladder do **not** count; a genuinely different axis does.
2. Readiness criteria start being **implemented as capabilities** — Factory's `/readiness-report` and `/readiness-fix` are real Droid commands and are already ingestable as `capability` pages under a Factory framework. If two or more frameworks ship a repo-assessment capability, the wiki gains an evidenced cross-framework cluster and probably a `stage-assess` split candidate on [[stage-align]].
3. The **comparison table above stops scaling** — the same test that governs the [[claude-code|harness]] and [[sandcastle|runtime]] matrices.

Until then this page carries the whole layer, and the gaps listed above are tracked here rather than as stub nodes.

## Using this in practice

The useful synthesis is not "adopt one rubric" but the ordering both agree on. Roughly:

1. **Score honestly, mechanically, and repeatedly.** Factory's variance work (7% → 0.6% by grounding each run against the last) is the detail that makes an LLM-evaluated rubric usable as a metric rather than a vibe. A score you cannot trend is not a score.
2. **Fix the level you are on, not the level you want.** The 80% gate exists because L4 practices are inert on an L2 substrate — auto-merge without a trustworthy test suite is just faster breakage.
3. **Prefer criteria that become computational controls.** A lint rule, a pinned dependency, a `CLAUDE.md`, a CI gate — each converts a recurring human correction into something the agent gets for free forever, which is [[topic-harness-engineering]]'s steering loop with a scoreboard attached.
4. **Remediate with the agent.** `/readiness-fix` is the loop closing on itself: the agent improves the environment that determines how well the agent works. [[pattern-knowledge-compounding]] pointed at the substrate rather than at the solution corpus.

## See Also
- [[topic-harness-engineering]] — the sibling overlay: the controls you build *around* the model. This page is the substrate those controls require; it closes that page's flagged *harnessability / ambient affordances* gap.
- [[factory-droid]] — the harness that ships `/readiness-report` and `/readiness-fix`; the strongest candidate for turning this topic into evidenced capability pages.
- [[agent-os]] — the framework whose entire value proposition is the guide layer that Visdom's Context Engineering L2–L3 criteria describe.
- [[sandcastle]] · [[warren]] — the runtime layer that Visdom's Infrastructure perspective scores as a maturity ladder.
- [[stage-learn]] — the compounding loop the rubrics place at L4–L5.
- Factory.ai, *Agent Readiness* ([capture](https://github.com/pmackay/sdlc-wiki/blob/main/raw/reference/2026-08-07-factory-agent-readiness.md)) · VirtusLab, *Visdom AI-Native SDLC Maturity Matrix* ([capture](https://github.com/pmackay/sdlc-wiki/blob/main/raw/reference/2026-08-07-visdom-maturity-matrix.md)).
