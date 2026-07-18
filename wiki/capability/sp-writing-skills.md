---
type: capability
subtype: skill
belongs_to: "[[superpowers]]"
implements: "[[stage-learn]]"
delegates_to: ["[[sp-test-driven-development]]"]
produces: ["[[artifact-skill-doc]]"]
applies: ["[[pattern-knowledge-compounding]]", "[[pattern-test-driven-development]]"]
equivalent_to: ["[[gstack-skillify]]"]
sources: "Superpowers v6.1.1 (2026)"
raw: ["../../raw/superpowers/2026-07-17-superpowers.md"]
updated: 2026-07-17
---

# writing-skills

The library's self-growth skill: create or edit a skill so future agents can find and apply a proven technique → [[artifact-skill-doc]]. Its central claim is that **writing skills IS Test-Driven Development applied to process documentation** ([[pattern-test-driven-development]] via [[sp-test-driven-development]] as required background).

> **The Iron Law (same as TDD):** *"NO SKILL WITHOUT A FAILING TEST FIRST."* The "test" is a pressure scenario run against a subagent: watch it *fail* (baseline — the agent rationalizes without the skill), write the skill addressing those exact rationalizations, watch it *pass* (the agent complies), then refactor to close loopholes. Applies to new skills *and* edits.

Most of the skill is **Skill Discovery Optimization**: the description field must state *only when to use* the skill (never summarize its workflow — a summarized workflow becomes a shortcut agents take instead of reading the body); keyword coverage, active-voice gerund naming, aggressive token-budget targets, cross-references via `**REQUIRED SUB-SKILL:**` markers (never `@`-links, which force-load and burn context), and rules for when a flowchart earns its place. Companion refs: `anthropic-best-practices.md`, `persuasion-principles.md`, `testing-skills-with-subagents.md`.

This is **capability compounding** — a successful run hardens into a permanent, reusable skill so the lifecycle compounds ([[pattern-knowledge-compounding]]) — the direct counterpart to [[gstack-skillify]] (which codifies a successful scrape into a permanent browser-skill). It sits in [[stage-learn]] as the agent-capability flavor: the product is not shipped software but *reusable knowledge future agents read*. Superpowers touches stage-learn *only* through this skill (no retrospective / solution-corpus capability).

## See Also
- [[sp-test-driven-development]] — the required background; this skill is TDD applied to documentation.
- [[sp-using-superpowers]] — the bootstrap that discovers and enforces the skills this one writes.
- [[gstack-skillify]] — the counterpart capability-compounding skill (codify a proven run into a permanent skill).
- [[artifact-skill-doc]] — the SKILL.md it produces.
- [[pattern-knowledge-compounding]] · [[pattern-test-driven-development]] — the techniques applied.
- [[stage-learn]] — the canonical stage this implements.
