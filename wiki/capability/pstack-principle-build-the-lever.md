---
type: capability
subtype: skill
belongs_to: "[[pstack]]"
implements: []
delegates_to: []
produces: []
applies: ["[[pattern-tooling-leverage]]"]
equivalent_to: []
sources: "pstack v0.15.2 — Lauren Tan (2026)"
raw: ["../../raw/pstack/2026-09-11-pstack-plugin.md"]
updated: 2026-09-11
---

# principle-build-the-lever

**Core principle.** Build the tool that does it or proves it, instead of working by hand. The tool is the artifact a reviewer can rerun.

Applies to any non-trivial work, not just bulk work: edits, migrations, analyses, checks. A codemod, script, generator, or a skill the subagents follow all count. The second clause is the load-bearing one and is why this is [[pattern-tooling-leverage]] rather than ordinary automation advice — the tool exists so the *reviewer* can re-derive the result, which is also what [[pstack-create-verification-skill]] and [[pstack-show-me-your-work]] are for.

## See Also
- [[pstack-poteto-mode]] — indexes this principle inline and reads the index at task start.
- [[pstack]] — the twenty-three-principle set this belongs to.
