---
type: pattern
sources: "GitHub/spec-kit — spec-driven.md (2026)"
updated: 2026-07-04
---

# Pattern: Project constitution (externalized governing principles)

Codify a project's **immutable, cross-cutting principles into one durable, versioned document** — a "constitution" — and **mechanically gate every downstream artifact against it**. The constitution is authored up front, persists across all features, and is the fixed reference that plans and analyses must satisfy.

Three coupled moves:

1. **Externalize.** Principles live in a single named artifact ([[artifact-constitution]], `.specify/memory/constitution.md`) organized as numbered "articles," not scattered as prose inside individual skills or prompts.
2. **Make it governing law.** Later phases don't merely *consult* the principles — they are **gated** against them. Spec Kit's [[speckit-plan]] runs "Phase -1" constitutional gates; [[speckit-analyze]] audits every artifact for compliance and requires justified exceptions.
3. **Keep it immutable-by-default.** Unlike a per-change spec, the constitution is not consumed and rewritten each feature; it changes only through deliberate amendment.

## Why it's distinctive

This is the axis on which Spec Kit differs from the other frameworks. GSD, Matt Pocock, and Addy all *have* strong principles — but they embed them **inside individual skills** (Addy's per-skill "Red Flags," MP's design heuristics), applied at the point of use. OpenSpec has no project-wide charter at all. Only Spec Kit lifts the principles out into one governing document that acts as a compliance gate — the same "externalize the rules" move that a linter config or an ADR log makes, applied to whole-project architecture.

Contrast with [[pattern-anti-rationalization]] (Addy): both are guardrail mechanisms, but anti-rationalization pre-empts *excuses within a skill*, whereas a constitution asserts *positive project-wide law* checked across artifacts.

## Applied by (backlinks)

Spec Kit:

- [[speckit-constitution]] — authors and maintains the constitution.
- [[speckit-analyze]] — enforces it as a cross-artifact compliance gate.

## See Also
- [[artifact-constitution]] — the artifact this pattern is built on.
- [[artifact-adr]] — a per-decision governance record; the constitution is its project-wide, up-front counterpart.
- [[pattern-spec-driven-development]] — the broader SDD context Spec Kit sits in.
- [[speckit]] — the framework built around this pattern.
