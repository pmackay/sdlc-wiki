---
type: capability
subtype: skill
belongs_to: "[[addy-agent-skills]]"
implements: "[[stage-release]]"
delegates_to: []
produces: []
applies: []
equivalent_to: []
sources: "Addy Osmani — Agent Skills (2026)"
raw: ["../../raw/addy-agent-skills/2026-07-04-agent-skills.md"]
updated: 2026-07-04
---

# Deprecation & Migration

Starts from a **code-as-liability** mindset: every line has ongoing cost — tests, docs, security patches, onboarding overhead — so code that no longer earns its keep should go. Because Hyrum's Law makes any observable behavior something a consumer depends on, removal requires *active* migration, not just an announcement. The skill distinguishes **advisory** deprecation (optional, migrate on your own timeline) from **compulsory** (hard deadline, but you must supply migration tooling), defaulting to advisory.

It supplies a build-the-replacement-first migration process, patterns (strangler, adapter, feature-flag switching), the Churn Rule (infrastructure owners migrate their own users), and a protocol for removing **zombie code** — unowned code that everyone depends on. This is really a maintenance activity folded into the release stage for now, since no other framework in the wiki covers it.

## See Also
- [[pattern-contract-first]] — the discipline strained when retiring a contract consumers depend on.
- [[stage-release]] — the stage this is folded into.
