---
type: capability
subtype: sub-agent
belongs_to: "[[compound-engineering]]"
implements: "[[stage-review]]"
delegates_to: []
produces: ["[[artifact-security-audit]]"]
applies: ["[[pattern-fresh-context-subagents]]", "[[pattern-adversarial-review]]"]
equivalent_to: ["[[addy-security-auditor]]"]
sources: "Compound Engineering — EveryInc/compound-engineering-plugin (2026)"
raw: ["../../raw/compound-engineering/2026-07-04-compound-engineering-every.md", "../../raw/compound-engineering/2026-07-04-compound-engineering-plugin.md"]
updated: 2026-07-05
---

# ce-security-sentinel

An elite **Application Security Specialist** that thinks like an attacker — *where are the
vulnerabilities, how could this be exploited?* — and performs comprehensive security audits
(input validation, auth, secrets, injection, etc.) to find and report vulnerabilities before
they can be exploited → [[artifact-security-audit]].

It implements [[stage-review]] (security quality gate) and is a **direct** counterpart to
Addy's [[addy-security-auditor]]. In Compound Engineering it is also dispatched by [[ce-compound]]
as part of the learning council — on a durable-learning invocation it converts its analysis into
lesson validation (vulnerability class, exploit path, prevention guidance) rather than a
standalone audit, feeding [[artifact-solution-doc]].

## Cross-framework equivalents
`ce-security-sentinel` ↔ [[addy-security-auditor]] (`equivalent_to`) — both are attacker-minded
OWASP security reviewers producing a security audit.

## See Also
- [[addy-security-auditor]] — the direct counterpart persona.
- [[ce-code-review]] — dispatches a security lens; [[ce-compound]] — dispatches this agent to mine security lessons.
- [[stage-review]] — the canonical stage this supports; [[stage-learn]] — its compound-council role.
