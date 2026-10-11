---
type: capability
subtype: skill
belongs_to: "[[matt-pocock-skills]]"
implements: "[[stage-align]]"
delegates_to: []
produces: []
applies: ["[[pattern-grilling]]"]
equivalent_to: []
docs_url: "https://www.aihero.dev/skills-to-questionnaire"
sources: "Matt Pocock — Skills for Real Engineers v1.3.1 (2026-10-04)"
raw: ["../../raw/matt-pocock-skills/2026-10-04-skills-v1.3.1-update.md"]
updated: 2026-10-11
---

# to-questionnaire

`/to-questionnaire` — a user-invoked productivity skill: "Turn a decision you can't fully answer into a questionnaire for someone else to fill in." The output is a Markdown file (`to-questionnaire-<slug>.md`) handed to **one person** to fill in async, or worked through together in a meeting.

[[mp-ask-matt]] routes it under Standalone and frames it as "the inverse of `/grill-me`": mine someone else, not yourself.

## The defining move: grill the send, not the subject

A normal grilling session ([[mp-grilling]]) interrogates the topic, and the topic is exactly what the user can't answer here. So the interview covers only the **send**, which the user can always answer:

1. **Who is it going to?** The recipient's role, expertise, and relationship to the user, asked in one exchange. This sets the tone and how much context the document must carry.
2. **What do you need back?** The specific decisions or facts the user can't resolve alone, asked in one exchange.
3. **Write the questionnaire.** Questions aimed at the **gap** between what the recipient knows and what the user needs. Done when every item from step 2 is covered.

## Document shape

A **discovery questionnaire**: Purpose / From–To / How your answers will be used, a one-paragraph Context, How to answer ("partial answers and 'I don't know' are useful"), then one `##` section per theme with questions **most-important-first** ("async means you may only get one pass"). Each question carries one idea with an answer stub beneath it, and a one-line *why this matters* only where the question could be misread. It closes with an "Anything else?" catch-all.

## Where it sits

This is a distinct flavor of [[stage-align]], **delegated elicitation**. Every other align capability in the wiki interviews the person at the keyboard (the grilling cluster) or processes incoming reports (the intake cluster). `to-questionnaire` targets a **third party** who holds the missing knowledge. What comes back feeds [[mp-grill-with-docs]] or [[mp-to-spec]]. No other framework pages an equivalent yet.

## See Also
- [[mp-grill-me]] · [[mp-grilling]] — the self-interview it inverts.
- [[mp-grill-with-docs]] · [[mp-to-spec]] — where the answers go next.
- [[pattern-grilling]] — the elicitation pattern, here pointed at the send.
- [[stage-align]] — the canonical stage this implements.

## Version history
- **v1.2.0 (2026-08-05):** graduated from `in-progress/` into `productivity/`; shipped in the plugin and routed by [[mp-ask-matt]] as the inverse of `/grill-me`.
