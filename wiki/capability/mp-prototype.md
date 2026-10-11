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

`/prototype` — a **model-invoked** engineering skill that builds a **throwaway prototype** to answer one design question: does this state model feel right, or what should this UI look like ([[pattern-throwaway-prototype]]). Being model-invoked, the agent and other skills can reach for it autonomously. In MP's main flow it is the prototype detour, bridged into and out of by [[mp-handoff]] when a question needs a runnable answer.

## Two ideas it is built on

- **The demo is a single shareable HTML file.** The logic branch produces one self-contained file (plain HTML/CSS/JS, no build, no server) that a non-developer can open by double-click and drive in their own domain language. The file has a labelled state panel, always-available free-play buttons, and tabbed **guided walkthroughs** (each a scenario with the ordered buttons to press). The portable pure-logic module lifts into the real code; the HTML shell is the throwaway. The UI branch produces radically different variations toggleable from one route.
- **The prototype is a primary source.** "Throwaway is a constraint on how the code is written, not a promise to destroy it." Once it has answered its question, the prototype is captured as runnable evidence on a throwaway **`prototype/<name>` branch** out of main, with a context pointer on the implementation issue. Main keeps only the validated decision, and the exploration stays findable. The verdict and the question are recorded durably in an issue, ADR, or commit.

The second idea makes the pattern *build → learn → archive off-trunk*. [[mp-wayfinder]] uses the same move for research (`research/<name>` branches).

## See Also
- [[mp-to-spec]] — turn validated learnings into a spec.
- [[mp-handoff]] — the bridge into and out of the prototype's own directory.
- [[pstack-arena]] — pstack's competing-candidates relative.
- [[stage-implement]] — the canonical stage this implements.

## Version history

### v1.2.0 (2026-08-05)
- The logic branch switched from a runnable terminal app to a single shareable HTML file.
- Prototypes are kept on a `prototype/<name>` branch instead of being deleted, which shifted [[pattern-throwaway-prototype]] from *build → learn → discard* to *build → learn → archive off-trunk*.

### v1.1.0 (2026-07-08; ingested 2026-07-09)
- Became model-invoked (it was user-invoked before).

### Initial ingest (2026-06-28)
- Paged as a user-invoked skill building throwaway prototypes: a terminal app for state/logic, or toggleable UI variations from one route.
