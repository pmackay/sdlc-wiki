---
type: pattern
sources: "obra/superpowers — skills/verification-before-completion (2026); sipyourdrink-ltd/bernstein (2026); jayminwest/seeds (2026); gastownhall/beads (2026); disler/super-simple-software-factory (2026)"
raw: ["../../raw/superpowers/2026-07-17-superpowers.md"]
updated: 2026-08-31
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

Seeds (convention only, not enforced):

- [[seeds-close]] — `--reason` is free text, but the framework's docs consistently fill it evidentially (*"Fixed; covered by store.test.ts"*), so a closed seed points at what makes its claim checkable. Nothing gates on it — the contrast with [[bernstein]]'s janitor, which *"does not trust agent claims—verifies them"*, is the point of recording it here.

Beads (recording, not verifying):

- [[beads-audit]] — an append-only `.beads/interactions.jsonl` of `llm_call` / `tool_call` entries with prompts, responses, exit codes, and issue ids, for *"auditing ('why did the agent do that?')"*, plus `good`/`bad` labels appended as new entries. Commits carry a matching `Agent-Signature:` trailer. A claim is checkable against the recorded call that produced it — but nothing checks it, the contrast with [[bernstein]]'s janitor.

## Enabled by (infrastructure)

Everywhere above this pattern is a *skill* — an Iron Law the agent is instructed to obey and may quietly rationalize away. The [execution layer](../runtime/index.md) is where it becomes a property of the substrate instead:

- [[bernstein]] (platform) — the **janitor** runs after every agent and evaluates the task's own declarative **completion signals** (`path_exists`, `glob_exists`, `test_passes`, content match) plus a gate pipeline (build · lint · type-check · tests · security · PII) over the actual diff. The agent's report is not an input. The design statement is the pattern verbatim: it *"does not trust agent claims—verifies them."* A rejected task does not merely block — `record_and_escalate()` retries it on a more capable model. This is the first documented case in the wiki of evidence-before-claims enforced *below* the agent rather than requested of it.
- [[sssf]] (library) — the same enforcement at a fraction of the weight, and stated as a design constraint on *when* a check is possible: *"Gates verify claims, never predictions. Nobody knows which files an agent will touch before it finishes"*, so gates run **after** the agent against the envelope's own declarations — `artifacts_exist`, `files_non_empty`, `json_parses`, `diff_matches_claims`, `tests_pass(cmd)`. The envelope is treated as *"a manifest of claims"* and each gate records one `{item, ok, note}` check per item, so the evidence and not just the verdict lands in the trace. Its `verdict_consistent` gate extends the pattern to a *reviewer's* honesty — an approval carrying blocking items, or a rejection naming no problem, *"is a claim the harness can refute without reading a line of the diff."* Also enforced separately from gates: an agent's `writes:` boundary is checked by diffing the working tree before and after the call, so a claim of "I changed nothing" is verified rather than trusted.

## See Also
- [[pattern-anti-rationalization]] — the sibling discipline (excuse→rebuttal tables + Red Flags); frequently co-applied.
- [[pattern-deterministic-gates]] — usually what supplies the evidence; distinct in consequence — violate this pattern and you get a false claim, violate a gate and the work is blocked.
- [[addy-doubt-driven-development]] — adversarial fresh-context self-check, a related honesty mechanism.
- [[topic-harness-engineering]] — a **sensor** that forces a computational check (the command's real output) to back an inferential claim.
- [[stage-validate]] — the empirical "does it actually work / did it actually pass" stage this pattern polices.
- [[superpowers]] — the framework whose signature this pattern is.
- [[bernstein]] — the runtime that enforces this below the agent (janitor completion signals + gate pipeline) rather than instructing it.
