---
type: capability
subtype: command
belongs_to: "[[openspec]]"
implements: "[[stage-validate]]"
applies: ["[[pattern-spec-driven-development]]"]
equivalent_to: ["[[gsd-verify-work]]", "[[gsd-verifier]]", "[[speckit-converge]]"]
sources: "Fission-AI/OpenSpec docs — commands.md (2026)"
raw: ["../../raw/openspec/2026-07-04-openspec-framework.md"]
updated: 2026-07-04
---

# /opsx:verify

`/opsx:verify` — "Validate that implementation matches your change artifacts." It checks
three things against the change folder:

- **Completeness** — are all requirements met?
- **Correctness** — does the implementation align with the spec deltas?
- **Coherence** — is it consistent with `design.md`?

It **reports issues without blocking archive** — advisory, in keeping with OpenSpec's *fluid
not rigid* principle (no hard phase gate). Shipped in the expanded profile; paged here
because it is OpenSpec's only [[stage-validate]] capability. The CLI `openspec validate`
is a lower-level sibling that checks artifact *correctness and consistency* (well-formed
deltas) rather than implementation conformance.

## Cross-framework equivalents

`verify` is a **functional / spec-conformance** validator: it confirms the build *does what
the spec says*. That puts it alongside GSD's [[gsd-verify-work]] (conversational UAT with
auto-diagnosis) and its post-execution reviewer [[gsd-verifier]] (goal-backward analysis) —
`equivalent_to` both. Spec Kit's [[speckit-converge]] joins this cluster: it also assesses
the implementation against the spec/plan/tasks, but where `verify` merely *reports*
(advisory, non-blocking), `converge` is action-oriented — it appends the gap back into
`tasks.md` as new work. It sits on the *does it work* side of [[stage-validate]], **not** the
*is it good* quality-review side ([[addy-code-review]] et al.); OpenSpec ships no quality-gate
review, so it does not bear on the parked `stage-review` split.

## See Also
- [[openspec-apply]] — produces the implementation this checks.
- [[openspec-archive]] — the finalization that verification precedes (but does not gate).
- [[gsd-verify-work]] · [[gsd-verifier]] — functional-validation counterparts.
- [[speckit-converge]] — Spec Kit's assess-vs-spec counterpart; re-plans the gap instead of only reporting it.
- [[stage-validate]] — the canonical stage this implements.
