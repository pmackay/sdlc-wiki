---
type: sdlc-stage
aka: { gsd: "Verify (UAT)", addy-agent-skills: "Verify (browser-testing)", openspec: "verify", speckit: "converge", compound-engineering: "test / dogfood", gstack: "Test (QA / benchmark / iOS)", superpowers: "verification-before-completion" }
sources: "Synthesized from GSD + Addy Osmani + OpenSpec + Spec Kit + Compound Engineering + gstack + Superpowers (2026)"
updated: 2026-07-17
---

# Stage: Validate

Canonical lifecycle stage: **confirm the built software *works*** — that it satisfies its
requirements when actually run: user-acceptance testing, runtime/browser testing, goal-backward
verification, and spec-conformance checking, diagnosing and fixing functional gaps. Framework-
neutral name (was `stage-verify`, GSD's term). This is the *empirical* half of "confirm the build
is sound" — **run it and observe**. The *evaluative* half — judging whether the code is **good**
(correctness review, security, performance, simplicity) — is now the sibling stage [[stage-review]].

**Derived projection** — evidence is the capabilities that `implements: [[stage-validate]]`.

> **Narrowed on 2026-07-05: the quality-review half was split out to [[stage-review]].** This was
> long the widest stage, bundling *does it work* (functional) with *is it good* (quality). Addy
> Osmani treated them as two distinct phases (Verify ∥ Review); **gstack became the second**
> framework with that clean partition (a **Test** phase ∥ a **Review** phase), clearing the
> ≥2-framework bar. Validate now holds only the **functional** side; see [[stage-review]] for the
> quality gate. GSD, OpenSpec, and Spec Kit ship *only* a functional validator (no review), which
> is the evidence that made the split clean.

## Implemented by (backlinks)

GSD — *Verify* (does it work):

- [[gsd-verify-work]] — conversational UAT with auto-diagnosis → [[artifact-uat-md]].
- [[gsd-verifier]] — goal-backward analysis after execution (does the build achieve the goal).

Addy Osmani — Agent Skills — *Verify* (does it work):

- [[addy-browser-testing]] — live runtime data via Chrome DevTools MCP.

OpenSpec — *Verify* (does it match the spec):

- [[openspec-verify]] — check implementation vs artifacts for completeness, correctness, coherence (advisory, non-blocking).

Spec Kit — *Verify* (does it match the spec, then re-plan the gap):

- [[speckit-converge]] — assess the codebase against spec/plan/tasks and **append the outstanding work back into `tasks.md`** as new tasks (action-oriented; loops back to [[stage-plan]] / [[stage-implement]]).

Compound Engineering — *functional testing*:

- [[ce-test-browser]] — diff-scoped end-to-end browser tests; counterpart to [[addy-browser-testing]].
- [[ce-dogfood]] — autonomous, self-fixing diff-scoped browser QA ([[pattern-autonomous-loop]]).
- [[ce-test-xcode]] — iOS simulator build/test via XcodeBuildMCP.

gstack — its **Test** sprint phase (does it work) + enabling browser infrastructure:

- [[gstack-qa]] — real-browser QA that fixes bugs, re-verifies, and generates a regression test per fix → [[artifact-atomic-commit]] ([[pattern-autonomous-loop]], [[pattern-test-driven-development]]).
- [[gstack-qa-only]] — the same methodology, report-only.
- [[gstack-ios-qa]] — live-device iOS QA on real hardware (USB/Tailscale); counterpart to [[ce-test-xcode]].
- [[gstack-ios-fix]] — autonomous iOS bug fixer with regression-snapshot capture ([[pattern-autonomous-loop]]).
- [[gstack-browse]] — the persistent headless-Chromium daemon ("the eyes") behind all live testing; [[gstack-open-gstack-browser]] (headed) and [[gstack-setup-browser-cookies]] (auth) support it, and [[gstack-ios-sync]] keeps the iOS bridge current.

Superpowers — *evidence-gate validation* (do the claims hold):

- [[sp-verification-before-completion]] — the Iron Law "no completion claims without fresh verification evidence": run the command, read the full output, then claim ([[pattern-evidence-before-claims]]). A distinctive validator — it verifies the **agent's own success claims** against reproducible command output rather than checking the build against a spec/goal (the empirical honesty half of "confirm the build is sound").

(Note: [[gstack-benchmark]] is a performance audit, so it lives in [[stage-review]] with the other
performance capabilities, not here — even though gstack colloquially groups it under "Test".)

## Cross-framework equivalents

The frameworks check *different functional things* — complementary lenses. GSD's [[gsd-verify-work]]
checks **functional** correctness via UAT; OpenSpec's [[openspec-verify]] and Spec Kit's
[[speckit-converge]] add **spec-conformance** (does the build satisfy the change's
requirements/design); Addy's [[addy-browser-testing]] and CE's [[ce-test-browser]] / [[ce-dogfood]]
plus gstack's [[gstack-qa]] add **runtime browser testing** with real data; CE's [[ce-test-xcode]]
and gstack's [[gstack-ios-qa]] cover native iOS. GSD's [[gsd-verifier]], OpenSpec's
[[openspec-verify]], and Spec Kit's [[speckit-converge]] are the nearest analogues (all
spec/goal-backward); Spec Kit's is distinctive in being **action-oriented** — it re-plans the gap
into new tasks rather than only reporting it ("bidirectional feedback"). Superpowers'
[[sp-verification-before-completion]] adds a **different lens entirely** — not "does the build match
the spec" but "did the agent actually run the check it's claiming passed" — a cross-cutting
[[pattern-evidence-before-claims|evidence gate]] applied at *every* "done", with no counterpart in
the other frameworks (not set `equivalent_to`). Its presence also makes Superpowers the **third
framework** (after Addy and gstack) to cleanly separate functional *validate* from quality
*review* — reinforcing the 2026-07-05 split below.

> **Resolved 2026-07-05 (the former `stage-review` split candidate).** The quality-gate activities
> that used to be parked here — code review, security, performance, simplification, architecture &
> design/DX audit — were **promoted** into [[stage-review]] once gstack became the second framework
> (after Addy) to treat *Verify* and *Review* as distinct lifecycle phases. See [[stage-review]] for
> that stage and its clusters.

## See Also
- [[stage-review]] — the sibling split out of this stage (2026-07-05): validate confirms the software **works**, review confirms it is **good**.
- [[stage-implement]] — produces what is validated.
- [[stage-release]] — runs once validation (and review) pass.
