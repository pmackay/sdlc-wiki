---
type: pattern
sources: "Tessl docs (2026)"
raw: ["../../raw/tessl/2026-09-12-tessl-platform.md"]
updated: 2026-09-12
---

# Pattern: Supply-chain scanning (the instructions are an attack surface)

Scan a capability **before it is installed** for content designed to subvert the agent that loads it: prompt injection buried in the instructions, hardcoded secrets, suspicious download URLs, unverifiable external dependencies, and hidden or obfuscated text. Grade findings by severity and surface them at install time.

## Why it is distinctive

The wiki already has guardrail patterns, and this one is pointed the other way. [[pattern-edit-guardrails]] bounds what the agent may **write** — confirm destructive commands, lock edits to a directory, route writes through validated jobs. [[gh-aw]]'s firewall bounds what it may **reach**. This bounds what it may **read**.

That gap existed because capabilities used to be things you wrote. Once they are things you **install from a public index**, the threat model changes completely: *"installing skills from public sources exposes you to new supply-chain and prompt-injection risk"* ([[tessl]]). A skill is a prompt that runs with your agent's permissions, so an untrusted skill is untrusted code — and unlike code, it is plain prose that reads as innocuous and is not compiled, sandboxed, or diffed by anyone.

**It is the classic software supply chain, one level up.** Everything the industry learned about dependency confusion, typosquatting, and malicious transitive packages applies to a registry of skills, which is why the instance that anchors it is built by [[tessl]] (founded by Snyk's founder, with Snyk scoring built in) and why the other serious entrant is JFrog. The failure mode is familiar and the artifact is new.

**Warning is a real design choice, not a weakness.** Tessl surfaces critical and high findings at install, *"warning rather than blocking and leaving the decision to you"*, and keeps hard enforcement in a separate mechanism — install policies, which are governance rather than scanning. Contrast [[gh-aw]], whose threat-detection verdict hard-blocks every safe-output job. Both are defensible; the split matters because a scanner that blocks gets disabled, and a policy that warns gets ignored.

**Hidden text is the tell worth remembering.** Of the listed detections, *hidden and obfuscated text* is the one with no analogue in ordinary dependency scanning. It exists because the consumer is a language model reading prose, so an attack can hide in whitespace, comments, or encoding that no human reviewer would notice and no linter would flag.

## Supplied by (registry)

- [[tessl]] — [[tessl-review-security]] runs the scan and can gate CI on severity; findings are graded and surfaced on install, and a serious finding on a third-party skill *"can signal a supply-chain attack, so treat it with care"*. [[tessl-inventory]] is the precondition at org scale: you cannot scan an estate you have not indexed.

## Applied by (backlinks)

Tessl:

- [[tessl-review-security]] — the scan itself, gateable in CI on severity.
- [[tessl-install]] — can install from **a specific commit**, noted in the docs as useful *"when the registry shows security results for that commit"* — provenance leaking into the install syntax.
- [[tessl-inventory]] — the precondition at org scale: you cannot scan an estate you have not indexed.

## See Also
- [[pattern-edit-guardrails]] — bounds what the agent may write; this bounds what it may read. The pair covers both directions.
- [[pattern-deterministic-gates]] — where a scan becomes enforcement (a CI gate failing on high or critical).
- [[pattern-source-grounding]] — the optimistic use of external material; this is the pessimistic one.
- [[artifact-capability-bundle]] — the unit being scanned.
- [[topic-ai-native-sdlc]] — managed settings with marketplace pinning, the enterprise control that sits alongside scanning.
