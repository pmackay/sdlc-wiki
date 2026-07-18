---
type: artifact
sources: "obra/superpowers — skills/writing-skills (2026)"
raw: ["../../raw/superpowers/2026-07-17-superpowers.md"]
updated: 2026-07-17
---

# Artifact: skill doc (SKILL.md)

A reusable **skill definition** — a `SKILL.md` file (plus any supporting reference files, scripts, or
prompt templates in its directory) that captures a proven technique, pattern, or reference so future
agents can discover and apply it. Written by [[sp-writing-skills]] via its TDD-for-documentation loop:
YAML frontmatter with `name` + a *when-to-use-only* `description`, then a body optimized for discovery
(keyword coverage, cross-references, flowcharts only where a decision is non-obvious).

What makes it distinctive is that it is **executable process knowledge**: unlike a
[[artifact-solution-doc]] (a lesson agents *read* as grounding) or an [[artifact-adr]] (a one-time
decision record), a skill doc *changes what the agent can do* — once in the library it triggers
automatically (via [[sp-using-superpowers]]) and is followed as a gated procedure. It is the unit that
makes the [[superpowers]] library **grow itself**, the [[pattern-knowledge-compounding|capability-
compounding]] output of [[stage-learn]].

## Produced by (backlinks)
- [[sp-writing-skills]] — authors/edits a skill, test-first against subagent pressure scenarios.
- [[gstack-skillify]] — the gstack counterpart: codifies a successful run into a permanent browser-skill (same capability-compounding idea, a scrape-specific instance).

## See Also
- [[artifact-solution-doc]] — machine-consumable *lessons* agents read (vs a skill agents *run*).
- [[artifact-explainer]] · [[artifact-retrospective]] — the other [[stage-learn]] outputs (human-facing knowledge).
- [[pattern-knowledge-compounding]] — the technique this artifact realizes (capability-compounding form).
- [[stage-learn]] — the stage this artifact is an output of.
