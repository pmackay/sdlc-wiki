---
type: capability
subtype: skill
belongs_to: "[[matt-pocock-skills]]"
implements: "[[stage-implement]]"
delegates_to: []
produces: []
applies: ["[[pattern-systematic-debugging]]"]
equivalent_to: ["[[gsd-debugger]]", "[[addy-debugging]]", "[[ce-debug]]", "[[gstack-investigate]]", "[[sp-systematic-debugging]]"]
docs_url: "https://www.aihero.dev/skills-diagnosing-bugs"
sources: "Matt Pocock — Skills for Real Engineers (2026); v1.2.3–v1.3.1 (2026)"
raw: ["../../raw/matt-pocock-skills/2026-10-04-skills-v1.3.1-update.md", "../../raw/matt-pocock-skills/2026-06-28-skills-for-real-engineers.md"]
updated: 2026-10-11
---

# diagnosing-bugs

A **model-invoked** engineering skill that runs a structured debugging loop: **reproduce → minimize → hypothesize → instrument → fix** (see [[pattern-systematic-debugging]]). A feedback-loop answer to failure mode #3: don't guess, shrink the problem and test hypotheses against evidence.

Its cross-framework counterpart is GSD's [[gsd-debugger]] sub-agent, which tracks hypotheses and evidence in persistent session state — see `equivalent_to`.

> **v1.2.3 → v1.3.1 changes.** (1) **Redact** (v1.2.3). Redaction is now the first move on every command, output, and captured artifact the skill shows: write `<REDACTED>`, build loops against env vars so credentials stay in the environment, and quote only the signal-carrying lines. (2) **Post-mortem hand-off removed** (v1.3.0). Phase 6 used to hand off to [[mp-improve-codebase-architecture]], which is user-invoked and so unreachable from an often-unattended bug-fixing flow; Phase 6 is now "Cleanup" only. (3) **Retro instead** (v1.3.1). [[mp-ask-matt]] now sends you to [[mp-retro]] once the fix is in, "to ask what would have prevented the bug", and to improve-codebase-architecture only where the finding is a missing seam.

## See Also
- [[gsd-debugger]] — GSD's equivalent debugging capability.
- [[mp-tdd]] — the test-first feedback loop.
- [[addy-debugging]] — Addy's debugging skill; same evidence-driven, no-guessing loop.
- [[stage-implement]] — the canonical stage this implements.
- [[mp-retro]] — the post-fix follow-up (v1.3.1).
