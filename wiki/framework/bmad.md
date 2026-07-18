---
type: framework
source_url: "https://github.com/bmad-code-org/BMAD-METHOD"
docs_url: "https://docs.bmad-method.org/"
sources: "bmad-code-org/BMAD-METHOD README + docs.bmad-method.org (v6.10.0, 2026)"
raw: ["../../raw/bmad/2026-07-04-bmad-method-framework.md"]
updated: 2026-07-04
---

# BMAD-METHOD

**BMAD** — "**B**reakthrough **M**ethod for **A**gile **A**I **D**riven Development" (the docs
also gloss it "Build More Architect Dreams") by **bmad-code-org** — is the wiki's **most
lifecycle-complete and most role-oriented framework**: an AI-driven agile method built around a
cast of **named expert personas** (Analyst, PM, Architect, Developer…) who *facilitate* the
human through a scale-adaptive pipeline from idea to shipped code. Install: `npx bmad-method
install` (Node.js 20.12+). ~50K★, MIT. Works in Claude Code / Cursor / Copilot, with planning
also available as Gemini Gems / ChatGPT GPTs ("web bundles").

Its stated stance is the sharpest articulation in the wiki of *agent-as-collaborator*:
"traditional AI tools do the thinking for you, producing average results. BMad agents and
facilitated workflows act as **expert collaborators** who guide you through a structured
process." Concretely, its workflows enforce a **facilitator** rule — "YOU ARE A FACILITATOR,
not a content generator; NEVER generate content without user input" — so planning is a
grilling dialogue (see [[pattern-grilling]]), not autogeneration.

## What makes BMAD different

Every other framework here exposes commands or skills; BMAD is the first to organize the whole
lifecycle around **distinct named personas with persistent character** — Mary the analyst,
John the PM, Winston the architect, Amelia the engineer — each carrying its own influences and
principles. That is its signature contribution ([[pattern-persona-agents]]), and it enables
[[pattern-persona-agents|Party Mode]], where the personas debate a decision as a roundtable.
Two more distinctions:

- **Scale-adaptive ceremony.** BMAD sizes the process to the work — a one-line fix skips
  straight to code (Quick Flow), an enterprise system runs the full PRD → architecture →
  epics → stories pipeline. The planning depth is a dial, not a fixed gate ([[pattern-scale-adaptive-planning]]).
- **Context-engineered story files.** Each unit of work is a self-contained [[artifact-story|story file]]
  that "embeds architectural decisions, dependency context, and project conventions directly
  into the implementation artifact," so the dev agent never loses context ([[pattern-context-engineering]]).

## The four-phase lifecycle (+ Quick Flow)

"The BMAD Method follows 4 distinct phases in sequence," plus a parallel Quick Flow track for
small work. Each phase's output "becomes context for the next." The source tree mirrors the
phases (`src/bmm-skills/{1-analysis,2-plan-workflows,3-solutioning,4-implementation}/`):

| Phase | Owning persona(s) | Stage |
|-------|-------------------|-------|
| 1. Analysis *(optional)* — explore & validate the idea | [[bmad-analyst]] · [[bmad-tech-writer]] | [[stage-align]] |
| 2. Planning — define what to build & for whom | [[bmad-pm]] · [[bmad-ux-designer]] | [[stage-specify]] |
| 3. Solutioning — decide how, break into stories | [[bmad-architect]] · [[bmad-pm]] | [[stage-plan]] |
| 4. Implementation — build it, one story at a time | [[bmad-dev]] | [[stage-implement]] · [[stage-review]] |
| Quick Flow *(parallel)* — skip 1–3 for small work | [[bmad-dev]] | [[stage-implement]] |

Like [[speckit]], **BMAD core ships no deploy/ship step**; it closes each epic with a
[[bmad-retrospective|retrospective]] (a learning close-out, see [[stage-release]]) rather than
a release to production.

## Capabilities

### Named agents (personas) — one page each

The six BMM personas ("BMad ships six named agents, each anchored to a phase"). Each is a skill
(`bmad-agent-*`) invoked by name; each dispatches a menu of workflow skills:

- [[bmad-analyst]] — **Mary** 📊; Analysis. Brainstorming, research, product briefs, PRFAQ, brownfield docs.
- [[bmad-tech-writer]] — **Paige** 📚; Analysis. Project documentation, diagrams, doc validation.
- [[bmad-pm]] — **John** 📋; Planning. PRD, epics & stories, readiness, course-correction.
- [[bmad-ux-designer]] — **Sally** 🎨; Planning. UX design specifications.
- [[bmad-architect]] — **Winston** 🏗️; Solutioning. The architecture spine.
- [[bmad-dev]] — **Amelia** 💻; Implementation. Story creation, dev, code review, sprints, retros (absorbed the classic SM + QA roles).

> **Conflict (version drift):** classic v4/v5 BMAD shipped separate **Scrum Master (Bob)**,
> **Product Owner (Sarah)**, **BMad Master**, and **BMad Orchestrator** agents. v6 folds these
> in — SM/QA duties → the Developer ([[bmad-dev]]), epic breakdown → the PM ([[bmad-pm]]),
> orchestration → the Party-Mode *skill*. Some secondary sources (e.g. DeepWiki) still list a
> `sm`/"Bob" agent; the v6 docs are canonical at "six named agents." This wiki follows v6.

### Workflow skills — one page each

Grouped by phase; each `implements:` a canonical stage:

- **Analysis** — [[bmad-brainstorming]], [[bmad-forge-idea]], [[bmad-research]], [[bmad-product-brief]], [[bmad-prfaq]], [[bmad-document-project]].
- **Planning** — [[bmad-prd]], [[bmad-ux]], [[bmad-spec]].
- **Solutioning** — [[bmad-architecture]], [[bmad-create-epics-and-stories]], [[bmad-check-implementation-readiness]].
- **Implementation** — [[bmad-sprint-planning]], [[bmad-create-story]], [[bmad-dev-story]], [[bmad-code-review]], [[bmad-correct-course]], [[bmad-retrospective]], [[bmad-quick-dev]].

### Core utility skills (mechanisms & tooling — catalogued, not paged)

Cross-phase `core-skills/` that back the paged capabilities rather than performing a lifecycle
stage themselves:

| Skill | Role |
|-------|------|
| `bmad-party-mode` | Summon multiple personas into one roundtable to debate a tradeoff — the [[pattern-persona-agents]] mechanism |
| `bmad-advanced-elicitation` | Push the LLM to reconsider its output (socratic / first-principles / pre-mortem / red-team) |
| `bmad-review-adversarial-general` · `bmad-review-edge-case-hunter` · `bmad-review-verification-gap` | The parallel review layers behind [[bmad-code-review]] ([[pattern-adversarial-review]], [[pattern-parallel-persona-review]]) |
| `bmad-checkpoint-preview` · `bmad-sprint-status` | Human-in-the-loop review aid; read-only sprint/risk summary |
| `bmad-generate-project-context` | Emit `project-context.md` (AI rules) — the [[pattern-context-engineering]] rules file |
| `bmad-qa-generate-e2e-tests` | Generate E2E tests for existing features (dispatched by [[bmad-dev]]) |
| `bmad-dev-auto` | Unattended one-iteration variant of [[bmad-quick-dev]] for an orchestrator |
| `bmad-shard-doc` | Split a large PRD/architecture by level-2 headings into focused files (sharding) |
| `bmad-help` · `bmad-customize` · `bmad-index-docs` | Routing, override authoring, doc indexing |

### Optional modules (expansion packs — catalogued, not paged)

Only **BMM** (+ shared `core`) installs by default; v6 "separated core functionality from
domain-specific modules for independent versioning." The rest are optional:

| Module | Code | What it adds |
|--------|------|-------------|
| BMad Builder | `bmb` | Meta-module: build custom agents / workflows / modules "from a conversation" |
| Creative Intelligence Suite | `cis` | 6 ideation personas (Carson, Dr. Quinn, Maya, Victor, Caravaggio, Sophia); SCAMPER, TRIZ |
| Test Architect | `tea` | **Murat** — risk-based testing, ATDD, NFR audits, release **gate** decisions, requirement-to-test traceability (the quality-review depth BMM core lacks) |
| Game Dev Studio | `gds` / BMGD | Game personas for Unity / Unreal / Godot / Phaser; GDD generation; 21+ game types |
| Whiteport Design Studio | `wds` | Design-first UX methodology (Saga, Freya, Mimir) |
| BMad Loop | `bmad-loop` | Deterministic Python unattended dev loop with adversarial review (no personas) |

> The **TEA** module's Murat is BMAD's answer to a dedicated quality reviewer — it clusters
> with [[addy-security-auditor]] / [[addy-test-engineer]] on the [[stage-review]] quality-gate
> side, but ships outside core, so it is catalogued here rather than paged.

## Artifacts produced

- [[artifact-story]] — the signature: a context-rich `story-[slug].md` (AC + tasks + Dev Notes + Dev Agent Record) that is the atomic unit of implementation.
- [[artifact-architecture]] — `ARCHITECTURE-SPINE.md`, a lean spine of *invariants only*.
- [[artifact-product-brief]] — `brief.md` (+ the PRFAQ variant), the pre-PRD scoping document.
- [[artifact-prd]] — `prd.md` (create/update/validate), the durable requirements spec.
- [[artifact-spec-md]] — the `SPEC.md` five-field kernel (Quick Flow's lightweight spec).
- [[artifact-design-md]] — `DESIGN.md` + `EXPERIENCE.md`, the UX design specification.
- [[artifact-research-md]] — market / domain / technical research reports.
- [[artifact-atomic-commit]] — working, tested code committed per story.
- [[artifact-review-report]] — the adversarial code-review findings.

## Patterns applied

- [[pattern-persona-agents]] — its signature: a distinct named expert persona per SDLC role, plus Party-Mode roundtables.
- [[pattern-scale-adaptive-planning]] — its second signature: size the ceremony to the work (Quick Flow → BMad Method → Enterprise; classic Levels 0–4).
- [[pattern-context-engineering]] — story files + `project-context.md` + `.memlog.md` keep agents fully contexted.
- [[pattern-spec-driven-development]] — PRD → architecture → stories drive the build.
- [[pattern-grilling]] — the facilitator stance: interrogate the human to decisions.
- [[pattern-plan-verification-loop]] — the implementation-readiness gate before code.
- [[pattern-adversarial-review]] — forge-idea and the "reviewer must find issues" code review.
- [[pattern-parallel-persona-review]] — the Blind Hunter / Edge Case Hunter / Acceptance Auditor review layers.
- [[pattern-fresh-context-subagents]] — one story at a time; code review in a fresh context / different LLM.
- [[pattern-test-driven-development]] — the Developer's test-first ("Kent Beck's TDD") discipline.
- [[pattern-vertical-slice]] — stories as independently shippable slices.

## See Also
- [[compound-engineering]] — Every's compounding loop; **the co-framework of the [[stage-learn]] stage**: BMAD's [[bmad-retrospective]] (human-facing learning close-out) and CE's [[ce-compound]] (machine-consumable [[artifact-solution-doc|solution corpus]]) are the two flavors that jointly promoted learning-capture out of [[stage-release]] into its own canonical stage. Also [[bmad-dev-story]] ↔ [[ce-work]], [[bmad-code-review]] ↔ [[ce-code-review]], [[bmad-check-implementation-readiness]] ↔ [[ce-doc-review]], [[bmad-brainstorming]] ↔ [[ce-ideate]].
- [[stage-align]], [[stage-specify]], [[stage-plan]], [[stage-implement]], [[stage-review]], [[stage-release]] — the canonical lifecycle this framework implements (its quality gate [[bmad-code-review]] lands in [[stage-review]]; it ships no functional [[stage-validate]] capability). Deepest coverage of the align/specify/plan front-end of any framework here.
- [[gsd]] — closest sibling: both are full-lifecycle, persona/subagent-driven, context-engineered. [[bmad-dev-story]] ↔ [[gsd-execute-phase]], [[bmad-check-implementation-readiness]] ↔ [[gsd-plan-checker]], [[bmad-code-review]] ↔ [[gsd-verifier]]. GSD carries the ship/deploy side BMAD core omits.
- [[addy-agent-skills]] — shares breadth and personas; [[bmad-code-review]] ↔ [[addy-code-review]], and Party-Mode ↔ Addy's [[pattern-parallel-persona-review]] `/ship` fan-out. Addy carries release/ops; BMAD carries the richer front-end.
- [[speckit]] — sibling that also stops before release; both gate plans ([[bmad-check-implementation-readiness]] ↔ [[speckit-analyze]]) and are spec-driven. SpecKit governs via a [[artifact-constitution]]; BMAD governs via personas + `project-context.md`.
- [[matt-pocock-skills]], [[openspec]] — share the specify/plan/execute clusters; see the stage pages.
