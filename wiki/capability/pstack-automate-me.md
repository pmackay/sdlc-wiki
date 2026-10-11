---
type: capability
subtype: skill
belongs_to: "[[pstack]]"
implements: "[[stage-learn]]"
delegates_to: ["[[pstack-unslop]]"]
produces: ["[[artifact-skill-doc]]"]
applies: ["[[pattern-knowledge-compounding]]", "[[pattern-wave-parallelism]]", "[[pattern-context-engineering]]"]
equivalent_to: ["[[sp-writing-skills]]", "[[gstack-skillify]]", "[[agent-os-discover-standards]]"]
sources: "pstack v0.15.2 — Lauren Tan (2026)"
raw: ["../../raw/pstack/2026-09-11-pstack-plugin.md"]
updated: 2026-09-11
---

# /automate-me

Drafts the user their **own `-mode` skill** — `jay-mode`, `priya-mode` — mined from how they have actually worked, routing through pstack underneath. The framework's answer to a problem it names about itself in the README: *"poteto-mode is my style. you may not want exactly that."*

That framing is the reason this capability matters beyond its mechanics. Every other framework in the wiki asks you to adopt its methodology; pstack ships a capability whose job is to **replace its own entry point with yours** while keeping the principle and skill layer as the base. [[pstack-poteto-mode]] becomes one mode skill alongside another rather than the thing you conform to.

It orchestrates three skills rather than replacing them: an inline mining pass, Cursor's built-in `create-skill` for authoring, and [[pstack-unslop]] for prose discipline.

**Evidence comes from transcripts, not from an interview.** The skill surveys recent agent conversations for recurring patterns, fanning out parallel subagents across slices of history (two to four weeks split three ways, so each slice has enough material), each returning a short structured list of observed patterns with evidence pointers. Scoping is tight and stated as a privacy rule: use only the active workspace's `agent-transcripts/` directory and **do not glob across `~/.cursor/projects/*/`**, because that crosses workspace boundaries and reads private chats from unrelated projects. The same rule appears verbatim in [[pstack-reflect]].

**It is built for repeat runs, not one-shot generation.** It first looks for an existing `*-mode/SKILL.md` matching the user's handle, including in a personal category directory, and confirms intent before proceeding. In update mode the whole flow changes shape: mining covers only history since the skill was last edited (`git log -1 --format=%cI <path>`), the interview asks what has changed or is missing rather than what to capture from zero, and the file is edited in place — **preserve sections the user has not contradicted, revise ones with new evidence, add new sections only for genuinely new rules.** That is [[pattern-knowledge-compounding]] with an explicit anti-clobber policy, closest in the wiki to [[agent-os]]'s bidirectional profile sync.

## See Also
- [[pstack-reflect]] — the sibling compounding skill, targeting one edit to an existing skill rather than a whole mode.
- [[pstack-poteto-mode]] — the mode this is designed to sit beside, or replace as the entry point.
- [[sp-writing-skills]] · [[gstack-skillify]] — the skill-authoring counterparts.
- [[stage-learn]] — the canonical stage this implements.
