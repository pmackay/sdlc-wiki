---
type: capability
subtype: skill
belongs_to: "[[superpowers]]"
implements: "[[stage-validate]]"
delegates_to: []
produces: []
applies: ["[[pattern-evidence-before-claims]]", "[[pattern-anti-rationalization]]", "[[pattern-deterministic-gates]]"]
equivalent_to: []
sources: "Superpowers v6.1.1 (2026)"
raw: ["../../raw/superpowers/2026-07-17-superpowers.md"]
updated: 2026-08-31
---

# verification-before-completion

Superpowers' signature honesty gate: **never claim work is complete, fixed, or passing without fresh verification evidence** ([[pattern-evidence-before-claims]]). *"Claiming work is complete without verification is dishonesty, not efficiency."*

> **The Iron Law:** *"NO COMPLETION CLAIMS WITHOUT FRESH VERIFICATION EVIDENCE."* If you haven't run the verification command **in this message**, you cannot claim it passes.

The **gate function** is mechanical: before asserting any status or even expressing satisfaction — identify the command that proves the claim → run it fresh and complete → read the full output, check the exit code, count failures → only then state the claim *with* its evidence. A "Common Failures" table maps each claim to what actually proves it and what does *not* (tests pass ⇒ test-command output showing 0 failures, **not** "should pass"; agent completed ⇒ VCS diff shows changes, **not** the agent's success report). Red Flags include the giveaway words — "should", "probably", "seems to" — and *any expression of satisfaction* ("Great!", "Perfect!", "Done!") before verification.

This is a functional-validation discipline: it asks *does it actually work / did the command actually pass* — so it implements [[stage-validate]] (run it and observe), the empirical sibling of the quality gate [[stage-review]]. It has **no direct counterpart** in the other frameworks: where GSD's [[gsd-verifier]] and OpenSpec's [[openspec-verify]] verify the *build against a goal/spec*, this skill verifies the *agent's own claims against fresh evidence* — a cross-cutting anti-dishonesty gate rather than a spec-conformance check. It is the clearest exemplar of [[pattern-evidence-before-claims]], and kin to [[addy-doubt-driven-development]]'s adversarial self-check.

## See Also
- [[sp-systematic-debugging]] — calls this to confirm a fix before any "fixed" claim.
- [[sp-subagent-driven-development]] — its "trust the diff, not the agent's report" rule is this discipline applied to delegation.
- [[addy-doubt-driven-development]] — the nearest kin (adversarial fresh-context self-review).
- [[pattern-evidence-before-claims]] · [[pattern-anti-rationalization]] · [[pattern-deterministic-gates]] — the techniques applied (the last being the exit-code check its gate function demands).
- [[stage-validate]] — the canonical stage this implements; contrast [[stage-review]] (quality).
