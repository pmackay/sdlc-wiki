---
type: capability
subtype: command
belongs_to: "[[gstack]]"
implements: "[[stage-review]]"
delegates_to: []
produces: "[[artifact-security-audit]]"
applies: ["[[pattern-adversarial-review]]"]
equivalent_to: ["[[addy-security-auditor]]", "[[ce-security-sentinel]]", "[[addy-security]]"]
sources: "gstack — Garry Tan (2026)"
raw: ["../../raw/gstack/2026-07-05-gstack-framework.md"]
updated: 2026-07-05
---

# /cso

`/cso` — the **Chief Security Officer**. Runs an **OWASP Top 10 + STRIDE** threat model. Zero-noise by design: 17 false-positive exclusions, an 8/10+ confidence gate, and independent finding verification. Each finding includes a **concrete exploit scenario**. Produces a security audit ([[artifact-security-audit]]).

gstack's member of the cross-framework **security-audit** cluster — alongside Addy's [[addy-security-auditor]] / [[addy-security]] and Compound Engineering's [[ce-security-sentinel]]. Its signature is the noise-suppression stack (exclusions + confidence gate + independent verification) and mandatory exploit scenarios.

## See Also
- [[addy-security-auditor]] · [[ce-security-sentinel]] — attacker-minded security-audit counterparts.
- [[addy-security]] — the OWASP-hardening skill.
- [[stage-review]] — the canonical stage this implements (Review side, security lens).
