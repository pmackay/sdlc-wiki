---
type: capability
subtype: command
belongs_to: "[[tessl]]"
implements: []
delegates_to: []
produces: ["[[artifact-security-audit]]"]
applies: ["[[pattern-supply-chain-scanning]]", "[[pattern-deterministic-gates]]"]
equivalent_to: ["[[gstack-cso]]", "[[addy-security-auditor]]"]
sources: "Tessl docs — CLI v0.108.0 (2026)"
raw: ["../../raw/tessl/2026-09-12-tessl-platform.md"]
updated: 2026-09-12
---

# tessl review run security

Scan a skill or plugin for risky or malicious content before it reaches a developer, with Snyk-powered scoring. The wiki's anchor for [[pattern-supply-chain-scanning]], and its first capability whose subject is **the instructions rather than the code**.

What it looks for: **prompt injection buried in instructions**, hardcoded secrets, suspicious download URLs, unverifiable external dependencies, and **hidden or obfuscated text**. Findings are graded by severity, and `--threshold` fails CI on high or critical.

The last detection is the one with no analogue in ordinary dependency scanning, and it explains why this is a distinct pattern rather than a variation on package auditing. The consumer here is a language model reading prose, so an attack can hide in whitespace, encoding, or text no human reviewer would notice and no linter would flag. A skill is a prompt that runs with your agent's permissions; an untrusted skill is untrusted code that happens to look like documentation.

**It warns rather than blocks**, by design. Critical and high findings are surfaced at install, *"warning rather than blocking and leaving the decision to you"*, with hard enforcement kept in a separate mechanism ([[tessl-workspace]]'s install policies). The docs are blunt about the stakes: *"a serious finding on a third-party skill can signal a supply-chain attack, so treat it with care."* Compare [[gh-aw]], whose threat verdict hard-blocks every safe-output job — both are defensible, and the split matters because a scanner that blocks gets disabled while a policy that warns gets ignored.

Its cross-framework counterparts ([[gstack-cso]], [[addy-security-auditor]]) audit the *product* for OWASP and STRIDE issues. This audits the *toolchain that builds it*.

## See Also
- [[pattern-supply-chain-scanning]] — the pattern this anchors.
- [[tessl-inventory]] — the precondition at org scale; you cannot scan an estate you have not indexed.
- [[tessl-workspace]] — where install policy turns a finding into enforcement.
- [[gstack-cso]] · [[addy-security-auditor]] — product-side security audits, for contrast.
