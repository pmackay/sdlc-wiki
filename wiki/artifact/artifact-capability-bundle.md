---
type: artifact
sources: "Tessl docs (2026)"
raw: ["../../raw/tessl/2026-09-12-tessl-platform.md"]
updated: 2026-09-12
---

# Artifact: Capability bundle

A **versioned package of agent context and extensions, installed and updated as one unit** — the unit of trade in the [supply layer](../registry/index.md). [[tessl]] calls it a *plugin*, and the comparison it reaches for is the right one: *"Everything in a plugin is installed, versioned, and updated as one unit, much like a package in npm or pip."*

What it carries is broader than instructions:

- **Skills** — procedural workflows loaded when the task matches ([[artifact-skill-doc]]).
- **Rules** — standards applied to every task, always on.
- **MCP servers** — live tools and data, not just text.
- **Hooks** — deterministic commands bound to agent lifecycle events (`PreToolUse`, `PostToolUse`, `UserPromptSubmit`, `SessionStart`, `Stop`).
- **Evals** — the scenarios it is graded against, kept with the thing they grade ([[artifact-eval-suite]]).

That composition is the interesting part. A bundle is not only *context*; through hooks and MCP servers it extends the **harness itself**, so installing one from a registry changes the agent's execution primitives and not just its prompt. The supply layer reaches down into the harness layer at exactly this point.

**Why it is a separate artifact from [[artifact-skill-doc]].** A `SKILL.md` is one piece of process knowledge. A bundle is a *release*: it has a version, a changelog, an owner, a visibility setting, a security score, an eval suite, and a rollback path. The wiki already records frameworks shipping through marketplaces ([[superpowers]], [[addy-agent-skills]], [[compound-engineering]], [[pstack]]); this is the shape they ship *as*, and paging it separately is what lets the layer say that the framework bundle is coming apart into independently versioned parts.

## Produced by (backlinks)

Tessl:

- [[tessl-plugin]] — creates, lints, packs, inspects, publishes, unpublishes, and archives the bundle; `tessl plugin new` scaffolds it and `tessl plugin pack` produces the distributable.
- [[tessl-skill]] — `tessl skill import` promotes a standalone skill into a bundle, which is the prerequisite for evaluating it.
- [[tessl-install]] — consumes it: install, pin, list, check outdated, update, roll back.

## See Also
- [[artifact-skill-doc]] — the single unit of process knowledge a bundle packages.
- [[artifact-eval-suite]] — shipped inside the bundle, graded against it.
- [[artifact-standards]] — rules travel in the bundle alongside skills.
- [[pattern-supply-chain-scanning]] — what gets scanned before one is installed.
