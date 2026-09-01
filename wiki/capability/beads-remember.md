---
type: capability
subtype: command
belongs_to: "[[beads]]"
implements: []
produces: []
applies: ["[[pattern-knowledge-compounding]]", "[[pattern-session-handoff]]"]
equivalent_to: ["[[ce-compound]]", "[[gstack-learn]]"]
sources: "gastownhall/beads — docs/workflows + docs/CLI_REFERENCE.md (MIT, 2026)"
raw: ["../../raw/beads/2026-08-31-beads.md"]
updated: 2026-08-31
---

# bd remember

`bd remember "insight"` · `bd recall <key>` · `bd memories` · `bd forget <key>` — *"store a memory that persists across sessions and account rotations"*, auto-keyed from the content or pinned with `--key`, and **injected into every session by [[beads-prime]]** without anyone loading it.

```bash
bd remember "always run tests with -race flag"
bd remember "Dolt phantom DBs hide in three places" --key dolt-phantoms
bd remember "auth module uses JWT not sessions" --key auth-jwt
bd recall dolt-phantoms
```

The README's instruction to agents is the sharp part: *"Use `bd remember` for persistent project memory; **do not create MEMORY.md files.**"* That is the same argument [[beads-todo]] makes about markdown checklists, aimed at knowledge instead of tasks — a file an agent writes is a file that rots, is not queryable, is not merged, and is not guaranteed to be read next time. A memory in the store is all four.

**This is why the wiki's node for this layer is `store` and not `tracker`.** Beads is an issue tracker that also ships a durable knowledge base, keyed, mergeable, and auto-primed; strip the issues away and what is left is [[warren]]'s `.mulch/` with a different CLI. The layer holds state, and work items are only one kind.

Against the process-layer implementations of [[pattern-knowledge-compounding]] the difference is *who is responsible for reading it back*. [[ce-compound]] and [[gstack-learn]] write lessons to a corpus and trust a later session to consult it; [[seeds-plan-prompt]] pulls the relevant subset into a planning prompt on demand. Beads pushes the whole set into context at session start unconditionally — cheapest to get right, and it scales badly on purpose, which is what [[beads-compact]] is for.

Maps to **no canonical SDLC stage**: storing an insight performs no lifecycle step, and unlike [[ce-compound]] there is no harvesting pass — an agent calls `remember` when it notices something, so the *deciding* is in whatever skill told it to.

## See Also
- [[beads-prime]] — injects these every session.
- [[beads-kv]] — the untyped sibling for non-insight state.
- [[warren]] — `.mulch/`, the same capability as runtime infrastructure.
- [[ce-compound]] · [[gstack-learn]] · [[sp-writing-skills]] — the process-layer forms.
