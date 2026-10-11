---
type: capability
subtype: sub-agent
belongs_to: "[[pstack]]"
implements: []
delegates_to: []
produces: []
applies: ["[[pattern-fresh-context-subagents]]", "[[pattern-context-engineering]]"]
equivalent_to: []
sources: "pstack v0.15.2 — Lauren Tan (2026)"
raw: ["../../raw/pstack/2026-09-11-pstack-plugin.md"]
updated: 2026-09-11
---

# poteto-agent

The subagent that carries the framework's full style into a delegate. Spawned as `subagent_type: "poteto-agent"` with `is_background: true`. Its whole body is one instruction: read [[pstack-poteto-mode]]'s SKILL.md in full before any work, including its inline principles index, and navigate to a leaf `principle-*` skill whenever that principle is applied.

The reason it exists is a **context-inheritance problem** that this wiki has not seen paged elsewhere. A generic subagent (`generalPurpose`) starts without the parent's mode skill loaded, so a delegate spawned mid-playbook silently drops the principles, the reply rules, and the autonomy policy. pstack's own documentation is blunt about it: *"Substituting `generalPurpose` skips that read and drifts."* [[pstack-poteto-mode]] therefore mandates this subagent type for any delegate spawned inside a playbook step, while explicitly exempting the routed workflow skills ([[pstack-how]], [[pstack-why]], [[pstack-interrogate]], [[pstack-reflect]], [[pstack-swarm]]) which set their own subagent types deliberately to get *model diversity* — respect what the skill prescribes, do not override to `poteto-agent`.

Its agent definition also carries a resumption rule: resume an existing `poteto-agent` for the conversation rather than spawning a sibling.

## See Also
- [[pstack-poteto-mode]] — the skill this agent reads in full; the two route through the same wrapper.
- [[pstack-comment-sicko]] — the framework's other shipped subagent.
- [[pattern-fresh-context-subagents]] — the technique, with this as the style-preserving variant.
