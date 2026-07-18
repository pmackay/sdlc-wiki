---
type: capability
subtype: skill
belongs_to: "[[addy-agent-skills]]"
implements: "[[stage-review]]"
delegates_to: ["[[addy-security-auditor]]"]
produces: ["[[artifact-security-audit]]"]
applies: []
equivalent_to: []
sources: "Addy Osmani — Agent Skills (2026)"
raw: ["../../raw/addy-agent-skills/2026-07-04-agent-skills.md"]
updated: 2026-07-05
---

# Security & Hardening

Treats every external input as hostile, every secret as sacred, and every authorization check
as mandatory. It starts with a five-minute threat model — map trust boundaries, name the
assets, run STRIDE, write abuse cases — then supplies OWASP Top 10 prevention patterns
(injection, broken auth, XSS, broken access control, SSRF), auth and secrets-management
practices, dependency auditing with an `npm audit` triage tree, and even an OWASP-LLM section
for AI features.

Its distinctive mechanism is the **three-tier boundary system**: *Always Do* controls with no
exceptions (validate input, parameterize queries, hash passwords, set security headers), *Ask
First* actions requiring human approval (new auth flows, new PII storage, CORS changes), and
*Never Do* prohibitions (committing secrets, logging sensitive data, trusting client-side
validation). It emits an [[artifact-security-audit]] and can delegate deep auditing to the
[[addy-security-auditor]] persona. Security is a new domain for this wiki.

## See Also
- [[addy-security-auditor]] — the persona this delegates auditing to.
- [[artifact-security-audit]] — the audit it produces.
- [[stage-review]] — the canonical stage this implements.
