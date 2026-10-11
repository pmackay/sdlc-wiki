---
type: artifact
sources: "Matt Pocock — Skills for Real Engineers (2026); v1.3.0 rename (2026-10-04)"
updated: 2026-10-11
---

# Artifact: Domain model (GLOSSARY.md)

The project's shared-language glossary / domain model, stored as `GLOSSARY.md` (`GLOSSARY-MAP.md` indexes several in a multi-context repo). It was `CONTEXT.md` / `CONTEXT-MAP.md` until Matt Pocock's v1.3.0 (2026-10-04) renamed it everywhere the skills read and write it; existing files must be `git mv`'d. It maps project jargon to precise concepts so the agent can stay terse and consistent — the answer to failure mode #2 (verbosity). Bootstrapped by [[mp-grill-with-docs]] and deepened by [[mp-domain-modeling]].

> **Naming conflict (cross-framework), resolved upstream 2026-10-04:** GSD also writes a `CONTEXT.md`, but it means something different: *locked phase decisions and scope* (see [[artifact-phase-context]]). Until v1.3.0 the two frameworks shared the filename for different artifacts. Matt Pocock's rename to `GLOSSARY.md` removes the clash going forward; repos set up before v1.3.0 may still carry an MP `CONTEXT.md`.

## Produced by (backlinks)
- [[mp-grill-with-docs]] — creates/updates it during grilling.
- [[mp-domain-modeling]] — sharpens it.

## Read by
- [[mp-tdd]] · [[mp-diagnosing-bugs]] · [[mp-triage]] · [[mp-codebase-design]] · [[mp-improve-codebase-architecture]] — read it for the domain vocabulary.
- [[mp-wait-what]] · [[mp-pr]] — write their output in its ubiquitous language (v1.2.0 / v1.3.0).

## See Also
- [[artifact-phase-context]] — GSD's same-named but distinct artifact.
- [[artifact-adr]] — decisions recorded alongside the model.
