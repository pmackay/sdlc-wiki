---
type: artifact
sources: "Agent OS v3.0.0 — Builder Methods (2026)"
raw: ["../../raw/agent-os/2026-08-05-agent-os.md"]
updated: 2026-08-05
---

# Artifact: Standards (externalized coding conventions)

A durable, project-local corpus of **declarative coding conventions** — *"our API responses use this format"* — that an agent reads as governing context. In [[agent-os]] this is the `agent-os/standards/` folder: one concise Markdown file per convention, nested by domain (`api/response-format.md`, `database/migrations.md`, root-level `naming-conventions.md`), plus an **`index.yml`** that maps each standard to a one-sentence description so the right ones can be *matched and injected without loading them all*. Authored to be token-frugal — *"Every word costs tokens. Keep them concise"* — and to *"document only unconventional patterns, not framework defaults."*

Standards are the canonical **guide (feedforward control)** of [[topic-harness-engineering]]: externalized project knowledge the agent consults *before* acting, standing in for the *"we don't do it that way here"* intuition it lacks. Agent OS distinguishes them sharply from Skills — *"Standards describe **what** conventions to follow; Skills describe **how** to do tasks"* — and refines them over time by syncing project-refined standards back into reusable **profiles** ([[pattern-knowledge-compounding]] applied to conventions).

Related but distinct externalized-convention artifacts:
- [[artifact-constitution]] — Spec Kit's *gated, immutable, up-front* principles; standards are *advisory, injected on demand, mined from existing code*.
- [[artifact-adr]] — a *per-decision* rationale record; a standard is a *standing rule*.
- [[artifact-solution-doc]] — *harvested lessons* re-injected as grounding; standards are *authored conventions*.

## Produced by (backlinks)

Agent OS:

- [[agent-os-discover-standards]] — mines the codebase into new standards files (with "why" rationale).
- [[agent-os-index-standards]] — maintains the `index.yml` matcher over the corpus.

## See Also
- [[agent-os-inject-standards]] — deploys standards into the working context (reference vs embedded snapshot).
- [[pattern-context-engineering]] — the pattern the injected standards serve.
- [[pattern-knowledge-compounding]] — the sync-to-profile loop that refines standards across projects.
- [[topic-harness-engineering]] — standards as the guide layer; how the layer thins as models improve.
