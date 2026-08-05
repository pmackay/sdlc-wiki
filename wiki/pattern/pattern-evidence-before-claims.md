---
type: pattern
sources: "obra/superpowers — skills/verification-before-completion (2026)"
raw: ["../../raw/superpowers/2026-07-17-superpowers.md"]
updated: 2026-07-17
---

# Pattern: Evidence before claims (verify, then assert)

Before making **any** statement that work is complete, fixed, or passing — including a mere expression of satisfaction ("Great!", "Done!") — run the command that would prove it, read the full output (exit code, failure count), and only then state the claim *with* that fresh evidence. The discipline treats an unverified success claim as **dishonesty, not optimism**: *"If you haven't run the verification command in this message, you cannot claim it passes."*

Superpowers makes it a first-class skill ([[sp-verification-before-completion]], the Iron Law *"no completion claims without fresh verification evidence"*) with a mechanical gate function and a table mapping each claim to what actually proves it — tests pass ⇒ the test command's 0-failures output (not "should pass"); agent completed ⇒ the VCS diff (not the agent's own success report).

## Why it's distinctive

It is adjacent to but distinct from its neighbors. [[pattern-anti-rationalization]] stops the agent talking itself *out of a process*; evidence-before-claims stops it declaring a process *finished* without proof — the two often ship together in the same skill but target different lies. It differs from spec-conformance verification ([[gsd-verifier]], [[openspec-verify]], which check the *build* against a goal/spec) by checking the *agent's own assertions* against reproducible command output — a cross-cutting honesty gate, applied at every "done", not a single validate step. It is the concrete technique behind Superpowers' *"Evidence over claims"* philosophy pillar, and kin to [[addy-doubt-driven-development]]'s adversarial self-review.

## Applied by (backlinks)

Superpowers:

- [[sp-verification-before-completion]] — the signature skill: run → read → verify → only then claim.
- [[sp-subagent-driven-development]] — applies it to delegation ("trust the diff, not the agent's report").
- [[sp-systematic-debugging]] — Phase 4 confirms a fix with fresh evidence before any "fixed" claim.

## See Also
- [[pattern-anti-rationalization]] — the sibling discipline (excuse→rebuttal tables + Red Flags); frequently co-applied.
- [[addy-doubt-driven-development]] — adversarial fresh-context self-check, a related honesty mechanism.
- [[topic-harness-engineering]] — a **sensor** that forces a computational check (the command's real output) to back an inferential claim.
- [[stage-validate]] — the empirical "does it actually work / did it actually pass" stage this pattern polices.
- [[superpowers]] — the framework whose signature this pattern is.
