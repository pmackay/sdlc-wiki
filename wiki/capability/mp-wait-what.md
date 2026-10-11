---
type: capability
subtype: skill
belongs_to: "[[matt-pocock-skills]]"
implements: []
delegates_to: []
produces: []
applies: ["[[pattern-context-engineering]]"]
equivalent_to: []
docs_url: "https://www.aihero.dev/skills-wait-what"
sources: "Matt Pocock — Skills for Real Engineers v1.3.1 (2026-10-04)"
raw: ["../../raw/matt-pocock-skills/2026-10-04-skills-v1.3.1-update.md"]
updated: 2026-10-11
---

# wait-what

`/wait-what` — a user-invoked productivity skill, "Stop. That last message did not land: re-pitch it." Its whole body is one instruction: re-pitch with a little context, in **ASD-STE100 Simplified Technical English**, using the ubiquitous language from `GLOSSARY.md` (following `GLOSSARY-MAP.md` to the right one in a multi-context repo).

**New in v1.2.0 (2026-08-05).** It is a "one-word corrective for model verbosity", usable mid-conversation and inside any other skill.

## The mechanism is the name

The changelog argues that concision skills "fail by growing: a 400-line skill still leaves the model verbose." So this one is three lines, and the work is done by a single **leading word** (the concept [[mp-writing-for-agents]] defines). Names that describe the *output* (`/tldr`, `/no-fluff`) make the model clip words and lose the reader further. Naming the *listener's state* asks for both halves at once: fewer words **and** the missing context.

## Where it sits

Off-stage. It repairs one message and does not prevent the next. The upfront cure for jargon is a shared language built with [[mp-grill-with-docs]] / [[mp-domain-modeling]] ([[artifact-domain-model]]). `wait-what` is the after-the-fact fix that reuses that same vocabulary. It addresses the README's failure mode #2, "The Agent Is Way Too Verbose".

## See Also
- [[mp-domain-modeling]] · [[artifact-domain-model]] — the `GLOSSARY.md` it re-pitches in.
- [[mp-writing-for-agents]] — the leading-word theory it is a three-line instance of.
- [[mp-ask-matt]] — routes it under Standalone.
