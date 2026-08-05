# Source capture — Martin Fowler, "Harness Engineering"

- URL: https://martinfowler.com/articles/harness-engineering.html
- Captured: 2026-08-05
- Type: external reference (not a framework ingest) — grounding source for `wiki/topic/topic-harness-engineering.md`

Immutable capture of the article's vocabulary and framework, extracted for the topic page. Quotes are verbatim where marked.

## Core definition

"Agent = Model + Harness." The **harness** is everything constructed *around* the model to steer its behaviour — **not** the CLI/program itself. For coding agents it splits into two bounded contexts:

- **Builder harness** — built into the agent by its vendor (system prompt, code retrieval, orchestration).
- **User harness** — the controls users construct for their own system and use case.

"A well-built outer harness serves two goals: it increases the probability that the agent gets it right in the first place, and it provides a feedback loop that self-corrects."

The harness acts as a **cybernetic governor** — a regulation system combining feedforward and feedback control.

Motivating gap: "A coding agent has none of this: no social accountability, no aesthetic disgust at a 300-line function, no intuition that 'we don't do it that way here.'" Guides and sensors externalize the implicit developer knowledge the agent lacks.

## The two control families

- **Guides (feedforward controls)** — anticipatory; steer the agent *before* it acts to raise first-attempt quality. Examples: AGENTS.md files, skills, bootstrap scripts, codemods, reference documentation, how-to guides, coding-convention documents.
- **Sensors (feedback controls)** — observational; enable self-correction *after* the agent acts. Examples: structural tests (ArchUnit), pre-commit hooks, custom linters, review-agent skills, dead-code detection, dependency scanners.

Both are necessary; neither is sufficient alone.

## Control types (cross-cutting)

- **Computational controls** — deterministic, fast (milliseconds–seconds): tests, linters, type checkers.
- **Inferential controls** — semantic, AI-based (code-review agents, "LLM as judge"); slower, richer, run on GPU/NPU.

## The steering loop (refinement over time)

"Whenever an issue happens multiple times, the feedforward and feedback controls should be improved." The human iteratively refines guides and sensors in response to recurring agent failures.

## Other coined terms

- **Keep quality left** — distribute checks across the lifecycle; earlier detection = cheaper fixes.
- **Harnessability** — the degree to which a codebase is amenable to harness controls, given its structural properties.
- **Ambient affordances** — "structural properties of the environment itself that make it legible, navigable, and tractable to agents."
- **Harness templates** — pre-bundled guides and sensors for common service topologies.

## Taxonomies proposed

**By regulation dimension (what is being governed):**
1. **Maintainability harness** — internal code quality/maintainability (the most developed today).
2. **Architecture fitness harness** — fitness functions defining and checking architectural characteristics.
3. **Behaviour harness** — functional correctness (least mature; relies on specs + AI-generated test coverage + manual testing).

**By lifecycle placement (when controls run):**
- Pre-commit / pre-integration (fast, frequent).
- Post-integration pipeline (expensive, semantic).
- Continuous drift monitoring (outside the change lifecycle).

**By control type:** computational vs inferential; feedforward vs feedback.
