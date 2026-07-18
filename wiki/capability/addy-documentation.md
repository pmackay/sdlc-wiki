---
type: capability
subtype: skill
belongs_to: "[[addy-agent-skills]]"
implements: "[[stage-release]]"
delegates_to: []
produces: ["[[artifact-adr]]"]
applies: []
equivalent_to: []
sources: "Addy Osmani — Agent Skills (2026)"
raw: ["../../raw/addy-agent-skills/2026-07-04-agent-skills.md"]
updated: 2026-07-04
---

# Documentation & ADRs

Documents decisions, not just code — capturing the *why*, the constraints, and the alternatives
rejected, the context future humans and agents can't recover from the diff. Its highest-value
output is the **Architecture Decision Record**: a numbered, dated file (Status / Context /
Decision / Alternatives Considered / Consequences) written for any choice that would be
expensive to reverse, kept immutable and superseded rather than deleted. It also covers inline
documentation (comment the *why*, never the *what*), typed and OpenAPI API docs, READMEs, and
agent-facing context files.

This skill produces the same [[artifact-adr]] type as Matt Pocock's [[mp-grill-with-docs]], but
at decision and ship time — recording a settled choice — rather than surfacing decisions during
grilling. It sits in the release stage as the durable record a shipped change leaves behind.

## See Also
- [[artifact-adr]] — the decision record it produces.
- [[mp-grill-with-docs]] — the Matt Pocock skill that produces the same artifact during grilling.
- [[stage-release]] — the canonical stage this implements.
