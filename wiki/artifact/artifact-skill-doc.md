---
type: artifact
conforms_to: ["[[std-agent-skills]]"]
sources: "obra/superpowers — skills/writing-skills (2026); pstack v0.15.2 — Lauren Tan (2026); Tessl docs (2026)"
raw: ["../../raw/superpowers/2026-07-17-superpowers.md"]
updated: 2026-10-11
---

# Artifact: skill doc (SKILL.md)

A reusable **skill definition** — a `SKILL.md` file (plus any supporting reference files, scripts, or prompt templates in its directory), laid out to the open Agent Skills format ([[std-agent-skills]]), that captures a proven technique, pattern, or reference so future agents can discover and apply it. Written by [[sp-writing-skills]] via its TDD-for-documentation loop: YAML frontmatter with `name` + a *when-to-use-only* `description`, then a body optimized for discovery (keyword coverage, cross-references, flowcharts only where a decision is non-obvious).

What makes it distinctive is that it is **executable process knowledge**: unlike a [[artifact-solution-doc]] (a lesson agents *read* as grounding) or an [[artifact-adr]] (a one-time decision record), a skill doc *changes what the agent can do* — once in the library it triggers automatically (via [[sp-using-superpowers]]) and is followed as a gated procedure. It is the unit that makes the [[superpowers]] library **grow itself**, the [[pattern-knowledge-compounding|capability- compounding]] output of [[stage-learn]].

## Produced by (backlinks)
- [[sp-writing-skills]] — authors/edits a skill, test-first against subagent pressure scenarios.
- [[gstack-skillify]] — the gstack counterpart: codifies a successful run into a permanent browser-skill (same capability-compounding idea, a scrape-specific instance).

pstack:

- [[pstack-create-verification-skill]] — a project-local `verify-<app>` skill with Launch / Doctor / Drive / Evidence / Cleanup / Helpers sections, written for an agent that will read it cold mid-task.
- [[pstack-automate-me]] — a personal `<handle>-mode` skill drafted from the user's own transcripts, updated in place on repeat runs.
- [[mp-writing-for-agents]] — Matt Pocock's model-invoked reference for writing any agent-facing document (skills, `AGENTS.md`/`CLAUDE.md`, pointed-at docs); fires whenever one is created or edited (v1.2.0).
- [[pstack-reflect]] — targeted edits to existing skills, each routed from a synthesized learning and gated by a structural-enforcement check.
- [[pstack-maintain-verification-skill]] — proven corrections to a generated verification skill and its feature map.

Tessl — the layer that treats this artifact as a **tradeable dependency** rather than as a note to self:

- [[tessl-skill]] — scaffolds, lints, publishes, and unpublishes it; `skill import` promotes a loose `SKILL.md` into an [[artifact-capability-bundle]], which is the prerequisite for evaluating it at all.
- [[tessl-review-fix]] — rewrites it iteratively until it clears a quality threshold.

A registry changes what the artifact *is*: it acquires a version, an owner, a visibility setting, a security score, an eval suite, and a rollback path. See [[artifact-capability-bundle]] for the shape it ships as.

## See Also
- [[artifact-capability-bundle]] — the versioned package a skill ships inside once it is distributed rather than written in place.
- [[artifact-eval-suite]] — the scenarios that prove a skill changes behavior.
- [[artifact-solution-doc]] — machine-consumable *lessons* agents read (vs a skill agents *run*).
- [[artifact-explainer]] · [[artifact-retrospective]] — the other [[stage-learn]] outputs (human-facing knowledge).
- [[pattern-knowledge-compounding]] — the technique this artifact realizes (capability-compounding form).
- [[stage-learn]] — the stage this artifact is an output of.
- [[std-agent-skills]] — the open format this artifact follows.
