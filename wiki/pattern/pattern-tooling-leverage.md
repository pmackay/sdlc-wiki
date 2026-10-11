---
type: pattern
sources: "pstack v0.15.2 — Lauren Tan (2026)"
raw: ["../../raw/pstack/2026-09-11-pstack-plugin.md"]
updated: 2026-09-11
---

# Pattern: Tooling leverage (build the lever, not the result)

For any non-trivial work — bulk edits, a migration, an analysis, a check — **build the tool that does it or proves it instead of doing it by hand**. A codemod, a script, a generator, or a skill the subagents follow. The result is then a by-product of something re-runnable.

The second clause is the load-bearing one and is what separates this from ordinary automation advice: ***the tool is the artifact a reviewer can rerun***. The point is not that the agent works faster. It is that a reviewer who does not trust the agent's claim can re-derive the result themselves, which converts an assertion into evidence. That makes this the constructive complement of [[pattern-evidence-before-claims]]: one says a claim needs proof, this one says **build the thing that produces the proof**.

It also answers a failure mode specific to agents. An agent that edits 200 call sites by hand produces 200 opportunities to silently diverge and no way to check; an agent that writes the codemod produces one artifact whose correctness is inspectable and whose application is uniform. [[pstack]] states it as a principle explicitly scoped *to any non-trivial work, not just bulk work*, closing the loophole where "this is only a few files" defeats it.

## Applied by (backlinks)

pstack:

- [[pstack-principle-build-the-lever]] — the principle statement, with the reviewer-rerun clause.
- [[pstack-create-verification-skill]] — generates a per-repository harness that drives the real app, so behavior can be proven rather than asserted.
- [[pstack-blast-radius]] — rung 4 of its evidence ladder is a script that calls the real code and fails loud, shipped in the writeup.
- [[pstack-show-me-your-work]] — prefers evidence produced by committed scripts over hand-made one-offs.

## See Also
- [[pattern-evidence-before-claims]] — the claim-side complement; this is the means of producing the evidence.
- [[pattern-deterministic-gates]] — what the lever often becomes once the lesson is worth enforcing.
- [[pattern-knowledge-compounding]] — a lever kept and reused is how tooling compounds.
