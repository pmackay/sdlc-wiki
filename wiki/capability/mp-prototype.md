---
type: capability
subtype: skill
belongs_to: "[[matt-pocock-skills]]"
implements: "[[stage-implement]]"
delegates_to: []
produces: []
applies: ["[[pattern-throwaway-prototype]]"]
equivalent_to: []
docs_url: "https://www.aihero.dev/skills-prototype"
sources: "Matt Pocock — Skills for Real Engineers v1.1 (2026); v1.2.0 reshape (2026-08-05)"
raw: ["../../raw/matt-pocock-skills/2026-10-04-skills-v1.3.1-update.md", "../../raw/matt-pocock-skills/2026-07-09-skills-v1.1-update.md"]
updated: 2026-10-11
---

# prototype

`/prototype` — a **model-invoked** (since v1.1; it was user-invoked before) engineering skill that builds a **throwaway prototype** to answer one design question: does this state model feel right, or what should this UI look like ([[pattern-throwaway-prototype]]). Being model-invoked, the agent and other skills can reach for it autonomously. In MP's main flow it is the prototype detour, bridged into and out of by [[mp-handoff]] when a question needs a runnable answer.

## v1.2.0 reshape (2026-08-05): one HTML file, kept as a primary source

The changelog builds it on two ideas:

- **The demo is a single shareable HTML file.** The logic branch no longer builds a terminal app. It produces one self-contained file (plain HTML/CSS/JS, no build, no server) that a non-developer can open by double-click and drive in their own domain language. The file has a labelled state panel, always-available free-play buttons, and tabbed **guided walkthroughs** (each a scenario with the ordered buttons to press). The portable pure-logic module still lifts into the real code; the HTML shell is the throwaway. The UI branch still produces radically different variations toggleable from one route.
- **The prototype is a primary source.** "Throwaway is a constraint on how the code is written, not a promise to destroy it." The prototype is no longer deleted once it has answered its question. It is captured as runnable evidence on a throwaway **`prototype/<name>` branch** out of main, with a context pointer on the implementation issue. Main keeps only the validated decision, and the exploration stays findable. The verdict and the question are still recorded durably in an issue, ADR, or commit.

The second idea shifts the [[pattern-throwaway-prototype]] pattern from *build → learn → discard* to *build → learn → archive off-trunk*. [[mp-wayfinder]] uses the same move for research (`research/<name>` branches).

## See Also
- [[mp-to-spec]] — turn validated learnings into a spec.
- [[mp-handoff]] — the bridge into and out of the prototype's own directory.
- [[pstack-arena]] — pstack's competing-candidates relative.
- [[stage-implement]] — the canonical stage this implements.
