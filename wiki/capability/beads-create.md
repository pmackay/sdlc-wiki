---
type: capability
subtype: command
belongs_to: "[[beads]]"
implements: []
produces: ["[[artifact-issue]]"]
applies: []
equivalent_to: ["[[seeds-create]]"]
sources: "gastownhall/beads — README + docs/core-concepts + docs/CLI_REFERENCE.md (MIT, 2026)"
raw: ["../../raw/beads/2026-08-31-beads.md"]
updated: 2026-08-31
---

# bd create

`bd create "Title"` — file a bead. Type (`bug`, `task`, `feature`, `epic`, `chore`, …), priority (`-p 0`–`4`), description, labels, assignee, and the structured fields beads keeps distinct from prose: `--design`, `--notes`, `--acceptance`. Content with shell-hostile characters goes in via `--stdin` or `--body-file` rather than being escaped.

Three siblings share the page because they are the same act at different ceremony:

- **`bd q "Fix login bug"`** — quick capture that prints *only* the ID, built for pipelines: `ISSUE=$(bd q "New feature")`, `bd q "Task" | xargs bd show`.
- **`bd create-form`** — an interactive form, for humans.
- **`bd batch`** — many write operations in a single database transaction, so a bulk import either all lands or none does.

`bd create` also accepts a markdown or graph-JSON document to create a whole set of beads with their edges at once — the manual counterpart to the [[beads-cook]] → [[beads-mol]] pipeline.

The ID it returns is a **content hash** (`bd-a1b2`), derived from title, description, creator, and creation time plus a collision nonce, with the hash length extending automatically as the database grows. That is a design decision in service of multi-agent work: two agents on two branches cannot mint the same ID, so *"merges never renumber work"*. Hierarchical IDs (`bd-a3f8.1.1`) express epic structure in the identifier itself.

Maps to **no canonical SDLC stage**: recording that a unit of work exists is not performing a lifecycle step. (Contrast [[seeds-create]], which the wiki files under [[stage-plan]] — that store treats filing as the low-ceremony tier of its own planning dial, while beads' charter keeps methodology out.)

## See Also
- [[beads-ready]] — where a created bead surfaces once nothing blocks it.
- [[beads-dep]] — wiring it into the graph.
- [[beads-todo]] — the lighter wrapper for throwaway task beads; [[beads-mol]] — the templated bulk alternative.
- [[artifact-issue]] — what it produces.
