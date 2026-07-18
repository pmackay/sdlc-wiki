---
type: capability
subtype: skill
belongs_to: "[[addy-agent-skills]]"
implements: "[[stage-align]]"
delegates_to: []
produces: []
applies: ["[[pattern-grilling]]"]
equivalent_to: ["[[mp-grill-me]]", "[[gsd-discuss-phase]]", "[[speckit-clarify]]", "[[ce-brainstorm]]", "[[gstack-office-hours]]", "[[sp-brainstorming]]"]
sources: "Addy Osmani — Agent Skills (2026)"
raw: ["../../raw/addy-agent-skills/2026-07-04-agent-skills.md"]
updated: 2026-07-04
---

# Interview Me

Extracts what the user *actually* wants rather than what they think they should want,
by asking **one question at a time — each with a guess attached** — until the agent can
predict the user's reaction to the next three questions (~95% confidence). The distinctive
move is the confidence number in the opening hypothesis, which forces honesty about how
much is still unknown, and the "if you didn't have to justify it to anyone, what would you
actually want?" probe that cuts through best-practice talk.

It sits at the very front of the funnel: run before any spec, plan, or code, and hand the
confirmed statement of intent downstream to [[addy-idea-refine]] or a spec. It implements
[[stage-align]] and applies the cross-framework [[pattern-grilling]] technique.

## See Also
- [[mp-grill-me]] — the Matt Pocock equivalent in the grilling cluster.
- [[gsd-discuss-phase]] — the GSD equivalent alignment step.
- [[speckit-clarify]] — Spec Kit's grilling step; resolves spec ambiguities flagged as `[NEEDS CLARIFICATION]`.
- [[stage-align]] — the canonical stage this implements.
