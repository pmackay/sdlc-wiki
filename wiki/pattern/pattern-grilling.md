---
type: pattern
sources: "Matt Pocock — Skills for Real Engineers (2026); Open GSD docs (2026); GitHub/spec-kit (2026); bmad-code-org/BMAD-METHOD (2026); obra/superpowers (2026); Agent OS — Builder Methods (2026)"
updated: 2026-08-05
---

# Pattern: Grilling (elicitation interview loop)

Before acting, interrogate the human: ask pointed questions and keep going until every decision branch is resolved. Closes the user↔agent communication gap that otherwise produces work the user didn't want. The loop is reusable and composable — other skills invoke it rather than re-implementing question-asking.

## Applied by (backlinks)

Matt Pocock — Skills for Real Engineers:

- [[mp-grilling]] — the canonical reusable loop.
- [[mp-grill-me]] — interview on a plan/design.
- [[mp-grill-with-docs]] — grilling that also writes docs.

GSD:

- [[gsd-discuss-phase]] — "adaptive questioning" to gather phase context before planning.

Addy Osmani — Agent Skills:

- [[addy-interview-me]] — interviews the user to resolve decisions before work begins.

Spec Kit:

- [[speckit-clarify]] — iterative Q&A that resolves the `[NEEDS CLARIFICATION]` markers in the spec.

BMAD:

- [[bmad-pm]] · [[bmad-analyst]] — the persona **facilitator** stance: "YOU ARE A FACILITATOR, not a content generator; NEVER generate content without user input."
- [[bmad-prd]] — a Coaching path that interrogates the human to each requirement rather than drafting the doc.

A fifth framework joins the cluster. BMAD's twist is that grilling is not a dedicated interview *skill* but the default *stance of every planning persona* — the agents refuse to invent content, so the whole planning phase is an elicitation dialogue. Spec Kit inverts the usual order: it drafts the spec first ([[speckit-specify]]) with ambiguities flagged, then grills to resolve them — versus grilling *before* the spec exists.

Compound Engineering:

- [[ce-brainstorm]] — dialogue that resolves requirements (WHAT) before planning.

gstack:

- [[gstack-office-hours]] — YC-Office-Hours reframing with six forcing questions.

Superpowers:

- [[sp-brainstorming]] — Socratic **one-question-at-a-time** refinement with a HARD-GATE before any implementation; the design is presented in sections for approval before it flows into planning.

Agent OS — grilling as the *only* interaction mode (every command is an AskUserQuestion interview):

- [[agent-os-shape-spec]] — structured questions (scope → visuals → references → standards) drive the whole spec, one question at a time.
- [[agent-os-plan-product]] — one-question-at-a-time vision/roadmap/tech-stack interview.
- [[agent-os-discover-standards]] — 1-2 **"why" questions** per candidate standard, to capture rationale, not just the rule.

## See Also
- [[stage-align]] — the stage where this applies.
- [[pattern-spec-driven-development]] — what the resolved decisions feed.
