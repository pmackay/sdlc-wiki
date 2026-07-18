---
type: pattern
sources: "Matt Pocock — Skills for Real Engineers (2026); Open GSD docs (2026); obra/superpowers (2026)"
updated: 2026-07-17
---

# Pattern: Systematic debugging

Don't guess at fixes. Follow a disciplined loop — **reproduce → minimize → hypothesize → instrument → fix** — tracking hypotheses against evidence so each step shrinks the problem or rules out a cause.

## Applied by (backlinks)

Matt Pocock — Skills for Real Engineers:

- [[mp-diagnosing-bugs]] — the explicit reproduce→minimize→hypothesize→instrument→fix loop.

GSD:

- [[gsd-debugger]] — investigates bugs with persistent session state for hypotheses and evidence.

Addy Osmani — Agent Skills:

- [[addy-debugging]] — evidence-driven reproduce→hypothesize→fix loop, no guessing.

Compound Engineering:

- [[ce-debug]] — causal-chain root-cause with explicit prediction-confirmation before the fix.

gstack:

- [[gstack-investigate]] — Iron Law: no fixes without investigation; auto-freezes scope; stops after 3 failed fixes.
- [[gstack-ios-fix]] — the autonomous iOS analogue.

Superpowers:

- [[sp-systematic-debugging]] — a four-phase process (investigate → pattern → hypothesis → fix); Iron Law "no fixes without root-cause investigation first"; **question the architecture after 3 failed fixes** — the same stop-after-3 discipline as [[gstack-investigate]].

## See Also
- [[pattern-test-driven-development]] — the sibling feedback loop for new code.
- [[stage-implement]] — the stage where this applies.
