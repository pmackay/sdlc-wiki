---
type: capability
subtype: skill
belongs_to: "[[superpowers]]"
implements: []
delegates_to: []
produces: []
applies: ["[[pattern-anti-rationalization]]"]
equivalent_to: ["[[addy-using-agent-skills]]", "[[gstack-router]]", "[[mp-ask-matt]]"]
sources: "Superpowers v6.1.1 (2026)"
raw: ["../../raw/superpowers/2026-07-17-superpowers.md"]
updated: 2026-07-17
---

# using-superpowers

The **bootstrap** skill, injected at session start (and again after compaction). It is the reason a
14-skill library behaves as a whole methodology: it establishes the rule that the agent must **find
and invoke a relevant skill before *any* response or action** — including clarifying questions,
codebase exploration, or file reads.

> **The rule:** *"If you think there is even a 1% chance a skill might apply to what you are doing,
> you ABSOLUTELY MUST invoke the skill. IF A SKILL APPLIES TO YOUR TASK, YOU DO NOT HAVE A CHOICE."*

It sets **skill priority** (process skills like [[sp-brainstorming]] / [[sp-systematic-debugging]]
run first and set the approach, then implementation skills), a **Red Flags** table of the exact
rationalizations that mean *stop, you're talking yourself out of a skill* ("this is just a simple
question", "I need more context first", "let me explore the codebase first"), and a precedence order
(user instructions > skills > default behavior). This is [[pattern-anti-rationalization]] applied to
skill *discovery* itself — the mechanism that makes every other Superpowers skill non-optional.

No stage: it is a meta/dispatcher skill, not a lifecycle activity. It is the direct counterpart to
the other frameworks' routers — [[addy-using-agent-skills]], [[gstack-router]], and [[mp-ask-matt]] —
but is the most coercive of the four: the others help the agent *pick* a skill; this one forbids it
from *not* picking one.

## See Also
- [[sp-writing-skills]] — the other meta skill; grows the library this one enforces.
- [[addy-using-agent-skills]] · [[gstack-router]] · [[mp-ask-matt]] — cross-framework routers.
- [[pattern-anti-rationalization]] — the technique it embodies.
- [[superpowers]] — the framework whose gated pipeline this bootstrap activates.
