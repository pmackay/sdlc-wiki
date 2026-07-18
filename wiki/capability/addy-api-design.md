---
type: capability
subtype: skill
belongs_to: "[[addy-agent-skills]]"
implements: "[[stage-implement]]"
delegates_to: []
produces: []
applies: ["[[pattern-contract-first]]", "[[pattern-deep-modules]]"]
equivalent_to: ["[[mp-codebase-design]]"]
sources: "Addy Osmani — Agent Skills (2026)"
raw: ["../../raw/addy-agent-skills/2026-07-04-agent-skills.md"]
updated: 2026-07-04
---

# API & Interface Design

Design interfaces that make the right thing easy and the wrong thing hard. The mechanism is
**contract-first** (define the typed interface before implementing it — the types are the
documentation, per [[pattern-contract-first]]), consistent error semantics, and validation at
system boundaries only while internal code trusts its types. It is governed by **Hyrum's Law**
(every observable behavior becomes a de facto contract) and the **One-Version Rule** (extend
rather than fork), pushing addition over modification for backward compatibility.

It applies [[pattern-deep-modules]] and clusters with Matt Pocock's deep-module design skill.
It implements [[stage-implement]].

## See Also
- [[mp-codebase-design]] — the Matt Pocock equivalent in the design cluster.
- [[pattern-contract-first]] — define the contract before the implementation.
- [[pattern-deep-modules]] — simple interface over substantial implementation.
- [[stage-implement]] — the canonical stage this implements.
