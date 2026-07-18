---
type: capability
subtype: skill
belongs_to: "[[superpowers]]"
implements: "[[stage-implement]]"
delegates_to: []
produces: ["[[artifact-atomic-commit]]"]
applies: ["[[pattern-test-driven-development]]", "[[pattern-anti-rationalization]]"]
equivalent_to: ["[[mp-tdd]]", "[[addy-tdd]]"]
sources: "Superpowers v6.1.1 (2026)"
raw: ["../../raw/superpowers/2026-07-17-superpowers.md"]
updated: 2026-07-17
---

# test-driven-development

The RED-GREEN-REFACTOR spine of the methodology ([[pattern-test-driven-development]]): write one
minimal failing test → **watch it fail for the right reason** → write the simplest code to pass →
watch it pass with pristine output → refactor while green → repeat.

> **The Iron Law:** *"NO PRODUCTION CODE WITHOUT A FAILING TEST FIRST."* Wrote code before the test?
> *"Delete it. Start over."* — no keeping it "as reference", no "adapting" it while writing the test.
> *"If you didn't watch the test fail, you don't know if it tests the right thing."*

Its length is almost entirely [[pattern-anti-rationalization]]: an exhaustive excuse→reality table
("too simple to test", "I'll test after", "already manually tested", "deleting X hours is wasteful"
= sunk-cost fallacy, "TDD is dogmatic, I'm being pragmatic") plus a Red-Flags "STOP and start over"
list. It carries a companion `testing-anti-patterns.md` (testing mocks instead of real behavior,
test-only methods on production classes), a "when stuck" table (hard-to-test = hard-to-use design
signal), and a verification checklist. Each green step ends in a commit → [[artifact-atomic-commit]].

Superpowers is the fourth+ framework in the TDD cluster, alongside [[mp-tdd]] (red→green, refactor
moved to review), [[addy-tdd]] (red-green-refactor + Prove-It), plus GSD's `--tdd` flag and Spec Kit's
constitution-mandated TDD — all clustered at [[pattern-test-driven-development]]. Superpowers' is
among the strictest, matching Spec Kit's non-negotiability but enforcing it through rhetoric (delete-
and-restart) rather than a constitution gate.

## See Also
- [[sp-writing-plans]] — bakes this red-green micro-loop into every task's steps.
- [[sp-subagent-driven-development]] · [[sp-executing-plans]] — the executors that run this per task.
- [[sp-systematic-debugging]] — its Phase-4 fix step writes a failing test via this skill.
- [[mp-tdd]] · [[addy-tdd]] — the cross-framework TDD cluster.
- [[pattern-test-driven-development]] · [[pattern-anti-rationalization]] — the techniques applied.
- [[stage-implement]] — the canonical stage this implements.
