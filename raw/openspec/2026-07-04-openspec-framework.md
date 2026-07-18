---
source_urls:
  - https://github.com/Fission-AI/OpenSpec/
  - https://raw.githubusercontent.com/Fission-AI/OpenSpec/main/README.md
  - https://raw.githubusercontent.com/Fission-AI/OpenSpec/main/docs/concepts.md
  - https://raw.githubusercontent.com/Fission-AI/OpenSpec/main/docs/commands.md
collected: 2026-07-04
published: Unknown
author: Fission AI
---

# OpenSpec (Fission-AI/OpenSpec)

## What it is
**Spec-driven development (SDD) for AI coding assistants.** OpenSpec is a lightweight
specification framework designed to align human developers and AI coding assistants on
requirements *before* implementation. It adds structure to collaborative AI-driven
development without rigid ceremony. Install: `npm install -g @fission-ai/openspec@latest`
(requires Node.js 20.19.0+), then `openspec init` in a project.

## Core philosophy (four/five principles)
- **Fluid not rigid** — "no phase gates, work on what makes sense."
- **Iterative not waterfall** — "learn as you build, refine as you go."
- **Easy not complex** — "lightweight setup, minimal ceremony."
- **Brownfield-first** — "works with existing codebases, not just greenfield."
- **Scalable** — from personal projects to enterprises.

The framework embraces changing requirements and deepening understanding rather than
enforcing sequential phases.

## Directory structure
OpenSpec creates an `openspec/` folder within a project:

```
openspec/
├── specs/           # Source of truth for current system behavior
├── changes/         # Proposed modifications (active work)
└── changes/archive/ # Completed changes with preserved context
```

## Specs (the living source of truth)
Specs describe how the system **currently behaves** using structured requirements and
scenarios, organized by logical domain (feature areas, components, bounded contexts).

**Requirements** state what the system must do without specifying implementation. RFC 2119
keywords: **MUST/SHALL** (absolute), **SHOULD** (recommended with exceptions), **MAY**
(optional).

**Scenarios** provide concrete, testable examples using Given/When/Then structure:
```
#### Scenario: [name]
- GIVEN [precondition]
- WHEN [action]
- THEN [observable result]
- AND [additional result]
```

Example structure:
```markdown
### Requirement: [behavior description]
[One sentence stating what system SHALL/MUST/SHOULD do]

#### Scenario: [specific case]
- GIVEN [initial state]
- WHEN [user/system action]
- THEN [expected outcome]
```

**Spec focus:** observable behavior users/systems rely on, inputs, outputs, error
conditions, external constraints. **Avoid:** implementation details, framework choices,
internal structure, execution plans.

## Changes (self-contained folders of proposed modifications)
Changes package proposed modifications as self-contained folders containing artifacts and
delta specs. Multiple changes can exist simultaneously without conflicts.

```
openspec/changes/[change-name]/
├── proposal.md       # Intent, scope, high-level approach (Why and what)
├── design.md         # Technical approach and architecture decisions (How)
├── tasks.md          # Implementation checklist with checkboxes
├── .openspec.yaml    # Optional metadata
└── specs/            # Delta specifications
    └── [domain]/
        └── spec.md   # Changes relative to main specs
```

Artifact flow: `proposal → specs → design → tasks → implement`.

## Delta specs (the signature mechanism)
Delta specs describe changes **relative to** current specifications, so you never rewrite
the whole product spec — you describe only what is changing. Three sections:

```markdown
## ADDED Requirements
### Requirement: [new behavior]
[requirement text with scenarios]

## MODIFIED Requirements
### Requirement: [changed behavior]
[updated text] (Previously: [old text])
[updated scenarios]

## REMOVED Requirements
### Requirement: [deprecated behavior]
(Reason for removal)
```

**Operation order on apply/archive:** RENAMED → REMOVED → MODIFIED → ADDED. (If a
requirement is renamed, subsequent modifications correctly target the new header.)

**Section operations when merged into main spec (on archive/sync):**
- **ADDED** → appended to main spec
- **MODIFIED** → replaces existing requirement
- **REMOVED** → deleted from main spec

Delta specs clarify exactly what's changing, prevent merge conflicts across parallel
changes, and emphasize brownfield modifications over complete rewrites.

## Artifact files
- **proposal.md** — problem statement, scope boundaries (in/out of scope), proposed
  technical approach at a high level.
- **design.md** — technical approach, architecture decisions with rationale, data flow and
  component interactions.
- **tasks.md** — hierarchically numbered implementation checklist (1.1, 1.2, …) with
  checkboxes, grouped under logical headings.
- **specs/** — delta specifications showing ADDED/MODIFIED/REMOVED requirements relative to
  the corresponding main spec domain.

## Spec-driven cycle
Specifications form the **evolving source of truth**. The cycle: current specs → propose
changes as deltas → implement changes → archive merges deltas into specs → specs describe
new behavior → repeat. Requirements capture "what," scenarios demonstrate "when,"
implementation ("how") stays in design.md and tasks.md, never in specs.

Human-agent loop: human provides intent/constraints → agent drafts behavior-first
requirements and scenarios → agent preserves implementation detail in design/tasks →
validation confirms clarity before coding.

---

## AI slash commands (chat interface)

### Core profile (default)
- **`/opsx:explore`** — "Think through ideas, investigate problems, and clarify requirements
  before committing to a change." Opens an exploratory conversation without creating
  structure, investigates the codebase, compares approaches. Transitions to propose when
  ready.
- **`/opsx:propose`** — "Create a new change and generate planning artifacts in one step."
  Generates proposal, specs, design, and tasks immediately. Best for straightforward changes
  with clear requirements.
- **`/opsx:apply`** — "Implement tasks from the change." Works through task lists
  sequentially, writing code and marking items complete. Resumes from checkpoints if
  interrupted.
- **`/opsx:sync`** — "Merge delta specs from a change into main specs." Intelligently
  integrates change specifications into the primary documentation. Usually invoked during
  archive, rarely needed manually.
- **`/opsx:archive`** — "Archive a completed change." Finalizes work, optionally syncs specs,
  moves the change folder to archive with a timestamp. Preserves an audit trail.

### Expanded workflow (custom profile)
Enable via `openspec config profile`, then `openspec update`:
- **`/opsx:new`** — "Start a new change scaffold." Creates the change folder and metadata
  file, awaits artifact generation. Requires a change name and optional schema.
- **`/opsx:continue`** — "Create the next artifact in the dependency chain." Generates one
  artifact at a time, respects dependencies, reads required files for context. Incremental
  control.
- **`/opsx:ff`** — "Fast-forward through artifact creation." Generates all planning artifacts
  sequentially in dependency order. Faster than continue for straightforward changes.
- **`/opsx:verify`** — "Validate that implementation matches your change artifacts." Checks
  completeness (all requirements met), correctness (spec alignment), and coherence (design
  consistency). Reports issues without blocking archive.
- **`/opsx:bulk-archive`** — "Archive multiple completed changes at once." Handles spec
  conflicts across simultaneous changes by inspecting actual implementation; archives in
  chronological order.
- **`/opsx:onboard`** — "Guided onboarding through the complete OpenSpec workflow."
  Interactive 15–30 minute tutorial using the real codebase; creates an actual change,
  implements work, archives the result while explaining each phase.

### Legacy commands (deprecated)
- **`/openspec:proposal`** — creates all artifacts simultaneously in the older format.
- **`/openspec:apply`** — legacy implementation command.
- **`/openspec:archive`** — legacy archive command.

### Workflow stages ↔ commands
| Stage | Commands |
|-------|----------|
| Exploration | `/opsx:explore` |
| Planning | `/opsx:propose`, `/opsx:new`, `/opsx:continue`, `/opsx:ff` |
| Implementation | `/opsx:apply` |
| Validation | `/opsx:verify` |
| Finalization | `/opsx:sync`, `/opsx:archive`, `/opsx:bulk-archive` |
| Learning | `/opsx:onboard` |

### Tool-specific syntax
Most tools use `/opsx:command` (Claude Code, Copilot IDE). Cursor and Windsurf use
`/opsx-command` (hyphens). Kimi CLI and Trae use skill-based syntax like
`/skill:openspec-propose`.

---

## Terminal CLI commands
- **`openspec init`** — initialize OpenSpec in a project; create the directory structure.
- **`openspec update`** — regenerate skills and command files after configuration changes
  (also refreshes AI agent instructions).
- **`openspec config profile`** — switch between command profiles (core vs expanded).
- **`openspec validate`** — check artifact correctness and consistency.
- **`openspec list`** — display all changes (active and archived).
- **`openspec show`** — display a specific change's details and artifacts.
- **`openspec diff`** — compare artifact versions or changes.
- **`openspec archive`** — terminal-based change-archival alternative.

## Key features
- **Stores (Beta)** — separate planning repositories shared across teams via Git, enabling
  cross-repo feature coordination and centralized requirement ownership.
- **Multi-tool integration** — works with 30+ AI assistants through slash-command support;
  compatible with npm, pnpm, yarn, bun, nix.
- **Brownfield support** — designed for adoption on existing codebases through the
  `/opsx:explore` discovery phase.

## Contributing / license
Small fixes may be submitted directly; larger changes require submitting an OpenSpec change
proposal first. AI-generated code is welcomed when tested and verified, with attribution to
the model used. License: MIT.
