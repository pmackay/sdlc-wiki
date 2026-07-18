---
type: pattern
sources: "Addy Osmani — Agent Skills (2026); obra/superpowers (2026)"
updated: 2026-07-17
---

# Pattern: Anti-rationalization (excuse/rebuttal tables)

Every process step an agent is tempted to skip is pre-empted by naming the **rationalization**
("I'll add tests later", "this change is too small to review") and pairing it with a
documented **rebuttal**. Coupled with a **Red Flags** list of warning signs that something
has gone wrong. The technique hard-codes discipline into the workflow so the agent cannot
quietly take the shortest path — the excuse it would reach for is already answered on the page.

This is the **co-signature** mechanism of two frameworks. [[addy-agent-skills]] puts the table in
*every* skill; [[superpowers]] pushes it furthest, escalating the same instinct into **Iron Laws**
(delete code written before its test; no fix without root-cause; no completion claim without
evidence), per-skill **Red Flags** "STOP — you're rationalizing" tables, and a bootstrap
([[sp-using-superpowers]]) that aims the technique at skill *discovery* itself. Both frameworks use it
to make their skills resist the shortest-path default that motivates the pack.

## Applied by (backlinks)

Addy Osmani — Agent Skills (every skill carries the table; representative):

- [[addy-tdd]] — rebuts "I'll add tests later".
- [[addy-code-review]] — rebuts "the change is too small to review".
- [[addy-security]] — rebuts "no one will attack this".
- [[addy-incremental-implementation]] — rebuts "it's faster to do it all at once".

Superpowers (Iron Laws + Red Flags + excuse→reality tables in nearly every skill):

- [[sp-using-superpowers]] — the Red-Flags table for skill discovery ("this is just a simple question", "let me explore first").
- [[sp-test-driven-development]] — the fullest excuse→reality table ("too simple to test", "deleting X hours is wasteful" = sunk cost).
- [[sp-systematic-debugging]] — rebuts "quick fix now, investigate later" and "one more fix attempt".
- [[sp-verification-before-completion]] — rebuts "should work now", "I'm confident", "agent said success".
- [[sp-receiving-code-review]] — the *social* variant: forbids performative agreement ("You're absolutely right!").

## See Also
- [[addy-agent-skills]] · [[superpowers]] — the two frameworks that standardize this across all skills.
- [[pattern-adversarial-review]] — a stronger, active form of the same distrust-your-own-output instinct.
- [[pattern-evidence-before-claims]] — the adjacent discipline: not talking yourself *out of* a process, but not declaring one *finished* without proof.
