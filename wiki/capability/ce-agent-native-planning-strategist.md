---
type: capability
subtype: sub-agent
belongs_to: "[[compound-engineering]]"
implements: "[[stage-plan]]"
delegates_to: []
produces: []
applies: ["[[pattern-fresh-context-subagents]]"]
equivalent_to: []
sources: "Compound Engineering — EveryInc/compound-engineering-plugin (2026)"
raw: ["../../raw/compound-engineering/2026-07-04-compound-engineering-every.md", "../../raw/compound-engineering/2026-07-04-compound-engineering-plugin.md"]
updated: 2026-07-05
---

# ce-agent-native-planning-strategist

An **agent-native planning strategist** that decides whether a plan should treat *agents as
first-class users*, then translates that decision into concrete planning inputs. It applies
pressure selectively: agent-native planning is load-bearing when the product already has an
agent/assistant/MCP/plugin/skill surface, when the work changes such surfaces, when it touches a
primary domain action (create/read/update/…/export), or when the action is repetitive,
high-volume, or naturally expressed in language.

Dispatched by [[ce-plan]], it implements [[stage-plan]]. It is a distinctive Compound
Engineering contribution — no other framework here has a planning input that asks "should agents
be first-class users of this?", reflecting Every's agent-native product stance. It pairs with the
`agent-native-reviewer` persona lens on [[ce-code-review]] (plan-time vs review-time).

## See Also
- [[ce-plan]] — the dispatcher.
- [[ce-architecture-strategist]] — the architecture-alignment planning sibling.
- [[stage-plan]] — the canonical stage this supports.
