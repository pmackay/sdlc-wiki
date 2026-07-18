---
type: capability
subtype: skill
belongs_to: "[[addy-agent-skills]]"
implements: "[[stage-implement]]"
delegates_to: []
produces: []
applies: ["[[pattern-source-grounding]]"]
equivalent_to: []
sources: "Addy Osmani — Agent Skills (2026)"
raw: ["../../raw/addy-agent-skills/2026-07-04-agent-skills.md"]
updated: 2026-07-04
---

# Source-Driven Development

Ground every framework- or library-specific decision in official documentation rather than
memory: **detect** the stack and exact versions from the dependency file, **fetch** the precise
docs page (not the homepage), **implement** the documented patterns, and **cite** full-URL
sources for every non-obvious decision. Anything that can't be verified is explicitly flagged
as unverified — honesty over false confidence.

The distinctive value is countering plausible-but-outdated training-data patterns that look
correct but break against current versions. It applies [[pattern-source-grounding]] and
implements [[stage-implement]].

## See Also
- [[pattern-source-grounding]] — the underlying pattern.
- [[addy-doubt-driven-development]] — sibling verification skill; SDD checks framework facts, doubt-driven checks your reasoning.
- [[stage-implement]] — the canonical stage this implements.
