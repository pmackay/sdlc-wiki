---
type: capability
subtype: command
belongs_to: "[[seeds]]"
implements: []
produces: ["[[artifact-atomic-commit]]"]
applies: ["[[pattern-session-handoff]]", "[[pattern-worktree-isolation]]"]
equivalent_to: []
sources: "Jaymin West — jayminwest/seeds README + AGENTS.md + SPEC.md (MIT, v0.5.15, 2026)"
raw: ["../../raw/seeds/2026-08-31-seeds.md"]
updated: 2026-08-31
---

# sd sync

`sd sync` — stage and commit the `.seeds/` changes (`--status` to inspect first, `--dry-run` to preview). It commits **locally and only locally**: *"No remote sync. `sd sync` commits locally. `git push` handles the rest"*, and the framework's agent workflow is explicit that an agent should not push unless asked.

This is the step that makes the tracker durable, and it is the reason seeds has no audit trail of its own — *"Git IS the audit trail. Use `git log .seeds/issues.jsonl`."* Plan revisions are not kept as separate rows for the same reason; the JSONL diff is the history, which keeps storage simple and avoids inflating the id space.

It maps to **no canonical SDLC stage**. It looks like [[stage-release]] and is not: what it delivers is tracker state, not a change to the product. Seeds ships nothing — it has no PR, deploy, or version step anywhere in its surface.

Its two pattern edges both come from the commit being the boundary object. [[pattern-session-handoff]]: once committed, a fresh agent picks up the queue with `sd prime` + `sd ready` instead of reconstructing where the last one stopped. [[pattern-worktree-isolation]]: committed JSONL is exactly what `merge=union` reconciles when parallel worktree branches land.

## See Also
- [[seeds-close]] — the state change this commits.
- [[seeds-init]] — installs the gitattributes that make these commits mergeable.
- [[seeds-prime]] — the other half of the handoff, on the read side.
- [[artifact-atomic-commit]] — what it produces.
