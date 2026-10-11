---
type: capability
subtype: skill
belongs_to: "[[pstack]]"
implements: []
delegates_to: ["[[pstack-unslop]]"]
produces: ["[[artifact-diataxis-docs]]", "[[artifact-standards]]"]
applies: ["[[pattern-deterministic-gates]]"]
equivalent_to: ["[[gstack-document-generate]]", "[[addy-documentation]]"]
sources: "pstack v0.15.2 — Lauren Tan (2026)"
raw: ["../../raw/pstack/2026-09-11-pstack-plugin.md"]
updated: 2026-09-11
---

# /technical-writing

A **layered technical-writing standard** for docs, RFCs, readmes, PR descriptions, and commit messages. Four established standards stacked, each answering one question:

- **Diátaxis** — what kind of document is this? One document, one mode, picked by two questions: does the content inform action or understanding, and does it serve learning or work?
- **Google developer style** — how do sentences address the reader?
- **Simplified Technical English (STE)** — how much does each sentence carry?
- **Global English** — can any sentence be read two ways?

Three rules sit above the layers. Cut every word that does no work (*"in order to" is "to"; "it is important to note that" is nothing*). Use the short everyday word (*"use" not "utilize"*) — a long word has to buy its length with precision. And the escape clause that keeps it usable: **when a rule makes a sentence worse, fix the sentence another way or leave it alone.** *A sentence that follows every rule and sounds like a machine wrote it has failed.*

Two sections make it more than a style sheet. **The codebase is the word list** — write the real symbol, file, flag, or command name, never a synonym or a description of it — and *do not invent jargon*: use the words a developer would say out loud, *"move", "delete", "a budget that only decreases"*, not *"evacuate", "ratchet", "endgame"*. A new offender is proposed as a diff to [[pstack-unslop]]'s abstract-metaphor rule rather than being fixed locally. **Vary the rhythm** is the counterweight to the layers: a document can obey all four and still read machine-written if every sentence is clipped short with no view anywhere and nothing specific. Mix sentence lengths on purpose, keep the long sentence that carries one thought, have a view where the mode allows it, and be specific over sterile — *not "schema changes can cause issues" but "a column rename fails the build"*.

pstack is the second framework here to adopt Diátaxis explicitly, after [[gstack]]'s documentation skills, and the first to treat prose style as a **stack of named external standards** rather than house rules.

## See Also
- [[pstack-unslop]] — the always-on floor this sits on; new jargon offenders are proposed as edits to it.
- [[pstack-bro]] — the opposite end of the register.
- [[gstack-document-generate]] · [[addy-documentation]] — the documentation counterparts.
- [[artifact-diataxis-docs]] — the artifact shape.
