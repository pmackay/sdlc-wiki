---
type: capability
subtype: sub-agent
belongs_to: "[[pstack]]"
implements: "[[stage-review]]"
delegates_to: ["[[pstack-how]]", "[[pstack-why]]"]
produces: ["[[artifact-review-report]]"]
applies: ["[[pattern-persona-agents]]", "[[pattern-adversarial-review]]"]
equivalent_to: []
sources: "pstack v0.15.2 — Lauren Tan (2026)"
raw: ["../../raw/pstack/2026-09-11-pstack-plugin.md"]
updated: 2026-09-11
---

# Comment Sicko

A read-only, single-purpose adversarial reviewer available as `subagent_type: "Comment Sicko"`, normally invoked through [[pstack-no-comments]] rather than directly. It hunts code comments: narration, banners, commented-out corpses, and workaround sermons. It is the wiki's most extreme [[pattern-persona-agents]] instance, written in a deliberately deranged first-person voice (*"I hate comments… Everything else is meat"*) rather than the professional-role register of [[gstack]]'s CEO and QA-lead personas or [[bmad]]'s named specialists.

**Its keep-list is the actual contract**, and it is short: legal or license headers; non-obvious behavior forced by an external dependency, platform, vendor, or protocol that cannot be reshaped; `// prettier-ignore`-style suppressions whose rule is faulty, pedantic, or style-only; doc comments defining a public API contract; and issue or RFC links explaining a constraint code cannot express. Ambiguity resolves against the comment.

Two mechanisms make it more than a linter. First, **a surprise in our own code is never a keep** — it is flagged `MUST KILL` on the exact guilty symbol, converting a comment into a rename, extract, type, or rearchitecture task so the behavior becomes obvious without prose. That is [[pstack-principle-encode-lessons-in-structure]] applied to comments. Second, before judging a thin `IMPORTANT` or `do not remove` claim it **runs [[pstack-how]] or [[pstack-why]] on the named symbol** — a reviewer subagent that invokes the framework's own investigation skills to check a claim rather than deferring to it.

It reports only and never writes application code: touched files, deletion count, `MUST KILL` flags one line each, and skips. Acting on the report is [[pstack-no-comments]]'s job.

## See Also
- [[pstack-no-comments]] — the skill that spawns it and acts on its findings.
- [[pstack-interrogate]] — the framework's broad adversarial review; Comment Sicko is the narrow single-axis one.
- [[pstack-poteto-agent]] — the framework's other shipped subagent.
- [[stage-review]] — the canonical stage this implements.
