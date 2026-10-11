---
type: capability
subtype: command
belongs_to: "[[tessl]]"
implements: []
delegates_to: []
produces: []
applies: ["[[pattern-measure-first]]", "[[pattern-knowledge-compounding]]"]
equivalent_to: []
sources: "Tessl docs — CLI v0.108.0 (2026)"
raw: ["../../raw/tessl/2026-09-12-tessl-platform.md"]
updated: 2026-09-12
---

# Tessl Observability

*"See where skills actually **activate** across agent sessions, not just where they're installed. Mine agent logs to find recurring mistakes."* One of the six platform components, surfaced through the web app rather than as a single CLI command.

The distinction in that sentence is the contribution. **Installed is not loaded.** A skill only fires when its description matches the task, so an organization can have a skill deployed everywhere and used nowhere, and the two states are indistinguishable from any install-side view. Activation telemetry is the only way to tell them apart — and the fix for a skill that never fires is a [[tessl-review|description]] problem, not a content one, which is why [[tessl-eval]] ships a mode that measures activation alone.

This is the wiki's first capability that measures **agent behavior in production** rather than in a test. Every other measurement here runs against a scenario or a diff; this reads what actually happened across real sessions, and it is the input the [[tessl-agent]] mines for recurring mistakes.

It also completes the layer's loop, which is worth stating as a whole: [[tessl-inventory]] finds what exists, observability finds what is *used*, [[tessl-eval]] proves whether use helps, [[tessl-review-security]] checks whether it is safe, and [[tessl-workspace]] policy decides what is allowed. Discover → observe → measure → verify → govern, applied to a corpus of instructions.

## See Also
- [[tessl-agent]] — mines this data and proposes fixes.
- [[tessl-eval]] — its activation-only mode answers the same question in a test.
- [[tessl-inventory]] — what exists, as against what runs.
- [[pattern-measure-first]] — baseline before changing.
