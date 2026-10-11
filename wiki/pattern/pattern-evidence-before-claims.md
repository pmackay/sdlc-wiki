---
type: pattern
sources: "obra/superpowers — skills/verification-before-completion (2026); sipyourdrink-ltd/bernstein (2026); jayminwest/seeds (2026); gastownhall/beads (2026); disler/super-simple-software-factory (2026); pstack v0.15.2 — Lauren Tan (2026); Tessl docs (2026); Builder.io — BuilderIO/skills (2026)"
raw: ["../../raw/superpowers/2026-07-17-superpowers.md"]
updated: 2026-10-11
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

pstack — **co-signature; the only framework here that *grades* evidence rather than merely requiring it**:

- [[pstack-blast-radius]] — a five-rung ladder from *"you said so"* (worthless) through *pointed at the line*, *showed the bad case cannot happen*, *ran it*, to *reproduced it in the running app*. The writeup must **say where it stopped**, and anything below rung 4 is marked **unproven**. Its premise: *"a blast-radius writeup that sounds right is worthless, it reads as convincing whether or not it's true."*
- [[pstack-figure-it-out]] — verdicts are VERIFIED, NOT VERIFIED, or INCONCLUSIVE. ***Inconclusive is not a pass. Do not hide a negative.*** And: *"when something passes too easily, suspect the observation method before the system."*
- [[pstack-principle-prove-it-works]] — the principle statement: verify against the real artifact, not a proxy, a self-report, or "it compiles".
- [[pstack-create-verification-skill]] — writes the proof standards into every generated harness: the real user path not a test-only endpoint, the action *and* the resulting state, side effects alongside what is visible.
- [[pstack-poteto-mode]] — every claim in the reply carries its evidence or its label in the same sentence: **measured, inferred, or guess**.

Tessl — the same discipline pointed at the *instructions* rather than the work:

- [[tessl-eval]] — *"Every change ships with evidence instead of a guess."* Runs the agent with and without the context and scores the difference, so a claim that a skill helps is measured rather than asserted ([[pattern-capability-evals]]).

builder-skills (**co-signature**: applied to the agent's *inputs* as much as its outputs):

- [[builder-factory-collect]] · [[builder-factory-lookback]] · [[builder-factory-human-digest]] — *"Keep `empty`, `unavailable`, and `truncated` distinct"*; *"Never report 'no recurring issues' when coverage is partial."* A broken connector is not a clean queue.
- [[builder-factory-ship]] — *"a merge is not live proof"*; an inconclusive result is never turned into success.
- [[builder-factory]] — a schedule written to YAML *"is only a request"* until the saved job is read back.
- [[builder-efficient-fable]] · [[builder-efficient-frontier]] · [[builder-agent-watchdog]] — subagent and other-agent reports are *"leads, not facts"* until the cited files are reopened.
- [[builder-an]] · [[builder-webmcp]] · [[builder-visual-edit]] — one read, one smallest mutation, one readback; a queued task is not proof an edit completed.

Matt Pocock — Skills for Real Engineers:

- [[mp-pr]] — every PR body carries before/after evidence: screenshots "S-tier", the exact failing-then-passing test "A-tier" (v1.3.0).

## Enabled by (infrastructure)

Everywhere above this pattern is a *skill* — an Iron Law the agent is instructed to obey and may quietly rationalize away. The [execution layer](../runtime/index.md) is where it becomes a property of the substrate instead:

- [[bernstein]] (platform) — the **janitor** runs after every agent and evaluates the task's own declarative **completion signals** (`path_exists`, `glob_exists`, `test_passes`, content match) plus a gate pipeline (build · lint · type-check · tests · security · PII) over the actual diff. The agent's report is not an input. The design statement is the pattern verbatim: it *"does not trust agent claims—verifies them."* A rejected task does not merely block — `record_and_escalate()` retries it on a more capable model. This is the first documented case in the wiki of evidence-before-claims enforced *below* the agent rather than requested of it.
- [[sssf]] (library) — the same enforcement at a fraction of the weight, and stated as a design constraint on *when* a check is possible: *"Gates verify claims, never predictions. Nobody knows which files an agent will touch before it finishes"*, so gates run **after** the agent against the envelope's own declarations — `artifacts_exist`, `files_non_empty`, `json_parses`, `diff_matches_claims`, `tests_pass(cmd)`. The envelope is treated as *"a manifest of claims"* and each gate records one `{item, ok, note}` check per item, so the evidence and not just the verdict lands in the trace. Its `verdict_consistent` gate extends the pattern to a *reviewer's* honesty — an approval carrying blocking items, or a rejection naming no problem, *"is a claim the harness can refute without reading a line of the diff."* Also enforced separately from gates: an agent's `writes:` boundary is checked by diffing the working tree before and after the call, so a claim of "I changed nothing" is verified rather than trusted.

## Supplied by (registry)

- [[tessl]] — makes evidence a **condition of publication** rather than a discipline the author has to keep. A review score is attached automatically on publish and shown in search results, and [[tessl-eval]] supplies the measured with/without difference, so the claim *"this skill helps"* arrives at the installer already carrying its evidence.

## See Also
- [[pattern-tooling-leverage]] — the constructive complement: build the thing that produces the proof, so a reviewer can rerun it.
- [[pattern-anti-rationalization]] — the sibling discipline (excuse→rebuttal tables + Red Flags); frequently co-applied.
- [[pattern-deterministic-gates]] — usually what supplies the evidence; distinct in consequence — violate this pattern and you get a false claim, violate a gate and the work is blocked.
- [[addy-doubt-driven-development]] — adversarial fresh-context self-check, a related honesty mechanism.
- [[topic-harness-engineering]] — a **sensor** that forces a computational check (the command's real output) to back an inferential claim.
- [[stage-validate]] — the empirical "does it actually work / did it actually pass" stage this pattern polices.
- [[superpowers]] — the framework whose signature this pattern is.
- [[bernstein]] — the runtime that enforces this below the agent (janitor completion signals + gate pipeline) rather than instructing it.
