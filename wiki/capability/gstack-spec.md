---
type: capability
subtype: command
belongs_to: "[[gstack]]"
implements: "[[stage-specify]]"
delegates_to: []
produces: ["[[artifact-spec-md]]", "[[artifact-issue]]"]
applies: ["[[pattern-spec-driven-development]]", "[[pattern-adversarial-review]]", "[[pattern-worktree-isolation]]"]
equivalent_to: ["[[speckit-specify]]", "[[addy-spec-driven-development]]", "[[mp-to-spec]]", "[[openspec-propose]]", "[[bmad-prd]]", "[[bm-prd-creator]]", "[[nano-spec-create]]", "[[agent-os-shape-spec]]"]
sources: "gstack — Garry Tan (2026)"
raw: ["../../raw/gstack/2026-07-05-gstack-framework.md"]
updated: 2026-08-05
---

# /spec

`/spec` — the **Spec Author**. Turns vague intent into a **precise, executable spec in five phases** (why → scope → technical, with mandatory code-reading → draft → file). A **Codex quality gate** blocks specs below 7/10 before filing; fail-closed secret redaction runs before anything leaves the machine; it dedupes against existing issues, files a **GitHub issue** ([[artifact-issue]]), and archives the spec to the team corpus for recall. `--execute` spawns `claude -p` in a **fresh git worktree** ([[pattern-worktree-isolation]]); [[gstack-ship]] auto-closes the source issue on merge. Plan-mode aware.

This is gstack's member of the multi-framework **specify** cluster ([[pattern-spec-driven-development]]) — author the durable spec before code — alongside [[speckit-specify]], [[addy-spec-driven-development]], [[mp-to-spec]], [[openspec-propose]], and [[bmad-prd]]. Distinctive here: the **cross-model quality gate** ([[pattern-adversarial-review]] via [[gstack-codex]]) and the file-an-issue-then-execute-in-a- worktree handoff.

## See Also
- [[gstack-codex]] — the cross-model reviewer behind the spec quality gate.
- [[gstack-ship]] — auto-closes the issue this files on merge.
- [[speckit-specify]] · [[bmad-prd]] · [[openspec-propose]] — specify-cluster counterparts.
- [[stage-specify]] — the canonical stage this implements.
