---
type: capability
subtype: skill
belongs_to: "[[superpowers]]"
implements: "[[stage-review]]"
delegates_to: []
produces: []
applies: ["[[pattern-anti-rationalization]]"]
equivalent_to: []
sources: "Superpowers v6.1.1 (2026)"
raw: ["../../raw/superpowers/2026-07-17-superpowers.md"]
updated: 2026-07-17
---

# receiving-code-review

The **reception** side of review — how the agent should *respond* to feedback: *"Code review requires technical evaluation, not emotional performance."* A response pattern of read → restate (or ask) → verify against the codebase → evaluate for *this* codebase → respond (technical acknowledgment or reasoned pushback) → implement one item at a time, testing each.

> **Forbidden responses:** *"You're absolutely right!"*, *"Great point!"*, *"Thanks for catching that!"* — any performative agreement or gratitude. *"Actions speak. Just fix it."* Also forbidden: blind implementation before verification, and implementing a partially-understood batch (clarify **all** unclear items first — items may be related).

It distinguishes trusted (human partner) from external feedback (be skeptical: does it break things? is it YAGNI? does the reviewer have full context?), tells the agent **when to push back** (breaks functionality, violates YAGNI, wrong for the stack, conflicts with prior decisions) and how (technical reasoning, reference working tests), and how to gracefully correct its own pushback when wrong. This is [[pattern-anti-rationalization]] pointed at the *social* pressure to agree.

**Novel capability — no other framework here pages the review-reception side.** Every other framework in the wiki models *producing* review ([[sp-requesting-code-review]] and the whole code-review cluster); Superpowers is alone in also codifying how to *receive* it, making it a distinctive contribution to [[stage-review]]. (It is *not* set `equivalent_to` any capability — it has no counterpart.)

## See Also
- [[sp-requesting-code-review]] — the production side; this skill handles the findings it returns.
- [[addy-code-review]] · [[ce-code-review]] · [[gstack-review]] — review producers whose output this reception discipline would consume.
- [[pattern-anti-rationalization]] — the technique it embodies (no performative agreement).
- [[stage-review]] — the canonical stage this implements.
