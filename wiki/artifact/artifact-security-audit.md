---
type: artifact
sources: "Addy Osmani — Agent Skills (2026); Tessl docs (2026)"
updated: 2026-09-12
---

# Artifact: Security audit report

A vulnerability and threat-model assessment of a change: input handling / injection vectors, authentication & authorization (including IDOR), data protection and secrets, dependency CVEs, scored against the **OWASP Top 10**. Prioritizes practical, exploitable issues over theoretical risk, each with a recommended mitigation.

## Produced by (backlinks)
- [[addy-security]] — the security-and-hardening skill.
- [[addy-security-auditor]] — the Security-Engineer persona (also in the `/ship` fan-out).

- [[ce-security-sentinel]] — Compound Engineering's attacker-minded security auditor (also mines security lessons for ce-compound).
- [[gstack-cso]] — gstack's Chief Security Officer: OWASP Top 10 + STRIDE audit with concrete exploit scenarios.

Tessl — the first security audit here whose subject is **the toolchain rather than the product**:

- [[tessl-review-security]] — scans a skill or plugin for prompt injection buried in instructions, hardcoded secrets, suspicious download URLs, unverifiable external dependencies, and hidden or obfuscated text; Snyk-powered, severity-graded, gateable in CI ([[pattern-supply-chain-scanning]]). Where [[gstack-cso]] and [[addy-security-auditor]] model exploits against the shipped application, this one asks whether the instructions the agent is about to load are trying to subvert it.

## See Also
- [[artifact-review-report]] · [[artifact-perf-audit]] — the sibling reports merged at `/ship`.
- [[stage-review]] — the stage this artifact gates.
