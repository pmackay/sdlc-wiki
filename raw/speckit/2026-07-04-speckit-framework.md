---
source_urls:
  - https://github.com/github/spec-kit
  - https://github.github.com/spec-kit/
  - https://raw.githubusercontent.com/github/spec-kit/main/spec-driven.md
collected: 2026-07-04
published: Unknown
author: GitHub (github/spec-kit)
---

# Spec Kit (github/spec-kit)

## What it is
**Spec Kit** is GitHub's open-source toolkit for **Spec-Driven Development (SDD)** — a
methodology that "flips the script on traditional software development" by making
specifications *executable* rather than merely advisory. Instead of treating code as
primary, SDD treats the specification as the foundation that directly generates working
implementations. The goal: build "high-quality software faster" by helping developers
"focus on product scenarios and predictable outcomes instead of vibe coding every piece
from scratch."

Community scale: 106K+ GitHub stars, 200+ contributors, 105 community extensions
(60+ authors), 22 presets, and alternative SDD processes (AIDE, Canon, Product Forge,
FX→.NET, MAQA).

## The Specify CLI
Requires the `uv` package manager and Python 3.11+.

```bash
uv tool install specify-cli --from git+https://github.com/github/spec-kit.git@vX.Y.Z
# or run without installing:
uvx --from git+https://github.com/github/spec-kit.git specify init my-project --integration copilot
```

Self-management: `specify self check`, `specify self upgrade --dry-run`, `specify self upgrade`.
Integrations: `specify integration list`. Works offline, behind firewalls, and on Windows,
macOS, and Linux. Supports 30+ AI coding agents including GitHub Copilot, Claude Code,
Gemini CLI, Qwen Code, Codex CLI, and many others — "switch freely between agents with a
single command. No lock-in."

### Extensions, Presets, Bundles
- **Extensions** add new capabilities/commands (e.g. Jira integration, domain workflows):
  `specify extension search/add <name>`.
- **Presets** customize *how* existing workflows function — modifying templates and
  instructions to enforce organizational standards: `specify preset search/add <name>`.
- **Bundles** package curated sets of extensions, presets, and workflows into versioned,
  role-oriented configurations for team personas (product manager, developer, security
  researcher, etc.): `specify bundle search/info/install <bundle-id>`.

## Core slash commands

**Essential SDD workflow:**

| Command | Purpose (verbatim) |
|---------|--------------------|
| `/speckit.constitution` | "Create or update project governing principles and development guidelines" |
| `/speckit.specify` | "Define what you want to build (requirements and user stories)" |
| `/speckit.plan` | "Create technical implementation plans with your chosen tech stack" |
| `/speckit.tasks` | "Generate actionable task lists for implementation" |
| `/speckit.implement` | "Execute all tasks to build the feature according to the plan" |

**Optional commands:**

| Command | Purpose (verbatim) |
|---------|--------------------|
| `/speckit.clarify` | "Clarify underspecified areas" |
| `/speckit.analyze` | "Cross-artifact consistency & coverage analysis" |
| `/speckit.checklist` | "Generate custom quality checklists that validate requirements completeness, clarity, and consistency" |
| `/speckit.converge` | "Assess the codebase against spec/plan/tasks and append remaining work as new tasks" |
| `/speckit.taskstoissues` | Convert task lists into GitHub issues for tracking |

## Development contexts
1. **0-to-1 Development** (Greenfield) — generate applications from scratch.
2. **Creative Exploration** — parallel implementations exploring diverse solutions.
3. **Iterative Enhancement** (Brownfield) — adding features and modernizing existing systems.

## The SDD workflow (from spec-driven.md)

Core process: **Spec → Plan → Tasks → Implement**, where each phase produces a Markdown
artifact that feeds the next, enabling "structured context instead of ad-hoc prompts."
The conceptual document elaborates the phases:

### Phase 1: Constitution
Establishes immutable architectural principles in `.specify/memory/constitution.md`.
Described as nine "articles": Articles I–III universal (library-first design, CLI
interfaces, test-driven development), IV–VI project-defined, VII–IX mandating simplicity,
anti-abstraction, and integration-first testing. The constitution is "the architectural
DNA of the system, ensuring that every generated implementation maintains consistency."

### Phase 2: Specify (`/speckit.specify`)
Transforms vague ideas into structured feature specs. Auto-assigns sequential feature
numbers (001, 002…), creates semantic branch names, generates `specs/[branch-name]/spec.md`
from templates. Output: `spec.md` with user stories, acceptance criteria, and explicit
`[NEEDS CLARIFICATION]` markers for ambiguities. Focuses on "WHAT users need and WHY"
rather than implementation details.

### Phase 3: Clarify (`/speckit.clarify`)
Iterative dialogue matures the vague spec: edge cases, boundary conditions, acceptance
criteria precision, removal of `[NEEDS CLARIFICATION]` markers, identification of
organizational constraints. No distinct artifact — `spec.md` evolves during this phase.

### Phase 4: Plan (`/speckit.plan`)
Generates implementation planning from the finalized spec. Validates alignment with
constitutional principles through phase gates; converts business requirements into
technical architecture with documented rationale. Output artifacts:
- `plan.md` — high-level implementation strategy with phase breakdown
- `data-model.md` — entity definitions and schema design
- `contracts/` — API specifications (REST endpoints, WebSocket events)
- `research.md` — technology investigation and comparative analysis
- `quickstart.md` — key validation scenarios for acceptance testing

Constitutional enforcement: "Phase -1" gates enforce simplicity (≤3 projects),
anti-abstraction (framework-direct usage), and integration-first testing.

### Phase 5: Analyze (`/speckit.analyze`)
Validates specs and plans against constitutional principles: architectural compliance
with all nine articles, consistency checking for contradictions and gaps, justified
exceptions documentation. "Continuous refinement as an ongoing process rather than a
one-time gate." Ensures "every technical choice links back to specific requirements."

### Phase 6: Tasks (`/speckit.tasks`)
Converts the plan into an executable task list. Inputs: `plan.md` (required), plus
optional `data-model.md`, `contracts/`, `research.md`. Derives concrete tasks from API
contracts, entities, and test scenarios; marks independent tasks `[P]` for
parallelization; sequences dependent work; prioritizes test-first (contract tests before
integration tests before unit tests). Output: `tasks.md`.

### Phase 7: Implement (`/speckit.implement`)
Executes the tasks, translating specs to implementation. TDD is "NON-NEGOTIABLE" — tests
must be written and fail (Red) before implementation code. Generate unit tests from
acceptance criteria → get test approval → confirm tests fail → implement to pass.

### Phase 8: Checklist (`/speckit.checklist`)
Per the current docs, generates custom quality checklists that validate requirements
completeness, clarity, and consistency (described by the team as "unit tests for your
English"). (The conceptual spec-driven.md instead frames checklist as continuous
validation of generated code against specifications — an older framing.)

## Key artifacts

| Artifact | Purpose |
|----------|---------|
| `.specify/memory/constitution.md` | Immutable architectural/governing principles (project-level) |
| `specs/<feature>/spec.md` | Feature requirements with user stories + acceptance criteria + `[NEEDS CLARIFICATION]` |
| `specs/<feature>/plan.md` | Technical architecture and implementation strategy |
| `data-model.md` | Entity definitions, relationships, and schemas |
| `contracts/` | API specifications and interface definitions |
| `research.md` | Technology investigation and options analysis |
| `quickstart.md` | Key validation scenarios and acceptance tests |
| `tasks.md` | Ordered, parallelizable (`[P]`) task list |

## Central principles (from spec-driven.md)
- **Specifications as lingua franca:** "The specification becomes the primary artifact.
  Code becomes its expression in a particular language and framework. Maintaining software
  means evolving specifications." "Specifications don't serve code — code serves specifications."
- **Executable specifications:** precision and unambiguity are prerequisites for code
  generation; specs must be testable and verifiable.
- **Continuous refinement:** consistency validation happens throughout, not as a final gate.
- **Research-driven context:** technical decisions emerge from systematic investigation.
- **Bidirectional feedback:** production metrics/incidents inform spec evolution —
  "performance bottlenecks become new non-functional requirements."
- **Branching for exploration:** multiple implementations from one spec to explore
  different optimization targets (performance, maintainability, cost, UX).

SDD "amplifies human capability by automating mechanical translation" while preserving
creative and critical-thinking work that requires human judgment.
