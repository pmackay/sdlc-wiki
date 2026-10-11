---
type: pattern
sources: "Matt Pocock — Skills for Real Engineers (2026); Open GSD docs (2026); obra/superpowers (2026); pstack v0.15.2 — Lauren Tan (2026); Builder.io — BuilderIO/skills (2026)"
updated: 2026-09-26
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

pstack:

- [[pstack-principle-fix-root-causes]] — reproduce first, ask why until you reach it, resist nil-check guards that silence crashes.
- [[pstack-principle-attack-the-premise]] — the escalation rung above it, and pstack's distinctive addition to this cluster: when **two or more fixes sharing one premise have failed the same gate**, take a census of which actors hold the imbalance and then question the premise rather than writing another fix that assumes it. Where [[gstack-investigate]] and [[sp-systematic-debugging]] answer repeated failure with *stop after three*, pstack names the next move.
- [[pstack-benny-reproduce-and-fix]] — repro through the real UI gates any attempted fix.
- [[pstack-poteto-mode]] — the Bug fix, Runtime forensics, and Trace forensics playbooks, the latter two delivering *a diagnosis, not a fix*.

builder-skills:

- [[builder-factory-lookback]] — the population-scale version. Cluster recurring reports, trace representatives to their shared boundary, separate confirmed causes from hypotheses and state what would disprove each, and prefer *"one verified correction at that boundary over a pile of caller-specific patches."*

## See Also
- [[pattern-test-driven-development]] — the sibling feedback loop for new code.
- [[stage-implement]] — the stage where this applies.
