---
source_url: https://docs.bmad-method.org/ ; https://github.com/bmad-code-org/BMAD-METHOD
collected: 2026-07-04
published: 2026-07-03 (v6.10.0)
---

# BMAD-METHOD (v6)

> Source capture for the sdlc-wiki ingest. Compiled from the official docs
> (docs.bmad-method.org), the GitHub repo (bmad-code-org/BMAD-METHOD, branch `main`,
> release v6.10.0), the official expansion-module repos, DeepWiki, and the repo's
> `SKILL.md` / `customize.toml` source files. Verbatim quotes marked with quotation marks.

## What it is

**BMAD** = "**B**reakthrough **M**ethod for **A**gile **A**I **D**riven Development" (the docs
also gloss the acronym as "Build More Architect Dreams"). An "AI-driven agile development
framework designed to function as an **expert collaborator** rather than replacing human
thinking." Tagline: "traditional AI tools do the thinking for you, producing average results.
BMad agents and facilitated workflows act as expert collaborators who guide you through a
structured process."

- **Install:** `npx bmad-method install` (prerelease: `npx bmad-method@next install`). Node.js 20.12+.
- **Version:** v6.10.0, released 2026-07-03. Stable + `next` channels.
- **Stats:** ~50.1k GitHub stars, ~5.8k forks. MIT license.
- **Works with:** Claude Code, Cursor, GitHub Copilot (IDE); Google Gemini Gems + ChatGPT Custom GPTs ("web bundles") for planning.

## Two structural changes that define v6

1. **Modularization.** "Core functionality is now separated from domain-specific modules
   (BMM, BMB, TEA, BMGD, CIS, WDS) for independent versioning and release channels." Only
   **BMM** (+ shared `core` skills) installs by default; the rest are optional modules.
2. **Skills-Based Architecture.** Everything migrated to "a unified Markdown-based 'Skill'
   format (`SKILL.md`)." Agents AND workflows are now `bmad-*` skills, invoked by name.
   (The old v4/v5 `src/modules/bmm/agents/` + `.../workflows/` layout is gone; current tree
   is `src/bmm-skills/{1-analysis,2-plan-workflows,3-solutioning,4-implementation}/` and
   `src/core-skills/`.)

## The four-phase lifecycle (+ Quick Flow)

"The BMAD Method follows 4 distinct phases in sequence" plus a parallel Quick Flow track:

| Phase | Verbatim tagline | Activities |
|-------|------------------|-----------|
| 1. **Analysis** (optional) | "Explore the problem space and validate ideas before committing to planning." | brainstorming, research (market/domain/technical), product brief, PRFAQ, forge-idea, document-project |
| 2. **Planning** | "Define what to build and for whom." | PRD (create/update/validate), UX design specs |
| 3. **Solutioning** | "Decide how to build it and break work into stories." | architecture "spine", epics/stories decomposition, implementation-readiness gate |
| 4. **Implementation** | "Build it, one story at a time." | sprint planning, create-story → dev-story → code-review loop, correct-course, retrospective |
| **Quick Flow** (parallel) | "Skip phases 1-3 for small, well-understood work." | `bmad-quick-dev`, `bmad-dev-auto` |

"Each document becomes context for the next phase." The PRD workflow "accepts product briefs,
PRFAQ documents, research findings, and brainstorming reports as input."

## Scale-adaptive planning (two representations)

**Classic v6 — numeric Levels 0-4** (source: `.../workflow-status/project-levels.yaml`,
"BMM Project Scale Levels - Source of Truth"):

| Level | Title | Stories | Documentation | Architecture? |
|-------|-------|---------|---------------|--------------|
| 0 | Single Atomic Change | 1 | Minimal - tech spec only | no |
| 1 | Small Feature | 1-10 | Tech spec | no |
| 2 | Medium Project | 5-15 | PRD + optional tech spec | no |
| 3 | Complex System | 12-40 | PRD + architecture + JIT tech specs | yes |
| 4 | Enterprise Scale | 40+ | PRD + architecture + JIT tech specs | yes |

`workflow-init` auto-suggests a level from keyword/story-count hints but "always asks for
confirmation"; "you can always run create-prd later"; levels are changeable mid-project.

**Current v6 (v6.10) — stakes-calibrated tiers** (the numeric labels were dropped from the
working skills; PRD skill uses "Stakes calibration" prose instead):

- **Quick Flow** — "Bug fixes, simple features, clear scope (1-15 stories)" — tech-spec only.
- **BMad Method** — "Products, platforms, complex features (10-50+ stories)" — PRD + Architecture + UX.
- **Enterprise** — "Compliance, multi-tenant systems (30+ stories)" — PRD + Architecture + Security + DevOps.

Solutioning gate per tier: "Quick Flow: Skip entirely. BMad Method Simple: Optional. BMad
Method Complex: Required. Enterprise: Required." Rule: "If you have multiple epics that could
be implemented by different agents, you need solutioning." "Choose your track based on
planning needs, not story math"; "Story counts are guidance, not definitions."

## CORE MODULE — BMM (6 named agents)

The docs' Named Agents page: "BMad ships **six named agents**, each anchored to a phase of the
BMad Method." Each agent is a skill (`bmad-agent-*`), invoked by name or natural language
("Hey Mary…"). All share an 8-step activation (resolve customize.toml → adopt persona → load
config → greet by name+icon → dispatch menu).

### 1. Analyst — Mary 📊 (`bmad-agent-analyst`, Analysis)
"Help the user ideate research and analyze before committing to a project." "Channels Michael
Porter's strategic rigor and Barbara Minto's Pyramid Principle discipline."
Menu: BP brainstorming, MR market-research, DR domain-research, TR technical-research, CB
product-brief, WB PRFAQ, DP document-project.

### 2. Technical Writer — Paige 📚 (`bmad-agent-tech-writer`, Analysis)
"Capture and curate project knowledge so humans and future LLM agents stay in sync." "Writes
with Julia Evans's accessibility and Edward Tufte's visual precision."
Menu: DP document-project, WD write-document, MG mermaid-gen, VD validate-doc, EC explain-concept.

### 3. Product Manager — John 📋 (`bmad-agent-pm`, Planning)
"Translate product vision into a validated PRD, epics, and stories that development can
execute." "Thinks like Marty Cagan and Teresa Torres. Writes with Bezos's six-pager discipline."
Menu: PRD create/update/validate, CE create-epics-and-stories, IR check-implementation-readiness,
CC correct-course.

### 4. UX Designer — Sally 🎨 (`bmad-agent-ux-designer`, Planning)
"Turn user needs and the PRD into UX design specifications that inform architecture and
implementation." "Grounded in Don Norman's human-centered design and Alan Cooper's persona discipline."
Menu: CU produce UX plan → DESIGN.md (visual identity) + EXPERIENCE.md (behavioral logic).

### 5. System Architect — Winston 🏗️ (`bmad-agent-architect`, Solutioning)
"Convert the PRD and UX into technical architecture decisions that keep implementation on
track." "Channels Martin Fowler's pragmatism and Werner Vogels's cloud-scale realism." "Boring
technology for stability."
Menu: CA architecture, IR check-implementation-readiness.

### 6. Senior Software Engineer (Developer) — Amelia 💻 (`bmad-agent-dev`, Implementation)
"Implement approved stories with test-first discipline and ship working, verified code."
"Disciplined in Kent Beck's TDD and the Pragmatic Programmer's precision. Speaks in file paths
and AC IDs." **This agent absorbed the classic Scrum-Master + QA duties.**
Menu: DS dev-story, QD quick-dev, QA qa-generate-e2e-tests, CR code-review, SP sprint-planning,
CS create-story, ER retrospective.

**Conflict / version note:** classic v4/v5 BMAD shipped separate **Scrum Master (Bob)**,
**Product Owner (Sarah)**, **BMad Master**, and **BMad Orchestrator** agents. In v6 core these
were folded in: story creation / sprint planning / retrospectives → the Developer (Amelia);
epic/story breakdown → the PM (John); multi-agent "orchestration" → the `bmad-party-mode`
*skill* (not a persona). Some secondary sources (e.g. DeepWiki) still list a `sm` agent and
"Bob" — treat as a legacy/transitional listing; the v6 docs say "six named agents." The Test
Architect (Murat) is NOT in core — it ships as the TEA module.

## BMM workflow skills (by phase)

### Phase 1 — Analysis (`src/bmm-skills/1-analysis/`) + core skills
- `bmad-brainstorming` (core) — "Facilitate a brainstorming session using diverse creative techniques" (facilitator/partner/autonomous modes) → brainstorm.html keepsake.
- `bmad-forge-idea` (core) — "Pressure-test an idea through persona-driven interrogation until it hardens, proves out, or dies cheaply" → forge-report.html; forged-idea.md.
- `bmad-market-research` / `bmad-domain-research` / `bmad-technical-research` — three sibling research skills (market/competition/customers; industry domain; tech feasibility) → research reports.
- `bmad-product-brief` — "Create, update, or validate a product brief" → brief.md + addendum.md.
- `bmad-prfaq` — "Working Backwards PRFAQ challenge that stress-tests a product concept customer-first" → prfaq-{project}.md (Amazon press-release + FAQ).
- `bmad-document-project` — "Document brownfield projects for AI context" (full-scan + deep-dive) → project docs.

### Phase 2 — Planning (`src/bmm-skills/2-plan-workflows/`)
- `bmad-prd` — "Create, update, or validate a PRD" (consolidated 3-intent skill; Fast or Coaching paths; a Decision-Log pattern; `.memlog.md` append-only audit trail) → prd.md, addendum.md, .memlog.md.
- `bmad-ux` — "Plan UX patterns and design specifications" → DESIGN.md (visual identity) + EXPERIENCE.md (behavioral logic / IA).
- `bmad-spec` (core) — "Distill any intent input into the SPEC kernel + companions — the canonical, preservation-validated machine contract." SPEC.md = five-field kernel (Problem, Capabilities, Constraints, Non-goals, Success signal).
- (deprecated: bmad-create-prd / bmad-edit-prd / bmad-validate-prd → consolidated into bmad-prd; removed in v7.)

### Phase 3 — Solutioning (`src/bmm-skills/3-solutioning/`)
- `bmad-architecture` — "Produce the architecture: a lean spine of invariants … projected into whatever format the work needs." Output ARCHITECTURE-SPINE.md. The spine "fixes only the invariants … design paradigm, boundary and dependency rules, how state is mutated, who owns shared data … Everything structural (stack, tree, full data shape) is seed: true at cold-start, owned by the code once it exists."
- `bmad-create-epics-and-stories` — "Break requirements into epics and user stories" → epics.md.
- `bmad-check-implementation-readiness` — "Validate PRD, UX, Architecture and Epics specs are complete" → PASS / CONCERNS / FAIL readiness report.
- `bmad-generate-project-context` — "Create project-context.md with AI rules" (tech stack + implementation rules loaded by dev skills).

### Phase 4 — Implementation (`src/bmm-skills/4-implementation/`)
- `bmad-sprint-planning` — "Generate sprint status tracking from epics" → sprint-status.yaml.
- `bmad-create-story` — "Creates a dedicated story file with all the context the agent will need to implement it later" → story-[slug].md (AC, tasks/subtasks, Dev Notes, Dev Agent Record).
- `bmad-dev-story` — "Execute story implementation following a context filled story spec file." Strict: "Execute ALL steps in exact order"; "Continue in a single execution until the story is COMPLETE … UNLESS a HALT condition is triggered."
- `bmad-code-review` — "Review code changes adversarially using parallel review layers (Blind Hunter, Edge Case Hunter, Acceptance Auditor) with structured triage." Runs "fresh context, ideally different LLM."
- `bmad-correct-course` — "Manage significant changes during sprint execution" (mid-sprint re-routing; owned by PM John).
- `bmad-retrospective` — "Post-epic review to extract lessons and assess success" (party-mode review) → lessons + action items.
- `bmad-sprint-status` — read-only "Summarize sprint status and surface risks."
- `bmad-checkpoint-preview` — "LLM-assisted human-in-the-loop review. Make sense of a change, focus attention where it matters, test."
- `bmad-qa-generate-e2e-tests` — "Generate end to end automated tests for existing features."
- `bmad-quick-dev` — Quick Flow: "Intent in, code changes out, with as few human-in-the-loop turns as possible — without sacrificing quality." Routes: "Small, zero-blast-radius changes can go straight to implementation. Everything else goes through planning." 3 checkpoints (intent, spec, review) → spec-*.md + code.
- `bmad-dev-auto` — "performs one unattended development-loop iteration": clarify → create/resume spec → implement → review → write terminal status. Resumes from spec status (draft/ready-for-dev/in-progress/in-review/done/blocked). "Its main purpose is to be used by an orchestrator."

### Story-driven dev loop
Governed by `sprint-status.yaml`. Story status: backlog → ready-for-dev → in-progress →
review → done. "Developer typically creates next story ONLY after previous one is 'done' to
incorporate learnings." "Dev moves story to 'review', then Dev runs code-review (fresh context,
ideally different LLM)." Loop: sprint-planning → create-story → dev-story → code-review →
(correct-course if needed) → repeat → retrospective per epic.

### Cross-phase core skills
`bmad-party-mode` — "Orchestrates lively group discussions between installed BMAD agents…
the personas hold different priorities. The Architect guards the design, the PM guards scope,
the Dev guards what's actually buildable." Modes: Session (one model voices all), Auto,
Subagent ("a separate agent for each persona every substantive round"), Agent-team (Claude
Code only). `bmad-advanced-elicitation` — "Push the LLM to reconsider, refine, and improve its
recent output" (socratic, first principles, pre-mortem, red team). `bmad-shard-doc` — "Splits
large markdown documents into smaller, organized files based on level 2 sections" (PRD/arch
sharding; dual-discovery: whole doc takes precedence over sharded). `bmad-help`,
`bmad-customize`, `bmad-index-docs` — tooling. `bmad-review-adversarial-general` /
`bmad-review-edge-case-hunter` / `bmad-review-verification-gap` — the review layers behind
code-review ("a review technique where the reviewer must find issues. No 'looks good' allowed";
"Zero findings triggers a halt"; "Human filtering remains the essential final step").

## Optional modules (expansion packs)

| Module | Code | What it is | Agents |
|--------|------|-----------|--------|
| **BMad Builder** | bmb | "Build AI agents, workflows, and modules from a conversation." Meta-module: Agent/Workflow/Module builders + npm publish. | The Agent Builder (`bmad-agent-builder`) + sample agents |
| **Creative Intelligence Suite** | cis | "Brainstorming, ideation, storytelling, design thinking, and problem-solving." SCAMPER, TRIZ, reverse brainstorming. | 6: Carson (brainstorming coach), Dr. Quinn (problem solver), Maya (design thinking), Victor (innovation strategist), Caravaggio (presentation master), Sophia (storyteller) |
| **Test Architect** | tea | "Quality strategy, test automation, and release gate decisions for enterprise teams." 9 workflows. | 1: Murat — "Master Test Architect and Quality Advisor" (risk-based testing, ATDD, API/UI automation, NFR audits, release GATE, requirement-to-test traceability) |
| **Game Dev Studio** | gds/BMGD | "Game design and development for Unity, Unreal, Godot, Phaser." 21+ game types. | ~5: Cloud Dragonborn (game architect), Samus Shepard (game designer), Link Freeman (game dev = consolidated dev+QA+SM), Indie (solo dev), Paige (tech writer) |
| **Whiteport Design Studio** | wds | "Strategic UX and Design first planning methodology." Phase 0-8 flow. | 3: Saga (analyst), Freya (UX designer), Mimir (builder) |
| BMad Loop | bmad-loop | "Deterministic, Python-based unattended dev loop with adversarial review." | 0 personas (automation tool) |

## Distinctive techniques

- **Named persona agents** — a distinct expert persona (with name, icon, influences, principles) per SDLC role: Mary/Paige/John/Sally/Winston/Amelia (+ module personas). "each agent carries a distinct persona with persistent facts and principles that shape decisions across all dispatched workflows."
- **Party Mode** — summon multiple persona agents into one roundtable for tradeoff decisions / "what are we missing?" / pressure-testing.
- **Agentic planning** — persona agents FACILITATE the human to decisions: "YOU ARE A FACILITATOR, not a content generator; NEVER generate content without user input."
- **Context-engineered development** — "Stories in BMad aren't isolated tickets. Each story file embeds architectural decisions, dependency context, and project conventions directly into the implementation artifact," so dev agents never context-switch. Plus project-context.md (AI rules) + .memlog.md (append-only audit trail).
- **Scale-adaptive / just-in-time planning** — ceremony scales to complexity (Levels 0-4 / Quick-Method-Enterprise tracks); JIT tech specs; architecture "spine" of invariants only, structure deferred to code.
- **Adversarial / pressure-testing review** — forge-idea ("survives with earned conviction or dies cheaply"); code-review parallel layers (Blind Hunter / Edge Case Hunter / Acceptance Auditor), "reviewer must find issues."
- **Fresh-context-per-story** — one story at a time; code-review in fresh context / different LLM.
- **Document sharding** — split large PRD/architecture by level-2 headings into focused files.
- **Two-phase separation (web planning vs IDE implementation)** — "Planning work and implementation work want different tools." Web LLMs (Gems/GPTs, "web bundles") for conversation/canvas/research; IDE for files/terminal/codebase. Cost angle: planning in a Gem is "zero marginal dollars."

## Sources
- https://docs.bmad-method.org/ (welcome, reference/workflow-map, reference/agents, reference/modules, tutorials/getting-started, explanation/{named-agents,analysis-phase,why-solutioning-matters,adversarial-review,party-mode,quick-dev,web-bundles}, llms-full.txt)
- https://github.com/bmad-code-org/BMAD-METHOD (main @ v6.10.0: src/bmm-skills/, src/core-skills/, bmad-modules.yaml, docs/; classic tags v6.0.0-alpha.23/v6.2.0 for the Levels 0-4 project-levels.yaml)
- Module repos: bmad-builder, bmad-module-creative-intelligence-suite, bmad-method-test-architecture-enterprise, bmad-module-game-dev-studio, bmad-method-wds-expansion
- https://deepwiki.com/bmad-code-org/BMAD-METHOD
</content>
