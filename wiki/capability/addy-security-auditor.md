---
type: capability
subtype: sub-agent
belongs_to: "[[addy-agent-skills]]"
implements: "[[stage-review]]"
delegates_to: []
produces: ["[[artifact-security-audit]]"]
applies: ["[[pattern-fresh-context-subagents]]"]
equivalent_to: ["[[ce-security-sentinel]]"]
sources: "Addy Osmani — Agent Skills (2026)"
raw: ["../../raw/addy-agent-skills/2026-07-04-agent-skills.md"]
updated: 2026-07-05
---

# Security Auditor (persona)

A Security Engineer persona focused on vulnerability detection, threat modeling, and secure-coding review. It reasons from trust boundaries — where untrusted data enters — applying STRIDE before enumerating findings, and covers input handling, auth, data protection, infrastructure, third-party integrations, and AI/LLM features, mapping issues to the OWASP Top 10 (including the LLM Top 10). Findings are classified Critical through Info, each with a concrete recommendation and, for Critical/High, a proof of concept. Its lens is deliberately practical: exploitable issues over theoretical risk, and never disabling a control as a "fix".

It runs as a stateless review subagent with a fresh context and never invokes other personas — deeper passes are initiated by the user or a slash command, not by another reviewer. It is invoked directly via [[addy-security]], and participates in the [[addy-shipping]] `/ship` fan-out, where three review subagents (this one, the code reviewer, and the test engineer) run in parallel.

## See Also
- [[addy-security]]
- [[artifact-security-audit]]
- [[addy-shipping]]
- [[stage-review]]
