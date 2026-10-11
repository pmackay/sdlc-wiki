---
type: capability
subtype: skill
belongs_to: "[[pstack]]"
implements: "[[stage-review]]"
delegates_to: ["[[pstack-comment-sicko]]", "[[pstack-architect]]", "[[pstack-how]]", "[[pstack-why]]"]
produces: ["[[artifact-review-report]]"]
applies: ["[[pattern-adversarial-review]]", "[[pattern-deep-modules]]", "[[pattern-deterministic-gates]]"]
equivalent_to: ["[[addy-code-simplification]]", "[[ce-simplify-code]]"]
sources: "pstack v0.15.2 — Lauren Tan (2026)"
raw: ["../../raw/pstack/2026-09-11-pstack-plugin.md"]
updated: 2026-09-11
---

# /no-comments

Spawns [[pstack-comment-sicko]], audits its report, and acts on the accepted findings. [[pstack-poteto-mode]] fires it before review. The division of labour is strict: the subagent flags and never writes application code, this skill does the fixing.

Most of the skill is the **audit of its own reviewer**, which is unusual and is the reason it is paged separately. It rejects application-code edits, scope escapes, exception-protected deletions, misstated `MUST KILL` reasons, and flags that treat kept intentional code as guilty — and it rejects *without restoring the comments*. A keep survives only with proof it is about something outside the team's control. Thin `IMPORTANT` or `do not remove` claims get [[pstack-how]] or [[pstack-why]] run on their symbol before judgment. The asymmetry that resolves ambiguity is explicit: **if a kill is ambiguous, do not restore; if a keep is refuted or still ambiguous, delete it.** A rejected report is reverted and rerun once with the failure named; a second rejection is reported open and fails the skill.

**Its contribution is treating a comment as a bug report against the code.** Accepted findings are not deleted and forgotten. Trivial ones are fixed directly by deleting a dead path, dropping a parameter, or using the real API; anything needing a shape runs [[pstack-architect]] once for the accepted set and **stops at the sketch** (architect shapes, this skill implements). Then the **smallest root-cause fix in scope** is implemented and every named workaround removed. [[pstack-principle-fix-root-causes]] and [[pstack-principle-redesign-from-first-principles]] are cited as *intent only* — **neither authorizes widening the fence or fixing instances outside it**, and symptom guards are never bolted on. That fence discipline is what keeps a comment sweep from becoming an unreviewable refactor.

**Constraint comments get an encoding offer rather than a deletion.** For a comment saying *do not remove*, *do not change wording*, or *talk to X before changing*, the skill offers the cheapest in-scope type, runtime, test, or CI lint that makes the constraint enforceable, waits for approval, and then **encodes it and deletes the comment**. Without approval the comment is deleted anyway and the constraint reported open. That is [[pstack-principle-encode-lessons-in-structure]] run at the level of a single line of code: the comment's job moves into the type system or CI, where it cannot be ignored.

Lint and TypeScript suppressions are audited alongside, with correctness or safety suppressions staying actionable `MUST KILL`s.

## See Also
- [[pstack-comment-sicko]] — the subagent it spawns and audits.
- [[pstack-architect]] — shapes any fix that needs one; this skill implements it.
- [[addy-code-simplification]] · [[ce-simplify-code]] — the complexity-reduction counterparts.
- [[stage-review]] — the canonical stage this implements.
